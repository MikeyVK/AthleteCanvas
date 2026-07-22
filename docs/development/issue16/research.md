<!-- docs\planning\issue16\research.md -->
<!-- template=research version=8b7bb3ab created=2026-03-07T10:34Z updated= -->
# Foundational Architecture Research

**Status:** DRAFT  
**Version:** 1.1  
**Last Updated:** 2026-03-07

---

## Purpose

Establish the architectural foundation that all current and future epics depend on. This research supersedes single-user assumptions made in Epic 1 research and will drive a revised epic list and child issue updates.

## Scope

**In Scope:**
Project scaffolding, multi-tenancy (user model, data isolation via RLS), authentication (JWT, MFA, OAuth), API-first design, command/query service layer, frontend platform strategy, hexagonal architecture package layout, Garmin Direct-First ingestion, Vector Storage & RAG, Background worker security, Secure sharing (E2EE) and Anonymization, Zero-Trust Operator Security.

**Out of Scope:**
Implementation of any component (that belongs to child issues), AI layer design (Epic 2), deployment/infrastructure (later epic), specific UI design/wireframes

## Prerequisites

Read these first:
1. Epic 1 research.md v1.2 — findings remain valid except Finding 3 (SQLite, now superseded)
2. Epic 1 design brainstorm — architectural gaps identified there are the direct input for this research
---

## Problem Statement

Critical architectural gaps discovered during Epic 1 design brainstorm: no project scaffolding baseline exists, multi-user and multi-platform requirements are unaddressed, the frontend data ingestion layer is entirely missing, the command/query service layer connecting frontend to backend is undefined, and auth (JWT, MFA, OAuth per-user) has not been designed. Furthermore, architectural friction points around vector isolation, background worker security, waitlist security, and third-party ingestion polling (Garmin) were identified. These gaps affect all current and future epics.

## Research Goals

- Determine project scaffolding baseline: package layout, pyproject.toml, import conventions, Alembic env, test structure
- Evaluate and decide relational storage: PostgreSQL + pgvector + RLS for multi-user isolation
- Define unified vector storage & hierarchical rollups strategy
- Research auth stack: JWT, MFA (WebAuthn vs TOTP), Garmin OAuth per-user with PKCE for mobile
- Define API-first design principles: versioning, OpenAPI, CORS, platform-agnostic endpoint design
- Design command/query service layer (CQRS-light) connecting FastAPI routes to domain services
- Define frontend platform strategy: web-first with mobile-extensible design, PWA, React Native path
- Determine hexagonal architecture package structure for multi-user, multi-platform backend
- Assess impact of multi-tenancy on existing Epic 1 child issues #7-#15
- Define Direct-First Garmin Ingestion with Smooth Flat Queue bootstrapping
- Establish Background Worker Security (Two-Tier System Consent via data_shares)
- Design Secure Sharing (E2EE) and Anonymization Architecture (Secure Views)
- Define Zero-Trust Operator Security (Decentralized Private Key)

---

## Background

Epic 1 was designed assuming single-user SQLite. During design brainstorm, three critical gaps emerged: (1) no project scaffolding exists as a cross-epic foundation; (2) multi-user + multi-platform (web, Android, iOS) + MFA requirements invalidate the single-user storage and auth assumptions; (3) the frontend layer for data ingestion and the command/query service connecting it to the backend are entirely absent from the design.

## Open Questions

- ✅ [RESOLVED] PostgreSQL vs SQLite: what is the exact migration path and dev experience tradeoff?
- ✅ [RESOLVED] Vector Storage: what is the serialization and isolation strategy without external stores?
- ✅ [RESOLVED] WebAuthn: which Python library, what is the registration/authentication flow, recovery strategy?
- ✅ [RESOLVED] PKCE flow: how does garth handle mobile OAuth callbacks, what are the deep link requirements?
- ✅ [RESOLVED] CQRS-light: how do Commands and Queries map to FastAPI routes and internal service calls?
- ✅ [RESOLVED] React Native + Expo: what is the monorepo strategy relative to the existing Vite frontend?
- ✅ [RESOLVED] User model: what fields are required, where does it live in the hexagonal structure?
- ✅ [RESOLVED] Frontend Framework epic: what is the minimal scope to unblock all feature epics?


## Findings

### Finding 1 — Project Scaffolding & Monorepo Structure

**Decision: flat hexagonal layout, pnpm monorepo, no src-layer, no root pyproject.toml.**

#### Repository layout

```
/ (repo root)
  backend/
    athletecanvas/
      domain/          # ActivityRecord, User, AppConfig — pure logic, no IO
      ports/           # IActivityWriter, IEmbeddingStore, BaseAdapter — interfaces only
      services/        # ImportOrchestrator, EmbeddingPipeline, AuthService — use cases
      adapters/
        inbound/       # FastAPI routes, request/response schemas
        outbound/      # PostgreSQLRepo, GarminAdapter, etc.
    tests/
      unit/
      integration/
    alembic/
    alembic.ini
    pyproject.toml     # sole Python entry point
  frontend/            # React + Vite (web)
    src/
    package.json
  mobile/              # React Native + Expo — from day one
    src/
    package.json
    app.json
  shared/              # OpenAPI-generated client types — consumed by frontend + mobile
    api/
    package.json
  docs/
  .st3/
  package.json         # pnpm workspace root
  pnpm-workspace.yaml  # declares frontend/, mobile/, shared/
  Makefile             # cross-language convenience: make test, make lint, make dev
  .python-version      # pyenv/uv Python version pin for the entire repo
```

#### Rationale

- **No `src/` layer** — `src/` is a Python packaging convention for published libraries. For a FastAPI application it adds indirection without benefit. `backend/athletecanvas/` directly is simpler and unambiguous.
- **Hexagonal layers** — dependency rule: everything points inward. `domain/` and `ports/` never import from `services/` or `adapters/`. `services/` depends on `ports/`, never on concrete adapters. `adapters/outbound/` implements `ports/`. `adapters/inbound/` (FastAPI routes) calls `services/`.
- **`services/` inside `athletecanvas/`** — application-level use cases, not HTTP handlers. They orchestrate domain logic via ports. Testable without a running server.
- **`shared/` from day one** — OpenAPI spec → codegen → `shared/api/` → both `frontend` and `mobile` import the same typed client. Prevents drift without extra effort per endpoint.
- **pnpm workspaces** — manages `frontend/`, `mobile/`, `shared/` as a single workspace. Faster and cleaner than npm workspaces for monorepos.
- **No root `pyproject.toml`** — Python has no native workspace support. A root-level Python config creates ambiguity. If a second Python package is added later (e.g. `scripts/`), a `uv` workspace can be introduced at that point (YAGNI).
- **`Makefile` as cross-language entrypoint** — `make test`, `make lint`, `make dev` abstract over `pytest` vs `pnpm` vs `docker compose`. Single command surface for CI and developers.
- **Tests in `backend/tests/`** — separate from source, split into `unit/` and `integration/`. Compatible with Alembic env setup and standard pytest discovery.

#### Cross-epic impact

This structure is the prerequisite for all epics. Every child issue in every epic operates within this layout. The `shared/` package means any endpoint added in any epic is immediately available to both web and mobile without additional work.

### Finding 2 — Relational & Vector Storage: PostgreSQL + pgvector + SQLAlchemy Core + Alembic

**Decision: PostgreSQL as the *sole* store for both relational data and vector embeddings, isolated fundamentally via Row-Level Security (RLS). SQLAlchemy Core for repositories, Alembic for migrations, pytest-postgresql for integration tests.**

#### Unified Storage & Row-Level Security (RLS)
SQLite is insufficient for multi-user writes. Furthermore, splitting relational data and vector data across different systems creates complex synchronization risks. PostgreSQL with the `pgvector` extension becomes the single source of truth for both relational tables and the `user_embeddings` table. 

Data isolation is not handled via application-level `WHERE` clauses. Instead, we enforce PostgreSQL Row-Level Security (RLS) using `user_uuid` at the database kernel level. This guarantees strict data isolation for all operations, making cross-tenant data leakage structurally impossible.

#### Why PostgreSQL over SQLite

SQLite is a single-writer database. With multiple users importing data concurrently, write-lock contention is inevitable and unrecoverable without an architectural rewrite. PostgreSQL is the baseline for any multi-user application.

SQLite is entirely deprecated. Unit tests must rely purely on in-memory FakeAdapters (zero DB dependency). Integration tests use pytest-postgresql. Using SQLite for testing is strictly forbidden as it lacks native support for pgvector and JSONB.

#### ORM strategy: SQLAlchemy Core (not ORM)

In hexagonal architecture, domain models (Pydantic) must remain independent of persistence concerns. SQLAlchemy ORM couples models to table definitions — a known anti-pattern in hexagonal design. SQLAlchemy Core keeps the two separate:

- **Domain model** (`domain/models.py`) — pure Pydantic, no ORM decorators
- **Table definition** (`adapters/outbound/storage/tables.py`) — SQLAlchemy `Table` objects, internal detail of the adapter
- **Repository** (`adapters/outbound/storage/postgresql.py`) — maps between the two explicitly

asyncpg (raw SQL, no ORM) was considered and rejected: it requires abandoning Alembic, which is non-negotiable for a schema that will evolve across many epics.

#### Alembic for migrations

Alembic manages schema evolution the same way Git manages code: every change is a versioned, reversible migration stored in `backend/alembic/versions/`. The database carries its own version pointer (`alembic_version` table). `alembic upgrade head` is idempotent and safe to run in CI/CD pipelines. Manual SQL migration management across multiple epics is rejected as a high-risk approach.

#### Test strategy: two-tier

- **Unit tests** (`tests/unit/`) — zero DB dependency. All services (`services/`) are tested via fake adapters implementing the port interfaces (e.g. `FakeActivityWriter(IActivityWriter)`). Fakes are first-class citizens, not throwaway mocks.
- **Integration tests** (`tests/integration/`) — `pytest-postgresql` spins up a real PostgreSQL process per test session. No dialect mismatch possible. No Docker daemon required in CI.

```
make test-unit    → pytest tests/unit/       (no DB, fast)
make test-int     → pytest tests/integration/ (pytest-postgresql)
make test         → both
```

#### Test code quality is production code quality

Tests are subject to the same SOLID, DRY, and Config-over-Code principles as production code. This is non-negotiable and enforced by quality gates:

- **Fixtures are ports** — `ActivityRecordFactory`, `UserFactory` are shared builders in `conftest.py`, never inline dicts repeated per test
- **Fake adapters, not mocks** — `FakeActivityWriter(IActivityWriter)` is a real class with an in-memory list. `unittest.mock.patch()` is fragile on refactor; fakes are not
- **`conftest.py` per layer** — `tests/unit/conftest.py` and `tests/integration/conftest.py` are separate. No single root-level conftest becoming a dumping ground
- **Config over hardcoded values** — DSNs, model paths, feature flags via pytest fixtures, never hardcoded strings scattered across test files
- **DRY assertions** — reusable assertion helpers (`assert_activity_equals(a, b)`) instead of 15 repeated `assert` statements per test
- **Quality gates apply equally** — ruff, type checking, coverage thresholds cover `tests/` identically to `athletecanvas/`

This principle extends to design: if a service cannot be tested with a fake adapter implementing a port, the port interface is wrong. Testability is a design signal.

#### Local dev setup

```
docker compose up -d  # starts PostgreSQL for local development
alembic upgrade head  # applies all pending migrations
```

`make dev` abstracts this. No local PostgreSQL installation required.

### Finding 3 — Project Onboarding & Reference Docs Technical Debt

**Decision: a single project README.md at repo root + a lean agent.md covering the full project. Reference docs scope-locked to AthleteCanvas. Addressed in a dedicated scaffolding child issue.**

#### The problem

A fresh agent or developer starting on this project today has no single entry point. `docs/coding_standards/` existed but referenced S1mpleTrader V3 throughout, linked to non-existent files (`TDD_WORKFLOW.md`, `GIT_WORKFLOW.md`, `docs/architecture/`, `docs/reference/`), and contained MCP server-specific guardrails from a different project. This creates immediate context pollution for any agent that reads these docs.

#### What good onboarding requires

1. **Root `README.md`** — one file, answers: what is this project, how do I run it locally, what is the architecture in one paragraph, where are the docs
2. **`agent.md`** — compact, no duplication with README. Links to coding standards, explains the MCP workflow, lists the epics. Agent context budget is limited — every redundant line is wasted
3. **`docs/coding_standards/`** — already cleaned up in this branch: S1mpleTrader refs removed, dode links removed, test code quality added, README rewritten as lean quick reference
4. **No orphaned reference docs** — removed all links to `TDD_WORKFLOW.md`, `GIT_WORKFLOW.md`, `docs/architecture/`, `docs/reference/`, `docs/implementation/` that do not exist

#### What remains to be done (scaffolding epic child issue)

- Root `README.md` — does not yet exist for AthleteCanvas
- `agent.md` — exists but needs a full review pass: remove S1mpleTrader context, align with new epic structure, add links to this foundational research and Epic 1 research

These are implementation tasks for the scaffolding child issue, not research findings. They are captured here to ensure they are not forgotten.

#### Principle: agent context is a scarce resource

`agent.md` must follow the same Config-over-Code principle applied to code: reference, don't duplicate. A 50-line `agent.md` that points to the right docs is more valuable than a 500-line `agent.md` that tries to contain everything and goes stale.

### Finding 4 — Unified Vector Storage & Hierarchical Rollups

**Decision: Deprecate external vector stores. Use pgvector with standard B-Tree indexes, Jinja2 deterministic serialization, and hierarchical rollups.**

#### Vector Storage & Indexing
External vector stores are completely deprecated to minimize infrastructure and eliminate split-brain syncing. Vectors are stored in `user_embeddings` alongside relational data. We explicitly avoid global HNSW indexes (which suffer from post-filtering recall loss). Instead, we rely on a standard B-Tree index on `user_uuid` to filter a specific user's records, followed by an exact Cosine Distance flat scan, which is extremely fast for personal-scale datasets (<10,000 activities).

#### Deterministic Text Serialization
Before vectorization, structured data (e.g., `TrackingRecord`) is converted into a natural language string using rigid, deterministic **Jinja2 templates** (e.g., combining activity type, duration, heart rate, and weather). This guarantees semantic stability in the 384-dimensional latent space of the static `all-MiniLM-L6-v2` model, preventing coordinate drift that dynamic serialization (via an LLM) would cause.

#### Hierarchical Vector Rollups
To support Retrieval-Augmented Generation (RAG) effectively over years of data, vectors are rolled up hierarchically:
- **Micro-scale**: Per-activity/per-record vectors.
- **Meso-scale**: "Week-Summary Vectors" generated dynamically at the end of each week.
- **Macro-scale**: "Block-Summary Vectors" representing entire training cycles.
The query path utilizes hierarchical retrieval (filtering macro-level first, zooming into meso-trends, and lastly retrieving micro-details).

#### 0-Day Opt-Out via RAG Shield
Because the generative LLM accesses user history purely via Retrieval-Augmented Generation (RAG), a user account deletion triggers an immediate database cascade delete of all relational data and vectors. The LLM instantly loses all context, creating a cryptographically hard 0-day opt-out shield without the need for model retraining.

### Finding 5 — Authentication & Identity: Delegated to Ory Kratos

**Decision: Ory Kratos handles all identity management. FastAPI is a pure resource server. Zero custom auth code.**

#### Why delegated identity, not DIY

Building authentication from scratch — WebAuthn registration flows, TOTP seed generation, refresh token rotation, account recovery — is high-risk, high-maintenance work that is not differentiating. Every hour spent on auth is an hour not spent on the core platform. More importantly, rolling custom auth is one of the most reliable ways to introduce security vulnerabilities (OWASP A07 Identification and Authentication Failures).

Ory Kratos is a self-hosted, open-source (Apache 2.0) identity and user management system written in Go. It is not a SaaS product — no paid dependency, no data leaving the infrastructure.

#### What Ory Kratos handles

- **Passkeys / WebAuthn** — primary MFA, FIDO2 compliant, device-bound credentials
- **TOTP** — fallback MFA (Google Authenticator, Authy), also used as account recovery codes
- **Registration & login flows** — Kratos exposes headless API flows; the React frontend drives the UI
- **Account recovery** — built-in recovery via email OTP or backup codes; no custom flow needed
- **Session management** — Kratos issues sessions; FastAPI validates them via the Ory `check` endpoint or JWT introspection
- **React Native** — `@ory/client` SDK works on React Native; no WebAuthn bridge required at the application layer

#### FastAPI as a pure resource server

FastAPI receives requests with a `Bearer` token or session cookie. It calls the Ory `toSession` endpoint (or validates a JWT signed by Ory) to verify identity. If valid, it extracts `user_uuid` from the token and proceeds. If not, it returns 401.

FastAPI owns **zero** user credentials, **zero** password hashes, **zero** WebAuthn state. The `users` table in PostgreSQL contains only application-level data: `user_uuid` (foreign key to Ory's identity ID), preferences, consent records, linked data-source tokens. No auth state lives in the application DB.

```
Client → Ory Kratos (login/register/MFA) → session token
Client → FastAPI (resource requests + Bearer token) → Ory /sessions/whoami → user_uuid → application logic
```

#### Third-party data source tokens (Garmin, Strava, etc.)

OAuth2 tokens for external data sources (Garmin SSO session via `garth`, Strava OAuth2, etc.) are **application-level** secrets, not identity credentials. They are stored encrypted in PostgreSQL under the `user_uuid`. Ory Kratos does not manage these — this is the application's responsibility.

Encryption at rest: AES-256-GCM, key from `AppConfig` (environment variable, never hardcoded). Token fields are encrypted before insert, decrypted after fetch — handled by a dedicated `ITokenStore` port.

#### No paid dependencies

All components are free and open-source:

| Component | License | Role |
|---|---|---|
| Ory Kratos | Apache 2.0 | Identity & MFA |
| Ory Hydra (optional) | Apache 2.0 | OIDC provider (if AthleteCanvas ever issues tokens to third parties) |
| `@ory/client` | MIT | React + React Native SDK |

Ory Cloud (the hosted SaaS version) is explicitly **not used**. Kratos runs as a Docker container alongside the application.

#### Mobile considerations

React Native uses `@ory/client` for all auth flows. The Kratos SDK handles passkey flows via platform APIs (iOS Face ID / Touch ID, Android Biometrics). On devices without biometric support, TOTP is the fallback. There is no custom WebAuthn bridge in the application layer.

### Finding 6 — Data Ingestion Architecture

**Decision: `TrackingRecord` as the universal domain envelope, `IDataSource` port per external source, hybrid PostgreSQL storage (fixed columns + JSONB payload), ARQ for background jobs, `garth` polling as the primary Garmin data path.**

#### The core principle: uniform pipeline, diverse payload

The ingestion pipeline has one job regardless of whether a GPS activity, a sleep record, a weight measurement, or a user settings sync arrives. The diversity lives in the payload, not in the pipeline. This separates two concerns that must not be entangled: *how data moves through the system* (pipeline) and *what the data looks like* (schema per type).

#### Domain model: `TrackingRecord`

`TrackingRecord` is the universal envelope. It is not "health data" — it is any data that is tracked over time for a user. The discriminator `record_type` determines how the payload is interpreted.

```
TrackingRecord
├── record_type: RecordType      # discriminator enum
├── user_uuid: UUID
├── source_id: str               # "garmin", "strava", "polar", "manual"
├── external_id: str             # source's own ID — deduplication key
├── recorded_at: datetime        # when the event occurred (not ingested)
├── ingested_at: datetime        # when we stored it
├── payload: dict                # type-specific data, Pydantic-validated
└── is_embeddable: bool          # whether this record goes to pgvector user_embeddings

RecordType:
  ACTIVITY       # GPS, HR, power, cadence, elevation
  SLEEP          # stages, HRV, SPO2, duration, score
  BODY_METRICS   # weight, body fat, VO2max, bone mass
  USER_SETTINGS  # HR zones, FTP, age, height, units preference
  USER_PROFILE   # static/sensitive: blood type, medical notes — encrypted
```

Pydantic discriminated unions validate the payload at ingestion boundary. If a payload does not conform to its declared `record_type` schema, it is rejected before touching PostgreSQL.

#### PostgreSQL storage: hybrid fixed + JSONB

A single `tracking_records` table with fixed columns for indexed/constrained fields and JSONB for the type-specific payload:

```sql
CREATE TABLE tracking_records (
    id            BIGSERIAL PRIMARY KEY,
    user_uuid     UUID NOT NULL REFERENCES users(user_uuid),
    record_type   TEXT NOT NULL,
    source_id     TEXT NOT NULL,
    external_id   TEXT NOT NULL,
    recorded_at   TIMESTAMPTZ NOT NULL,
    ingested_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
    payload       JSONB NOT NULL,
    UNIQUE (user_uuid, source_id, external_id)
);
```

The `UNIQUE (user_uuid, source_id, external_id)` constraint makes every sync operation idempotent: `INSERT ... ON CONFLICT DO NOTHING`. The same poll can run ten times without data corruption or duplicate records.

New `RecordType` values require no migration — only a new Pydantic model for payload validation, a corresponding `is_embeddable` rule, and (if indexed queries are needed on a payload field) an optional functional index on the JSONB column.

#### What goes to pgvector

Not all `TrackingRecord` types carry semantic meaning suitable for embedding:

| RecordType | Relational | pgvector |
|---|---|---|
| `ACTIVITY` | ✅ | ✅ semantic search, pattern matching |
| `SLEEP` | ✅ | ✅ longitudinal patterns |
| `BODY_METRICS` | ✅ | ❌ time series, no semantic value |
| `USER_SETTINGS` | ✅ | ❌ |
| `USER_PROFILE` | ✅ (encrypted fields) | ❌ |

`is_embeddable=True` on a `TrackingRecord` triggers automatic queuing for the embedding pipeline after PostgreSQL persist. The embedding pipeline is decoupled from ingestion — it reads from a queue, not from the ingestion path directly.

#### The `IDataSource` port

```python
class IDataSource(Protocol):
    source_id: str  # matches source_id in TrackingRecord

    async def fetch_since(
        self, user: UserContext, since: datetime
    ) -> list[RawRecord]: ...

    async def normalize(self, raw: RawRecord) -> TrackingRecord: ...

    async def check_connection(self, user: UserContext) -> ConnectionStatus: ...
```

The pipeline calls only this interface. Adding a new data source = one new adapter class implementing `IDataSource`. No pipeline changes, no new tables.

#### Garmin: Direct-First Priority & garth Bootstrapping

To protect user privacy and eliminate expensive middlemen, our primary strategic goal is securing direct, official API connections (such as the free Garmin Connect Developer Program). This minimizes user-facing costs and removes "man-in-the-middle" data brokers.

During the initial bootstrapping phase (while official business verification is pending), we may temporarily utilize simulated secure browser sessions (via `garth` in Python). We maintain the Charter's *Moral Moat* by **transparently communicating this mechanism to our users** during onboarding.

While simulated sync is active, we enforce hard limits via a **Smooth Flat Queue** to protect Garmin's resources:
- Activation-triggered, debounced sync (max once per 30 mins per user).
- Strict global concurrency lock of max 2 concurrent workers (flat average of ~2 requests per minute platform-wide).
- Jittered queue scheduling.

#### Background task queue: ARQ over Celery

ARQ (async-first Redis queue, MIT license) is chosen over Celery. Celery was designed for synchronous Python and adds broker-configuration complexity that does not fit the async FastAPI stack. ARQ integrates natively with `asyncio`, requires only Redis, and is sufficient for the load profile of a personal/small multi-user platform.

Three trigger paths for sync jobs:

| Trigger | Path | Notes |
|---|---|---|
| **Scheduled** | ARQ cron | Deprecated for simulated APIs (`garth`) to prevent IP bans ("Thundering Herd"). Reserved strictly for official webhooks or internal platform rollups. |
| **User-initiated** | `POST /sync/{source_id}` → enqueue → `202 Accepted` | UI "refresh" button |
| **Activation-based** | App foreground event → API call → enqueue | Debounced: max 1 job per user per source per 60s to prevent queue flooding |

#### Adapter implementation priority

1. **Garmin (Direct / Bootstrapped `garth` polling)** — first working demo; existing personal data available immediately
2. **Strava (OAuth2 + webhook)** — real-time, second largest activity dataset
3. **Polar / Fitbit / Withings** — same OAuth2 + webhook pattern as Strava; marginal cost per additional adapter is low once the webhook receiver infrastructure exists
4. **Apple Health / Google Health Connect** — native SDK adapters, mobile-only, separate epic

### Finding 7 — Secure Sharing & Anonymization Architecture

**Decision: Database-enforced RLS sharing, Defense-in-Depth Cryptographic Sharing (E2EE), and Secure Database Views for 0-day opt-out anonymization.**

#### Cryptographic Sharing Protection (Defense-in-Depth)
To mitigate the risk of a compromised `data_shares` table, we implement **End-to-End Encrypted (E2EE) Sharing** using public-key cryptography (libsodium/PyNaCl). All tracking data is encrypted at rest using a unique `user_data_key`. When User A shares with Coach B, User A's client encrypts the `user_data_key` with Coach B's public key and uploads it to `data_shares`. Attackers reading `data_shares` only gain raw ciphertexts.

To ensure absolute resilience against network and cryptographic threats, the following defense-in-depth layers are mandated:
- **MitM & CA Compromise:** Implement Out-of-Band (OOB) fingerprint verification for sharing setup. Prevent CA hijacking via DNS CAA records, Certificate Transparency (CT) monitoring, and strict Certificate Pinning in mobile apps.
- **Post-Quantum Cryptography (PQC) Transition:** While current symmetric data encryption (AES-256) is quantum-safe, the asymmetric key exchange prepares for a hybrid transition combining classical ECC (Curve25519) with ML-KEM (Kyber) to thwart "harvest now, decrypt later" attacks.

#### Aggregated Analytics (0-Day Opt-Out via Secure Views)
To solve the "Anonymization vs. Erasure Paradox", we use a **Secure Database View** combined with dynamic RLS:
- An `anonymized_research_data` View is exposed to the research role. This View strips out identifiers (`user_uuid`), buckets sensitive data, and joins `user_consent`.
- If a user toggles consent to `FALSE` (or deletes their account), their data instantly and dynamically vanishes from the research dataset in real-time (0-day opt-out).

### Finding 8 — Background Worker Security (Two-Tier System Consent)

**Decision: Background processes (like ARQ) use a uniform `data_shares` grant model, abandoning dynamic context switches.**

#### Uniform `data_shares` Approach
Rather than using dynamic session-level context-switching (`SET LOCAL app.current_user_id`), we unify background processing under the same **Dynamic Grant** model used for sharing. 
- The background worker has its own dedicated system UUID (`arq_background_worker`).
- During registration (or opt-in), a system-level share is written to `data_shares` granting the `arq_background_worker` access to the user's data.
- This ensures a single, uniform access control mechanism across the entire platform, making data exposure fully auditable in a single table.

#### Two-Tier System Consent
- **Tier 1: Private Storage (Default)**: Data is ingested and encrypted. No background processing or rollups are executed.
- **Tier 2: AI Insights (Opt-In)**: The user grants the `arq_background_worker` access to generate Meso/Macro rollups and embeddings, enabling the hierarchical RAG coach.

When opting into Tier 2, the user's client encrypts their user_data_key with the arq_background_worker's public key. The worker decrypts the tracking records strictly in-memory (using CIA-grade protections) to generate the deterministic Jinja2 string and calculate the embedding. It then saves only the irreversible 384-float vector to the database, ensuring the server disk never holds plaintext activity data.

### Finding 9 — Zero-Trust Operator Security

**Decision: Decentralized Private Key, CIA-grade memory protection, and local processing to eliminate server-side RAM scraping.**

#### Decentralized Operations
Administrative functions (like sending invite emails for the waitlist) are structurally designed to never expose clear-text sensitive data to the central server's long-term memory. The application server only stores Public Keys and Encrypted payloads.

The Operator uses a local secure environment (a dedicated client) holding the Private Key. When sending waitlist emails:
1. The server provides the encrypted email addresses.
2. The local Operator Client decrypts the batch in-memory.
3. Emails are dispatched directly from the local machine (or via a direct SMTP relay).
4. Memory is securely scrubbed immediately after processing (`mlock`, `memzero`). **CRITICAL:** Because standard Python strings are immutable, plaintext emails must be processed using strictly mutable memory buffers (e.g., `bytearray` or `ctypes`). For high-value deployments, this decryption script must execute within a Hardware Trusted Execution Environment (TEE, e.g., Intel SGX / AMD SEV).

This model ensures that even if a hacker achieves root access and active memory scraping on the central server, the most valuable data (e.g., highly sensitive user contact info) remains inaccessible.

### Finding 10 — Deferred Work Notes (Branch Hygiene)

**Decision: Maintain strict branch hygiene on `epic/16`. Necessary updates to other epics are deferred until their respective branches are active.**

To prevent out-of-scope modifications on the current branch, the following critical updates are deferred and logged here. The Standalone Research Agent (`@research`) must execute these updates immediately upon checking out the respective branches:

- **Epic 1 (Data Fundament):** Update `docs/planning/issue1/planning.md` and `docs/planning/issue1/research.md`. Remove all references to SQLite and ChromaDB. Replace them with PostgreSQL, `pgvector`, SQLAlchemy Core, and Alembic as the single, unified source of truth.
- **Epic 18 (Marketing Site / Waitlist):** Update `docs/planning/issue18/research.md`. Implement the **Constant-Time Execution** requirement for subscribe/unsubscribe endpoints to prevent Waitlist Timing Attacks (using dummy operations and fixed response paddings). Ensure the Zero-Trust Offline Operator Decryption architecture (Finding 9) is fully integrated.

## Related Documentation
- **[docs/planning/issue1/research.md][related-1]**
- **[docs/planning/issue1/planning.md][related-2]**
- **[docs/coding_standards/README.md][related-3]**

<!-- Link definitions -->

[related-1]: docs/planning/issue1/research.md
[related-2]: docs/planning/issue1/planning.md
[related-3]: docs/coding_standards/README.md

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 |  | Agent | Initial draft |
| 1.1 | 2026-03-07 | Agent | Major architectural refactor: pgvector, RLS, Zero-Trust, E2EE sharing, and Deferred Notes |
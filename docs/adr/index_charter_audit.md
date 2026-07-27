# Architectural Decision Records (ADRs) vs Ypsia Charter Audit

This document is a living audit that maps all accepted and proposed ADRs against the foundational principles defined in `CHARTER.md` to ensure absolute alignment. The records are grouped by domain and level according to the **2D Taxonomy (Domain x Level)**.

---

## 1. Data & Storage Layer (1000-reeks)

### Strategic (1000 - 1499)

#### ADR 1000: Unified Sovereign Storage & Deployment Flexibility
- **Level:** Strategic
- **Decision:** PostgreSQL + pgvector + RLS + JSONB.
- **Audit:** ✅ **PASS**.
- **Rationale:** By using RLS (Row-Level Security) at the database kernel level, we ensure mathematically enforced tenant isolation. Keeping vector storage inside the exact same database (via `pgvector`) prevents data from leaking to third-party AI cloud services.

#### ADR 1001: Schemaless Domain Payload Implementation
- **Level:** Strategic
- **Decision:** JSONB (Binary JSON) Document Store over EAV or Protobuf.
- **Audit:** ✅ **PASS**.
- **Rationale:** JSONB proves to be the only architecture that combines infinite extensibility with high-speed queryability within a single Postgres instance.

#### ADR 1002: Universal Data Envelope (TrackingRecord Schema)
- **Level:** Strategic
- **Decision:** Hybrid Schema (Fixed Columns + JSONB Payload) with Strict Pydantic Boundary Validation.
- **Audit:** ✅ **PASS**.
- **Rationale:** Enables true domain agnosticism. Ypsia can ingest highly sensitive corporate finance data, IoT telemetry, and health metrics without the core database ever needing to "know" what the data means.

#### ADR 1003: Sovereign Multi-Modal Storage & Progressive Escalation
- **Level:** Strategic
- **Decision:** Progressive Storage Escalation (Local Disk -> Distributed) with Crypto-Shredding via PostgreSQL keys.
- **Audit:** ✅ **PASS**.
- **Rationale:** Resolves the tension between petabyte scalability (multi-modal media) and the single-vault Zero-Leakage guarantee.

#### ADR 1004: Multi-Scale Ephemeral Search Projections
- **Level:** Strategic
- **Decision:** CQRS-gebaseerde multi-scale indexeringsarchitectuur met ephemere read-projecties.
- **Audit:** ✅ **PASS**.
- **Rationale:** Disconnects historical base record immutability from derived search indexes, guaranteeing zero data destruction while enabling multi-scale retrieval.

---

## 2. Security & Identity Layer (2000-reeks)

### Strategic (2000 - 2499)

#### ADR 2000: Delegated Identity Management & B2B Federation
- **Level:** Strategic
- **Decision:** Self-hosted Identity Server (e.g., Ory Kratos) decoupling authentication from the core API.
- **Audit:** ✅ **PASS**.
- **Rationale:** Prevents Big Tech Identity SDKs (Google/Microsoft) from accessing the core data engine, honoring the Zero-Trust principle.

#### ADR 2001: Abstracted Credential Vault & Radical Transparency
- **Level:** Strategic
- **Decision:** Abstracting token encryption logic from ingestion, paired with Radical Transparency UI.
- **Audit:** ✅ **PASS**.
- **Rationale:** Refuses to let present-day cryptographic compromises permanently dictate the architecture.

---

## 3. Integration Layer (3000-reeks)

### Strategic (3000 - 3499)

#### ADR 3000: Direct-First Ingestion & Transparent Bootstrapping
- **Level:** Strategic
- **Decision:** Agnostic Hexagonal Ingestion rejecting commercial data brokers, with ethical simulated fallback.
- **Audit:** ✅ **PASS**.
- **Rationale:** Using data brokers violates the core directive of removing the 'man-in-the-middle'. We enforce Direct-First.

---

## 4. Intelligence (AI) Layer (4000-reeks)

### Strategic (4000 - 4499)

#### ADR 4000: Pluggable Brain & Multi-Faceted Semantic Translation
- **Level:** Strategic
- **Decision:** Abstracted Deterministic Serialization with Multi-Perspective Rendering.
- **Audit:** ✅ **PASS**.
- **Rationale:** Enforces deterministic vector stability, preventing "coordinate drift" caused by generative LLMs.

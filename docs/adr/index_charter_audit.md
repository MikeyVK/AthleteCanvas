# Architectural Decision Records (ADRs) vs Ypsia Charter Audit

This document is a living audit that maps all accepted ADRs against the foundational principles defined in the `CHARTER.md` to ensure absolute alignment. The records are grouped by architectural domain.

## 1. Data & Storage Layer (1000-reeks)

### ADR 1000: Unified Sovereign Storage & Deployment Flexibility
- **Decision:** PostgreSQL + pgvector + RLS + JSONB.
- **Audit:** ✅ **PASS**.
- **Rationale:** By using RLS (Row-Level Security) at the database kernel level, we ensure mathematically enforced tenant isolation. Keeping vector storage inside the exact same database (via `pgvector`) prevents data from leaking to third-party AI cloud services. Finally, a single unified database ensures the 'Host it yourself' principle remains accessible for individuals and SMEs.

### ADR 1001: Schemaless Domain Payload Implementation
- **Decision:** JSONB (Binary JSON) Document Store over EAV or Protobuf.
- **Audit:** ✅ **PASS**.
- **Rationale:** JSONB proves to be the only architecture that combines infinite extensibility with high-speed queryability within a single Postgres instance. Rejecting EAV prevents catastrophic performance degradation at scale, while rejecting Protobuf ensures the database is not blind to the user's data.

### ADR 1002: Universal Data Envelope (TrackingRecord Schema)
- **Decision:** Hybrid Schema (Fixed Columns + JSONB Payload) with Strict Pydantic Boundary Validation.
- **Audit:** ✅ **PASS**.
- **Rationale:** Enables true domain agnosticism. Ypsia can ingest highly sensitive corporate finance data, IoT telemetry, and health metrics without the core database ever needing to "know" what the data means. This infinite flexibility guarantees the platform can serve as a lifelong, universal intelligence engine without breaking schemas or forcing domain-specific rules onto the user.

### ADR 1003: Sovereign Multi-Modal Storage & Progressive Escalation
- **Decision:** Progressive Storage Escalation (Local Disk -> Distributed) with Crypto-Shredding via PostgreSQL keys.
- **Audit:** ✅ **PASS**.
- **Rationale:** Resolves the tension between petabyte scalability (multi-modal media) and the single-vault Zero-Leakage guarantee. By ensuring media is encrypted with keys managed by Postgres RLS, account deletion mathematically shreds the media files regardless of where they are stored. The progressive escalation (starting with Local Disk) perfectly honors the 'Host it yourself' simplicity requirement.

## 2. Security & Identity Layer (2000-reeks)

### ADR 2000: Delegated Identity Management & B2B Federation
- **Decision:** Self-hosted Identity Server (e.g., Ory Kratos) decoupling authentication from the core API.
- **Audit:** ✅ **PASS**.
- **Rationale:** Prevents Big Tech Identity SDKs (Google/Microsoft) from accessing the core data engine, honoring the Zero-Trust principle. Simultaneously enables frictionless federation for enterprise adoption without compromising individual sovereignty.

### ADR 2001: Abstracted Credential Vault & Radical Transparency
- **Decision:** Abstracting token encryption logic from ingestion, paired with Radical Transparency UI.
- **Audit:** ✅ **PASS**.
- **Rationale:** We refuse to let present-day cryptographic compromises permanently dictate the architecture. The abstraction allows for future upgrades to Secure Enclaves/MPC. The Radical Transparency mandate ensures the user is *always* informed of the exact security implications of syncing a 3rd-party integration.

## 3. Integration Layer (3000-reeks)

### ADR 3000: Direct-First Ingestion & Transparent Bootstrapping
- **Decision:** Agnostic Hexagonal Ingestion rejecting commercial data brokers, with ethical simulated fallback.
- **Audit:** ✅ **PASS**.
- **Rationale:** Using data brokers (like Vital API) violates the core directive of removing the 'man-in-the-middle'. We enforce Direct-First (official APIs). Where simulated bootstrapping is used, we protect the external provider's infrastructure with strict traffic-shaping (respecting their resources) and inform the user transparently.

## 4. Intelligence (AI) Layer (4000-reeks)

### ADR 4000: Pluggable Brain & Multi-Faceted Semantic Translation
- **Decision:** Abstracted Deterministic Serialization with Multi-Perspective Rendering.
- **Audit:** ✅ **PASS**.
- **Rationale:** Enforces deterministic vector stability, preventing "coordinate drift" caused by generative LLMs. By allowing the same data to be viewed through varying lenses (e.g., financial, physiological, behavioral), the AI builds a holistic, honest reflection of the user's reality, rather than a gamified highlight reel. Guaranteed technology-agnostic to support BYOAI.

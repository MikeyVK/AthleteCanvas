<!-- docs\development\issue16\research.md -->
<!-- template=research version=8b7bb3ab created=2026-07-11T20:35Z updated= -->
# Epic 16: Foundational Architecture & Friction Points Evaluation

**Status:** APPROVED  
**Version:** 1.0  
**Last Updated:** 2026-07-11

---

## Purpose

To document the approved architectural strategies across multiple domains before starting execution.

---

## Problem Statement

Evaluate architectural friction points across the data layer, background workers, security boundaries, and ingestion pipelines to establish a consistent foundation for Ypsia.

## Research Goals

- Determine storage and isolation model (pgvector vs ChromaDB)
- Define background worker data access security (data_shares)
- Establish waitlist and zero-trust private key constraints
- Decide on Garmin ingestion architecture (Smooth Flat Queue vs Aggregators)
- Establish secure sharing and anonymization architecture

---

## Findings

### 1. ChromaDB vs. pgvector (PostgreSQL RLS)

* **Status:** APPROVED
* **Core Proposal:** 
  - Deprecate ChromaDB completely.
  - Store all vector embeddings in a single PostgreSQL table (`user_embeddings`) under the same instance as relational data.
  - Implement data isolation via **PostgreSQL Row-Level Security (RLS)** using `user_uuid`.
  - Avoid global HNSW indexes for now to bypass post-filtering recall loss. Rely instead on a standard B-Tree index on `user_uuid` to filter a user's records, followed by an exact Cosine Distance flat scan (extremely fast for $<10,000$ activities per user).
* **Extended Context & Internal Mechanics:**
  - **Deterministic Text Serialization**: Before vectorization, structured data (e.g. `TrackingRecord`) is converted into a natural language string using rigid, deterministic **Jinja2 templates** (e.g., combining activity type, duration, heart rate, and weather). This guarantees semantic stability in the 384-dimensional latent space of the static `all-MiniLM-L6-v2` model, preventing coordinate drift that dynamic serialization (like using an LLM or MoE) would cause.
  - **Hierarchical Vector Rollups**: The vector storage schema must support multiple granularities of context:
    - *Micro-scale*: Per-activity/per-record vectors.
    - *Meso-scale*: "Week-Summary Vectors" generated dynamically or asynchronously at the end of each week.
    - *Macro-scale*: "Block-Summary Vectors" representing training cycles.
    The query path utilizes hierarchical retrieval (filtering at the macro-level first, then zooming into meso-trends, and lastly retrieving micro-details).
  - **Background Worker RLS Security (Uniform data_shares Approach)**: Rather than using dynamic session-level context-switching (`SET LOCAL app.current_user_id`), we unify background processing under the same **Dynamic Grant** model used for sharing. 
    - The background worker has its own dedicated system UUID (`arq_background_worker`).
    - During registration, a system-level share is written to `data_shares` granting the `arq_background_worker` access to the user's data.
    - This ensures a single, uniform access control mechanism across the entire platform, making data exposure fully auditable in a single table and allowing users to opt-out of background rollups by simply revoking the share.
  - **0-Day Opt-Out via RAG Shield**: The generative LLM (`all-MiniLM-L6-v2` is static and never trained on user logs) accesses user history purely via Retrieval-Augmented Generation (RAG). Because data lives under PostgreSQL, a database `DELETE` instantly and permanently removes the underlying data and vectors. In the next RAG retrieval step, the query returns empty, establishing a cryptographically hard 0-day opt-out shield without needing model retraining.
* **Decisions / Open Points:**
  - *Fully approved and aligned on pgvector, Jinja2 serialization, hierarchical rollups, and uniform data_shares for background workers.*

---

### 2. Documento "Split-Brain" Alignment

* **Status:** DEFERRED (Branch Hygiene Protection)
* **Core Proposal:** 
  - To preserve strict Git branch hygiene on `epic/16-foundational-architecture`, we **do not** modify `docs/development/issue1/` files directly within this branch.
  - Instead, we record a **Deferred Work Note** in the Issue 16 PR/Handover context.
  - Upon merging Issue 16 to `main`, the `@co` (coordination) agent will automatically intercept this note, update the active GitHub Issue #1 body with the revised requirements, and perform the documentation refactor (`issue1/research.md` and `issue1/planning.md`) as the very first step of the Epic 1 execution branch.
* **Decisions / Open Points:**
  - *Deferred plan accepted. No file modifications to Issue 1 will occur on this branch.*

---

### 3. Waitlist Timing Attacks (Issue 18)

* **Status:** DEFERRED (Branch Hygiene Protection)
* **Core Proposal:**
  - Enforce constant-time execution on the subscribe/unsubscribe endpoints by performing dummy operations (HMAC calculations and mock database writes/updates) on the "miss" path, and padding responses to a minimum time window (e.g., 50ms).
  - To maintain branch hygiene, **no** direct modifications to `docs/development/issue18/` will occur on the `epic/16` branch.
  - A **Deferred Work Note** will be logged for Issue 18. Upon checkout of Issue 18, the executing agent will refactor `issue18/research.md` to incorporate the constant-time execution requirements.
* **Decisions / Open Points:**
  - *Deferred plan accepted. No file modifications to Issue 18 will occur on this branch.*

---

### 4. Decentralized Private Key (Zero-Trust Waitlist)

* **Status:** DEFERRED (Branch Hygiene Protection)
* **Core Proposal:**
  - Keep the operator private key completely off the server.
  - The VPS stores only sealed ciphertexts.
  - The operator executes email delivery locally on a secure laptop via a Python script, downloading the ciphertexts, decrypting them locally, sending them via SMTP, and invoking a purge endpoint.
  - **CIA-Grade Client Memory Protection**: To prevent RAM-scraping attacks on the operator's machine during local decryption, the launch script must implement secure in-memory handling:
    - *No Immutable Strings*: Plaintext emails are processed strictly in mutable memory buffers (e.g., `bytearray` or `ctypes` character arrays).
    - *Memzero Overwrite*: Immediately after the SMTP transaction for a specific email completes, the memory buffer holding the plaintext address is explicitly overwritten with zeroes (`memzero`) in RAM, eliminating garbage-collector delays.
    - *Memory Locking (mlock)*: Lock the process RAM pages containing the private key and plaintext buffers using `mlock` to prevent the OS from writing them to swap files/pagefiles on disk.
    - *Enclave/TEE support*: For high-value deployments, run the decryption script within a Hardware Trusted Execution Environment (TEE) like Intel SGX or AMD SEV to encrypt process memory at the hardware level.
* **Decisions / Open Points:**
  - *Deferred plan accepted. Zero-trust local decryption and secure memory architecture approved for Issue 18.*

---

### 5. Garmin API "Thundering Herd" Polling

* **Status:** APPROVED (Provider-Agnostic, Direct-First Model)
* **Core Proposal:**
  - **API-Agnostic Hexagonal Adapter Design**: The core domain ingestion architecture is designed to be provider-agnostic. We define a generalized `HealthDataIngestionPort` that maps fitness/wellness metrics (activities, HRV, sleep, heart rate, stress) into a standardized internal data format. Specific providers (Garmin, Apple Health, Fitbit) are implemented purely as interchangeable adapters.
  - **Direct-First Strategic Priority**: To protect user privacy and eliminate expensive middlemen, our primary strategic goal is securing direct, official API connections (such as the free Garmin Connect Developer Program). This minimizes user-facing costs and removes "man-in-the-middle" data brokers.
  - **Transparent Bootstrapping Phase**: During the initial bootstrapping phase (while official business verification is pending or being processed), we may temporarily utilize simulated secure browser sessions (via `garth` in Python). We maintain the Charter's *Moral Moat* by **transparently communicating this mechanism to our users** during onboarding:
    > *"We strive to establish direct, secure, and officially authorized connections with device manufacturers to keep your costs as close to zero as possible. During our early bootstrap phase, we temporarily utilize a secure browser simulation to retrieve your Garmin logs, which will transition to direct API access as our official authorization is finalized."*
  - **Strict Traffic-Shaping (Smooth Flat Queue)**: While simulated sync is active, we enforce hard limits to protect Garmin's resources:
    - Activation-triggered, debounced sync (max once per 30 mins per user).
    - Strict global concurrency lock of max 2 concurrent workers (flat average of ~2 requests per minute platform-wide).
    - Jittered queue scheduling.
  - **Managed Aggregators (Research Only)**: Third-party health aggregators (like Vital API) are relegated to future research candidates for supporting long-tail devices, provided their data routing complies with Ypsia's privacy and encryption standards.
* **Decisions / Open Points:**
  - *Approved. Aligns Ypsia's ingestion architecture with clean domain-driven design, user transparency, cost minimization, and direct integration principles.*

---

### 6. Secure Sharing and Anonymization Architecture

* **Status:** APPROVED
* **Core Proposal:**
  - **Individual Sharing (Coach / B2B)**: Enforce access control at the PostgreSQL database level by dynamically expanding the RLS (Row-Level Security) policies to check a `data_shares` permission table. If a share is revoked or expires, access is blocked at the database kernel.
  - **Cryptographic Sharing Protection (Defense-in-Depth)**: To mitigate the risk of a compromised `data_shares` table (where an attacker inserts arbitrary rows to leak data), we implement **End-to-End Encrypted (E2EE) Sharing** using public-key cryptography (libsodium/PyNaCl):
    - All tracking data is encrypted at rest using a symmetric key (`user_data_key`) unique to the user.
    - When User A shares with Coach B, User A's client encrypts the `user_data_key` with Coach B's public key and uploads it to `data_shares`.
    - If an attacker inserts a rogue row in `data_shares`, they only gain access to raw ciphertexts. Without the data key encrypted for their public key, they cannot decrypt the data.
  - **Client Endpoint Compromise Mitigation**:
    - **Granular Scope**: The user limits shares to specific scopes (e.g. `activities` only, excluding sensitive `wellness` or `journal` records).
    - **Time-bounding**: Every share enforces a strict expiration (`expires_at`), limiting the exposure window.
    - **Ephemeral/Biometric Re-auth**: The coach's client requires local WebAuthn/Passkey re-authentication to unlock the private key stored in secure local storage, preventing raw cookie-stealing attacks.
  - **MitM Protection (Key Fingerprints)**: Leverage Out-of-Band (OOB) fingerprint verification (e.g., verifying a cryptographic hash of public keys via a QR code or phone call) for sharing, bypassing DNS/TLS hijacking risks.
  - **CA Compromise Mitigation (Defense-in-Depth)**:
    - **CAA Records**: Restrict certificate issuance at the DNS layer to trusted CAs only (e.g., Let's Encrypt).
    - **Certificate Transparency (CT) Monitoring**: Actively monitor CT logs to detect unauthorized certificates issued for `ypsia.nl`.
    - **Certificate Pinning**: Force mobile applications to validate the server's public key certificate pin, bypassing the compromised trust chain of default CAs.
  - **Post-Quantum Cryptography (PQC) Transition**:
    - **Symmetric Data Security**: Raw database records are encrypted via ChaCha20/AES-256, which are quantum-safe (Grover's algorithm only reduces their security to a still-unbreakable 128-bits).
    - **Hybrid Key Exchange**: Future transition of public-key sharing exchange to a hybrid model combining Curve25519 (classical ECC) with **ML-KEM** (Kyber - post-quantum KEM), securing traffic against "harvest now, decrypt later" attacks.
  - **Two-Tier System Consent (Background Rollups)**:
    - *Tier 1: Private Storage (Default)*: Data is ingested and encrypted. No background processing or rollups are executed.
    - *Tier 2: AI Insights (Opt-In)*: The user grants the `arq_background_worker` access to generate Meso/Macro rollups and embeddings. This enables the hierarchical RAG coach.
  - **Aggregated Analytics (Research / Opt-Out)**: Solve the "Anonymization vs. Erasure Paradox" using a **Secure Database View** combined with dynamic RLS:
    - Raw data remains in the user's secure table (cascading deletes and RLS apply).
    - Consent is stored in a `user_consent` table.
    - An `anonymized_research_data` View is exposed to the research role. This View strips out identifiers (`user_uuid`), buckets sensitive data (ages, time zones), and joins `user_consent`.
    - If a user toggles consent to `FALSE` (or deletes their account), their data instantly and dynamically vanishes from the research dataset in real-time.
* **Decisions / Open Points:**
  - *Aligned on View-based dynamic anonymization, uniform `data_shares` for background workers, E2EE cryptographic sharing, client-side compromise mitigation, MitM OOB verification, CA compromise protections, PQC transition strategy, and the Two-Tier system consent model for background rollups.*

---

## Approved Strategy

Direct-first API strategy, pgvector RLS isolation, uniform background worker data_shares, and strict branch hygiene via Deferred Work Notes.

## Related Documentation
None
---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-11 | Agent | Initial draft with foundational friction points evaluated |
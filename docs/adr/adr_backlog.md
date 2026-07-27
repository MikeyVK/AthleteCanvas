# ADR Backlog (Work in Progress & Candidates)

This backlog tracks upcoming architectural decisions for Ypsia that are currently under research, draft, or discussion. It is strictly mapped to the **2D Taxonomy (Domain x Level)**.

*Note: Accepted ADRs are moved to `docs/adr/index_charter_audit.md` to maintain DRY alignment.*

---

## 0. Core System Invariants (0000 - 0999)
*Ononderhandelbare technische wetten, direct afgeleid van het Sovereign Charter.*

### 📌 Candidate: Zero-Leakage & Sovereignty Boundary Mandate (ADR 0001)
- **Level:** Strategic Invariant (0000 - 0499)
- **Priority:** High.
- **Context:** Dicteert dat PII of unencrypted payload-data fysiek nooit de soevereine grens van de installatie mag overschrijden.

### 📌 Candidate: Cryptographic Erasure & Mathematical Right-to-be-Forgotten (ADR 0002)
- **Level:** Strategic Invariant (0000 - 0499)
- **Priority:** High.
- **Context:** Dicteert dat het verwijderen van een gebruikerssleutel alle afgeleide/externe data onmiddellijk en onomkeerbaar cryptografisch vernietigt (Crypto-Shredding).

---

## 1. Data & Storage Layer (1000-reeks)

### 📌 Candidate: Continuous Layer Propagation & Temporal Indexing (ADR 1502)
- **Level:** Tactical (1500 - 1999)
- **Priority:** High.
- **Context:** The implementation details of the *Indexing Engine* (tactische tegenhanger van ADR 1004). Defines how we structure retrieval efficiently using rolling windows, pgvector, and (optionally) Matryoshka dimension truncation to bypass LLM context limits.
- **Key Concepts:** Rolling windows, continuous layer propagation, B-Tree + Exact Cosine.

---

## 2. Security & Identity Layer (2000-reeks)

### 📌 Candidate: E2EE Sharing, System Consent & 0-Day Opt-Out (ADR 2002)
- **Level:** Strategic (2000 - 2499)
- **Priority:** High.
- **Context:** Hoe gebruikers veilig data delen met coaches (End-to-End Encryption) en hoe we geanonimiseerde data-aggregatie faciliteren zónder de Zero-Leakage belofte te breken.
- **Key Concepts:** The Anonymization vs. Erasure Paradox, System Consent for background workers.

### 📌 Candidate: Decentralized Cryptographic Administration (ADR 2003)
- **Level:** Strategic (2000 - 2499)
- **Priority:** Medium.
- **Context:** (Voortgekomen uit de Zero-Trust Waitlist operator security). Hoe platformbeheerders opereren zónder de centrale VPS de masterkeys te geven.

### 📌 Candidate: Post-Quantum Cryptography & Dynamic RLS Views (ADR 2501)
- **Level:** Tactical (2500 - 2999)
- **Priority:** High.
- **Context:** De concrete technologische implementatie (het gereedschap) behorende bij ADR 2002. 
- **Key Concepts:** libsodium/PyNaCl, Kyber ML-KEM transitie, PostgreSQL Secure Views.

### 📌 Candidate: Zero-Leakage API Surface & Constant-Time Boundaries (ADR 2502)
- **Level:** Tactical (2500 - 2999)
- **Priority:** Medium.
- **Context:** (Voortgekomen uit Waitlist Timing Attacks). Hoe we voorkomen dat publieke endpoints de status of identiteit van een gebruiker lekken.
- **Key Concepts:** Constant-time execution, dummy cryptographic operations.

---

## 3. Integration Layer (3000-reeks)
*(Momenteel geen openstaande items. Direct-First Ingestion is afgedekt in ADR 3000).*

---

## 4. Intelligence (AI) Layer (4000-reeks)

### 📌 Candidate: The Cognitive Lenses Contract (ADR 4001)
- **Level:** Strategic (4000 - 4499)
- **Priority:** High.
- **Context:** Defines the core Domain contract for AI retrieval. How the application asks the Intelligence component for insights (Causality, Anomaly, Goal) completely isolated from indexing tech.

### 📌 Candidate: The BYOAI / Local LLM Integration Layer (ADR 4500)
- **Level:** Tactical (4500 - 4999)
- **Priority:** High.
- **Context:** De concrete inrichting van de Embedding en Retrieval adapter. Definieert de integratie van lokale open-source modellen (bijv. Qwen3/Nomic) versus cloud-API's (LiteLLM) met waarborging van Zero-Leakage.

### 📌 Candidate: Lens Query Execution & Context Assembly (ADR 4501)
- **Level:** Tactical (4500 - 4999)
- **Priority:** Medium.
- **Context:** De tactische tegenhanger van ADR 4001. Definieert hoe de retrieval engine context windows bouwt en prompts assembleert per Cognitive Lens.

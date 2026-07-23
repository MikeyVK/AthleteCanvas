<!-- docs\adr\0004-e2ee-sharing-and-anonymization.md -->
<!-- template=adr version=b4627a40 created=2026-07-22T21:08Z updated= -->
# 0004: E2EE Sharing, System Consent & 0-Day Opt-Out Anonymization

**Status:** ACCEPTED  
**Version:** 1.1.0  
**Last Updated:** 2026-03-08  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

Users need to share data with coaches securely, and the platform requires access to data for internal AI background rollups and anonymized research. This must be done without compromising the Zero-Trust mandate, ensuring that revoked consent instantly removes data access (Anonymization vs. Erasure Paradox).

### Decision Drivers

- Defense-in-Depth Cryptography against database compromise
- 0-Day Opt-Out compliance
- Uniform access model for Background Workers

---

## Considered Options

### Option 1: E2EE data_shares and Secure Views (Chosen)

**Pros (+):**
- A rogue row in `data_shares` yields only undecryptable ciphertexts.
- Background worker access is auditable and revocable.
- Toggling consent dynamically drops the user's rows from the Analytics View instantly (0-day opt-out).

**Cons (-):**
- High cryptographic complexity on the client side (key management).

### Option 2: Server-Side Decryption with RLS Only

**Pros (+):**
- Much simpler client architecture.

**Cons (-):**
- A compromised application server or database admin has full access to plaintext health data.
- Violates the absolute Data Sovereignty clauses in the Charter.


---

## Decision Outcome

**Chosen Option:** Option 1: E2EE data_shares and Secure Views

### Rationale

E2EE ensures the server cannot transparently share data without client-side cryptographic intent. By treating the arq_background_worker as a virtual \"coach\" in the data_shares table, we unify Tier-2 AI consent. For anonymization, dynamic Secure Views instantly exclude records upon consent revocation, ensuring the 0-Day Opt-Out guarantee is mathematically enforced.

---

## Consequences

### Positive Consequences (+)

- CIA-grade defense-in-depth against database leaks.
- Prepares architecture for Post-Quantum Cryptography (PQC) transitions (e.g., Kyber).

### Negative Consequences & Risks (-)

- High cryptographic complexity on the client side (key management).
- Background AI rollups require the worker to decrypt data in memory securely to generate embeddings.

### Agent Implementation Guardrails

- Agents MUST NOT write plaintext user tracking payloads to the data_shares table.
- Agents MUST query aggregated analytical data exclusively through the consent-joined Secure Views, NEVER directly from the raw tracking tables.
- Agents MUST treat the arq_background_worker as a standard entity in the data_shares table to authorize background rollups (No BYPASSRLS superuser flags).
- Agents MUST enforce network defense-in-depth for sharing operations, including Out-of-Band (OOB) fingerprinting, Certificate Pinning, and prepare interfaces for hybrid Post-Quantum Cryptography (ML-KEM / Kyber).


---

## Confirmation & Verification

Verified via security audits of the E2EE key exchange and integration tests confirming view exclusions upon consent toggle.

## Related Documentation
- **[docs/development/issue16/research.md][related-1]**

<!-- Link definitions -->

[related-1]: docs/development/issue16/research.md

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-03-08 | Agent | Initial draft |
| 1.1.0 | 2026-07-22 | Agent | Added OOB fingerprinting, Certificate Pinning, and PQC transition guardrails |
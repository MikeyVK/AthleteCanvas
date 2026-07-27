<!-- docs\adr\2001-abstracted-credential-vault.md -->
<!-- template=adr version=b4627a40 created=2026-07-23T19:20Z updated= -->
# 2001: Abstracted Credential Vault & Radical Transparency

**Status:** ACCEPTED  
**Version:** 1.0.0  
**Last Updated:** 2026-07-23  
**Level:** Strategic  
**Category:** Security & Identity  
**Tags:** security, cryptography, transparency  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

Integrating external data providers (e.g., Enterprise CRMs, Financial Institutions, IoT platforms, Personal Data Vaults) requires storing 3rd-party OAuth tokens. The current technological landscape forces a compromise between absolute zero-trust security (E2EE, which prevents background ingestion) and usability (Server-side encryption). We refuse to let present-day technological limitations permanently dictate our architecture or compromise our Sovereign Charter. Furthermore, users must never be kept in the dark regarding the cryptographic reality of their data connections.

### Decision Drivers

- Maximize security without permanently sacrificing usability (background sync).
- Ensure the architecture can seamlessly upgrade to future cryptographic paradigms (Secure Enclaves, MPC, Homomorphic Encryption).
- Absolute adherence to the Charter's demand for data sovereignty.
- Radical transparency: Users must fully understand the security implications of any integration they enable.

---

## Considered Options

### Option 1: Abstracted Vault Interface + Radical Transparency (Chosen)

**Pros (+):**
- Future-proofs the codebase.
- Allows upgrading encryption paradigms without rewriting core ingestion logic.
- Honors the user through total transparency.

**Cons (-):**
- Requires strict interface boundaries in the codebase.

### Option 2: Hardcode a specific encryption strategy (e.g., Server-Side AES-256)

**Pros (+):**
- Faster to implement initially.

**Cons (-):**
- Technical debt.
- Locks the platform into current cryptographic limitations.
- Risks violating zero-trust principles without an easy upgrade path.


---

## Decision Outcome

**Chosen Option:** Option 1: Abstracted Vault Interface + Radical Transparency

### Rationale

By defining the Credential Vault as an abstract boundary, the core ingestion engine remains ignorant of how tokens are encrypted. It simply requests authenticated access from the Vault. This decouples our architecture from present-day cryptographic compromises. Coupled with Radical Transparency, we ensure that whatever vault implementation is currently active (e.g., AES-256 today, Secure Enclaves tomorrow), the UI explicitly communicates the exact security implications and risks to the user. This empowers the user to make an informed sovereign choice.

---

## Consequences

### Positive Consequences (+)

- Architecture is immune to cryptographic obsolescence.
- Unmatched trust built with users via radical transparency.

### Negative Consequences & Risks (-)

- Increased architectural overhead to maintain the vault abstraction layer.

### Agent Implementation Guardrails

- Agents MUST NOT hardcode encryption logic directly within the data ingestion workers or core API. All token handling MUST be routed through the abstract Vault interface.
- Agents MUST ensure that the UI/API layers provide clear, unvarnished warnings about the cryptographic implications (risks and benefits) of any 3rd-party connection.
- Agents MUST NOT store external API tokens in plaintext under any circumstances.


## Related Documentation
None
---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-23 | Agent | Initial draft |
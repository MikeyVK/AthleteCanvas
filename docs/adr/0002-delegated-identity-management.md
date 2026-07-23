<!-- docs\adr\0002-delegated-identity-management.md -->
<!-- template=adr version=b4627a40 created=2026-07-22T21:08Z updated= -->
# 0002: Delegated Identity Management via Ory Kratos

**Status:** ACCEPTED  
**Version:** 1.0.0  
**Last Updated:** 2026-03-08  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

Implementing secure authentication (WebAuthn, Passkeys, TOTP, account recovery) from scratch is a high-risk vector for security vulnerabilities (OWASP A07). ypsia needs a robust identity management system that does not leak data to SaaS providers.

### Decision Drivers

- Absolute security and mitigation of OWASP auth vulnerabilities
- Support for modern authentication (Passkeys/WebAuthn/FIDO2)
- Data sovereignty (No third-party SaaS lock-in like Auth0 or Firebase)
- Zero-Trust backend architecture

---

## Considered Options

### Option 1: Self-hosted Ory Kratos (Chosen)

**Pros (+):**
- Enterprise-grade, open-source (Apache 2.0) identity server.
- Built-in, audited flows for WebAuthn, TOTP, and account recovery.
- FastAPI code remains pristine and holds zero credentials.

**Cons (-):**
- Adds an additional Go-based binary/container to the deployment stack.
- Requires learning Ory's configuration format.

### Option 2: Custom FastAPI Auth implementation (DIY)

**Pros (+):**
- No external infrastructure dependencies.

**Cons (-):**
- Massive risk of introducing critical security flaws (OWASP A07).
- High maintenance burden for cryptographic standards and recovery edge-cases.
- Difficult to securely handle cross-platform WebAuthn flows.


---

## Decision Outcome

**Chosen Option:** Option 1: Self-hosted Ory Kratos

### Rationale

Building DIY authentication directly conflicts with our mandate to focus on the core product value. Ory Kratos ensures military-grade identity security while maintaining 100% data sovereignty (no data leaves the Hetzner node). Third-party OAuth tokens (e.g., Garmin) are treated as application-level secrets encrypted in Postgres, independent of the Kratos identity.

---

## Consequences

### Positive Consequences (+)

- Decoupled architecture: authentication load does not impact the API resource server.
- Standardized, audited WebAuthn and TOTP flows out of the box across Web and React Native.

### Negative Consequences & Risks (-)

- Adds an additional Go-based binary/container to the deployment stack.
- UI must handle headless API flows from Kratos.

### Agent Implementation Guardrails

- Agents MUST NOT implement custom password hashing, JWT signing, or MFA verification logic in the Python backend.
- Agents MUST route all identity verification through the Ory Kratos SDK or session validation endpoints.
- Agents MUST NOT design Postgres schema definitions for user passwords or primary authentication credentials.


---

## Confirmation & Verification

Verified via integration tests demonstrating 401 Unauthorized responses for invalid Kratos sessions.

## Related Documentation
- **[docs/development/issue16/research.md][related-1]**

<!-- Link definitions -->

[related-1]: docs/development/issue16/research.md

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-03-08 | Agent | Initial draft |
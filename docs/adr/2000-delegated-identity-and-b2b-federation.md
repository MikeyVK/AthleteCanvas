<!-- docs\adr\2000-delegated-identity-and-b2b-federation.md -->
<!-- template=adr version=b4627a40 created=2026-07-23T18:31Z updated= -->
# 2000: Delegated Identity Management & B2B Federation

**Status:** ACCEPTED  
**Version:** 1.0.0  
**Last Updated:** 2026-07-23  
**Level:** Strategic  
**Category:** Security & Identity  
**Tags:** security, authentication, zero-trust  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

Building custom authentication in FastAPI introduces a massive risk for OWASP A07 vulnerabilities (Identification and Authentication Failures). Furthermore, driving frictionless B2B adoption requires integrating with existing corporate identity providers (Microsoft Entra ID, Google Workspace) via Single Sign-On (SSO). However, Ypsia's Zero-Trust Sovereign Charter dictates that Big Tech SDKs must never infiltrate the core application logic or access the secure data vault.

### Decision Drivers

- Absolute security and mitigation of OWASP auth vulnerabilities.
- Frictionless B2B adoption via Identity Federation (OIDC/SAML SSO).
- Data sovereignty: The core application must remain completely decoupled from external Big Tech identity providers.
- Support for modern consumer authentication (Passkeys/WebAuthn/FIDO2).

---

## Considered Options

### Option 1: Self-hosted Identity Server (e.g., Ory Kratos or Keycloak) (Chosen)

**Pros (+):**
- Enterprise-grade security. Open source.
- Supports Passkeys/WebAuthn and acts as a bridge for OIDC/SAML B2B federation.
- FastAPI code remains pristine and holds zero credentials.

**Cons (-):**
- Adds an additional binary/container (Go or Java) to the deployment stack.
- Requires managing an external configuration format.

### Option 2: Custom FastAPI Auth implementation (DIY)

**Pros (+):**
- No external infrastructure dependencies.

**Cons (-):**
- High maintenance burden for cryptographic standards.
- Massive risk of introducing critical security flaws.
- Difficult to securely handle cross-platform WebAuthn flows and enterprise SAML federation.

### Option 3: SaaS Identity Provider (Auth0, Firebase)

**Pros (+):**
- Extremely easy to implement.

**Cons (-):**
- Immediately violates the Sovereign Charter.
- Big Tech retains an audit log of user logins and accesses PII (emails).


---

## Decision Outcome

**Chosen Option:** Option 1: Self-hosted Identity Server (e.g., Ory Kratos or Keycloak)

### Rationale

A self-hosted identity server acts as an impenetrable shield for our core application. It handles the heavy cryptographic lifting for consumers (Passkeys, 2FA) and native identity federation (OIDC) for B2B enterprise clients without forcing us to embed Big Tech SDKs in the core Ypsia codebase. The external Identity Provider (e.g., Microsoft Azure) authenticates the user, but our Identity Server mints a purely local Ypsia session and maps it to a local `user_uuid`. The Python (FastAPI) backend only ever sees and trusts this local UUID, ensuring 100% data sovereignty while offering seamless Single Sign-On adoption.

---

## Consequences

### Positive Consequences (+)

- Decoupled architecture: authentication load and complexity do not impact the core API.
- Frictionless B2B integration: Enterprises can use existing identity providers to securely access their sovereign intelligence data.
- Standardized, audited WebAuthn and TOTP flows out of the box.

### Negative Consequences & Risks (-)

- Adds an additional binary/container to the deployment stack.
- The frontend UI must handle headless API flows from the Identity Server.

### Agent Implementation Guardrails

- Agents MUST NOT implement custom password hashing, JWT signing, or MFA verification logic in the Python backend.
- Agents MUST route all identity verification through the Identity Server SDK or session validation endpoints.
- Agents MUST NOT design Postgres schema definitions for user passwords or primary authentication credentials.
- Agents MUST ensure the core backend never directly interacts with external Big Tech identity SDKs. All federation MUST be handled by the Identity Server.


## Related Documentation
None
---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-23 | Agent | Initial draft |
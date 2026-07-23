<!-- docs\adr\0005-zero-trust-operator-security.md -->
<!-- template=adr version=b4627a40 created=2026-07-22T21:08Z updated= -->
# 0005: Zero-Trust Operator Security

**Status:** ACCEPTED  
**Version:** 1.0.0  
**Last Updated:** 2026-03-08  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

Administrative tasks (like decrypting and emailing the waitlist at launch) require access to sensitive PII. Executing this decryption on the central Hetzner VPS creates a massive attack surface: if the server is compromised, the private key and plaintext PII can be extracted via RAM scraping.

### Decision Drivers

- Zero-Trust Architecture
- Physical hardware separation of Private Keys
- CIA-grade memory protection against immutable string leaks

---

## Considered Options

### Option 1: Decentralized Local Operator Client with CIA-Grade Memory Protection (Chosen)

**Pros (+):**
- The VPS never sees the private key or the plaintext PII.
- Mitigates server-side RAM scraping attacks completely.
- Complete control over local memory scrubbing.

**Cons (-):**
- Operator must physically execute the launch sequence.
- Python's garbage collector makes memory scrubbing difficult, requiring low-level code implementation.

### Option 2: Server-Side In-Memory Decryption

**Pros (+):**
- Fully automated launch.

**Cons (-):**
- Fatal vulnerability window: If the VPS is compromised, the key and all emails are exposed in RAM.
- Violates the Zero-Trust principle.


---

## Decision Outcome

**Chosen Option:** Option 1: Decentralized Local Operator Client with CIA-Grade Memory Protection

### Rationale

The central server must never be the weakest link. By decentralizing the operator private key, we eliminate the highest-value target for attackers on the VPS. To achieve true CIA-grade security on the operator's local machine, the decryption script must bypass Python's immutable strings by using mutable buffers (bytearray or ctypes) combined with explicit memory zeroing (memzero) and page locking (mlock), preventing OS swap-file leaks.

---

## Consequences

### Positive Consequences (+)

- Bulletproof protection of the platform's initial userbase.
- Enforces strict operational security hygiene.

### Negative Consequences & Risks (-)

- Operator must physically execute the launch sequence.
- Python's garbage collector makes memory scrubbing difficult, requiring low-level code implementation.

### Agent Implementation Guardrails

- Agents MUST NOT generate server-side FastAPI endpoints that accept, load, or process the operator's private key.
- Agents MUST NOT store plaintext sensitive data (like emails) in standard, immutable Python str variables within the local operator scripts.
- Agents MUST utilize mutable buffers (e.g., bytearray, ctypes) and implement explicit memory zeroing (memzero) and mlock directly after processing sensitive batches locally.
- Agents MUST NOT decrypt or process plaintext PII using standard immutable Python strings on the backend application server.


---

## Confirmation & Verification

Verified via code review ensuring ctypes/bytearray usage, mlock/memzero implementation, and absence of private key references in the VPS backend codebase.

## Related Documentation
- **[docs/development/issue18/research.md][related-1]**
- **[docs/development/issue16/research.md][related-2]**

<!-- Link definitions -->

[related-1]: docs/development/issue18/research.md
[related-2]: docs/development/issue16/research.md

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-03-08 | Agent | Initial draft |
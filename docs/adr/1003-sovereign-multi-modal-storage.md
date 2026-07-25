<!-- docs\adr\1003-sovereign-multi-modal-storage.md -->
<!-- template=adr version=b4627a40 created=2026-07-24T16:52Z updated= -->
# Sovereign Multi-Modal Storage & Progressive Escalation

**Status:** ACCEPTED  
**Version:** 1.0.0  
**Last Updated:** 2026-07-24  
**Category:** Data & Storage  
**Tags:** storage, media, encryption  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

Ypsia must ingest multi-modal data (audio, images, video) to be a true Universal Intelligence Engine. However, storing petabytes of binary blobs in PostgreSQL (ADR 1000) will destroy database scalability. Conversely, defaulting to external cloud object storage (e.g., AWS S3) violates the Sovereign Charter (Big Tech dependence) and breaks the 'mathematically enforced zero-leakage' provided by PostgreSQL's Row-Level Security (RLS).

### Decision Drivers

- Support for multi-modal ingestion (images, audio, video).
- Preserve the 'Host it yourself' simplicity for self-hosters.
- Preserve the mathematically enforced Zero-Leakage guarantee (Charter).
- Ensure long-term petabyte scalability for the SaaS environment.

---

## Considered Options

### 

**Pros (+):**
- Scales infinitely, maintains Zero-Leakage via key destruction, extremely lightweight for self-hosters (local disk).

**Cons (-):**
- Requires implementing the IMediaStorage abstraction and Crypto-Shredding logic.

### 

**Pros (+):**
- 100% RLS compliance out of the box.

**Cons (-):**
- Unscalable database size; WAL logs and backups become unmanageable.

### 

**Pros (+):**
- Infinite scale natively.

**Cons (-):**
- Violates the Charter (Big Tech dependence), heavy infrastructure burden for self-hosters.


---

## Decision Outcome

**Chosen Option:** Option 1: Progressive Storage Escalation with Crypto-Shredding

### Rationale

We implement an IMediaStorage adapter and a Progressive Escalation Ladder. For self-hosters (Phase 1), encrypted media is stored on the Local File System ('local-disk'), keeping infrastructure minimal and fast without overloading the database. For SaaS scale (Phase 2), we escalate to self-hosted distributed storage (e.g., MinIO). Crucially, media is ALWAYS encrypted with a 'user_media_key' stored in PostgreSQL. If a user deletes their account, the Postgres cascade destroys the key, instantly and mathematically rendering the external media unreadable (Crypto-Shredding). This preserves the Sovereign Vault principle while enabling multi-modal petabyte scale.

---

## Consequences

### Positive Consequences (+)

- Self-hosters can run a fully multi-modal AI coach without needing any external cloud storage.
- The SaaS platform can scale to petabytes of media without blowing up the PostgreSQL backups.
- Account deletion guarantees absolute, mathematical destruction of media (Crypto-Shredding).

### Negative Consequences & Risks (-)

- Requires careful memory management during the encryption of large media streams to avoid RAM exhaustion.

### Agent Implementation Guardrails

- Agents MUST NOT store large binary media (images, video, audio) directly in PostgreSQL tables.
- Agents MUST use the IMediaStorage port to abstract the storage backend.
- Agents MUST encrypt all media before it leaves the application memory, using a key managed by PostgreSQL RLS.
- Agents MUST record the media location as a URI (e.g., 'ypsia://local-disk/uuid') within the TrackingRecord JSONB payload.


## Related Documentation
None
---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-24 | Agent | Initial draft |
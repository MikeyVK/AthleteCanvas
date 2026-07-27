<!-- docs\adr\1000-unified-sovereign-storage.md -->
<!-- template=adr version=b4627a40 created=2026-07-23T18:21Z updated= -->
# 1000: Unified Sovereign Storage & Deployment Flexibility

**Status:** ACCEPTED  
**Version:** 1.0.0  
**Last Updated:** 2026-07-23  
**Level:** Strategic  
**Category:** Data & Storage  
**Tags:** database, postgresql, isolation, architecture  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

Ypsia is a Sovereign Intelligence Engine handling sensitive personal, social, and (future) corporate data. The storage layer must provide mathematically enforced data isolation, infinite schema flexibility for AI-generated artifacts, and enable the application to run as a multi-tenant SaaS (for SMEs/consumers) or as a fully physically isolated single-tenant installation (for Enterprises or self-hosters).

### Decision Drivers

- Support for both Multi-tenant SaaS (Logical isolation) and Enterprise/Self-host (Physical isolation).
- Infinite schema flexibility for AI-generated content.
- AI Vector embeddings must remain in the same vault as raw data (Zero-Trust).
- Deployment simplicity to realize the 'Host it yourself' principle.

---

## Considered Options

### Option 1: PostgreSQL + pgvector + RLS + JSONB (Chosen)

**Pros (+):**
- Single unified system. Perfect for self-hosting.
- RLS ensures 100% watertight SaaS multi-tenancy.
- Code runs identically on a shared or dedicated physical database.

**Cons (-):**
- Requires strict RLS discipline.
- At massive scale (millions of users), vertical scaling of Postgres can become a bottleneck, requiring sharding.

### Option 2: Fragmented Architecture (Postgres + MongoDB + Pinecone)

**Pros (+):**
- Individual components are optimized for their specific tasks.

**Cons (-):**
- Extremely complex to self-host (fatal for open-source adoption).
- 'Split-brain' risk: Permissions in Mongo drift from Pinecone.
- Massive privacy risk if corporate data ends up in a cloud vector DB.


---

## Decision Outcome

**Chosen Option:** Option 1: PostgreSQL + pgvector + RLS + JSONB

### Rationale

PostgreSQL uniquely provides a foundation that combines strong relational access controls (via Row-Level Security), document flexibility (via JSONB), and high-dimensional vector search (via pgvector) within a single transaction domain. By building the application to always rely on RLS-based tenant separation, the exact same codebase runs seamlessly on our shared SaaS environment and on a physically isolated on-premise database of an Enterprise or open-source user. This makes 'Bring Your Own Database' and the open-source mission achievable without compromising SaaS security.

---

## Consequences

### Positive Consequences (+)

- Single database infrastructure (extremely easy to self-host).
- Mathematically enforced Zero-Leakage in the SaaS environment via the database kernel.
- Future-proof: AI can invent and store endless new formats in JSONB.

### Negative Consequences & Risks (-)

- Developers/Agents must be extremely disciplined when writing RLS policies; a mistake here instantly breaches the SaaS model.

### Agent Implementation Guardrails

- Agents MUST ensure all tables containing user, social, or corporate data have RLS enabled and strictly enforce tenant/user boundaries.
- Agents MUST NOT introduce external vector stores (e.g., Pinecone) or external document stores (e.g., MongoDB). Everything stays in Postgres.
- Agents MUST design the backend to be instance-agnostic: the exact same codebase must function seamlessly connected to a multi-tenant SaaS database or an isolated single-tenant physical database.
- Agents MUST utilize JSONB columns for dynamic AI-generated content (dashboards, insight reports, analytical summaries) to prevent schema explosion.


## Related Documentation
None
---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-23 | Agent | Initial draft |
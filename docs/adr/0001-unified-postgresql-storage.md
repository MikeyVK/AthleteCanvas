<!-- docs\adr\0001-unified-postgresql-storage.md -->
<!-- template=adr version=b4627a40 created=2026-07-22T21:07Z updated= -->
# 0001: Unified PostgreSQL Storage & RLS Vector Isolation

**Status:** ACCEPTED  
**Version:** 1.1.0  
**Last Updated:** 2026-03-08  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

ypsia requires a highly secure, multi-tenant storage solution for both relational tracking data and high-dimensional semantic embeddings (vectors). The system must guarantee strict zero-leakage data isolation and instantaneous account deletion.

### Decision Drivers

- Multi-tenant data privacy (Zero-leakage)
- Infrastructure simplicity (No split-brain sync issues)
- 0-Day Opt-Out (Immediate cryptographic or physical deletion)
- Deterministic semantic stability for embeddings

---

## Considered Options

### Option 1: PostgreSQL + pgvector + RLS (Chosen)

**Pros (+):**
- Unified transactional consistency (ACID) for relational and vector data.
- Strict kernel-level data isolation via RLS.
- Instant 0-Day Opt-Out via ON DELETE CASCADE.
- Highly performant for personal-scale datasets (<10,000 activities) using B-Tree indexing and exact Cosine Distance flat scans.

**Cons (-):**
- Scaling to billions of vectors globally requires partitioning strategies.
- Vector search latency is tied to the main database CPU limits.

### Option 2: PostgreSQL + External Vector DB (ChromaDB)

**Pros (+):**
- Purpose-built for massive-scale vector retrieval.

**Cons (-):**
- Creates a 'split-brain' architecture risking data synchronization failures.
- Multi-tenant isolation requires managing thousands of individual collections, causing fatal OOM crashes and file-descriptor exhaustion.
- Deleting an account requires distributed transaction rollbacks.


---

## Decision Outcome

**Chosen Option:** Option 1: PostgreSQL + pgvector + RLS

### Rationale

PostgreSQL with pgvector and RLS perfectly aligns with the Sovereign Charter. It structurally enforces data privacy at the kernel level and guarantees 0-day opt-out via ON DELETE CASCADE. We avoid global HNSW or IVFFlat indices to prevent recall loss, and rely on standard B-Tree indexing on user_uuid followed by exact scans. Embedding generation utilizes deterministic Jinja2 text serialization to ensure mathematical stability in the latent space.

---

## Consequences

### Positive Consequences (+)

- Unified transactional consistency (ACID) for relational and vector data.
- Strict kernel-level data isolation via RLS.
- Instant 0-Day Opt-Out via ON DELETE CASCADE.
- Single source of truth; drastically simplified DevOps and backup strategies.
- RAG shield is cryptographically hard: if Postgres deletes the row, the LLM loses context instantly.

### Negative Consequences & Risks (-)

- Scaling to billions of vectors globally requires partitioning strategies.
- RLS policies must be meticulously crafted and tested for every new table.

### Agent Implementation Guardrails

- Agents MUST NOT generate database connection code, SDK clients, or queries for ChromaDB, Qdrant, Pinecone, or any other external vector store.
- Agents MUST NOT use SQLite except for purely in-memory FakeAdapters in unit tests.
- Agents MUST enforce RLS policies on all new PostgreSQL tables containing user data.
- Agents MUST utilize deterministic templates (e.g., Jinja2) for text serialization prior to embedding; dynamic serialization via LLMs or MoE is strictly forbidden.
- Agents MUST NOT implement global HNSW or IVFFlat indexes on the user_embeddings table; filtering must occur via B-Tree on user_uuid first.


---

## Confirmation & Verification

Verified via pytest-postgresql integration tests ensuring RLS blocks cross-tenant reads and CASCADE deletes wipe user_embeddings synchronously.

## Related Documentation
- **[docs/development/issue16/research.md][related-1]**

<!-- Link definitions -->

[related-1]: docs/development/issue16/research.md

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-03-08 | Agent | Initial draft |
| 1.1.0 | 2026-07-22 | Agent | Added HNSW prohibition and exact B-Tree flat scan guardrails |
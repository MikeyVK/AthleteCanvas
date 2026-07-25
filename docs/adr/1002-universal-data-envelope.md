<!-- docs\adr\1002-universal-data-envelope.md -->
<!-- template=adr version=b4627a40 created=2026-07-24T08:02Z updated= -->
# 1002: Universal Data Envelope (TrackingRecord Schema)

**Status:** ACCEPTED  
**Version:** 1.0.1  
**Last Updated:** 2026-07-24  
**Category:** Data & Storage  
**Tags:** database, schema, agnostic  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

To function as a Universal Intelligence Engine, Ypsia must be able to ingest and store an infinite variety of data types (e.g., IoT telemetry, financial transactions, physiological metrics, behavioral logs) uniformly. Creating a distinct database table or complex polymorphic relation for every new domain leads to exponential schema complexity, brittle migrations, and forces the core architecture to 'know' about specific domains, violating the Sovereign Charter.

### Decision Drivers

- Infinite extensibility across any data domain.
- Zero database migrations required for new data types.
- Absolute data integrity (no 'garbage in, garbage out').
- High-performance indexing for temporal retrieval.

---

## Considered Options

### Option 1: Hybrid Universal Envelope (Fixed Columns + JSONB Payload) (Chosen)

**Pros (+):**
- Infinite domain flexibility without database migrations.
- Extremely fast indexing on the fixed metadata columns (time, user, source).
- Strict Pydantic models at the API/Worker boundary guarantee data integrity.

**Cons (-):**
- Relies heavily on application-level typing; developers must diligently define schemas.

### Option 2: Polymorphic Relational Tables (One table per data type)

**Pros (+):**
- Strongest database-level guarantees and foreign keys.

**Cons (-):**
- Requires constant database migrations for every new sensor or data type.
- Forces the core architecture to understand specific domain models.

### Option 3: Pure Document Store (e.g., MongoDB)

**Pros (+):**
- Maximum schema flexibility natively.

**Cons (-):**
- Violates ADR 1000 (Unified Sovereign Storage), fragmenting the architecture.
- Lacks strong relational multi-tenant guarantees (RLS).


---

## Decision Outcome

**Chosen Option:** Option 1: Hybrid Universal Envelope (Fixed Columns + JSONB Payload) with Strict Boundary Validation

### Rationale

By separating the 'pipeline metadata' (who, when, what type) from the 'domain payload', the core database schema becomes perfectly stable and universally scalable. 

**Conceptual Structure:**
The schema strictly separates systemic metadata from domain data.
1. **Fixed Systemic Columns:** We mandate fixed relational columns for data that the core engine needs for routing, authorization, and temporal querying (e.g., Tenant ID, Temporal Timestamp, Source Origin, and the Record Type discriminator). These are indexed for extreme performance.
2. **Domain Payload:** The actual domain-specific data (whether it's a heartbeat, a financial ledger entry, or a pointer to an external media blob) is stored in a schemaless document format (JSONB).
3. **Boundary Validation:** To prevent the document payload from degrading into an untyped data swamp, strict validation schemas (e.g., Pydantic models) are enforced at the application boundary. The database accepts the JSONB, but the application guarantees its exact structure based on the Record Type discriminator.

---

## Consequences

### Positive Consequences (+)

- The core ingestion and storage engine is now truly domain-agnostic.
- New integrations (e.g., Banking API, IoT Sensor) require only a new Python adapter class and Pydantic model, zero SQL migrations.

### Negative Consequences & Risks (-)

- JSONB payload fields cannot easily enforce database-level foreign keys if needed in the future.

### Agent Implementation Guardrails

- Agents MUST use the TrackingRecord hybrid pattern (Fixed Metadata + JSONB) for all domain data.
- Agents MUST NOT create new database tables for specific data types (e.g., no 'heart_rate' or 'bank_transaction' table).
- Agents MUST define a strict Pydantic schema for every new `record_type` payload and validate it at the adapter boundary before storage.
- Agents MUST use the `is_embeddable` boolean flag to decouple the ingestion pipeline from the vector embedding pipeline.

## Related Documentation
- [ADR 1003: Sovereign Multi-Modal Storage & Progressive Escalation](./1003-sovereign-multi-modal-storage.md)

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-24 | Agent | Initial draft (Corrupted Headings) |
| 1.0.1 | 2026-07-24 | Agent | Fixed headings, added SQL schema, linked ADR 1003 |
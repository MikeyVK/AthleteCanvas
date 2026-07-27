<!-- docs\adr\1001-schemaless-domain-payload.md -->
<!-- template=adr version=b4627a40 created=2026-07-24T19:17Z updated= -->
# Schemaless Domain Payload Implementation

**Status:** ACCEPTED  
**Version:** 1.0.0  
**Last Updated:** 2026-07-24  
**Level:** Strategic  
**Category:** Data & Storage  
**Tags:** database, jsonb, architecture  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

Within the Universal Data Envelope (ADR 1002), the domain-specific data must be stored in a schemaless format to prevent database migrations when new sensor types or API integrations are added. We must choose the optimal storage mechanism for this schemaless payload within PostgreSQL that balances read/write performance, queryability, and complexity.

### Decision Drivers

- Must support infinite schema flexibility.
- Must allow fast database-level querying and filtering on the payload data.
- Must support deeply nested hierarchical data.

---

## Considered Options

### Option 1: JSONB (Binary JSON) Document Store (Chosen)

**Pros (+):**
- Native support for nested structures, extremely fast querying and indexing via GIN indexes, ubiquitous in modern API ecosystems.

**Cons (-):**
- Slightly higher storage footprint than binary formats; lacks native database-level schema validation.

### Option 2: Entity-Attribute-Value (EAV) Pattern

**Pros (+):**
- Pure relational SQL, no document-store features needed.

**Cons (-):**
- Catastrophic read performance at scale due to complex self-joins; fundamentally unsuited for nested or hierarchical telemetry data.

### Option 3: Binary Serialization (Protobuf / FlatBuffers) via bytea

**Pros (+):**
- Smallest possible storage footprint, fastest serialization in code.

**Cons (-):**
- The database is completely blind to the content. Impossible to execute SQL queries or filters on the internal data attributes.


---

## Decision Outcome

**Chosen Option:** Option 1: JSONB (Binary JSON) Document Store

### Rationale

JSONB uniquely satisfies the requirement of infinite schema flexibility while maintaining database-level queryability. Unlike Protobuf, we can index and search inside the JSONB payload (e.g., finding all records where a specific metric spiked) directly via SQL. Unlike EAV, we can retrieve complex hierarchical data in a single rapid query without destructive JOIN penalties. To mitigate the lack of database-level schema validation, ADR 1002 mandates strict application-level boundary validation (Pydantic).

---

## Consequences

### Positive Consequences (+)

- Developers can add new integrations instantly without touching SQL.
- The AI and analytics dashboards can query deeply nested domain data directly via PostgreSQL GIN indexes.

### Negative Consequences & Risks (-)

- JSONB has a slightly higher storage footprint than compiled binary formats.
- Lacks database-level strict schema validation (mitigated by Pydantic boundaries in ADR 1002).

### Agent Implementation Guardrails

- Agents MUST use JSONB columns for schemaless domain data.
- Agents MUST NOT implement Entity-Attribute-Value (EAV) tables for tracking records or telemetry data.
- Agents MUST NOT store queryable domain data as opaque binary blobs (bytea / Protobuf) if the application requires filtering on that data via SQL.


## Related Documentation
None
---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-24 | Agent | Initial draft |
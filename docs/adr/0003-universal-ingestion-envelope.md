<!-- docs\adr\0003-universal-ingestion-envelope.md -->
<!-- template=adr version=b4627a40 created=2026-07-22T21:08Z updated= -->
# 0003: Universal Ingestion Envelope & Direct-First Adapters

**Status:** ACCEPTED  
**Version:** 1.1.0  
**Last Updated:** 2026-03-08  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

ypsia must ingest health and activity data from multiple sources (Garmin, Strava, Apple Health, manual entry) with varying structures, while maintaining a single normalized internal data format. We must also prevent \"Thundering Herd\" IP bans when polling third-party APIs during the bootstrapping phase.

### Decision Drivers

- Schema stability and extensibility (Open/Closed Principle)
- Protection against third-party API rate limits and IP bans
- Idempotent upserts for safe reprocessing
- Minimization of data-broker middlemen

---

## Considered Options

### Option 1: Hybrid JSONB Envelope with Smooth Flat Queue (Chosen)

**Pros (+):**
- Adding new data types requires zero database schema migrations.
- `UNIQUE` constraints enforce idempotence automatically.
- Global Redis locks prevent API bans during simulated `garth` bootstrapping.

**Cons (-):**
- Requires strict Pydantic validation at the application boundary to ensure JSONB integrity.

### Option 2: Table-per-Type Architecture

**Pros (+):**
- Strict relational integrity and typing at the database level.

**Cons (-):**
- Schema explosion: adding a new wearable metric requires a new Alembic migration and adapter rewrite.
- Difficult to query across all chronologically adjacent records for contextual RAG.


---

## Decision Outcome

**Chosen Option:** Option 1: Hybrid JSONB Envelope with Smooth Flat Queue

### Rationale

The TrackingRecord domain envelope allows infinite extensibility without schema migrations. To adhere to the Sovereign Charter, we enforce a Direct-First Strategic Priority (official webhooks over aggregators). During bootstrapping, we implement strict traffic shaping: activation-triggered debounced syncing and a Global Concurrency Lock (max 2 workers) via Redis, preventing the \"Thundering Herd\" API ban scenario.

---

## Consequences

### Positive Consequences (+)

- Highly resilient to third-party API changes.
- Adding a new data source is a purely additive operation (new Adapter class).

### Negative Consequences & Risks (-)

- Querying deeply nested fields within JSONB can become slow without functional indexing.

### Agent Implementation Guardrails

- Agents MUST NOT create separate relational tables for new health data types (e.g., sleep_records, heart_rate_records). All tracking data MUST fit the tracking_records hybrid schema.
- Agents MUST utilize Pydantic discriminated unions to validate incoming JSONB payloads before insertion.
- Agents MUST NOT configure background polling crons (e.g., ARQ) that bypass or violate the global concurrency lock limits.
- Agents MUST treat simulated APIs (garth) as legacy targets strictly governed by the Smooth Flat Queue, and MUST prioritize official webhook integrations (e.g., Garmin Health API) where no polling is required.


---

## Confirmation & Verification

Verified via ImportOrchestrator unit tests demonstrating idempotent upserts and ARQ worker integration tests enforcing the Redis lock.

## Related Documentation
- **[docs/development/issue16/research.md][related-1]**

<!-- Link definitions -->

[related-1]: docs/development/issue16/research.md

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-03-08 | Agent | Initial draft |
| 1.1.0 | 2026-07-22 | Agent | Added legacy garth handling and official webhook priority guardrails |
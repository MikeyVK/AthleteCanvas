<!-- docs\adr\4000-pluggable-brain-semantic-translation.md -->
<!-- template=adr version=b4627a40 created=2026-07-24T07:05Z updated= -->
# 4000: Pluggable Brain & Multi-Faceted Semantic Translation

**Status:** ACCEPTED  
**Version:** 1.0.0  
**Last Updated:** 2026-07-24  
**Category:** Intelligence  
**Tags:** ai, vectors, deterministic, semantic  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

To function as a Universal Intelligence Engine, Ypsia's core must remain ignorant of specific domains (e.g., health, finance). Raw incoming data must be translated into natural language so the AI embedding model can understand it. If we use dynamic AI (LLMs) to perform this initial translation, we suffer from 'coordinate drift' (non-deterministic text causes unstable mathematical vectors). Furthermore, rendering a data point from only one perspective limits the AI's ability to cross-reference insights across different domains (e.g., financial vs. behavioral, or physiological vs. operational).

### Decision Drivers

- Absolute separation of domain intelligence from the core ingestion/storage engine.
- Mathematical stability (determinism) in the vector database to prevent coordinate drift.
- Support for multi-angle clustering and retrieval for deep analytical insights.
- Technology agnosticism: The templating mechanism must be abstracted to allow future upgrades.

---

## Considered Options

### Option 1: Pluggable Multi-Faceted Deterministic Translation (Chosen)

**Pros (+):**
- Guarantees vector stability.
- Allows infinite domain expansion.
- Multi-lens rendering enables profound AI insights.

**Cons (-):**
- Requires upfront engineering to design robust templates for each domain.

### Option 2: AI-driven dynamic summarization before embedding

**Pros (+):**
- Easier to implement initially; handles arbitrary JSON automatically.

**Cons (-):**
- Fatal coordinate drift. Vectors for similar events will shift unpredictably.
- High continuous compute cost.


---

## Decision Outcome

**Chosen Option:** Option 1: Pluggable Multi-Faceted Deterministic Translation

### Rationale

The true intelligence of Ypsia lies in translation. By using an abstracted, deterministic templating engine (conceptually similar to Jinja2, but technology-agnostic), we guarantee that identical data always produces identical text, resulting in perfectly stable vectors. To support deep, multi-angle analysis, a single incoming payload can be passed through multiple 'lenses' (e.g., a Financial Transaction template, a Physiological template, a Communication/Social template). This generates multiple targeted vectors for the same event, transforming Ypsia into a continuous, sovereign, life-scale analytical intelligence.

---

## Consequences

### Positive Consequences (+)

- Infinite extensibility: Ypsia can analyze anything simply by adding a new template plugin.
- Perfectly stable AI memory (no coordinate drift).
- Profound, multi-dimensional query capabilities (Multi-Angle Clustering).

### Negative Consequences & Risks (-)

- Creating high-quality templates requires deep domain expertise and maintenance.

### Agent Implementation Guardrails

- Agents MUST NOT use generative LLMs to summarize raw data into the primary vector store (to prevent drift). Translation must be deterministic.
- Agents MUST abstract the templating engine. Do not hardcode a dependency on Jinja2 deep in the core architecture.
- Agents MUST design domain plugins to support multi-faceted rendering (multiple perspectives per data point) where analytically valuable.


## Related Documentation
None
---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-24 | Agent | Initial draft |
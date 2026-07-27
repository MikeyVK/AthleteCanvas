<!-- docs\adr\3000-direct-first-ingestion.md -->
<!-- template=adr version=b4627a40 created=2026-07-23T19:41Z updated= -->
# 3000: Direct-First Ingestion & Transparent Bootstrapping

**Status:** ACCEPTED  
**Version:** 1.0.0  
**Last Updated:** 2026-07-23  
**Level:** Strategic  
**Category:** Integration  
**Tags:** integration, ingestion, anti-broker  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

To provide deep intelligence, Ypsia must retrieve data from external silos (e.g., enterprise systems, financial APIs, telemetry/IoT devices). Relying on commercial data brokers introduces a 'man-in-the-middle' that violates our data sovereignty principles. Furthermore, clandestinely scraping data to avoid firewalls is unethical and unstable. The platform needs an ingestion strategy that honors the Charter's demand for independence, transparency, and respect for external infrastructure.

### Decision Drivers

- Eliminate third-party data brokers to maintain zero-trust data sovereignty.
- Maintain a highly stable, ethical, and transparent connection to external services.
- Decouple the core engine from external API specifics (Hexagonal Architecture).

---

## Considered Options

### Option 1: Direct-First Integration with Transparent Bootstrapping (Chosen)

**Pros (+):**
- Honors data sovereignty by eliminating middlemen.
- Hexagonal design keeps the core clean.
- Radical transparency maintains the 'Moral Moat'.

**Cons (-):**
- Requires manual bootstrapping/simulation until official API partnerships are approved, which takes time.

### Option 2: Utilize commercial data aggregators/brokers (e.g., Plaid, Vital API, Segment)

**Pros (+):**
- Extremely fast to implement hundreds of integrations.

**Cons (-):**
- Fatal violation of the Charter.
- Introduces a commercial entity that can view, store, or monetize user data.


---

## Decision Outcome

**Chosen Option:** Option 1: Direct-First Integration with Transparent Bootstrapping

### Rationale

Ypsia's core engine must remain agnostic to the outside world, receiving data exclusively through interchangeable adapters. The strategic imperative is to secure direct, official API connections (e.g., Salesforce API, Garmin API, Banking APIs) to eliminate brokers. During the inevitable bootstrapping phase where official access is pending, we may use secure browser simulation. However, we reject clandestine scraping; instead, we employ Radical Transparency, explicitly informing the user that we are using a temporary simulation that may be slower. To respect the external provider, we implement strict traffic-shaping (e.g., flat concurrency queues), prioritizing ethical integration over brute-force data harvesting.

---

## Consequences

### Positive Consequences (+)

- Total ownership of the data pipeline. No leakage to aggregators.
- Ethical high ground and transparency build immense user trust.

### Negative Consequences & Risks (-)

- Initial integration development is slower and requires managing simulation fallbacks.

### Agent Implementation Guardrails

- Agents MUST implement external integrations as isolated adapters that map to standardized internal models.
- Agents MUST NOT introduce commercial data brokers into the ingestion pipeline.
- Agents MUST ensure any simulated API fallback mechanisms are accompanied by explicit, transparent UI warnings to the user.
- Agents MUST implement strict traffic-shaping (rate limits, jittered queues) on all outbound requests to protect external infrastructure.


## Related Documentation
None
---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-23 | Agent | Initial draft |
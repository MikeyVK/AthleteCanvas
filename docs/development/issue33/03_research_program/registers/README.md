# Canonical Research Registers

**Status:** PRELIMINARY  
**Version:** 0.4  
**Last updated:** 2026-08-08  
**Purpose:** Define the human-readable ownership, semantics, and integrity rules for the Issue 33 research records.  
**Machine-readable contract:** [register_schema.yaml](register_schema.yaml)  
**Governing method:** [RESEARCH_PROTOCOL.md](../RESEARCH_PROTOCOL.md), fixed at Protocol 0.1  
**Bounded execution profile:** [PILOT_MANIFEST.md](../PILOT_MANIFEST.md), proposed Manifest 0.3

## 1. Authority and baseline

This contract makes Protocol 0.1 recordable and mechanically testable. It does not create empirical authority, approve a candidate, or alter the Protocol. Where this README and `register_schema.yaml` differ, execution stops: neither source may silently override the other.

The baseline consists of header-only CSV files. No evidence record may be added until DEC-005, DEC-008, DEC-009, DEC-010, and DEC-011 are all Approved and the validation gate in section 13 has passed.

## 2. One canonical owner per record type

| Register | Canonical responsibility | One row represents |
|---|---|---|
| `workstream_register.csv` | Workstream framing, frozen search design, flow counts, saturation, and status | One bounded workstream |
| `research_question_register.csv` | Research question and PCC context | One bounded research question |
| `interest_register.csv` | Affected or protected interest and normative authority | One defined interest |
| `search_log.csv` | Reproducible search execution | One executed search |
| `search_links.csv` | Search-to-claim or search-to-source linkage | One typed linkage |
| `source_register.csv` | Source identity, provenance, authority, and bibliographic context | One source |
| `source_relations.csv` | Dependence, duplication, update, or citation relation between sources | One typed source relation |
| `screening_precommitments.csv` | Append-only sample plan, commitment, materialisation, and verification | One state record in one sample-plan chain |
| `screening_events.csv` | Primary, secondary, or adjudicated screening decision | One screening event |
| `claim_register.csv` | Atomic, challengeable proposition | One claim |
| `claim_assessments.csv` | Current epistemic and formulation assessment | One versioned assessment |
| `candidate_register.csv` | Candidate problem, mechanism, consequence, or other topology object | One candidate |
| `evidence_links.csv` | Source contribution to one claim | One versioned evidence link |
| `equality_assessments.csv` | Equality impact screen or full safeguard assessment | One versioned equality assessment |
| `topology_relations.csv` | Directed relation between claims or candidates | One versioned edge |
| `review_events.csv` | Review execution, target identity, reviewer provenance, and NO_FINDING | One completed or invalidated review event |
| `review_register.csv` | Defect or challenge raised by a review event | One finding; never a review execution |
| `gap_register.csv` | Evidence, coverage, method, or provenance gap | One tracked gap |
| `synthesis_register.csv` | Versioned workstream synthesis | One synthesis version |
| `implementation_register.csv` | Existing, proposed, historical, or hypothetical implementation | One implementation |
| `materiality_assessments.csv` | Eight-axis materiality and protected-interest gate | One versioned MAT assessment |
| `rootness_assessments.csv` | Seven-criterion provisional-root test | One versioned ROT assessment |
| `search_iterations.csv` | Predeclared or executed search iteration and novelty yield | One versioned iteration |

No other file may become a parallel owner for these record types.

## 3. CSV and identifier contract

All registers use UTF-8 without BOM, RFC 4180-compatible quoting, comma delimiters, and exactly one declared header row. Multi-value fields use `|`, contain unique nonempty members, and are validated member by member. Header order is normative.

The identifiers are namespaces, not scientific conclusions. Important prefixes are `WS`, `RQ`, `INT`, `SRCH`, `SLK`, `SRC`, `SRL`, `SSP`, `SSR`, `SCR`, `CLM`, `ASM`, `KAND`, `EVL`, `EQA`, `TOP`, `RVE`, `REV`, `GAP`, `SYN`, `IMP`, `MAT`, `ROT`, and `ITER`.

Canonical-document references resolve to the declared Protocol, Decision Log, or Pilot Manifest. A broken scalar, multi-value, polymorphic, or canonical-document foreign key is a hard validation failure.

## 4. Null semantics

- Blank means missing or not yet entered.
- `NOT_ASSESSED` means no assessment was performed.
- `UNKNOWN` means an assessment was performed but the evidence cannot determine the value.
- `NOT_APPLICABLE` means the field has no semantic application.
- `NONE_IDENTIFIED` means the declared search or check was performed and found no instance.

These values are not interchangeable. A blank or `NOT_ASSESSED` cannot be used to simulate counterevidence processing, a null yield, or a negative finding.

## 5. Currentness, immutability, and supersession

Currentness is graph-derived: a row is current only when no later row points to it through the table's declared supersession pointer. A status label cannot override that rule. Screening corrections use `supersedes_screening_event_id`; `prior_event_id` remains exclusively review lineage. At most one graph-current PRIMARY event may exist for each `source_id + workstream_id + stage`, and current/noncurrent rows use `ACTIVE`/`SUPERSEDED` coherently.

Every supersession chain is acyclic, preserves its declared natural key, and advances its audit timestamp strictly. Search iterations preserve `workstream_id + sequence`; assessments preserve their claim, candidate, or assessed object; review events preserve the immutable review tuple. Screening precommitments are append-only state records and may never be updated or deleted.

For pilot review targets:

- claim, evidence-link, ASM, MAT, ROT, EQA, and sample-record versions use their row ID;
- synthesis uses its registered `version`;
- topology uses `object_version`;
- every review stores the lowercase SHA-256 digest of the canonical target row;
- changed content gets a new row identity or version and a new digest, and must be reviewed again.

The canonical target-row serialization is the declared header order with minimal RFC 4180 quoting, UTF-8, one LF line ending between header and row, and no terminal LF.

## 6. Actor and reviewer provenance

Author provenance is required on every double-reviewed pilot object: actor name, actor type, system, and context locator. `HUMAN` uses `NOT_APPLICABLE` for system; `HUMAN_AI_HYBRID` and `AI` require nonempty system and context locators that are not `NOT_APPLICABLE`.

Reviewer types are `HUMAN`, `HUMAN_AI_HYBRID`, `AI_SAME_MODEL_FRESH_CONTEXT`, `AI_DIFFERENT_MODEL`, and `AI_OTHER`. AI-assisted review cannot use `NOT_APPLICABLE` for system, context, independence basis, shared-model risk, or oversight. Same-model fresh-context review records `HIGH`, `MODERATE`, or `UNKNOWN` shared-model risk.

A qualifying independent review has a context locator different from the author context. A human or hybrid reviewer also differs in reviewer identity. The same identity and context rules apply between a secondary screener and the primary, and between an adjudicator and every disputed reviewer. Adjudication is always independently true and follows exactly two same-object initial events. Different prompts, roles, or windows inside one continuing conversation do not create independent contexts.

## 7. Review events and findings

`review_events.csv` proves that a review happened, including a `NO_FINDING` result. `review_register.csv` stores findings only.

For each pilot object requiring double review, exactly two current `COMPLETED` initial review events must target the same `object_type + object_id + object_version + object_digest_sha256` tuple. They use the two roles assigned by Manifest 0.3, different context locators, and `reviewer_procedurally_independent=TRUE`. `R-ADJUDICATION` and `H-DECISION` never count as either initial slot.

An adjudication event references exactly the two disputed initial events and uses a third context distinct from the author and both initial reviewers.

Cardinality is exact:

- `NO_FINDING` has zero `REV` rows;
- `FINDINGS_RAISED` has at least one `REV` row;
- `CRITICAL` findings cannot be risk-accepted;
- `RISK_ACCEPTED` requires residual-risk reasoning and an Approved `DEC`;
- `CLOSED` requires an implemented revision and retest result.

## 8. Claim, candidate, evidence, and interest integrity

A `MIXED` claim declares at least two component challenge types and explicit boundary conditions. A non-mixed claim cannot use the mixed challenge type.

From `UNDER_REVIEW` onward, each candidate's `current_claim_assessment_ids` is exactly one current `VERIFIED` or `CHALLENGED` ASM for every registered claim and no other ASM. The strongest counterevidence is recorded as counterclaims, contradictory evidence links, or the exact sentinel `NONE_IDENTIFIED`. The sentinel is valid only when no applicable current ASM is `NOT_YET_SEARCHED`; genuinely inapplicable claims may remain `NOT_APPLICABLE`.

A normative status of `APPROVED` on an interest requires an existing Approved Decision Log entry. Other normative statuses cannot carry an authority decision.

## 9. Materiality, rootness, and equality

### 9.1 Materiality

A current MAT belongs to the same candidate as its pointer and uses only that candidate's claims. Its evidence links target those claims. A protected-interest ID is empty exactly when the interest state is `NOT_IDENTIFIED`; otherwise it resolves to an interest with the same normative status.

`ELIGIBLE` requires:

1. a protected interest;
2. at least one `HIGH` rating or at least two `MODERATE` ratings across the eight recorded axes;
3. a traceable structural mechanism;
4. recurrence or systemic operation;
5. processed counterevidence; and
6. processed mitigation evidence.

An explicit failure yields `NOT_ELIGIBLE`. A decisive unresolved `UNKNOWN` with no definitive failure yields `HOLD_UNKNOWN`. `NOT_ASSESSED` is draft-only.

### 9.2 Rootness

ROT records seven criterion states: causal path, upstreamness, persistence, explanatory gain, reducibility, countermodel, and scope boundary. `PROVISIONAL_ROOT` requires all seven `MET` and at least one current, same-candidate, `VERIFIED + ELIGIBLE` MAT. Any `NOT_MET` yields `NOT_ROOT`. An unresolved criterion with no failure yields `HOLD_UNKNOWN`.

### 9.3 Equality

`IMPACT_SCREEN` applies only to a claim or candidate and uses impact statuses. All ten full-safeguard fields are exactly `NOT_APPLICABLE`.

`FULL_SAFEGUARD` applies only to an `EXISTING` or `PROPOSED` implementation, requires all ten safeguards, and uses `PASS` or `FAIL`. A verified or challenged EQA cannot remain `NOT_ASSESSED`.

Every candidate has a current, same-candidate, verified or challenged IMPACT_SCREEN before topology determination, including a negative or not-applicable outcome. Candidate relevance maps exactly: `NOT_APPLICABLE -> NOT_APPLICABLE`, `NONE_IDENTIFIED -> NO_IMPACT_IDENTIFIED`, `POSSIBLE -> POSSIBLE_IMPACT`, and `MATERIAL -> MATERIAL_IMPACT`. Only `NOT_ASSESSED` may remain pointerless before that gate.

## 10. Search iterations and saturation

`PREDECLARED` iterations contain no execution results. `EXECUTED` and `VERIFIED` iterations contain all counts, five novelty states, details, reviewer, and completion time.

The result is deterministic:

- all five `NONE_IDENTIFIED` states yield `NULL_YIELD`;
- one or more `NOVEL_YIELD` states yield `NOVEL_YIELD`;
- `INVALIDATED` status yields `INVALIDATED`;
- `NOT_ASSESSED` is predeclaration-only.

Counts satisfy `identified >= deduplicated >= screened >= included >= 0`. They reconcile to retrieved-source links, distinct source IDs, primary screening events as of completion, and current included decisions as of completion.

Current iteration sequence is unique per workstream and contiguous from 1. `recorded_at` is the strictly increasing revision timestamp; `predeclared_at` remains immutable within a corrected `workstream_id + sequence` chain. `PROVISIONAL` saturation requires exactly three current, consecutive, `VERIFIED + NULL_YIELD` iterations in that workstream. It is a pilot stopping signal, not proof that no other evidence exists.

## 11. Screening precommitment and coverage

One independent sample plan is used per workstream and each of `TITLE` and `ABSTRACT`. Its linear append-only chain is `PRECOMMITTED -> MATERIALIZED -> VERIFIED`; PRECOMMITTED or MATERIALIZED may be invalidated, and a VERIFIED plan receives one later INVALIDATED successor when a late or backdated population-changing primary event appears. Each state carries forward all prior plan fields, and VERIFIED also byte-preserves every MATERIALIZED seed, snapshot, population, count, selection, and digest field.

The PRECOMMITTED row is recorded before its cutoff and exists in a Git commit that is a strict ancestor of the population snapshot and every primary screening-event commit for the same workstream and stage. It fixes Protocol `PROTOCOL-0.1`, cutoff, algorithm, 2,000 basis points, minimum size 1, and a SHA-256 commitment to a secret 256-bit CSPRNG seed. The seed-custodian context is absent from the set of primary-screener contexts; primary records may legitimately reuse one primary context.

The exact commitment is:

`SHA256_UTF8("SSP-COMMIT-V1|{plan}|{workstream}|{stage}|{protocol}|{cutoff}|PRIMARY_EXCLUSION_AS_OF_CUTOFF_V1|CSPRNG_256BIT|SEEDED_SHA256_LOWEST_V1|2000|1|{seed}")`

At the predeclared cutoff, MATERIALIZED reveals the seed and records a Git snapshot. The eligible population is every graph-current `ACTIVE + PRIMARY + EXCLUDE` event in the same workstream and stage with `reviewed_at <= cutoff`. Eligible event IDs are ASCII-sorted.

For each eligible event:

`selection_key = SHA256_UTF8("SSP-SELECT-V1|{seed}|{plan}|{workstream}|{source_id}|{stage}|{protocol}")`

Sort by `(selection_key, event_id)`. For population size `N`:

- `k=0` when `N=0`;
- otherwise `k=min(N,max(1,ceil(2000*N/10000)))`.

The population manifest line is:

`SSP-POP-V1|event_id|workstream|source|stage|decision|review_role|status|reviewed_at`

The selection manifest line is:

`SSP-SEL-V1|rank|selection_key_sha256|event_id`

Lines are LF-joined without a final LF and hashed as UTF-8 SHA-256. The empty population hashes empty bytes.

VERIFIED requires an independent graph-current `SCREENING_SAMPLE_REVIEW` of the MATERIALIZED row with `NO_FINDING`. Its object-author provenance equals the MATERIALIZED `recorded_by` fields. The reviewer context differs from materializer, PRE custodian, and every primary context; a human or hybrid identity also differs from the materializer. A primary event reviewed after the cutoff, or introduced after the population snapshot with backdated data that changes the cutoff population, makes the plan immediately unusable and requires an appended `INVALIDATED` record plus a new plan.

Every selected event receives exactly one `SECONDARY + DETERMINISTIC_SAMPLE` event. Every primary full-text exclusion receives `FULL_TEXT_CENSUS`, and every primary event marked high topology impact receives `HIGH_TOPOLOGY_CENSUS`. Adjudication uses both disputed-event IDs and a context distinct from all prior reviewers.

## 12. Pilot profile

`PILOT-MANIFEST-0.3` binds Pilot 0.1 to Protocol 0.1 and Contract 0.4. It fixes:

- candidates `KAND-018`, `KAND-038`, `KAND-039`, `KAND-052`, `KAND-053`, `KAND-056`, and `KAND-060`;
- workstreams `WS-001` through `WS-004`;
- the role pair per workstream;
- double review of claim, evidence link, ASM, MAT, ROT, EQA, synthesis, and topology objects;
- seeded 20% exclusion overlap at title and abstract stages;
- full-text and high-topology censuses;
- five decision gates.

## 13. Validation and execution gate

The empty baseline may be described as structurally conformant only after all 23 CSV headers, types, identifier patterns, enum members, and foreign-key targets pass.

Evidence collection additionally requires:

1. all five proposed decisions Approved;
2. an executable validator for every conditional, supersession, unique-current, computed, and cross-record constraint;
3. at least one accepted positive fixture and one rejected single-fault negative fixture per constraint;
4. canonical Protocol and Manifest targets resolved;
5. the passing validation checkpoint recorded before the first evidence row.

The canonical owner of this checkpoint is [BASELINE_AUDIT.md](../BASELINE_AUDIT.md). It records the schema hash, validator version, tested constraint IDs, positive and single-fault negative fixture counts, outcome, time, actor, authorised execution role, and seed-custodian assignment status. Before the first PRECOMMITTED Git commit, H-DECISION records the authorised Git execution role and seed-custodian identity/context in [STATUS.md](../STATUS.md); the PRECOMMITTED row then becomes the canonical custodian record.

Until then the package remains PRELIMINARY. A human approval of the method does not waive this execution gate.

## 14. Change control

Version 0.4 is a clean-break contract over an empty baseline. It separates review execution from findings, introduces commit-reveal sampling, and closes the MAT, ROT, ITER, EQA, multi-layer, current-pointer, provenance, and topology enforcement gaps found in the 0.3 cold audit.

Any substantive change creates version 0.5 or later and updates the Decision Log, Status, Pilot Manifest dependency, schema, affected headers, and validation fixtures. Protocol 0.1 changes only through an explicit new protocol decision.

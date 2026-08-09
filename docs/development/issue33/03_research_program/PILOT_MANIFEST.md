# Issue 33 Research Protocol Pilot Manifest

**Status:** PROPOSED — FROZEN FOR HUMAN DECISION  
**Version:** 0.3  
**Pilot identity:** Pilot 0.1  
**Frozen on:** 2026-08-08  
**Authority:** None until the Human Approval Decision Package is explicitly approved  
**Governing proposals:** [RESEARCH_CHARTER.md](RESEARCH_CHARTER.md) and [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md)  
**Execution contract:** [Register Contract 0.4](registers/README.md)  
**Decision dependencies:** DEC-005, DEC-008, DEC-009, DEC-010, and DEC-011 — all five must be Approved

## 1. Purpose and authority boundary

This manifest freezes one bounded test of Protocol 0.1. Approval would authorise method testing and provisional pilot records only.

It would not approve:

- production research;
- any candidate as a root problem;
- any empirical, legal, technical, or normative conclusion;
- any permanent evidence category or topology;
- any constitutional provision, product architecture, or Charter wording.

No pilot search, screening, evidence extraction, assessment, or synthesis may begin before all five decisions are Approved and the Contract 0.4 execution gate passes. The current standalone research role cannot create the Git commits required by the sampling precommitment; execution must use an explicitly authorised workflow role without changing the approved method.

## 2. Frozen candidate set

Inherited wording is a hypothesis source, not an accepted claim. Each workstream converts it into exact, bounded claims with challenge conditions before search design is frozen.

| Candidate | Inherited starting phenomenon | Workstream | Protocol characteristic exercised |
|---|---|---|---|
| KAND-018 | Model collapse or degradation under indiscriminate recursive training on model-generated data; not inevitable under every training design. | WS-001 | Technical and AI claim; historically overbroad formulation; substantial correction and counterevidence expected |
| KAND-038 | Digital power affects access, visibility, opportunity, or treatment without sufficient reasons, human review, hearing, or effective appeal. | WS-002 | Human and social effects; procedural, legal, and normative dimensions; equality impact |
| KAND-039 | Algorithmic reproduction or amplification of historic inequality through data, labels, target variables, and institutional use. | WS-002 | Empirical and causal claims; institutional power; equality impact; cross-layer mechanism |
| KAND-052 | Vulnerable dependence on a small number of suppliers, protocols, infrastructure layers, or geographic nodes. | WS-003 | Infrastructure concentration, resilience, benefits and trade-offs, cross-layer dependency |
| KAND-053 | Supply-chain attack or correlated-failure mechanisms through a shared component or supplier. | WS-003 | Technical and systemic-risk claim; boundary with ordinary cybersecurity; topology role testing |
| KAND-056 | Denial or invisibility of the physical materiality of digital systems, including energy, water, minerals, chips, buildings, logistics, and waste. | WS-004 | Ecological and intergenerational scope; possible lens-versus-root correction |
| KAND-060 | Geographic and social externalisation of energy, water, and material burdens relative to digital benefits. | WS-004 | Distributional and equality impact; ecological burden; cross-layer market and governance mechanisms |

The set is exhaustive for Pilot 0.1. Adding, removing, or substituting a candidate requires a new manifest version and renewed approval.

## 3. Frozen workstreams

Layer assignments remain proposed until DEC-005 is Approved.

| Workstream | Title | Candidates | Proposed layers | Primary question | Two initial review roles | Additional method review |
|---|---|---|---|---|---|---|
| WS-001 | Recursive AI Training and Knowledge Degradation | KAND-018 | L4 | Under which training-data and model conditions does recursive use of generated data degrade, preserve, or improve model behaviour, and which inherited wording survives? | R-EVIDENCE + R-METHOD | Same pair reviews query and eligibility design |
| WS-002 | Procedural Digital Power and Algorithmic Inequality | KAND-038, KAND-039 | L3, L4, L6 | Under which institutional and technical conditions do digitally mediated decisions impair procedural protection or reproduce unequal treatment, and what counterexamples or safeguards change the claim? | R-EVIDENCE + R-CONTEXT | R-METHOD separately reviews query, legal-method boundary, and protocol compliance |
| WS-003 | Concentrated Infrastructure Dependency and Correlated Failure | KAND-052, KAND-053 | L1, L2, L5, L6 | When does concentration or common dependency create material correlated risk, when does it create resilience benefits, and which phenomenon is upstream? | R-METHOD + R-EVIDENCE | Same pair reviews query and eligibility design |
| WS-004 | Digital Materiality and Unequal Externalisation | KAND-056, KAND-060 | L1, L5, L6 | Which physical burdens are attributable to digital systems, how are burdens and benefits distributed, and when is materiality a mechanism, lens, consequence, or root candidate? | R-EVIDENCE + R-CONTEXT | R-METHOD separately reviews query and eligibility design |

Each workstream registers its question, exact claims, affected interests, boundary conditions, anticipated evidence types, inclusions, exclusions, language and jurisdiction limits, search plan, and claim-specific challenge conditions before `search_design_frozen_at`. The freeze precedes both the first search and sample precommitment.

## 4. Reviewer roles

| Role | Function | Independence condition |
|---|---|---|
| P-RESEARCH | Primary research execution and provisional drafting | Cannot independently review an object it authored or assessed |
| R-METHOD | Methodology reviewer | Challenges protocol adherence, search design, rubrics, and stopping logic |
| R-EVIDENCE | Evidence reviewer | Challenges source quality, dependence, counterevidence, and wording |
| R-CONTEXT | Scope and context reviewer | Challenges applicability, omitted interests, equality, and cross-layer claims |
| R-ADJUDICATION | Third reviewer for a recorded disagreement | Authored neither the object nor either initial review |
| H-DECISION | Michel, human decision authority | Decides scope and normative governance boundaries; cannot upgrade empirical evidence |

Review coverage is established by completed review-event records, not by findings. A review with no defect uses `outcome=NO_FINDING` and has no dummy finding.

Every event records role, reviewer identity and type, system, exact context locator, independence basis, shared-model or team risk, human-oversight status, target author provenance, time, attack question, basis, outcome, and status.

## 4.1 Exact double-review set

The complete pilot analysis set is double reviewed. It is not a discretionary later sample.

The eight object types are:

1. `CLAIM`;
2. `EVIDENCE_LINK`;
3. `CLAIM_ASSESSMENT`;
4. `MATERIALITY_ASSESSMENT`;
5. `ROOTNESS_ASSESSMENT`;
6. `EQUALITY_ASSESSMENT`;
7. `SYNTHESIS`; and
8. `TOPOLOGY_RELATION`.

Each initial review targets one immutable tuple:

`object_type + object_id + object_version + object_digest_sha256`

Both slots count only when two current `COMPLETED` events target the identical tuple, use the two workstream roles, have distinct reviewer-context locators, are independently true, and neither context is the author context. A different role label or prompt inside one continuing session is not a distinct context. A qualifying fresh context is separately instantiated and receives only the frozen object, approved method, registered evidence, and neutral review brief.

Changed content changes row identity, version, or digest and requires renewed double review. Reviews never migrate to corrected content.

R-METHOD also reviews each frozen search strategy before execution. That review does not replace either assigned object-review slot.

## 4.2 Screening overlap: seeded commit–reveal

Independent verification covers:

- every primary full-text exclusion;
- every primary event marked high topology impact; and
- a seeded 20% sample of primary title and abstract exclusions per workstream and stage.

A separate append-only sample plan is created for each `workstream + TITLE` and `workstream + ABSTRACT` pair. The state sequence is `PRECOMMITTED -> MATERIALIZED -> VERIFIED`, or an `INVALIDATED` terminal record.

### Precommitment

The PRECOMMITTED row fixes:

- `PROTOCOL-0.1`;
- eligibility `PRIMARY_EXCLUSION_AS_OF_CUTOFF_V1`;
- stage and workstream;
- an RFC 3339 UTC cutoff;
- `CSPRNG_256BIT` seed generation;
- `SEEDED_SHA256_LOWEST_V1` selection;
- 2,000 basis points and minimum sample size 1;
- a seed-custody basis and context distinct from all primary screeners;
- a commitment to a secret 256-bit seed.

Its introduction commit must be a strict Git ancestor of every commit that introduces a primary screening event for the same workstream and stage.

The commitment is exactly:

`SHA256_UTF8("SSP-COMMIT-V1|{plan}|{workstream}|{stage}|{protocol}|{cutoff}|PRIMARY_EXCLUSION_AS_OF_CUTOFF_V1|CSPRNG_256BIT|SEEDED_SHA256_LOWEST_V1|2000|1|{seed}")`

### Materialisation

After the cutoff, MATERIALIZED reveals the seed and records the Git population snapshot. The eligible set is exactly every graph-current `ACTIVE` primary exclusion in the same workstream and stage with `reviewed_at <= cutoff`. Eligible event IDs are ASCII-sorted.

For each event:

`selection_key = SHA256_UTF8("SSP-SELECT-V1|{seed}|{plan}|{workstream}|{source_id}|{stage}|{protocol}")`

Sort by `(selection_key, screening_event_id)`. For `N` eligible events:

- `k=0` when `N=0`;
- otherwise `k=min(N,max(1,ceil(2000*N/10000)))`.

The first `k` events are selected.

Population-manifest lines are:

`SSP-POP-V1|event_id|workstream|source|stage|decision|review_role|status|reviewed_at`

Selection-manifest lines are:

`SSP-SEL-V1|rank|selection_key_sha256|event_id`

Both manifests use UTF-8, LF between lines, no terminal LF, and lowercase SHA-256. An empty manifest hashes empty bytes.

### Verification and invalidation

VERIFIED requires an independent `SCREENING_SAMPLE_REVIEW` of the exact MATERIALIZED row, `outcome=NO_FINDING`, and a different context from the seed custodian, materialiser, and primary screeners.

Only a VERIFIED plan can be shown to the secondary reviewer. Each selected primary event gets exactly one `SECONDARY + DETERMINISTIC_SAMPLE` event. A later primary event with `reviewed_at > cutoff` invalidates the verified plan; an INVALIDATED record and an entirely new plan are required before secondary sampling resumes.

A `FULL_TEXT_CENSUS` or `HIGH_TOPOLOGY_CENSUS` secondary event is independent of the sample. High-topology designation always includes a rationale.

## 4.3 Disagreement and adjudication

1. Initial judgements and rationales remain immutable.
2. Each reviewer records retain or revise after exchanging written reasons.
3. A remaining dispute creates an `R-ADJUDICATION` event referencing exactly both initial review-event IDs.
4. The adjudicator context differs from the author and both initial reviewer contexts.
5. Adjudication never substitutes for an initial slot.
6. Unresolved evidence disagreement yields `CONTESTED_MIXED`, `HOLD_UNKNOWN`, or an open finding as applicable.
7. Unresolved normative authority goes to H-DECISION while the empirical disagreement remains intact.
8. H-DECISION cannot upgrade empirical evidence.

Same-model fresh-context review is correlated AI-assisted procedural review, not independent human or external peer review. The pilot reports this limitation.

## 5. Coverage rationale

The manifest deliberately spans:

- seven inherited candidates, exceeding the Protocol minimum of five;
- technical and AI correction in WS-001;
- human, social, procedural, legal, and normative dimensions in WS-002;
- infrastructure concentration, resilience benefits, and correlated failure in WS-003;
- ecological, distributional, and intergenerational interests in WS-004;
- plausible benefits, mitigation, null effects, and contrary evidence in every workstream;
- cross-layer topology in WS-002, WS-003, and WS-004;
- equality impact in WS-002 and WS-004.

The full differentiated-implementation safeguard is not presumed validated. It is tested only if an `EXISTING` or `PROPOSED` implementation is separately registered in scope. Otherwise it is reported as untested.

## 6. Frozen execution sequence

1. Record all five approvals and the passing Contract 0.4 execution gate.
2. Instantiate primary, review, seed-custody, and adjudication contexts.
3. Register four workstreams, seven candidates, questions, and affected interests.
4. Convert inherited phenomena to atomic claims and freeze challenge conditions.
5. Freeze search designs and obtain required query reviews.
6. Commit PRECOMMITTED sample rows through an authorised workflow role.
7. Execute searches and primary screening without revealing seeds.
8. Materialise and independently verify the title and abstract samples after each cutoff.
9. Conduct sample, full-text, and high-topology secondary screening and adjudicate disputes.
10. Chart sources and complete EVL, ASM, MAT, ROT, EQA, topology, and synthesis records where applicable.
11. Complete the exact double-review set and resolve or retain findings.
12. Publish a pilot evaluation recommending accept, revise, or reject for each method component.

Steps may be halted but not silently skipped. A deviation is registered before dependent work proceeds.

## 7. Exit criteria

Pilot 0.1 is complete only when:

- every candidate and workstream has a recorded disposition;
- every claim has challenge conditions and a counterevidence state;
- every search and screening event is reconstructable;
- every sample chain and Git ancestry check is reproducible;
- source independence and common origin have been assessed;
- MAT, ROT, EQA, topology, and iteration logic records without free-form workarounds;
- all required review-event coverage is exact;
- disagreements, schema defects, workload failures, and untested components are reported;
- no open critical pilot finding remains;
- the evaluation reports burden, reviewer agreement, correlated-review risk, register validity, and recommended amendments;
- H-DECISION records whether a production protocol may be designed.

Completion does not convert provisional records into production findings.

## 8. Stop conditions

Pause the affected workstream when:

- an approval dependency is missing, rejected, superseded, or revoked;
- the six-layer scope changes materially;
- a critical provenance, ethics, legal-access, or protocol-integrity concern arises;
- required independent contexts cannot be instantiated;
- evidence inaccessibility would invalidate the pilot objective;
- the validator cannot faithfully enforce a required constraint;
- the precommitment ancestry, commitment, population, selection, or verification check fails;
- a schema defect prevents faithful recording.

## 9. Fixed evaluation outputs

The pilot evaluation reports, for each Protocol component:

- whether it was exercised;
- whether the register represented it without workaround;
- workload and latency;
- agreement and disagreement pattern;
- AI-context correlation and oversight limitations;
- false inclusion or exclusion risk;
- observed opportunities for gaming or leakage;
- proposed change and consequence;
- recommendation: `ACCEPT`, `REVISE`, `REJECT`, or `UNTESTED`.

No change becomes binding without a new decision.

## 10. Change control

Version 0.3 is frozen for decision. Any substantive pre-approval change creates Version 0.4 or later and restarts approval. After approval, a change to candidates, workstreams, reviewer coverage, sampling, exit criteria, or authority boundary requires a recorded amendment and human approval.

Editorial corrections that do not change meaning remain visible through Git and are listed in the next version note.

### Version note

Version 0.3 keeps Pilot 0.1 and Protocol 0.1 unchanged. It upgrades the execution dependency to Register Contract 0.4, separates review execution from findings, fixes exact immutable review targets, and replaces an unauditable post-hoc 20% selection with a seeded append-only commit–reveal procedure.

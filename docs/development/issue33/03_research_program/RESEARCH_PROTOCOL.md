# Ypsia Constitutional Internet Research Protocol



**Status:** PROTOCOL-V0.1 CANDIDATE — PILOT AUTHORITY PENDING  

**Version:** 0.1  

**Last updated:** 2026-08-08  

**Governing proposal:** [RESEARCH_CHARTER.md](RESEARCH_CHARTER.md)  

**Register contract:** [registers/README.md](registers/README.md) and [register_schema.yaml](registers/register_schema.yaml)  
**Methodology basis and deviations:** [METHODOLOGY_BASIS.md](METHODOLOGY_BASIS.md)  

**Document role:** Proposed operational, repeatable procedure  

**Normative status:** Research-method proposal; not a findings repository



## 1. Research design



Subject to approval of DEC-005, DEC-008, DEC-009, DEC-010, and DEC-011, Version 0.1 tests a design that combines:



1. a systematic scoping review for broad, reproducible discovery and coverage mapping;

2. targeted evidence syntheses for exact candidate claims and problem families;

3. structured counterevidence searches;

4. multi-axial candidate classification and causal-topology analysis;

5. formal adversarial review before constitutional determination.



The scoping review maps the field. It does not by itself prove individual claims. Targeted syntheses establish what may responsibly be concluded about a specific candidate.



### 1.1 Pilot and production authority



Limited pilot approval authorises only the frozen pilot manifest, method testing, and provisional records. Pilot assessments cannot establish permanent problem IDs, production evidence categories, or constitutional conclusions.



Production use requires a later decision that reviews pilot burden, reviewer agreement, register validity, bias risks, and unresolved protocol findings before freezing version 1.0.



Until DEC-005, DEC-008, DEC-009, DEC-010, and DEC-011 are all Approved, this document may be edited and reviewed but no pilot evidence collection begins.



## 2. Units of analysis



The primary unit is the **exact claim**, not the source, topic, or candidate title.



Stable entities are:



- **SRC:** identified source;

- **CLM:** exact empirical, causal, technical, legal, or normative proposition;

- **KAND:** temporary candidate phenomenon inherited from or added to the longlist;

- **SYN:** targeted evidence synthesis;

- **DEC:** durable decision;

- **REV:** formal review;

- **WS:** research workstream;

- **SRCH:** recorded search;

- **ITER:** predeclared search-iteration batch and yield;

- **RQ:** registered research question;

- **INT:** registered affected or protected interest;

- **IMP:** registered existing or proposed implementation;

- **MAT:** versioned materiality assessment;

- **ROT:** versioned rootness assessment;

- **GAP:** explicit knowledge gap.



The executable schemas and controlled vocabularies are defined in [registers/README.md](registers/README.md). Canonical CSV registers own workstreams, questions, interests, searches and iterations, sources, claims, candidates, implementations, evidence relationships, assessments, syntheses, topology, formal reviews, and gaps. A synthesis is a versioned Markdown artefact with a stable SYN identifier and a canonical record in synthesis_register.csv.



A source can support, qualify, or contradict several claims. Each relationship is recorded separately. A candidate may have multiple causal roles in different contexts; primary and secondary classifications are therefore allowed.



## 3. Stage 1 — Workstream framing



Each workstream begins with a PCC frame:



- **Population or affected interests:** persons, groups, institutions, communities, non-users, ecosystems, or future generations;

- **Concept:** structural condition, mechanism, power relation, benefit, harm, exclusion, dependency, or risk;

- **Context:** one or more of the six sociotechnical layers and relevant jurisdictions, sectors, and periods.



The workstream record must state:



- questions and claim-type-specific challenge conditions;

- included layers and cross-layer relationships;

- affected interests;

- known candidate IDs;

- terminology and synonyms;

- anticipated evidence types;

- explicit exclusions;

- pilot or production status;

- date on which the search design was frozen.



### 3.1 Claim-type-specific challenge conditions



Every claim must state what could materially weaken, narrow, or overturn it, using the appropriate test:



- **Empirical claim:** falsifying observation, null result, incompatible replication, or boundary evidence.

- **Causal claim:** causal disconfirmation, credible alternative pathway, failed mediation, or incompatible intervention evidence.

- **Descriptive claim:** contradictory measurement, sampling limitation, changed prevalence, or invalid generalisation.

- **Technical claim:** counterexample, incompatible implementation evidence, threat-model failure, or proof defect.

- **Legal claim:** superseding authority, jurisdictional limitation, contrary interpretation, or unresolved doctrinal conflict.

- **Normative claim:** internal inconsistency, conflict with an approved commitment, counterexample, excluded interest, or failed universalisation.

- **Projected claim:** invalidated assumptions, changed baseline, alternative scenario, or forecast failure.



Moral commitments recorded as approved founder premises are not treated as empirically falsifiable. Their interpretation and consistency remain challengeable.

`MIXED` is an intake-only label, not a shortcut around claim decomposition. Separable propositions must become distinct claims before searching or synthesis. If components are logically inseparable, retain one MIXED claim, set `challenge_condition_type=MIXED`, enumerate every applicable component test in `challenge_conditions`, and justify inseparability in `boundary_conditions`. Empirical-evidence, formulation, normative-recognition, and counterevidence assessments remain separate.



## 4. Stage 2 — Systematic discovery



Every workstream must document a coverage rationale and, unless a justified deviation is recorded, include:



- at least two relevant scholarly databases or indexes;

- at least one relevant official, legal, statistical, institutional, or technical repository;

- backward and forward citation searching from the most relevant included syntheses or primary sources;

- lower-tier web sources only for hypothesis discovery or locating stronger evidence.



Before execution, a second reviewer who is procedurally independent from authorship examines the proposed concepts, synonyms, exclusions, databases, counterevidence terms, language coverage, and date limits. Reviewer type, system, context, independence basis, shared-model or shared-team risk, human-oversight status, findings, and resulting changes are recorded.



English is the default discovery language. Dutch is added for Netherlands-specific evidence and law. Other languages are added when material to the workstream and feasible; language exclusions and their likely bias are recorded. No claim is generalised globally merely because only English-language evidence was searched.



A workstream may be called a **systematic scoping review** only when it satisfies these minimum coverage, query-review, screening, flow-count, and traceability requirements. A workstream with a justified but material deviation must be labelled a **systematised scoping review**.



For every search, record:



- search ID;

- platform or repository;

- exact query;

- date, language, period, and filters;

- result count where available;

- export, snapshot, or stable locator;

- workstream and layer;

- whether the search targets support, contradiction, null effects, mitigation, or discovery;

- notes on access limitations.



Search strings must include problem-neutral and counterevidence terms. Queries designed only to confirm an existing candidate are insufficient.



The programme should prefer primary and authoritative sources. Reviews are used to map a field and locate primary evidence, not to create the appearance of independent confirmation when several publications rely on the same underlying evidence.



## 5. Eligibility and screening



### 5.1 Include when a source



- directly informs an in-scope claim, mechanism, boundary condition, benefit, or counterclaim;

- has a traceable author, institution, and publication identity;

- provides enough methodological, legal, or technical context to evaluate its contribution;

- is applicable to at least one specified population, layer, sector, or jurisdiction;

- contributes evidence, authoritative normative interpretation, or a documented limitation.



### 5.2 Exclude as supporting evidence when a source



- is marketing or advocacy without independently assessable support;

- merely repeats another source;

- offers unsupported commentary or anecdote;

- concerns only a proposed solution without informing diagnosis;

- lacks sufficient provenance;

- is materially obsolete for the claim and has no historical function;

- is a search snippet, generated summary, or secondary quotation without verified source context.



Excluded sources remain in the screening record with a reason code when they reached an eligibility stage or materially influenced discovery.



### 5.3 Screening procedure



1. title and snippet screening;

2. abstract or executive-summary screening;

3. full-text eligibility assessment;

4. duplicate and common-origin check;

5. recorded inclusion or exclusion reason.



For the protocol pilot, a second reviewer procedurally independent from the primary screening decision verifies all full-text exclusions, all records with high topology impact, and a fixed random sample of at least 20 percent of title and abstract exclusions. Reviewer provenance, shared-model or shared-team risk, disagreements, and resolutions are recorded. Production review coverage is frozen after the pilot; any reduction is a declared protocol deviation.



Screening counts must permit reconstruction of identified, deduplicated, title-screened, abstract-screened, full-text-assessed, included, and excluded records per workstream. Duplicate and common-origin exclusions remain separately identifiable.



## 6. Data charting and source appraisal



For each included source, record:



- citation and stable locator;

- source type and publication status;

- funding, institutional position, and declared conflicts where available;

- study or analysis design;

- population, geography, jurisdiction, sector, and period;

- layer or cross-layer relationship;

- exact result or normative proposition used;

- whether it supports, qualifies, or contradicts the claim;

- causal status: causal, correlational, descriptive, theoretical, projected, technical, legal, or normative;

- limitations stated by the source;

- additional reviewer-identified limitations;

- applicability to the current question;

- relationship to other sources and underlying datasets;

- page, section, table, paragraph, timestamp, or version locator;

- verification date and reviewer.



Appraise at least:



- directness;

- internal validity or legal and technical authority;

- transparency;

- precision;

- independence;

- applicability;

- recency where material;

- risk of selective or interested presentation.



Do not collapse these dimensions into an unexplained numeric score. A concise categorical judgement must retain the reasons that generated it.



## 7. Provenance and source preservation



Every durable source record uses one source-provenance class:



- A — exact recovered artefact;

- B — literal recovered text;

- C — researcher summary;

- D — unrecoverable historical source context;

- E — new research.



A project hypothesis is not a source. It is registered as a claim or candidate origin with type PROJECT_HYPOTHESIS, FOUNDER_STATEMENT, or another controlled origin and an exact origin locator.



A local copy is stored only when lawful, necessary, and proportionate. Otherwise record citation, DOI or stable URL, access date, version, locator, and a sufficiently precise claim-bound extraction. Copyrighted publications must not be added to the repository merely for convenience.



Copies, mirrors, reviews, and publications sharing the same dataset or institutional analysis are not automatically independent evidence.



## 8. Candidate registration and classification



A candidate record must contain:



- neutral working title;

- exact surviving claim or claims;

- originating source or hypothesis;

- primary classification;

- permitted secondary classifications;

- six-layer location;

- causal mechanism;

- fundamental benefit or harm;

- affected interests;

- boundary conditions;

- equality implications;

- related candidates and typed relationships;

- linked current claim-assessment IDs and their separate empirical-evidence, formulation, normative-recognition, and counterevidence states;

- strongest counterevidence;

- provisional action.



Primary classifications are:



- root problem;

- mechanism;

- consequence;

- affected interest or interest-holder;

- example;

- tension or trade-off;

- mitigation;

- solution constraint;

- hypothesis error.

Corrected and rejected are candidate or assessment states, not primary causal-topology classifications.



Permitted topology relationships include:



- causes;

- enables;

- amplifies;

- mediates;

- constitutes;

- results in;

- affects;

- mitigates;

- conflicts with;

- is an example of;

- is a component of.



Classification must not force a phenomenon that serves different causal roles in different contexts into one exclusive category.



### 8.1 Fundamental-harm rubric



Every proposed fundamental harm records the protected interest as APPROVED, NORMATIVELY_RECOGNISED, PROPOSED, or NOT_IDENTIFIED. A proposed or recognised interest may be researched, but it does not become an adopted Ypsia commitment without human approval.



Assess each materiality dimension as HIGH, MODERATE, LOW, or UNKNOWN with evidence and reasoning:



- severity for the affected interest;

- scale and affected population or system;

- duration and recurrence;

- reversibility and recoverability;

- unequal concentration or externalisation of burden;

- loss of agency, protection, voice, or contestability;

- systemic or cross-layer spillover;

- ecological or intergenerational persistence.



Pilot 0.1 freezes the following shared anchors before independent scoring:



| Dimension | HIGH | MODERATE | LOW |

|---|---|---|---|

| Severity | Death, serious or lasting impairment, loss of a fundamental right or protection, or comparably grave ecological damage. | Substantial but bounded impairment that remains meaningful after context and mitigation are considered. | Limited inconvenience, friction, or minor impairment. |

| Scale | Large-population, system-wide, or structurally unavoidable exposure for the affected class. | A bounded but substantial population, community, institution, ecosystem, or system segment. | Isolated, small, or narrowly local exposure. |

| Duration and recurrence | Persistent, cumulative, continuous, or repeatedly produced as a default structural pattern. | Recurring or medium-term, but bounded in time or frequency. | Transient, rare, or short-lived. |

| Reversibility and recoverability | Irreversible, practically unavailable to reverse, or recoverable only with extreme time, cost, or lost opportunity. | Reversible only through significant intervention, time, cost, or support. | Readily reversible with ordinary remedies and little residual loss. |

| Unequal externalisation | Material burdens concentrate on people, communities, regions, or generations with substantially less benefit, power, or voice. | A measurable and meaningful burden-benefit or voice imbalance that is bounded in scope. | No material disparity identified, or only a minor imbalance. |

| Agency and contestability | Effective choice, explanation, hearing, review, exit, or remedy is absent for a material decision or dependency. | One or more safeguards are materially constrained, but a usable alternative or remedy remains. | Only minor friction affects otherwise effective agency and contestability. |

| Systemic spillover | Effects cascade across layers, sectors, institutions, or common dependencies and can create correlated failure or power. | Effects span multiple systems or actors but remain bounded and containable. | Effects remain local to one component, actor, or use. |

| Ecological or intergenerational persistence | Long-lived, cumulative, irreversible, threshold-sensitive, or transferred materially to future generations. | Measurable persistence or future burden that is substantial but bounded or recoverable. | Short-lived, local, and readily recoverable ecological effect with no material future transfer. |



UNKNOWN means evidence was sought but cannot determine the rating; it forces HOLD_UNKNOWN when it could change threshold eligibility. NOT_APPLICABLE is permitted only when the dimension has no logical application to the exact candidate and a reason is recorded; it never counts toward the threshold. Every rating requires its own evidence-linked rationale in materiality_assessments.csv.



For the Protocol 0.1 pilot, a harm is eligible for further fundamental-harm consideration only when:



1. the affected interest and its status are explicit;

2. a digitally mediated structural mechanism is traceable;

3. at least one materiality dimension is HIGH or at least two are MODERATE;

4. the pattern is recurring, systemic, or structurally reproducible rather than an isolated incident;

5. contrary evidence and plausible mitigation have been assessed.



Eligibility is not constitutional determination. UNKNOWN ratings remain visible and can force a hold rather than being treated as zero.



### 8.2 Rootness rubric



A candidate may be proposed as a root problem only when it:



1. has a traceable causal path to at least one eligible fundamental harm or unjustified material risk;

2. is causally upstream of multiple manifestations, or explains a recurring class of structurally similar harm;

3. persists when one downstream manifestation is mitigated;

4. adds explanatory power beyond a broader parent condition;

5. cannot be reduced to a more precise in-scope condition without losing material causal meaning;

6. has a credible countermodel describing what would be observed if it were not root-level;

7. has its scope, cross-layer dependencies, and boundary conditions recorded.



The rubric is reasoned rather than additive. A broad label does not become root-level by accumulating examples, severity language, or citations.



## 9. Stage 3 — Targeted evidence synthesis



A targeted synthesis is required when:



- a candidate is proposed as an independent root problem;

- several candidates may form one problem family;

- a core causal claim remains unclear;

- evidence is contested, conditional, or predominantly normative;

- the candidate has high constitutional impact.



Before searching, freeze:



- the exact claim;

- proposed causal mechanism;

- affected interests;

- boundary conditions;

- inclusion criteria;

- candidate null and alternative explanations;

- known benefits and mitigations;

- the minimum evidence that would materially narrow, contradict, or support the claim.



Each synthesis reports:



1. exact question and claim;

2. source-selection method;

3. evidence supporting the claim;

4. counterevidence and null findings;

5. heterogeneity and boundary conditions;

6. causal assessment;

7. normative recognition, separately from empirical support;

8. applicability to Ypsia's later constitutional deliberation;

9. separate empirical-evidence, formulation, normative-recognition, and counterevidence assessments;

10. justified wording and prohibited stronger wording;

11. topology implications;

12. remaining uncertainty.



Meta-analysis is performed only when outcome, design, and population comparability justify it. Narrative synthesis must not conceal incompatible measures or contexts.



## 10. Counterevidence protocol



For every material claim:



1. formulate the strongest credible null hypothesis;

2. formulate at least one alternative causal explanation;

3. identify plausible benefits and legitimate countervailing interests;

4. search specifically for null results, contradictory findings, replication failures, heterogeneity, successful mitigations, and updated evidence;

5. assess whether mitigation removes the root problem or only reduces one manifestation;

6. revise claim wording before assigning confidence;

7. record unsuccessful counterevidence searches without treating absence as confirmation;

8. assign every claim entering synthesis, topology, or determination one counterevidence state: SEARCHED_FOUND, SEARCHED_NONE_FOUND, NOT_YET_SEARCHED, or NOT_APPLICABLE, with justification.



The strongest counterargument must be stated in terms its proponents would recognise. Counterevidence from a weak source is not privileged merely because it is contrary. A claim with counterevidence state NOT_YET_SEARCHED cannot pass a determination gate.



## 11. Protocol-v0.1 assessment axes



Empirical evidence, claim formulation, and normative recognition are assessed on separate axes. They must never be collapsed into a single score or omnibus category.



### 11.1 Empirical evidence status



| Status | Operational definition | Permitted use |

|---|---|---|

| **ESTABLISHED_HIGH_CONFIDENCE** | Multiple independent, high-quality, and sufficiently direct bodies of evidence converge; major alternatives and limitations have been examined; the bounded formulation is robust across the relevant studied contexts. | “Evidence strongly supports…” Never generalise beyond recorded boundaries. |

| **CONVERGENT_CONDITIONAL** | Multiple independent sources generally support the claim, but effect, magnitude, or mechanism materially depends on population, design, sector, period, or context. | “Evidence supports under the following conditions…” |

| **CONTESTED_MIXED** | Credible independent evidence supports and contradicts the claim, or results materially diverge by method or context and cannot yet be reconciled. | Preserve competing interpretations and identify the source of disagreement. |

| **PLAUSIBLE_UNDERSTUDIED** | A coherent mechanism and limited direct evidence exist, but independent or sufficiently rigorous evidence is inadequate. | Retain as hypothesis or research priority; do not present as an established standalone problem. |

| **INSUFFICIENT_INCONCLUSIVE** | The required assessment was completed, but the available evidence is absent, too indirect, too weak, or too incompatible to establish even limited support or to refute the bounded claim. | Hold as an unresolved gap; neither support nor rejection language is permitted. |

| **REFUTED** | The strongest applicable evidence contradicts the exact bounded claim and no defensible narrowing preserves its central proposition. | Reject the claim while retaining its historical traceability. |

| **NOT_APPLICABLE** | The exact claim contains no empirical proposition, as with a purely normative or doctrinal proposition. | Do not use empirical language; assess formulation and applicable normative or legal authority instead. |

| **NOT_ASSESSED** | The required synthesis has not been completed. | No evidentiary conclusion permitted. |



### 11.2 Formulation status



- **ADEQUATELY_BOUNDED:** wording matches the population, context, mechanism, and uncertainty supported by evidence.

- **NEEDS_NARROWING:** a defensible core remains, but the current wording exceeds its evidence.

- **MATERIALLY_MISFORMULATED:** the wording confuses constructs, sources, causal direction, or legal or technical meaning.

- **CORRECTED:** replacement wording has been recorded and linked to the historical formulation.

- **NOT_ASSESSED:** no claim-level wording review has occurred.



A materially misformulated claim is not automatically refuted. Correction and rejection are distinct outcomes.



### 11.3 Normative recognition



- **AUTHORITATIVE:** directly recognised in binding or highly authoritative applicable instruments.

- **CONVERGENT:** recognised across multiple independent authoritative or well-reasoned frameworks.

- **LIMITED:** recognised in a bounded, non-binding, contested, or emerging framework.

- **CONTESTED:** credible normative authorities materially disagree.

- **NONE_IDENTIFIED:** a documented search found no applicable recognition.

- **NOT_APPLICABLE:** the exact claim contains no normative proposition or affected interest for which recognition is meaningfully assessable.

- **NOT_ASSESSED:** no normative-recognition search has occurred.



Normative recognition may coexist with any applicable empirical evidence status. It does not establish prevalence, magnitude, or causality.



Determination effects are explicit:



- NOT_ASSESSED and INSUFFICIENT_INCONCLUSIVE cannot support a permanent problem determination;

- NOT_APPLICABLE cannot be cited as empirical support and is valid only when the exact claim contains no empirical proposition;

- PLAUSIBLE_UNDERSTUDIED remains a hypothesis or registered gap rather than an established standalone problem;

- CONTESTED_MIXED preserves the material disagreement and cannot be silently treated as convergent;

- REFUTED rejects the exact bounded claim while retaining its provenance;

- ESTABLISHED_HIGH_CONFIDENCE and CONVERGENT_CONDITIONAL are only candidate support paths, still subject to the post-pilot admissibility decision and every other determination gate;

- normative-recognition NOT_APPLICABLE or NOT_ASSESSED cannot be presented as recognition.



No assessment is assigned by source count alone. Every status applies to an exact claim and must name its population, context, material limitations, and reviewer.



## 12. Equality assessment



### 12.1 Candidate-level equality impact screen



Every candidate receives a lightweight diagnostic screen before topology determination:



- equality relevance: NOT_ASSESSED, NOT_APPLICABLE, NONE_IDENTIFIED, POSSIBLE, or MATERIAL;

- persons or groups differently exposed, burdened, protected, or able to contest;

- whether the difference concerns rights content, protection threshold, practical access, voice, remedy, or distribution of risk and benefit;

- whether evidence supports the distributional claim or only suggests a hypothesis;

- whether non-users or indirectly affected interests are omitted;

- whether the candidate itself creates or amplifies arbitrary privilege, dependency, or concentrated power.



This screen diagnoses possible equality effects. It does not prescribe differentiated treatment or a remedy.



### 12.2 Full differentiated-implementation safeguard



Apply the full safeguard only when evaluating an existing or proposed differentiated treatment, accommodation, protection, or implementation. Record:



- the common right and substantive goal;

- the demonstrated relevant difference;

- evidence excluding stereotype as the basis;

- necessity;

- less differentiating effective alternatives;

- preservation of the universal minimum;

- privilege, dependency, and power effects;

- transparency and contestability;

- review date;

- identity of the party carrying the burden of proof.



Failure of a safeguard is a substantive finding. Passing the safeguard does not prove that the implementation is effective, optimal, or constitutionally required.



## 13. Consolidation and topology review



For each candidate, propose one action:



- retain independently;

- merge;

- model as parent or child;

- reclassify;

- hold for evidence;

- reject or archive as corrected.



Consolidation must preserve:



- exact claims;

- dissenting evidence;

- cross-layer causes;

- affected interests;

- minority and edge cases;

- historical candidate IDs.



Human topology approval confirms scope and conceptual organisation. It does not change evidence classifications.



## 14. Formal red-team review



The evidence-derived pre-human topology is preserved as a versioned review object before founder or stakeholder adjustment. Every human adjustment records the changed relationship, rationale, authority, and affected evidence. Formal review examines both the pre-human topology and the adjusted version so that normative steering cannot silently become empirical classification.



For the pilot, two reviewers procedurally independent from the primary synthesist review the fixed subset declared in the Pilot Manifest. Their reviewer type, system, context locator, independence basis, shared-model or shared-team risk, human-oversight status, judgements, disagreements, and resolutions are recorded.

Procedural independence means separate authorship and separately instantiated review context. It does not establish human independence, model diversity, external peer review, domain expertise, or uncorrelated error. A same-model fresh-context review is labelled AI-assisted procedural review and must not be represented as independent human duplicate review, expert peer review, model-diverse replication, or external validation.

A later cold-context pass by the primary synthesist may supplement review but does not count as procedurally independent. Human oversight supplies accountability but cannot upgrade empirical evidence or substitute automatically for relevant expertise. Production requirements for human, information-specialist, legal, technical, domain, or affected-interest review are decided after the pilot. If a required form of review is absent, the result is labelled with the narrower review actually performed.



For every finding, record:



- review ID;

- attacked object and version;

- attack question;

- finding;

- severity;

- supporting evidence or reasoning;

- required response;

- implemented revision;

- residual risk;

- retest result;

- closure decision.



Severity levels are:



- **Critical:** invalidates evidence, safety, or constitutional coherence.

- **Major:** can cause material injustice, omission, or misclassification.

- **Moderate:** limits clarity, applicability, or confidence.

- **Minor:** bounded improvement without material effect.



Critical findings block determination. Major findings require resolution or explicit and compelling risk acceptance.



## 15. Saturation and stopping



A **search iteration** is a predeclared query batch that covers the workstream's specified source classes, core concepts and synonyms, and at least one counterevidence or mitigation path. Its identity, batch scope, linked search IDs, flow counts, yield, and newly discovered mechanisms, interests, candidate families, and category-changing counterevidence are recorded as one unit in search_iterations.csv. Trivial wording variants do not constitute separate iterations.



A workstream may be labelled provisionally conceptually saturated only when three consecutive logged targeted search iterations produce:



- no new independent mechanism;

- no new fundamental benefit or harm;

- no new affected interest;

- no new candidate family;

- no counterevidence capable of changing an existing category.



The search sets and null yield must be recorded per workstream.



Conceptual saturation does not mean empirical sufficiency, final completeness, no need for updates, or permission to skip targeted synthesis.



Programme-level research closes only when:



- every in-scope workstream has an explicit status;

- all high-impact candidates have a synthesis or a documented evidence gap;

- cross-layer relationships have been reviewed;

- no open critical red-team finding remains;

- unresolved uncertainty is visible;

- the human research-closure decision is recorded.



## 16. Determination gates



No permanent problem ID may be proposed until:



- the claim and boundaries are precise;

- the candidate's causal role is clear;

- the required targeted synthesis is complete;

- source independence and quality have been reviewed;

- counterevidence has been processed;

- equality implications have been assessed;

- overlap has been resolved or justified;

- constitutional relevance has been separately approved;

- formal red-team review has no open critical finding.



The eventual admissibility of evidence categories for permanent IDs is decided only after the taxonomy pilot and formal topology review.



## 17. Records, session closure, and compaction safety



Canonical registers must be updated before a conclusion is treated as durable.



At the end of every materially relevant session, [STATUS.md](STATUS.md) records:



- evidence or decisions added;

- conclusions changed;

- provisional conclusions still in force;

- open questions and blockers;

- exactly one active object and one next action;

- the last previously known reliable commit or an explicit uncommitted checkpoint.



[START_HERE.md](START_HERE.md) remains a stable reading map and does not duplicate current status. The commit containing STATUS is resolved from Git HEAD or log; STATUS does not attempt to contain its own commit identifier.



Commit per coherent epistemic change, not per file or calendar session. Use an explicit checkpoint only when unfinished work would otherwise be vulnerable to loss. No conclusion may depend solely on chat history or a checkpoint labelled as unreviewed.



## 18. Deviations and amendments



Any protocol deviation must record:



- what changed;

- why;

- affected workstreams and claims;

- likely bias or limitation;

- whether prior work requires re-review.



Protocol changes require versioning and a decision-log entry. New evidence does not itself constitute a protocol change.



## 19. Pilot exit criteria



Version 0.1 may be proposed for freezing as version 1.0 only after [PILOT_MANIFEST.md](PILOT_MANIFEST.md), containing at least five distinct pilot candidates, is frozen and explicitly approved. Together, the candidates must include:



- one primarily empirical human or social claim;

- one technical or resilience claim;

- one ecological or intergenerational claim;

- one primarily legal or normative claim;

- one claim with substantial counterevidence or a known historical correction;

- at least one genuinely cross-layer mechanism;

- at least one candidate that triggers the equality-impact screen;

- at least one existing or proposed differentiated implementation if the full equality safeguard is to be validated.



A candidate may satisfy more than one characteristic, but the manifest still contains at least five distinct candidates and exercises every required procedure.



The pilot must test:



- register usability;

- source-independence assessment;

- screening reason codes;

- category ambiguity;

- equality assessment where relevant;

- reviewer reproducibility;

- workload and documentation burden.



Pilot lessons must be resolved through explicit protocol amendments rather than silent variation.


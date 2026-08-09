# Foundational Definitions for the Problem Research

**Status:** Approved  
**Version:** 0.1  
**Date:** 2026-08-08  
**Authority:** Explicit human approval in the Issue 33 research dialogue  
**Applies to:** Revision of the Issue 33 problem research  

## 1. Purpose

This document establishes the binding conceptual foundation for revising the
Issue 33 research into societal problems associated with digital systems.

The earlier research classified candidate problems before fixing shared
definitions of a problem, the Internet, digital data architecture, a digital
mechanism, an architectural deficit, and the role of a human norm. This allowed
normative qualifiers such as *unreasonable*, *sufficient*, *effective*,
*proportionate*, and *unjustified* to perform hidden analytical work.

This document corrects that foundation. It does not approve any existing
candidate, derive Charter provisions, or design the target architecture.

## 2. Binding separation

Every research object must keep the following elements separate:

1. the factual societal situation;
2. the explicit human norm;
3. the digital mechanism;
4. the architectural contribution or deficit;
5. the evidence status of each link.

Evidence can establish facts, mechanisms, consequences, prevalence, causal
contributions, counterevidence, and uncertainty. Evidence does not independently
choose the human norm.

## 3. The Internet

> **The Internet is the shared communication infrastructure through which
> connected systems exchange data using interoperable network protocols.**

The Internet provides connectivity and reach. It does not prescribe one data,
application, governance, or ownership architecture. Different digital data
architectures can exist within the same Internet.

Consequently, the counterfactual question for this research is not *what would
happen without the Internet?* It is:

> **What changes within the same Internet when digital data is governed by a
> different foundational architecture?**

## 4. Digital data architecture

> **A digital data architecture is the set of technically enforceable
> structures, rules, protocols, and assignments of authority that determine how
> digital data is formed, identified, stored, copied, combined, derived,
> exchanged, changed, and terminated throughout its lifecycle.**

It also determines:

- to which person, organisation, or thing data is related;
- which source or state is authoritative;
- who is authorised to perform which actions;
- whether provenance, purpose, and context remain attached;
- how rights, powers, duties, and responsibilities are represented;
- what happens when data crosses a system boundary;
- whether transformations, derivations, transfers, and decisions remain
  demonstrable afterwards;
- what happens during service change, termination, failure, and recovery.

*Technically enforceable* does not mean that software must make every decision.
It means that the architecture can represent human authority, rights, and
responsibilities and can make their effects persist across relevant data
operations and system boundaries.

A right that exists only in a policy document, but cannot be recognised or
executed by the data system, is not an architectural safeguard.

### 4.1 Current digital data architectures

The phrase *current digital data architectures* is shorthand for dominant and
mutually reinforcing architectural patterns. It does not assert the existence
of one deliberately designed global architecture.

Patterns such as provider-bound state, account-bound identity, detached
provenance, non-propagating permissions, or separately governed derived data
are research hypotheses until established for a specific problem chain.

## 5. Factual societal situation

> **A factual societal situation is an observable state or event that can be
> described without first calling it desirable, harmful, reasonable, unfair, or
> unacceptable.**

Its description identifies:

- the conditions under which it occurs;
- the people, organisations, or other interests involved;
- what happens;
- the directly observable consequence.

The description must not hide a normative threshold inside an adjective.

## 6. Societal problem

> **A factual societal situation becomes a societal problem within this research
> when its consequence conflicts with an explicit, approved human norm.**

The factual situation and the norm must remain separately visible. A source can
support the existence or consequence of a situation without thereby approving
the norm used to judge it.

## 7. Human norm

> **A human norm is an explicit human choice about the state that must hold. Its
> normative status is recorded independently from empirical evidence status.**

Every norm must identify:

- **subject:** who or what is protected;
- **object:** what the protection concerns;
- **required state:** what must hold;
- **scope:** under which stated conditions it applies;
- **exceptions:** only explicitly approved exceptions;
- **authority and status:** who proposed or approved it, and whether it is
  proposed or approved.

Words such as *reasonable*, *adequate*, *appropriate*, *material*,
*proportionate*, and *effective* may be used only when the applicable test or
threshold has been defined in advance. Otherwise the required state must be
stated directly.

Norms may be absolute. For example, the currently proposed norm for service
change is zero loss of user-bound digital value. Its exact subject, object,
scope, and meaning still require explicit definition before candidate 2 can be
approved.

## 8. Digital mechanism

> **A digital mechanism is a repeatable relation of technical operations, rules,
> or dependencies through which a factual societal situation arises, expands,
> or persists.**

A mechanism is not a technology label. *A platform*, *AI*, *a database*, or
*the cloud* is not, by itself, a mechanism. A mechanism must state the relevant
operation or dependency and its factual consequence.

A mechanism need not be intentional or malicious. It may arise from local
design choices that appear rational separately but generate a recurring effect
together.

## 9. Architectural contribution

Mere permission is insufficient. A general-purpose infrastructure can permit a
vast range of conduct without contributing to it.

An architectural property contributes to a digital mechanism only when evidence
supports at least one of these relations:

| Relation | Meaning |
|---|---|
| Facilitates | Makes the mechanism technically or organisationally easier or cheaper. |
| Incentivises | Gives actors an advantage for using the mechanism or a disadvantage for avoiding it. |
| Amplifies | Increases its reach, speed, frequency, consequence, or replicability. |
| Entrenches | Makes termination, correction, departure, contestation, or recovery harder. |
| Necessitates | Makes the mechanism unavoidable for a conforming implementation. |

The research record may note that an architecture *permits* a mechanism, but
permission alone cannot admit a candidate as an architectural problem.

Every claimed contribution must identify:

1. the concrete architectural property;
2. the mechanism affected by it;
3. the contribution relation from the table above;
4. the evidence for that relation;
5. the counterfactual change expected under a different foundational rule.

## 10. Architectural deficit

> **An architectural deficit is a property or missing foundational rule of a
> digital data architecture through which a digital mechanism is facilitated,
> incentivised, amplified, entrenched, or necessitated across systems or
> implementations.**

An architectural deficit requires evidence that:

1. the mechanism is not attributable solely to one implementation error or one
   malicious actor;
2. multiple otherwise valid implementations can exhibit it;
3. a named property or missing foundational rule contributes to it;
4. a different foundational rule would remove, weaken, limit, or make the
   mechanism correctable while the Internet remains available as communication
   infrastructure.

A missing law, business practice, or social norm is not automatically an
architectural deficit. It becomes architecturally relevant when the applicable
authority, right, duty, or responsibility cannot be represented or made to
persist through the data system, or when the architecture structurally
amplifies its absence.

## 11. Research boundary

### 11.1 Directly in scope

- data representation and semantics;
- identity and binding to people, organisations, or things;
- authority, powers, permissions, and delegation;
- provenance, purpose, context, and transformation history;
- storage, replication, synchronisation, retention, and deletion;
- exchange, portability, and interoperability;
- derivation, aggregation, inference, and transformation;
- technically represented rights, duties, and responsibilities;
- auditability, demonstrability, and accountability;
- behaviour during system change, termination, failure, and recovery.

### 11.2 Conditionally in scope

Applications, platforms, cloud systems, and AI models are in scope only insofar
as they instantiate an underlying data-architecture pattern, exploit an
architectural deficit, or provide evidence about the effect of a pattern.

### 11.3 Context, not architecture by itself

- law and regulation;
- business models and economic incentives;
- institutional power relations;
- societal norms;
- conduct of individual actors.

These may explain adoption or use of an architectural pattern. They become part
of the architectural analysis only where they are technically represented,
enforced, amplified, or made persistent.

### 11.4 Out of scope

- an incident caused only by one implementation error;
- individual misconduct without an evidenced architectural contribution;
- a societal problem for which digital systems are only a communication channel;
- a problem that would remain materially unchanged under a different data
  architecture;
- solving the complete operation of economies, politics, cultures, or human
  morality.

The word *materially* in the fourth exclusion does not decide the outcome. The
candidate record must define the compared outcome and the threshold used for
that specific counterfactual test.

## 12. Admission test

An architectural research candidate is in scope only if all answers are yes:

1. Does the property govern or influence how data exists, moves, changes, or is
   placed under authority?
2. Does the property occur as a pattern beyond one actor or implementation?
3. Does it contribute to a named digital mechanism?
4. Can an alternative foundational rule change that mechanism while retaining
   the Internet as communication infrastructure?
5. Can that alternative rule be technically specified or enforced?

Passing this boundary test does not establish the candidate. It only admits the
candidate for evidence assessment.

## 13. Complete research unit

Every revised candidate must contain these separately assessable fields:

| Element | Required question |
|---|---|
| Factual situation | What demonstrably happens, under which conditions, and to whom? |
| Human norm | Which explicit approved state conflicts with the consequence? |
| Digital mechanism | Which repeatable digital operation or dependency produces or sustains it? |
| Architectural contribution | Which foundational property contributes, and how? |
| Counterfactual test | What changes under a different foundational rule? |
| Evidence status | Which links are supported, contested, unknown, or falsified? |

A missing element must be recorded as missing. It may not be supplied by an
undefined normative adjective or by treating an architectural hypothesis as a
fact.

## 14. Consequence for the existing baseline

The existing provisional problem baseline and map predate these definitions.
They remain useful as source indexes and records of prior analysis, but their
candidate formulations and statuses are not grandfathered into the revised
research.

Each candidate must be reconstructed and reassessed under this document before
it can be accepted as a societal problem with an architectural contribution.
No existing candidate is rejected merely because the foundation changed, and no
existing candidate remains approved merely because it appeared in the previous
baseline.

Candidate 2 will be the first reconstruction and calibration case.

## 15. Change control

These definitions are binding for the revision of the Issue 33 problem research.
A substantive change requires:

1. an explicit proposed revision;
2. a recorded rationale and expected effect on prior work;
3. explicit human approval;
4. a new document version;
5. identification of candidates that require reassessment.

No research step may silently broaden the definition of the Internet, the data
architecture, an architectural contribution, or a societal problem.

## Version history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-08-08 | Initial approved definitions and revision boundary. |

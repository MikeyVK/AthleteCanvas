# Candidate 002 Architecture Test

**Status:** SUPPORTING RESEARCH — USEFUL DEEP DIVE, NOT A REPEATABLE PROTOCOL  
**Version:** 0.3  
**Last Updated:** 2026-08-09  
**Decision Basis:** Current Charter 4.0 direction in DECISION_LOG.md  
**Scope:** Candidate 2A and 2B only

---

## 1. Purpose

This document retains useful source findings, examples, and architectural patterns for candidate 2A and 2B. The procedure is not a template for the other candidates and is not a precondition for Charter text.

This document tests two approved factual problem cores and their human norms against four existing digital data architectures.

It does not select a target architecture. It does not claim that one of the tested architectures is a complete solution.

The tested architectures are comparative controls and possible solution directions. They are not the primary research subjects and cannot establish that commonly used platforms dysfunction in practice. Their role is narrower:

> Show whether parts of 2A and 2B are technically avoidable, identify mechanisms that may prevent them, and provide comparison material for later tests of commonly used platforms.

The comparison is limited to official specifications and official project documentation.

---

## 2. Approved Test Objects

### 2A — Loss of the digital source

**Factual core**

When a digital system changes, is replaced, or disappears, the digital source can be lost partly or completely. Source loss means that no intact, retrievable copy remains.

Temporary unavailability is not source loss unless it results in the disappearance of every intact, retrievable copy.

**Human norm**

Changing, replacing, or ending a system must cause zero loss of the digital source. Whether the source itself should end is a separate decision from the lifecycle of the system that currently stores or presents it.

### 2B — Loss of recorded connections

**Factual core**

When a digital system changes, is replaced, or disappears, the digital source can remain while recorded connections to people or organisations, their roles, contributions, actions, and history are lost partly or completely. The digital whole then loses part or all of a function it previously had.

**Human norm**

The same system event must cause zero loss or alteration of those recorded connections. The connections must remain intact, recognisable, checkable, and usable.

This norm does not require preservation of a provider-specific interface, score, ranking, recommendation, or algorithm. A deliberate decision to end a source, role, or relationship is a separate authority question.

---

## 3. How the Architectures Are Judged

Each architecture is tested on two different levels:

1. **Capability:** Can the architecture technically preserve the source or connection?
2. **Guarantee:** Does its core model require enough for the zero-loss norm to hold when a system or provider disappears?

A capability is not a guarantee. For example, an architecture may allow ten copies while still permitting every copy to be deleted.

The ratings mean:

- **Strong partial support:** the core model directly addresses an important part of the norm;
- **Partial support:** useful mechanisms exist, but essential conditions remain outside the architecture;
- **Limited support:** the architecture can carry relevant data but does not directly govern its meaning or continued existence;
- **No zero-loss guarantee:** the approved human norm is not guaranteed by the core architecture.

---

## 4. Comparison

| Architecture | 2A: digital source | 2B: recorded connections | Central limitation |
|---|---|---|---|
| Git | Strong partial support; no zero-loss guarantee | Partial support | Only represented repository history is preserved, and only while at least one copy retains the reachable objects |
| IPFS | Partial support; no zero-loss guarantee | Limited support | Content identity and integrity do not guarantee that any node continues to store the content |
| Solid | Partial support; no zero-loss guarantee | Strong partial support | App/data separation and linked data help, but storage continuity, URI continuity, and complete migration are not guaranteed |
| W3C Verifiable Credentials 2.0 | Partial support; no zero-loss guarantee | Strong partial support for credential relationships | The credential can travel, but verification can still depend on external issuer identifiers, keys, status information, or schemas |

No tested architecture guarantees both approved zero-loss norms by itself.

---

## 5. Git

### What Git preserves

Git stores content as immutable objects addressed by a hash of their contents. Trees record directory structure, and commits record a snapshot together with parent history and author metadata.

A distributed clone contains the repository and its history. If a central server disappears, another complete clone can restore the repository.

### 2A result

Git strongly reduces dependence on one provider. The source can survive the disappearance of the original server because complete copies can exist independently.

It does not guarantee zero loss. Unreachable objects can be garbage-collected, and Git cannot preserve a repository if every copy is lost or deleted. Continued existence therefore still depends on actual retention by one or more custodians.

**Rating:** strong partial support; no architecture-level zero-loss guarantee.

### 2B result

Git can preserve the connections it explicitly models: file structure, changes, commit parentage, timestamps, and recorded author information.

It does not automatically preserve provider-specific issues, pull requests, comments, permissions, social roles, or the real-world identity and authority behind an author name. Cryptographic signing is possible, but it is not a universal requirement of the core history model.

**Rating:** partial support.

### Finding from Git

Distributing the complete source and its history removes one system as a necessary point of survival. The protection applies only to connections included in the portable data model and only while an independent copy retains them.

---

## 6. IPFS

### What IPFS preserves

IPFS identifies content using a Content Identifier derived from the content. The identifier is independent of a server location. Retrieved content can therefore be checked against the requested identifier, and an altered object receives a different identifier.

Nodes can store and pin copies of the content.

### 2A result

IPFS separates the identity of the source from the location of its current provider and makes replication possible.

It does not guarantee persistence. Cached content may be garbage-collected, and official documentation explicitly states that content can disappear when no node continues to pin or otherwise retain it. A CID can continue to identify content even when no retrievable copy remains.

**Rating:** partial support; no architecture-level zero-loss guarantee.

### 2B result

IPFS can store linked, content-addressed data structures. It does not itself define the meaning of a person, role, contribution, authority, or historical relationship. Those connections must be represented and preserved by an additional data model and application rules.

**Rating:** limited support.

### Finding from IPFS

Stable content identity and integrity are not the same as continued existence. A source needs an explicit preservation responsibility in addition to a provider-independent identifier.

---

## 7. Solid Protocol

### What Solid preserves

Solid separates applications from externally stored data. It uses global identifiers, linked data, authentication, authorisation, and auxiliary resources for such matters as access control, descriptions, and provenance.

A person can use more than one conforming application with data held in Solid storage.

### 2A result

Changing an application need not destroy the source because the application does not have to own the only copy.

The protocol does not provide a general backup, migration, or minimum-replication guarantee. If the storage provider disappears, the continued existence of the source still depends on arrangements outside the core protocol.

**Rating:** partial support; no architecture-level zero-loss guarantee.

### 2B result

Solid directly supports portable links and machine-readable relationships between resources. This offers a stronger basis for preserving connections than an application-specific database that has no shared data model.

It does not guarantee that a replacement storage provider preserves every URI, auxiliary resource, vocabulary meaning, access rule, and provenance relationship. The current Solid Protocol document is also a Draft Community Group Report rather than a W3C Standard.

**Rating:** strong partial support.

### Finding from Solid

Separating data from applications protects against application replacement. It does not by itself separate the data and all its connections from the lifecycle of the storage service.

---

## 8. W3C Verifiable Credentials Data Model 2.0

### What Verifiable Credentials preserve

A verifiable credential can contain claims together with the issuer, credential subject, and cryptographic proof. A holder can present it to a verifier independently of the application in which it was first issued.

The verifier can check integrity and authenticity using the verification material referenced by the credential.

### 2A result

A credential can be held outside the issuer's original system or a particular wallet provider. This reduces dependence on that system for possession of the source.

The standard does not guarantee that a copy of the credential survives. Verification can also depend on external material such as issuer identifiers, verification methods, status lists, contexts, or schemas. Their continued availability and historical validity are not universally guaranteed by the data model.

**Rating:** partial support; no architecture-level zero-loss guarantee.

### 2B result

For the diploma example, the model can carry the relevant connections with the source: who issued the credential, who or what it concerns, what is asserted, and which proof allows integrity and issuer authenticity to be checked.

This is the strongest tested fit for that specific connection pattern. It does not make trust in the educational institution unnecessary. It makes the institution's assertion portable and checkable, subject to the continued interpretability and validity of its verification dependencies.

**Rating:** strong partial support for credential-shaped relationships.

### Finding from Verifiable Credentials

A relationship can travel with the source instead of remaining trapped in one provider's database. Its independent evidential value still depends on preserved verification material and an identifiable source of authority.

---

## 9. Cross-Architecture Findings

### 9.1 The two problem cores are technically distinguishable

The architectures address 2A and 2B differently:

- IPFS is strongest in stable content identity but weak in guaranteed persistence and social meaning.
- Solid is stronger in app-independent linked relationships but does not guarantee storage continuity.
- Verifiable Credentials are stronger in portable, checkable issuer-subject-claim relationships but retain external verification dependencies.
- Git combines distributed source copies with represented history, but only inside the repository model.

This supports keeping 2A and 2B as separate factual problem cores.

### 9.2 The required capabilities already exist in parts

The comparison shows that the following are technically possible:

- complete independent copies of source and history;
- provider-independent content identity and integrity checks;
- separation of applications from data;
- portable, machine-readable relationships;
- cryptographic checking of recorded claims and issuer connections.

The research therefore must not describe source and connection preservation as technically impossible.

### 9.3 The comparison exposes a design gap, not proof of platform dysfunction

None of the tested core architectures requires all of the following together:

1. at least one intact, retrievable source copy survives a system lifecycle event;
2. the connections necessary for its function survive with it;
3. those connections remain recognisable, checkable, and usable;
4. the result does not depend on the continued operation of the system that is being replaced or lost.

This is only a comparison finding. It does not show how commonly used platforms behave, how often 2A or 2B occurs, or whether their architectures facilitate those outcomes.

### 9.4 Provisional mechanism hypotheses

The comparison suggests two bounded hypotheses. They remain untested until examined against commonly used platforms, actual lifecycle events, and counterevidence:

**2A hypothesis**

Source loss is facilitated when continued existence remains an operational choice of the current custodians and the architecture contains no independent persistence condition that survives their system lifecycle.

**2B hypothesis**

Connection loss is facilitated when people, roles, actions, history, meaning, or verification dependencies remain in provider-specific state or in external resources that do not travel with the source under a shared, durable model.

These hypotheses still need testing against actual incumbent systems and counterexamples.

---

## 10. What This Test Does Not Establish

This comparison does not establish:

- how commonly each architecture is deployed correctly;
- whether users understand or control its preservation mechanisms;
- the economic cost of durable independent copies;
- the privacy, security, erasure, and data-minimisation trade-offs;
- that every digital source or connection should be preserved indefinitely;
- that the four mechanisms should be combined in a future architecture;
- that 2A or 2B is already a final, generally proven Internet problem.

---

## 11. Preliminary Conclusion

Existing architectures show that system-independent preservation is technically possible in meaningful parts. That makes them useful controls and possible solution sources.

They do not prove that the platforms people commonly use dysfunction, that 2A or 2B is frequent or material there, or that a shared architectural mechanism causes those outcomes. Those questions require evidence from the platforms and dependencies that form the present usage standard.

---

## 12. Next Steps

1. Select concrete, commonly used platform classes in which people store sources or depend on recorded connections.
2. Establish with platform documentation, observed lifecycle events, and empirical evidence whether 2A and 2B actually occur.
3. Determine whether the outcomes are incidental implementation failures or are facilitated by recurring architectural choices.
4. Assess materiality: who depends on the platform, what function is lost, and whether realistic recovery exists.
5. Use Git, IPFS, Solid, Verifiable Credentials, and other counterexamples only to test technical avoidability and possible remedies.
6. Only after those tests, decide whether 2A and 2B remain independent problem candidates, require further splitting, or can be rejected.

---

## 13. Official Sources

### Git

- [Git Book — About Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control.html)
- [Git Data Model](https://git-scm.com/docs/gitdatamodel.html)
- [Git Internals — Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects.html)
- [Git Book — Distributed Workflows](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows)

### IPFS

- [IPFS Documentation — Content Addressing](https://docs.ipfs.tech/concepts/content-addressing/)
- [IPFS Documentation — Persistence](https://docs.ipfs.tech/concepts/persistence/)
- [IPFS Documentation — Content Lifecycle](https://docs.ipfs.tech/concepts/lifecycle/)
- [IPFS Documentation — How IPFS Works](https://docs.ipfs.tech/concepts/how-ipfs-works/)

### Solid

- [Solid Protocol](https://solidproject.org/TR/protocol)

### W3C Verifiable Credentials

- [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/)
- [W3C announcement — Verifiable Credentials 2.0 is a W3C Standard](https://lists.w3.org/Archives/Public/w3c-news/2025AprJun/0000.html)

---

## Related Documents

- [Foundational Definitions](FOUNDATIONAL_DEFINITIONS.md)
- [Candidate 002 Reconstruction](CANDIDATE_002_RECONSTRUCTION.md)
- [Decision Log](DECISION_LOG.md)
- [Research Status](STATUS.md)

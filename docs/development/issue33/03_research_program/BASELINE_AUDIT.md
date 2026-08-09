# Issue 33 Research Baseline Audit

**Status:** PRELIMINARY  
**Version:** 0.3  
**Last updated:** 2026-08-08  
**Scope:** The 35 untracked files that existed before creation of 03_research_program

## 1. Outcome

- Existing untracked files: 35.
- Existing modified files: 0.
- Current explicit untracked classification after research-program setup: 72 files = group A 28 + group B 6 + group C 1 + group D 37.
- Working-tree size of the 35 files: 1,881,366 bytes.
- Unique Git blob content: 30 blobs totalling 1,205,044 bytes.
- Exact duplicate checkout content: five duplicate pairs accounting for 676,322 bytes; Git will store identical content once per object database.
- Transfer package integrity: all 27 records in MANIFEST.sha256 verified successfully. Together with the manifest file itself, the package contains 28 files.
- Credential scan: a heuristic pattern scan across the 35 file contents found no recognisable API token, private key, or other credential. This was not an entropy-based secret scan or external credential validation.
- Repository-size risk: low at the current size, provided future binary revisions remain deliberate.
- Diffability risk: one redundant Markdown representation contains a 78,012-character one-line base64 image payload.
- Distribution-provenance risk: the repository does not currently establish authorship or redistribution rights for the supplied PDF or image content, including both PNG artefacts.

This audit does not establish external redistribution rights and is not legal advice.

## 2. Baseline group A — recovered research archive

**Proposed commit subject:** Preserve recovered Issue 33 research archive

These 28 files form one integrity package and should be committed atomically before any of them is changed:

- ../START_HERE.md
- ../CODEX_HERVATINSTRUCTIE.md
- ../INTEGRATIE_IN_PROJECTMAP.md
- ../MANIFEST.md
- ../MANIFEST.sha256
- ../00_teruggevonden_exact/BRONNENREGISTER.md
- ../00_teruggevonden_exact/Kritiek_op_het_huidige_internet.pdf
- ../00_teruggevonden_exact/Kritiek_op_het_huidige_internet_tekstextractie.txt
- ../00_teruggevonden_exact/Projectmap_bestandslijst_2026-08-06.png
- ../00_teruggevonden_exact/Ypsia_Charter_v3.0_teruggevonden_contextkopie.md
- ../00_teruggevonden_exact/Ypsia_Constitutionele_Inventaris.md
- ../00_teruggevonden_exact/Ypsia_Constitutionele_Onderzoeksmethodiek.md
- ../00_teruggevonden_exact/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.1.md
- ../00_teruggevonden_exact/01_oorspronkelijk_onderzoek/Kritiek_op_het_huidige_internet.pdf
- ../00_teruggevonden_exact/01_oorspronkelijk_onderzoek/Kritiek_op_het_huidige_internet_tekstextractie.txt
- ../00_teruggevonden_exact/02_aanvullend_onderzoek/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.1.md
- ../01_werknotities_heronderzoek/README.md
- ../01_werknotities_heronderzoek/audit_initial_research.md
- ../01_werknotities_heronderzoek/heronderzoek_cross_domain.md
- ../01_werknotities_heronderzoek/heronderzoek_ecology_resilience.md
- ../01_werknotities_heronderzoek/heronderzoek_human_democracy.md
- ../02_overdrachtsdocumenten/BESLISLOGBOEK.md
- ../02_overdrachtsdocumenten/BRONNENREGISTER_v0.2.md
- ../02_overdrachtsdocumenten/CLAIM_BRON_TEGENBEWIJS_MATRIX.md
- ../02_overdrachtsdocumenten/KANDIDATENLONGLIST.md
- ../02_overdrachtsdocumenten/ONDERZOEKLOGBOEK_2026-08-06.md
- ../02_overdrachtsdocumenten/OPEN_GATEN_EN_RED_TEAMSTATUS.md
- ../02_overdrachtsdocumenten/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.2.md

**Atomicity reason:** MANIFEST.sha256 describes the other package members. Splitting the first baseline would create intermediate commits in which the recorded package is incomplete.

**Important:** Do not rewrite top-level START_HERE.md under the current manifest contract. MANIFEST.sha256 hashes that exact path, so a later rewrite would make verification at HEAD fail even if an earlier baseline commit remains valid. Current work instead uses 03_research_program/START_HERE.md as its canonical navigator. Any future change to the historical top-level path requires an explicit new manifest or archive-migration decision.

## 3. Baseline group B — current constitutional context

**Proposed commit subject:** Preserve current Issue 33 constitutional context

These six files are current context rather than members of the archive manifest:

- ../De Constitutionele Orde - Concept.md
- ../Grondwet van Ypsia - Concept (Deel 1 t_m 6).md
- ../Inhoudsopgave Ypsia Grondwet.md
- ../Paradigmaverschuiving.md
- ../Ypsia_Constitutionele_Inventaris.md
- ../Ypsia_Constitutionele_Onderzoeksmethodiek.md

They should be committed separately because their document identity differs from the immutable reference copies, even where current contents are byte-identical or semantically equivalent.

## 4. Baseline group C — quarantined redundant representation

**Proposed state:** Do not commit until provenance is consciously resolved.

File:

- ../Kritiek Op Het Huidige Internet.md

Findings:

- The text is an alternative Markdown representation of the archived PDF and extraction. After removal of the embedded base64 payload and normalisation of case, whitespace, and Markdown presentation, its unique-token Jaccard similarity is approximately 98.64 percent.
- Its principal additional payload is a 78,012-character base64 line encoding a 620 by 744 pixel PNG.
- Decoded PNG size: 58,507 bytes.
- Decoded PNG SHA-256: b3bcb01f49911a23fd776351a7d0cef5d9e9adabce1dad751d58cab7976904e4.
- No author, origin, caption, or licence is recorded for the embedded image.
- The one-line base64 payload is poorly diffable.

Safe later options:

1. confirm authorship and redistribution rights, extract the image to a separate file, and record provenance;
2. remove the image from the current representation while retaining the already archived original analysis;
3. leave the redundant Markdown representation outside version control.

No option should be applied without an explicit human decision because removal or alteration changes an existing artefact.

## 5. Exact duplicates

The following pairs are byte-identical:

1. Archive PDF and compatibility PDF under 01_oorspronkelijk_onderzoek.
2. Archive text extraction and compatibility extraction under 01_oorspronkelijk_onderzoek.
3. Archive v0.1 dossier and compatibility v0.1 dossier under 02_aanvullend_onderzoek.
4. Current and archived Ypsia_Constitutionele_Inventaris.md.
5. Current and archived Ypsia_Constitutionele_Onderzoeksmethodiek.md.

The first three pairs intentionally preserve historical relative links. The last two pairs currently have different document roles: immutable reference and living context. None should be removed merely as deduplication.

The current Grondwet concept and the recovered Charter 3.0 context copy have the same normalised word sequence apart from title and Markdown presentation. They remain separate document identities.

## 6. Binary and distribution considerations

Binary files in the archive package:

- PDF: 579,240 bytes, present at two byte-identical paths.
- Project-map PNG: 23,026 bytes.
- Checked-out binary total: 1,181,506 bytes.
- Unique binary blob total: 602,266 bytes.

Git object deduplication makes the present size acceptable. Repeatedly replacing PDFs or images would create permanent binary history and should therefore be avoided.

No repository-level LICENSE, COPYING, or NOTICE file was found during this audit. The PDF metadata records only its title and “Skia/PDF m153 Google Docs Renderer” as producer; no author or copyright field was visible.

For a private repository, this is primarily a provenance-documentation issue. Before public distribution, authorship and redistribution permission for supplied PDF and image content should be confirmed.

## 7. Baseline group D — canonical research programme

**Proposed commit subject:** Establish Issue 33 research governance and pilot package

These 37 files form the new living research layer and belong in a separate commit after groups A and B:

- ../CURRENT_RESEARCH.md
- START_HERE.md
- RESEARCH_CHARTER.md
- RESEARCH_PROTOCOL.md
- PILOT_MANIFEST.md
- METHODOLOGY_BASIS.md
- STATUS.md
- DECISION_LOG.md
- GLOSSARY.md
- BASELINE_AUDIT.md
- registers/README.md
- registers/register_schema.yaml
- registers/workstream_register.csv
- registers/research_question_register.csv
- registers/interest_register.csv
- registers/search_log.csv
- registers/search_iterations.csv
- registers/search_links.csv
- registers/source_register.csv
- registers/source_relations.csv
- registers/screening_precommitments.csv
- registers/screening_events.csv
- registers/claim_register.csv
- registers/claim_assessments.csv
- registers/candidate_register.csv
- registers/implementation_register.csv
- registers/evidence_links.csv
- registers/materiality_assessments.csv
- registers/rootness_assessments.csv
- registers/equality_assessments.csv
- registers/topology_relations.csv
- registers/review_events.csv
- registers/synthesis_register.csv
- registers/review_register.csv
- registers/gap_register.csv
- workstreams/README.md
- syntheses/README.md

The quarantined file in group C must not be accidentally included through broad staging.

The current root pointer is ../CURRENT_RESEARCH.md and the in-program canonical navigator is START_HERE.md. The historical top-level START_HERE.md is not rewritten, so the recovered manifest remains verifiable.

STATUS may record the already known group A and B commit identifiers before group D is committed. Group D cannot contain its own final commit hash; at resume time its containing commit is resolved from Git HEAD or log. A later meaningful checkpoint may record that identifier, but a self-referential follow-up commit is not required solely for bookkeeping.

## 8. Required verification before commits

1. Re-run Git status and stage only the explicit group file list.
2. Verify archive manifest integrity before group A.
3. Confirm no historical file changed before group A.
4. Validate Markdown structure and cross-references in group D.
5. Verify that all 23 canonical CSV files contain only their schema-matching header row before the pilot.
6. Verify that register_schema.yaml is valid machine-readable JSON/YAML, matches every CSV header, and passes scalar, multi-value, polymorphic, canonical-document, enum, conditional, supersession, unique-current, computed, and cross-record validation.
7. Record group A and B commit identifiers in STATUS before group D when available.
8. Resolve the commit containing group D from Git HEAD or log; do not create an otherwise meaningless self-referential commit.

## 9. Contract 0.4 correction checkpoint

The 0.3 cold audit found recordability gaps but no Protocol defect. Contract 0.4 and Pilot Manifest 0.3 therefore form a clean-break correction over the still-empty baseline. Two registers were added: review_events.csv records execution and NO_FINDING outcomes; screening_precommitments.csv records the seeded append-only sample-plan chain. Protocol 0.1 and every historical manifest-controlled file remain byte-unchanged.

## 10. Evidence-entry validation checkpoint

**Canonical owner:** This section of BASELINE_AUDIT.md  
**Status:** NOT_RUN — blocked by human approval and authorised validator implementation  
**Contract:** Register Contract 0.4  
**Schema SHA-256:** AB70BD60BA1E4F32695D0C7F0DEBA54CD20E7E45CECDE18EE5FFA3781525864D  
**Declared constraint IDs:** 149  
**Validator version:** NOT_IMPLEMENTED  
**Constraint IDs tested:** 0  
**Positive fixtures accepted:** 0  
**Single-fault negative fixtures rejected:** 0  
**Passed:** NO  
**Recorded at:** 2026-08-08  
**Recorded by:** standalone research role  
**Authorised Git execution role:** UNASSIGNED  
**Seed-custodian assignment:** UNASSIGNED

This is a durable negative gate record, not a failed empirical result. After all five governance decisions are Approved, an authorised implementation role may build the validator and fixtures. H-DECISION must then record the Git execution role and seed-custodian identity/context before PRECOMMITTED is introduced. This section is updated with the exact validator version, complete constraint-ID coverage, fixture totals, and pass result before the first evidence row.

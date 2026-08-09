# Workstream Artefact Guide

**Status:** PRELIMINARY  
**Version:** 0.1  
**Last updated:** 2026-08-08

## Purpose

A workstream dossier provides the readable framing and execution context for one bounded research workstream. workstream_register.csv remains authoritative for identity, status, scope fields, flow counts, and ownership. Research questions, interests, search iterations, and syntheses retain their own canonical register owners.

## Naming

- File: WS-###_<short-slug>.md
- Directory: this directory
- ID: existing workstream_id from workstream_register.csv
- New files must be created through the project research-document scaffold.

## Required sections

1. **Identity and status**
   - Workstream ID
   - Protocol version
   - Pilot or production role
   - Owner and independent reviewers
   - Frozen framing date

2. **Questions and challenge conditions**
   - Registered RQ identifiers and exact research questions
   - Claim IDs
   - Claim-type-specific weakening or disconfirmation conditions

3. **PCC frame**
   - Population or affected interests
   - Concept
   - Context and layers
   - Cross-layer relationships

4. **Scope**
   - Inclusion criteria
   - Exclusion criteria
   - Geography, jurisdiction, languages, sectors, and period
   - Explicit non-scope

5. **Coverage rationale**
   - Scholarly databases or indexes
   - Official, legal, institutional, statistical, or technical repositories
   - Citation-chain plan
   - Language and access limitations
   - Material protocol deviations

6. **Search-strategy review**
   - Review IDs
   - Reviewer independence
   - Findings and implemented revisions

7. **Search iterations, screening, and appraisal plan**
   - Predeclared ITER records and saturation-yield fields
   - Primary, secondary, and adjudication roles
   - Fixed independent-review sample
   - Applicable appraisal dimensions
   - Flow-count reconciliation rule

8. **Candidate and equality coverage**
   - Candidate IDs
   - Registered INT identifiers
   - Equality-impact screen requirements
   - Known counterevidence targets

9. **Open gaps and risks**
   - GAP IDs
   - Bias and applicability risks
   - Conditions that block synthesis

10. **Outputs**
   - Synthesis IDs owned by synthesis_register.csv
   - Review IDs
   - Required status transition

## Non-duplication rule

The dossier references register IDs. It does not reproduce bibliographies, source rows, search or iteration records, evidence extractions, screening events, materiality or rootness ratings, or mutable assessment statuses.

## Closure

A workstream dossier may be closed only when register flow counts reconcile, required synthesis and review objects exist, open gaps have an explicit disposition, and STATUS points to the next programme-level action.

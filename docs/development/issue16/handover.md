# Epic 16 Handover

## Huidige Status
- De sessie is gestart om de fundamentele architectuur frictiepunten (Epic 16) te evalueren en het fundament voor Ypsia strak te trekken.
- Alle belangrijke besluiten zijn succesvol geëvalueerd en vastgelegd in `docs/development/issue16/topics_evaluation.md`.
- Het originele fundamentele onderzoek (`docs/development/issue16/research.md`) is hersteld via git nadat deze per ongeluk was overschreven.
- De agent en gebruiker bevinden zich momenteel in de overgangsfase (stap 1): het originele `research.md` moet stap voor stap worden herzien en afgestemd op de nieuwe besluiten uit `topics_evaluation.md`.

## Belangrijkste besluiten (zie topics_evaluation.md)
- **pgvector vs ChromaDB**: Volledige deprecation van ChromaDB; we gebruiken PostgreSQL + pgvector + RLS voor alles.
- **Background Workers**: Strak `data_shares` model in plaats van dynamisch context switchen.
- **Waitlist Security**: Decentrale private key via CIA-grade client memory protectie (mlock, memzero).
- **Garmin Ingestion**: Direct-First model + Smooth Flat Queue via garth voor bootstrapping.
- **Privacy/Anonymization**: E2EE Cryptographic sharing en RLS-based secure views voor analytics.

## Volgende Stappen voor de Volgende Sessie / Andere Machine
1. Lees `docs/development/issue16/topics_evaluation.md` door om de vastgestelde besluiten te begrijpen.
2. Pak het originele `docs/development/issue16/research.md` erbij en ga verder met de stap-voor-stap doorlichting. De vorige sessie eindigde met het voorstel om *Finding 2 (PostgreSQL Storage)* en *Finding 4 (ChromaDB User Isolation)* aan te passen.
3. Vertaal de inzichten naar 'Deferred Work Notes' in dit issue, of voer de wijzigingen direct door in de originele documentatie, conform de gemaakte afspraken rondom Branch Hygiene.
4. Werk daarna de resterende Findings af (Auth, Garmin Ingestion, etc.).
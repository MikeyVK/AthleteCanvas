# Integratie in de lokale Ypsia-projectmap

**Status:** overdrachtsinstructie  
**Datum:** 2026-08-06

## Doel

Dit archief hoort als één zelfstandige onderzoeksmap naast de bestaande Ypsia-projectdocumenten te worden geplaatst. Zo blijven de huidige lokale bestanden de actuele projectbron en ontstaat geen tweede bestand met bijna dezelfde naam maar een andere inhoud.

## Voorgestelde plaatsing

Plaats de complete map als:

```text
Ypsia/
├── De Constitutionele Orde - Concept.md
├── Grondwet van Ypsia - Concept (Deel 1 t_m 6).md
├── Inhoudsopgave Ypsia Grondwet.md
├── Kritiek Op Het Huidige Internet.md
├── Paradigmaverschuiving.md
├── Ypsia_Constitutionele_Inventaris.md
├── Ypsia_Constitutionele_Onderzoeksmethodiek.md
└── Onderzoek/
    └── Internetkritiek_2026-08-06/
        └── [inhoud van dit pakket]
```

## Niet overschrijven

De gelijknamige bestanden in `00_teruggevonden_exact/` zijn referentiekopieën uit een eerdere Codex-werkruimte. Zij mogen niet automatisch de actuele bestanden in de projectroot vervangen. Eerst moet inhoudelijk en met hashes worden vastgesteld of zij werkelijk dezelfde versie zijn.

Dat geldt in het bijzonder voor:

- `Ypsia_Constitutionele_Onderzoeksmethodiek.md`;
- `Ypsia_Constitutionele_Inventaris.md`;
- de teruggevonden contextkopie van `Ypsia Charter v3.0`.

## Controle na plaatsing

Een nieuwe Codex-omgeving hoort na koppeling van de Ypsia-map:

1. `AGENTS.md` te zoeken en volledig te lezen wanneer dit bestand aanwezig is;
2. de zeven actuele projectbestanden uit de root te inventariseren;
3. `MANIFEST.sha256` voor dit onderzoeksarchief te verifiëren;
4. eventuele verschillen tussen actuele methodiek/inventaris en de referentiekopieën te rapporteren, zonder automatisch samen te voegen;
5. pas daarna de leesvolgorde in `START_HERE.md` te volgen.

## Nog uit te voeren zodra de lokale map is gekoppeld

- hashes vastleggen van de zeven actuele lokale projectbestanden;
- controleren of `Kritiek Op Het Huidige Internet.md` inhoudelijk gelijk is aan de teruggevonden PDF/tekstextractie of een latere Markdown-versie vormt;
- vaststellen welk Charter-/Grondwetbestand actueel en normatief leidend is;
- relatieve links vanuit dit archief naar de actuele rootdocumenten toevoegen;
- de projectbrede `AGENTS.md`-instructies in de overdracht verwerken wanneer die bestaan.

Deze handelingen zijn bewust niet gesimuleerd op basis van alleen een schermafbeelding.


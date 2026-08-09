# Ypsia — START HERE: overdracht internetkritiek

**Pakketversie:** 0.2  
**Datum:** 2026-08-06  
**Doel:** het onderzoek naar de fundamentele problemen van het huidige internet overdraagbaar maken naar een andere Codex-omgeving zonder contextcompressie te verbergen of verloren onderzoek achteraf als exact herstel te presenteren.

## Kernstatus

Dit pakket bevat twee strikt gescheiden lagen:

1. **Teruggevonden exacte artefacten** — ongewijzigde bestanden uit de eerdere werkruimte, controleerbaar via SHA-256.
2. **Reconstructie en heronderzoek** — nieuwe werkdocumenten van 2026-08-06 die aantoonbare bewaargaten vullen. Deze laag is geen woordelijke reconstructie van verloren gesprekken of zoekactiviteiten.

Het pakket is bedoeld om het onderzoek te hervatten. Het stelt nog geen probleemfamilies vast, kent geen permanente `P`-nummers toe en wijzigt het Charter of de Constitutionele Inventaris niet.

## Eerst lezen

Lees in een nieuwe Codex-omgeving in deze volgorde:

1. dit document;
2. [`00_teruggevonden_exact/Ypsia_Constitutionele_Onderzoeksmethodiek.md`](00_teruggevonden_exact/Ypsia_Constitutionele_Onderzoeksmethodiek.md);
3. [`02_overdrachtsdocumenten/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.2.md`](02_overdrachtsdocumenten/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.2.md);
4. [`02_overdrachtsdocumenten/KANDIDATENLONGLIST.md`](02_overdrachtsdocumenten/KANDIDATENLONGLIST.md);
5. [`02_overdrachtsdocumenten/CLAIM_BRON_TEGENBEWIJS_MATRIX.md`](02_overdrachtsdocumenten/CLAIM_BRON_TEGENBEWIJS_MATRIX.md);
6. [`02_overdrachtsdocumenten/BRONNENREGISTER_v0.2.md`](02_overdrachtsdocumenten/BRONNENREGISTER_v0.2.md);
7. [`02_overdrachtsdocumenten/BESLISLOGBOEK.md`](02_overdrachtsdocumenten/BESLISLOGBOEK.md) en [`02_overdrachtsdocumenten/OPEN_GATEN_EN_RED_TEAMSTATUS.md`](02_overdrachtsdocumenten/OPEN_GATEN_EN_RED_TEAMSTATUS.md);
8. [`02_overdrachtsdocumenten/ONDERZOEKLOGBOEK_2026-08-06.md`](02_overdrachtsdocumenten/ONDERZOEKLOGBOEK_2026-08-06.md);
9. de ruwe werknotities in `01_werknotities_heronderzoek/`;
10. voor de oorspronkelijke analyse: de PDF of tekstextractie in `00_teruggevonden_exact/`;
11. uitsluitend voor constitutionele context: de actuele Charter-, Grondwet-, Inhoudsopgave- en Inventarisbestanden in de lokale Ypsia-projectmap.

## Huidige onderzoeksfase

De open probleemverkenning en eerste lacune-audit zijn afgerond voor zover nu aantoonbaar geborgd. De eerstvolgende inhoudelijke fase is nog steeds:

> **Fase 2 — consolidatie van probleemfamilies.**

Die fase begint met classificatie, niet met Chartertekst:

1. iedere tijdelijke kandidaat beoordelen als mogelijk wortelprobleem, mechanisme, gevolg, belangendrager of voorbeeld;
2. overlap, hiërarchie en mogelijke samenvoegingen onderzoeken;
3. de voorlopige topologie expliciet aan Michel voorleggen;
4. pas daarna per voorlopige familie de bewijsbasis en het sterkste tegenargument aanscherpen;
5. vervolgens een formele red-teamtoets uitvoeren;
6. pas na goedkeuring permanente `P`-IDs toekennen.

## Harde overdrachtsregels

- `KAND-…` is een tijdelijke onderzoeksidentificatie en heeft geen constitutionele status.
- Geen enkel item in dit pakket mag stilzwijgend als vastgesteld probleem, recht, verbod, mandaat of architectuurprincipe worden behandeld.
- Het oorspronkelijke onderzoek is een hypothesekaart, geen voldoende bewijslaag voor alle claims.
- `A`, `B`, `C`, `D` en `E` zijn herkomstlabels; zij zeggen niet automatisch iets over wetenschappelijke zekerheid.
- `PH` is geen herkomstlabel maar een afzonderlijke hypothesestatus voor een eerdere projectgedachte die nog niet als onderzoeksuitkomst is onderbouwd.
- Ontbrekende historische inhoud blijft `niet exact herstelbaar`, ook wanneer nieuw onderzoek hetzelfde onderwerp opnieuw onderbouwt.
- Iedere voorgestelde probleemfamilie en ieder voorgesteld zelfstandig probleem vereist minimaal twee onafhankelijke, verifieerbare en claimgebonden bronnen.
- Een formele red-teamtoets is nog niet uitgevoerd op de complete kandidaat-topologie.
- Het actieve Charter en de actuele lokale projectdocumenten mogen niet vanuit dit archief stilzwijgend worden overschreven.

## Lokale Ypsia-projectbestanden

Op 2026-08-06 waren in Michels lokale projectmap volgens de aangeleverde schermafbeelding aanwezig:

- `De Constitutionele Orde - Concept.md`
- `Grondwet van Ypsia - Concept (Deel 1 t_m 6).md`
- `Inhoudsopgave Ypsia Grondwet.md`
- `Kritiek Op Het Huidige Internet.md`
- `Paradigmaverschuiving.md`
- `Ypsia_Constitutionele_Inventaris.md`
- `Ypsia_Constitutionele_Onderzoeksmethodiek.md`

Deze bestanden waren niet als leesbare bytes gekoppeld aan de omgeving waarin dit pakket is gebouwd. De schermafbeelding bewijst hun namen en aanwezigheid, maar niet hun exacte inhoud of hash. Daarom bevat dit pakket geen vermeend bijgewerkte vervangers voor die lokale bestanden. Zie [`INTEGRATIE_IN_PROJECTMAP.md`](INTEGRATIE_IN_PROJECTMAP.md).

## Pakketstructuur

| Map of bestand | Functie |
|---|---|
| `00_teruggevonden_exact/` | Ongewijzigde teruggevonden bron- en projectartefacten. |
| `01_werknotities_heronderzoek/` | Ruwe audits, bronnotities, als uitgevoerd geregistreerde zoekvragen en afwijzingsredenen uit het heronderzoek van 2026-08-06. |
| `02_overdrachtsdocumenten/` | Geordende indexen en matrices die een volgende sessie helpen hervatten. |
| `MANIFEST.sha256` | Integriteitscontrole van alle inhoudelijke bestanden. |
| `INTEGRATIE_IN_PROJECTMAP.md` | Veilige plaatsing naast de bestaande lokale Ypsia-documenten. |

Binnen `00_teruggevonden_exact/` staan daarnaast drie byte-identieke compatibiliteitskopieën onder de oudere relatieve mapnamen `01_oorspronkelijk_onderzoek/` en `02_aanvullend_onderzoek/`. Zij houden de links in het ongewijzigde historische `BRONNENREGISTER.md` bruikbaar; het zijn geen extra onderzoeksartefacten.

## Begrensde overdrachtsdekking

Dit pakket is overdrachtsgereed in de beperkte betekenis dat het naar beste weten:

- alle nu teruggevonden exacte onderzoeksartefacten bundelt;
- de op 2026-08-06 geïdentificeerde probleemkandidaten en signalen zichtbaar maakt;
- de bekende bewaargaten expliciet registreert;
- als uitgevoerd geregistreerd heronderzoek met zoekvragen en bronnotities bewaart;
- claims, bronnen, tegenargumenten en open bewijsbehoeften verbindt;
- de status en eerstvolgende stap overdraagbaar maakt.

Dit is geen claim van uitputtende inhoudelijke of historische volledigheid. Eerdere zoekopdrachten, tussenredeneringen en verworpen hypothesen bestonden niet meer als exact artefact en worden niet gefingeerd.

<!-- docs\adr\1004-multi-scale-ephemeral-search-projections.md -->
<!-- template=adr version=b4627a40 created=2026-07-26T15:54Z updated= -->
# 1004: Multi-Scale Ephemeral Search Projections

**Status:** PROPOSED  
**Version:** 1.0.0  
**Last Updated:** 2026-07-26  
**Level:** Strategic  
**Category:** Data & Storage  
**Tags:** cqrs, event-sourcing, multi-scale, ephemeral-projections, immutable-ssot  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Lead Architect  

---

## Context & Problem Statement

Ypsia verwerkt en bewaart langdurige, meerschalige (multi-scale) persoonlijke en bedrijfsmatige data waarvan het volume gedurende de levenscyclus van een entiteit gestaag groeit. Het doorzoeken en navigeren van meerschalige datasets stuit bij opvraging (retrieval) op fysieke en wiskundige limieten van verwerkings- en contextcapaciteiten.

We hebben een opslag- en indexeringsstrategie nodig die meerschalige navigatie over grote hoeveelheden data mogelijk maakt, zonder de feitelijke integriteit van de brondata op te offeren of de kernapplicatie vast te ketenen aan de specifieke zoek- en AI-technologie van vandaag.

### Decision Drivers

- Single Source of Truth (SSOT): Ruwe gebeurtenissen (Base Records) zijn de enige onveranderlijke waarheid en mogen nooit vervormd of gewist worden.
- Niet-Destructieve Navigatie: Het doorzoeken van de dataset op hoog abstractieniveau mag de gedetailederde, lage-resolutie feiten van individuele records niet vernietigen.
- Ontkoppeling van Zoektechnologie: De wiskundige structuren die nodig zijn voor vindbaarheid (zoals vectoren, bomen, grafen of indexen) zijn onderhevig aan snelle technologische evolutie.
- Architecturale Duurzaamheid: Het opslagfundament moet decennia meegaan, ongeacht veranderingen in hardware, rekenkracht, query-algoritmen of AI-modellen.

---

## Considered Options

### CQRS-gebaseerde multi-scale indexeringsarchitectuur (Gekozen)

Strikte scheiding tussen ruwe brondata (events) en niet-authoritatieve, herbruikbare zoek-indexen (ephemeral read-projections) met additieve spatial bounding boxes.

**Pros (+):**
- Maximale Datagarantie
- Toekomstbestendig
- Agnostische Schaalbaarheid

**Cons (-):**
- Uiteindelijke Consistentie (Eventual Consistency)
- Complexiteit in Beheer (re-projection pipelines)

### Destructieve Data Rollups (Afgekeurd)

Vectoren en events over tijd samenvoegen en de onderliggende detail-data verwijderen of overschrijven ter besparing van rekenkracht of opslag.

**Pros (+):**
- Simpeler qua database grootte
- Geen eventual consistency complexiteit

**Cons (-):**
- Vernietigt high-fidelity feiten
- Schendt SSOT principe
- Rigide en kalender-gebonden in plaats van data-gedreven


---

## Decision Outcome

**Chosen Option:** We kiezen voor een **CQRS-gebaseerde multi-scale indexeringsarchitectuur** waarin ruwe brondata en zoek-indexen strikt gescheiden zijn. De gelaagdheid en opbouw van zoek-indexen wordt uitsluitend gedreven door datavolume en query-behoefte, niet door hardgecodeerde domein- of tijdsdimensies.

Dit rust op de volgende vier architectonische wetten:

### 1. Ephemere Read-Projecties (CQRS)
Alle afgeleide zoek-indexen op welk abstractieniveau dan ook zijn **niet-authoritatieve read-projecties**. 
* De primaire event-store is de enige authoritatieve bron.
* Geen enkele zoek-index bevat unieke domein-data; de volledige indexering kan op elk moment wiskundig vernietigd en opnieuw opgebouwd worden vanuit de onveranderlijke brondata.

### 2. Additieve Hiërarchische Indexering
Hogere abstractielagen (geabstraheerde index-knooppunten) fungeren als **aanvullende navigatie-structuren** ("spatial bounding boxes") bovenop de Base Records. 
* Consolidatie of aggregatie op hoger niveau genereert extra zoek-knooppunten, maar verwijdert of overschrijft *nooit* de onderliggende detail-records.
* De brondata blijft op het onderste niveau permanent intact in haar oorspronkelijke getrouwheid (high fidelity).

### 3. Asynchrone Event-Driven Propagatie
Index-updates en het genereren van hogere abstractielagen verlopen **volledig asynchroon en event-driven**.
* De schrijf-transactie van een Base Record is strikt ontkoppeld van de verwerking in de zoek-index.
* Het bijwerken van de index-hiërarchie wordt getriggerd door datastromen en beschikbare verwerkingscapaciteit, niet door synchrone blokkades of vaststaande kalenderintervallen.

### 4. Encapsulatie van de Multi-Scale Index (`IMultiScaleIndex`)
De complete indexerings-, zoek- en clusteringstrategie wordt afgeschermd achter een abstracte `IMultiScaleIndex` Port.
* Het applicatiedomein kent alleen het concept van "een vraag of zoekopdracht stellen binnen een bepaalde context, schaal of lens".
* Hóé de indexer-adapter dit wiskundig of technisch oplost (via vector-embeddings, grafen, hiërarchische bomen of ruimtelijke indelingen) is een geïsoleerd implementatiedetail van de adapter.

### Rationale

Deze aanpak verzekert de levenslange integriteit van ruwe datastromen terwijl het meerschalige (van micro naar macro) AI-retrieval mogelijk maakt. Het isoleert de complexe, wisselende zoek- en vectoralgoritmen volledig van het kerndomein.

---

## Consequences

### Positive Consequences (+)

- Maximale Datagarantie: Het risico op dataverlies door index-fouten, algoritme-wijzigingen of AI-drift is nul, omdat alle indexen herstelbaar zijn vanuit de SSOT.
- Toekomstbestendig: Bij een overstap naar een nieuwe generatie zoektechnologieën hoeft alleen de indexer-adapter vervangen te worden; de brondata blijft onaangetast.
- Agnostische Schaalbaarheid: De applicatie kan efficiënt over gigantische datasets navigeren door eerst de top-level projecties te raadplegen en pas in te zoomen op detail-data wanneer de vraag dat vereist.

### Negative Consequences & Risks (-)

- Uiteindelijke Consistentie (Eventual Consistency): Er zit een korte asynchrone vertraging tussen het opslaan van een record en het beschikbaar komen ervan in de hiërarchische zoek-index.
- Complexiteit in Beheer: Het beheren van her-indexeringstrajecten (re-projection pipelines) vereist robuuste achtergrondverwerking.


---

## Confirmation & Verification

All integration and unit tests for search indexing MUST verify that base records are unchanged after an index rebuild. Code reviews MUST ensure `IMultiScaleIndex` is the only point of entry for multi-scale retrieval.

## Related Documentation
- **[docs/adr/0001-zero-leakage.md][related-1]**
- **[docs/adr/1000-unified-sovereign-storage.md][related-2]**
- **[docs/adr/1002-universal-data-envelope.md][related-3]**

<!-- Link definitions -->

[related-1]: docs/adr/0001-zero-leakage.md
[related-2]: docs/adr/1000-unified-sovereign-storage.md
[related-3]: docs/adr/1002-universal-data-envelope.md

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-26 | Agent | Initial draft |
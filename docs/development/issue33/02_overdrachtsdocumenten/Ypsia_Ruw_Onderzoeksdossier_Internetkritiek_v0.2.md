# Ypsia — Ruw onderzoeksdossier internetkritiek

**Status:** overdrachtsgereed voor de huidige kenbare stand; historisch niet woordelijk volledig  
**Versie:** 0.2  
**Datum:** 2026-08-06  
**Onderzoeksfase:** einde open probleemverkenning; vóór consolidatie van probleemfamilies  
**Normatieve status:** geen Chartertekst en geen vastgestelde Constitutionele Inventaris

## 1. Functie van versie 0.2

Versie 0.2 maakt het Ypsia-onderzoek naar de fundamentele problemen van het huidige internet overdraagbaar naar een andere Codex-omgeving. Zij vervangt versie 0.1 niet als historische momentopname. V0.1 is ongewijzigd opgenomen in `00_teruggevonden_exact/`.

V0.2 voegt toe wat voor een zelfstandige overdracht ontbrak:

- een bewijsgetrouwe audit van het oorspronkelijke dossier en de aanvullende samenvatting;
- een genormaliseerde inventaris van alle 79 oorspronkelijke bronvermeldingen;
- een traceerbare longlist van 63 kandidaatproblemen, mechanismen, gevolgen, spanningen en oplossingsbeperkingen;
- gerichte bronnotities en zoekvragen die in de nieuwe werknotities als uitgevoerd zijn geregistreerd;
- claim–bron–tegenbewijs-/beperkingenverbindingen;
- een beslislogboek, open-gatenregister, red-teamstatus en integratie-instructie;
- een manifest met hashes.

“Overdrachtsgereed” betekent hier dat een volgende omgeving de huidige stand, bronnen, onzekerheden en eerstvolgende stap kan reconstrueren. Het betekent niet dat alle eerdere gesprekken, browsepaden of tussenredeneringen woordelijk zijn hersteld.

## 2. Herkomstlabels

| Label | Betekenis |
|---|---|
| `A — Exact artefact` | Een oorspronkelijk of teruggevonden bestand is ongewijzigd aanwezig en met een hash controleerbaar. |
| `B — Letterlijk teruggevonden` | Een formulering is zichtbaar in bewaarde gespreksinhoud of projecttekst. |
| `C — Samengevat vastgelegd` | Alleen een latere samenvatting of procesregistratie is aanwezig. |
| `D — Niet exact herstelbaar` | Het bestaan of onderwerp is bekend, maar de oorspronkelijke ruwe onderzoeksactiviteit ontbreekt. |
| `E — Heronderzoek 2026-08-06` | Nieuwe audit of zoekronde van 2026-08-06 met eigen datum, bronnen, als uitgevoerd geregistreerde zoekvragen en beperkingen. |

De labels beschrijven herkomstintegriteit. Zij zijn geen automatische maat voor wetenschappelijke zekerheid.

`PH` staat buiten dit herkomststelsel. Het is een afzonderlijke epistemische status voor een eerdere projecthypothese of constitutionele denkroute die nog niet als onderzoeksuitkomst is onderbouwd.

## 3. Exact geborgde laag — `A`

In `00_teruggevonden_exact/` zijn ongewijzigd opgenomen:

- het twintigpagina-dossier `Kritiek_op_het_huidige_internet.pdf`;
- de reproduceerbare `pdftotext -layout`-extractie;
- `Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.1.md`;
- `BRONNENREGISTER.md` versie 0.1;
- `Ypsia_Constitutionele_Onderzoeksmethodiek.md` versie 0.1;
- `Ypsia_Constitutionele_Inventaris.md` versie 0.1;
- een teruggevonden contextkopie van `Ypsia Charter v3.0`;
- de door Michel aangeleverde schermafbeelding van de actuele lokale projectbestanden.

De PDF heeft volgens de teruggevonden en opnieuw gecontroleerde audit SHA-256:

`be96a1803d17bc4cec4f7d7b2181d642e0af337230601a00c4324662e7e84162`

De tekstextractie heeft SHA-256:

`196ba0ac53d17c9b895d3cd785633beef1632a42abe7eeb17537ab12124b407c`

De extractie is byte voor byte reproduceerbaar uit de PDF met `pdftotext -layout`. Zij blijft desondanks een zoekindex: tabellen, URL-regelafbrekingen, paginaovergangen en visuele hiërarchie kunnen in platte tekst vervormen.

## 4. Wat versie 0.1 aantoonbaar borgde — exact artefact met gemengde eerdere provenance

V0.1 bewaart:

- de centrale probleemrichting van het oorspronkelijke dossier;
- een kritische beoordeling van de asymmetrische dekking;
- drie expliciete claimcorrecties;
- vier aanvullende lacunelenzen;
- twintig aanvullende kandidaat-problemen;
- vijf onderwerpen die voorlopig vooral als verdieping, mechanisme of gevolg werden gezien;
- acht voorlopige onderzoeksdomeinen;
- de bronminimumregel;
- het verzadigings- en ROI-oordeel;
- de eerstvolgende onderzoeksfase;
- een expliciete lijst van niet geborgde ruwe inhoud.

V0.1 is exact aanwezig als huidige tekst. Niet zelfstandig verifieerbaar zijn alle onderliggende gesprekken, zoekactiviteiten en bronleesnotities waarnaar de labels `B` en `C` verwijzen.

## 5. Nieuwe bewijsgetrouwe audit — `E`

De audit in `01_werknotities_heronderzoek/audit_initial_research.md` stelde vast:

1. de bibliografie bevat exact 79 genummerde vermeldingen;
2. 43 nummers zijn als marker in de geëxtraheerde hoofdtekst aangetroffen;
3. 36 vermeldingen staan alleen in de bibliografie en worden niet zichtbaar aangehaald;
4. de audit codeert 34 passages uit het oorspronkelijke dossier als mogelijke probleemkandidaat of beperkingssignaal; dit aantal is een analytische inventarisatie, geen objectief gegeven van het document;
5. DOS-001 voegt twintig expliciete kandidaten en vijf verdiepende thema’s toe;
6. de eerste circa acht pagina’s zijn voornamelijk diagnostisch; daarna verschuift het zwaartepunt naar oplossingen, programma’s en protocollen;
7. bronlagen zijn vermengd: academisch, institutioneel, journalistiek, commercieel, project-/vendorbron, blog, aggregator, Reddit, Hacker News en Wikipedia;
8. verschillende passages gebruiken secundaire bronnen terwijl een primaire of institutionelere bron wel in de bibliografie staat;
9. één verwijzing is op titel evident inhoudelijk verkeerd gekoppeld: bron 33 over een C-compiler ondersteunt in de tekst een claim over “AI slop”;
10. veel markers staan achter alinea’s met meerdere empirische, causale en normatieve deelclaims, waardoor precieze claimdekking ontbreekt.

Dit maakt het oorspronkelijke dossier niet waardeloos. Het verandert de juiste functie: sterke hypothesekaart en denkrichting, maar geen complete claimgebonden bewijslaag.

## 6. Drie eerder vastgelegde inhoudelijke correcties — `B`-inhoud, `E`-parafrase

De correcties hieronder waren inhoudelijk al in v0.1 bewaard. De compacte formuleringen in deze versie zijn nieuwe parafrases van 2026-08-06 en dus niet woordelijk als `B — Letterlijk teruggevonden` te lezen. Voor de exact bewaarde formulering geldt v0.1, §4.2.

### 6.1 Model collapse

Model collapse is een aangetoond risico bij specifieke vormen van indiscriminerende recursieve training op synthetische data. Het is niet aangetoond als onvermijdelijk lot van ieder model. Het behouden van oorspronkelijke menselijke data kan degradatie beperken.

### 6.2 AI-samenvattingen en doorklikgedrag

De oorspronkelijke 58%-formulering betrof mensen die minstens één AI-samenvatting zagen, niet 58% van alle zoekopdrachten. In de later geregistreerde Pew-steekproef bevatte 18% van de zoekopdrachten een samenvatting; wanneer die verscheen daalde doorklikken naar reguliere resultaten van 15% naar 8%.

### 6.3 Gegevenswissing en AI-modellen

De EDPB kiest niet voor de algemene regel dat onrechtmatig gebruikte persoonsgegevens automatisch volledige “algoritmische destructie” vereisen. Beoordeling vindt per geval plaats, onder meer aan de hand van anonimiteit, rechtmatigheid en gevolgen van de verwerking.

De inhoudelijke correcties zijn bewaard in v0.1; de bovenstaande formuleringen zijn `E`-parafrases. De nieuwe audit laat zien dat dezelfde terughoudendheid ook op andere absolute formuleringen moet worden toegepast.

## 7. Huidige traceerbare open longlist — provenance `A/E`, afzonderlijke hypothesestatus `PH`

`KANDIDATENLONGLIST.md` bewaart 63 tijdelijke signalen. De lijst combineert bewust:

- 34 kandidaten of beperkingssignalen uit de oorspronkelijke PDF;
- twintig aanvullende kandidaten uit de vier lacunelenzen;
- drie aanvullende werkcodes voor de vijf expliciet bewaarde verdiepende thema’s; aandachtsexploitatie en synthetische ruis verwijzen naar reeds bestaande kandidaten;
- vier grensgebiedkandidaten uit de latere lacune-audit; staatsmacht en gedwongen digitalisering zijn daarbij afzonderlijk zichtbaar gehouden;
- twee eerder benoemde projecthypothesen over technologie als doel en onomkeerbaarheid, voor zover die niet al volledig door andere signalen worden gedekt.

Door overlap niet vroegtijdig weg te poetsen blijft zichtbaar wat later mogelijk:

- een wortelprobleem;
- een mechanisme;
- een gevolg;
- een belangendrager;
- een voorbeeld;
- een spanning;
- een beperking van een voorgesteld antwoord;
- of een te absolute/verworpen hypothese blijkt.

Geen `KAND`-code is een permanent constitutioneel ID.

## 8. Voorlopige onderzoeksdomeinen — niet vastgesteld

De acht uit v0.1 teruggevonden domeinen blijven bruikbare lenzen voor consolidatie:

1. digitale macht en politieke economie;
2. menselijke autonomie, cognitie en ontwikkeling;
3. kennis en informatie-integriteit;
4. democratie, procedurele rechtsbescherming en gelijkheid;
5. arbeid, verdeling en institutionele afhankelijkheid;
6. materiële en ecologische gevolgen;
7. technische weerbaarheid en structurele afhankelijkheid;
8. toekomstige generaties en belangen zonder stem.

Binnen de vier geselecteerde brede kaders — UNESCO, de Europese digitale beginselen, het VN-Kinderrechtencomité en het AI-Kaderverdrag van de Raad van Europa — werd geen aanvullend normatief domein aangetroffen buiten de bestaande acht onderzoekslenzen. Dit bewijst niet dat buiten deze selectie geen ander domein bestaat. De kruistoets liet wel zien dat drie grensgebieden zichtbaar moeten blijven:

- collectieve en relationele dataschade;
- staatsmacht en gedwongen digitalisering;
- de spanning tussen identiteit, anonimiteit en pseudonimiteit.

Dit is een begrensd ROI- en verzadigingssignaal binnen de gekozen kaders, geen bewijs van categorische of definitieve volledigheid.

## 9. Nieuwe brongebonden heronderzoekslaag — `E`

De ruwe notities in `01_werknotities_heronderzoek/` leggen per onderzoeksronde vast:

- de gebruikte lens en vraag;
- titel, instelling/auteurs, datum en stabiele vindplaats van de bron;
- bronsoort;
- welke specifieke claim de bron wel ondersteunt;
- welke sterkere formulering zij niet rechtvaardigt;
- beperkingen, tegenargumenten en onzekerheid;
- zoekvragen die in de werknotities als uitgevoerd zijn geregistreerd;
- niet geselecteerde bronnen en afwijzingsredenen.

Deze notities vullen v0.1 functioneel aan. Zij zijn niet retrospectief onderdeel van de oorspronkelijke ronde.

## 10. Bronnen- en bewijsstatus

De volledige actuele koppeling staat in `CLAIM_BRON_TEGENBEWIJS_MATRIX.md`. De hoofdregel blijft:

- minimaal twee onafhankelijke, verifieerbare en claimgebonden bronnen per voorgestelde probleemfamilie en per voorgesteld zelfstandig probleem;
- bij voorkeur een gezaghebbende synthese/juridisch kader plus een onafhankelijke primaire studie of officiële dataset;
- het belangrijkste tegenbewijs of de belangrijkste beperking bij jonge, omstreden of snel veranderende claims;
- afzonderlijke aanduiding van causaliteit, correlatie, theorie, projectie en normatieve beoordeling.

Een brede verklaring of conventie kan constitutionele relevantie en categorische dekking ondersteunen. Zij bewijst niet automatisch de empirische omvang of causaliteit van ieder afzonderlijk probleem.

## 11. Wat ook na v0.2 historisch ontbreekt — `D`

Niet exact herstelbaar blijven:

- de oorspronkelijke zoekvragen en volledige zoekresultaten uit de eerdere aanvullende ronde;
- alle toenmalige bronleesnotities, citaten en paginaverwijzingen;
- iedere tussenredenering, verworpen hypothese en alternatieve topologie;
- een woordelijk volledig pre-compressiegesprek;
- bewijs dat iedere geregistreerde externe bron destijds volledig in een specifieke versie is gelezen.

Deze waarheid wordt niet opgeheven doordat v0.2 nieuw onderzoek heeft uitgevoerd.

## 12. Formele red-teamstatus

Er is nog geen formele red-teamtoets uitgevoerd op een geconsolideerde probleemtopologie. Wel zijn:

- het oorspronkelijke dossier als volledige bewijslaag aangevallen en afgezwakt;
- drie inhoudelijke claims gecorrigeerd;
- bronmismatches, absolute formuleringen, oplossingsgestuurde asymmetrie en bewijsleemten geregistreerd.

De eerste formele red-teamtoets volgt pas nadat Michel de voorlopige classificatie en consolidatie heeft bijgestuurd. Zie `OPEN_GATEN_EN_RED_TEAMSTATUS.md`.

## 13. Eerstvolgende inhoudelijke stap

De volgende sessie start bij de longlist en maakt per `KAND`-item een voorlopige classificatie. Zij onderzoekt fundamentele schade, machtsmechanisme, belangendragers, overlap, constitutioneel bereik, bewijsstatus en het sterkste tegenargument.

Daarna wordt een voorlopige topologie aan Michel voorgelegd. Tot zijn inhoudelijke goedkeuring:

- geen permanente `P`-nummers;
- geen rechten, verboden of architectonische antwoorden afleiden;
- geen wijzigingen aan Charter of Grondwet;
- geen Mermaid-netwerk presenteren alsof relaties al zijn vastgesteld.

## 14. Integriteitsverklaring versie 0.2

V0.2 maakt zichtbaar onderscheid tussen exact artefact, bewaarde tekst, samenvatting, niet herstelbare historie en nieuw heronderzoek. Zij pretendeert niet de verloren onderzoeksgeschiedenis woordelijk te reconstrueren. Zij borgt wél voldoende ruwe en gestructureerde inhoud om het vervolg inhoudelijk, bronbewust en zonder start vanaf nul uit te voeren.

## 15. Wijzigingslogboek

| Versie | Datum | Wijziging |
|---|---|---|
| 0.1 | 2026-08-06 | Eerste duurzame bundeling van teruggevonden aanvullende onderzoeksinhoud, correcties, lacune-audits, kandidaat-problemen, bronstatus en bewaargaten. |
| 0.2 | 2026-08-06 | Exacte artefactaudit, volledige broninventaris, 63-item-longlist, nieuwe heronderzoeksnotities, claim–bron–tegenbewijsverbindingen, beslislogboek, open-gaten-/red-teamstatus en overdrachtsmanifest toegevoegd. |

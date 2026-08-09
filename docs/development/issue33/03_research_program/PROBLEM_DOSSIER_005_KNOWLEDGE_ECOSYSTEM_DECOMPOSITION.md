# Probleemdossier 005 — Bronrelaties, synthetische informatie en het kennisecosysteem

| Veld | Waarde |
|---|---|
| Status | PRELIMINARY |
| Versie | 0.3 |
| Laatst bijgewerkt | 2026-08-08 |
| Onderzoeksfase | Inhoudelijk bronnenonderzoek en ontleding |
| Primaire kandidaten | KAND-013–025 en KAND-037 |
| Voorlopig oordeel | De oorspronkelijke kennisecosysteemfamilie opsplitsen |
| Actieve kandidaten | Niet-herleidbare bronbasis bij vervangende antwoordsynthese; oncontroleerbare herkomst van schaalbaar geproduceerde inhoud |
| Onderzoeksrisico | Ontkoppeling van kennisconsumptie en bronbereik |
| Emerging risico | Conditionele convergentie van collectieve creatie |
| Geen zelfstandig probleem | Synthese, nul-klik, paywalls, bots, desinformatie, synthetische trainingsdata en model collapse in hun brede formuleringen |
| Bewijsvertrouwen | Verschilt sterk per deelclaim; zie §12 |

## 1. Doel en onderzoeksvraag

De voorlopige probleemkaart bracht KAND-013 tot en met KAND-025 en KAND-037 samen onder **verzwakking van het open, traceerbare en betrouwbare kennisecosysteem**. Die formulering is te breed voor Single Responsibility Principle (SRP). Zij vermengt:

- de vorm waarin informatie wordt aangeboden;
- de relatie tussen beweringen en bronnen;
- verkeer, erkenning en financiering van kennisproducenten;
- synthetische productie, bots en desinformatie;
- technische trainingsrisico's van AI-modellen;
- mogelijke convergentie van creatie en cultuur;
- en brede maatschappelijke gevolgen zoals verlies van vertrouwen.

Dit dossier onderzoekt welke onderdelen als zelfstandige, onderbouwbare problemen kunnen blijven bestaan. Het onderzoekt uitdrukkelijk **niet** welke architectuur, marktordening of regelgeving deze problemen moet oplossen.

## 2. Voorlopige ontleding

### 2.1 Actieve kandidaat 5A — Niet-herleidbare bronbasis bij vervangende antwoordsynthese

> Digitale antwoordsynthese kan voor gebruikers als vervangende kennisbron functioneren terwijl materiële beweringen niet betrouwbaar zijn te herleiden tot hun oorspronkelijke bron, context, beperkingen en tegenspraak.

De kandidaat gaat niet over de vraag of synthese mag bestaan. Hij gaat over de vraag of een ontvanger vanuit een concrete bewering betrouwbaar terug kan naar:

- de oorspronkelijke bron en relevante passage;
- de auteur of verantwoordelijke organisatie;
- publicatiedatum en versie;
- de context en beperkingen van het bewijs;
- eventuele transformaties of samenvattingen;
- en conflicterende bronnen of onzekerheid.

KAND-025 vormt de kern. KAND-013 en KAND-014 leveren mechanismen: platformgebonden synthese en verminderd bronbezoek.

### 2.2 Actieve kandidaat 5B — Oncontroleerbare herkomst van schaalbaar geproduceerde inhoud

> Digitale inhoud kan synthetisch worden gemaakt, gewijzigd en verspreid op een schaal en snelheid waarop ontvangers niet betrouwbaar kunnen vaststellen wie ervoor verantwoordelijk is, waar zij vandaan komt en hoe zij betekenisvol is bewerkt.

Kandidaat 5A vraagt: **waarop berust deze bewering?** Kandidaat 5B vraagt: **wie of wat heeft dit informatieobject voortgebracht, veranderd en verspreid?** Dat onderscheid blijft nodig. Menselijke of synthetische herkomst bepaalt niet automatisch of informatie waar is, maar herkomst kan materieel zijn bij onder meer getuigenis, auteurschap, publieke verantwoording, impersonatie en gecoördineerde beïnvloeding.

KAND-022 levert in versmalde vorm de probleemkern. KAND-021 is een mechanisme; KAND-024 een mogelijke kwaadaardige toepassing. Een algemene “crisis van sociaal vertrouwen” wordt niet als bewezen kernclaim overgenomen.

### 2.3 Onderzoeksrisico 5C — Ontkoppeling van kennisconsumptie en bronbereik

> Wanneer een antwoordintermediair een informatiebehoefte binnen zijn eigen interface vervult met materiaal van derden, kan consumptie van dat kenniswerk worden ontkoppeld van bezoek aan en zichtbaarheid van de bron.

Minder bronverkeer is aantoonbaar. Dat kan materieel zijn voor bronnen die voor erkenning, bereik of financiering van verwijzend verkeer afhankelijk zijn. De verdere keten is echter nog onvoldoende aangetoond:

`minder klikken → minder inkomsten → minder onafhankelijke productie → minder pluraliteit of toegankelijkheid`

Daarom is dit een **actief onderzoeksrisico**, nog geen vastgesteld wortelprobleem. KAND-014 is het directe mechanisme; KAND-015 bevat mogelijke gevolgen. Onderhandelingsmacht en gebruikscontrole horen primair bij de bredere familie van intermediaire macht.

### 2.4 Emerging risico 5D — Conditionele convergentie van collectieve creatie

> Wanneer veel makers door dezelfde modellen, standaardinstellingen of suggesties worden bemiddeld, kunnen hun uitkomsten naar elkaar convergeren en kan collectieve diversiteit afnemen, ook wanneer individuele kwaliteit of productiviteit stijgt.

Dit is een scherp begrensde opvolger van KAND-037. Het bewijs betreft vooral kortdurende creatieve taken. Het rechtvaardigt nog niet de stelling dat menselijke taal, cultuur of collectieve denkkracht als geheel homogeniseert.

### 2.5 Geen zelfstandige kandidaat — Model collapse en recursieve synthetische training

Model collapse is een echt technisch risico bij specifieke trainingscondities, vooral wanneer synthetische data eerdere echte data vervangen. Het is geen natuurwet van synthetische data en geen zelfstandig maatschappelijk internetprobleem. Behoud en accumulatie van echte data, selectie, filtering en verificatie kunnen degradatie voorkomen; gecureerde synthetische data kunnen prestaties juist verbeteren.

KAND-017 is een trendhypothese, KAND-018 het technische mechanisme, KAND-019 een vroeg gevolg en KAND-020 een mogelijk laat gevolg. Zij blijven traceerbaar als technische risico- en ontwerpkennis, niet als vier charterproblemen.

## 3. Bevindingen over synthese, klikken en bronrelaties

### 3.1 Antwoordsynthese vermindert bronbezoek overtuigend

Pew analyseerde 68.879 Google-zoekacties van 900 Amerikaanse volwassenen. Bij zoekpagina's met een AI Overview klikten gebruikers bij 8% van de bezoeken op een regulier resultaat, tegenover 15% zonder Overview; slechts 1% klikte op een bron in de synthese. Omdat verschillende soorten zoekvragen verschillend vaak een Overview krijgen, bewijst dit observationele ontwerp niet zelfstandig causaliteit.

Een gerandomiseerd veldexperiment vond bij daadwerkelijk getoonde AI Overviews ongeveer 40% minder organische uitgaande klikken en meer nul-klikzoekacties. Dat is sterker causaal bewijs, maar het betreft nog een working paper. De aanbieder rapporteert daartegenover meer zoekgebruik, stabiel totaal klikvolume en waardevollere resterende klikken, zonder de onderliggende data volledig openbaar te maken.

De houdbare conclusie is: **antwoordgestuurde synthese kan bronbezoek vervangen**. Een nul-klik is niet vanzelf schade; hij kan ook betekenen dat een eenvoudige vraag efficiënt is beantwoord.

### 3.2 Citatieaanwezigheid is geen volledige provenance

Een menselijke audit van vier generatieve zoekmachines uit 2023 vond dat gemiddeld 51,5% van de controleerbare zinnen volledig door citaties werd gedragen en 74,5% van de citaties de gekoppelde zin werkelijk ondersteunde. De systemen werden desondanks als vloeiend en bruikbaar ervaren. Deze percentages zijn geen actuele universele foutgraad, maar tonen wel dat een keurige citatie-interface schijnzekerheid kan bieden.

Een latere analyse van ongeveer 14.000 zoekgesprekken vond grote verschillen tussen systemen in het aantal geraadpleegde en werkelijk geciteerde bronnen. Die verschillen bij dezelfde vragen wijzen erop dat de attributiekloof mede uit ontwerpkeuzes voortkomt en niet uit een onveranderlijke technische grens.

### 3.3 Werkelijke bronnen kunnen kalibratie verbeteren

In een preregistreerd CHI-experiment verhoogden verklaringen de afhankelijkheid van zowel juiste als onjuiste AI-antwoorden. Werkelijke bronnen verminderden juist de afhankelijkheid van onjuiste antwoorden. Herkomstinformatie kan dus helpen, maar alleen wanneer zij geldig, specifiek en bruikbaar is; een decoratieve verwijzing is onvoldoende.

### 3.4 Betrouwbare synthese is technisch mogelijk

OpenScholar koppelt retrieval uit tientallen miljoenen wetenschappelijke publicaties aan iteratieve beantwoording en citatieverificatie. In de onderzochte wetenschappelijke taken bereikte het systeem citatienauwkeurigheid rond menselijk expertniveau en werd zijn synthese vaak boven menselijke referentieantwoorden verkozen. Dit is sterk tegenbewijs tegen de stelling dat synthese noodzakelijk bronverlies veroorzaakt.

De probleemkern is daarom conditioneel: **vervangende synthese zonder gelijkwaardige broncontrole**, niet synthese zelf.

### 3.5 Effecten op leren zijn gemengd

Zeven experimenten vonden na LLM-syntheses gemiddeld minder ervaren leerdiepte en korter, minder feitelijk en minder origineel advies dan na traditionele webzoekresultaten. Andere experimenten vonden juist betere feitelijke herinnering na AI-samenvattingen dan na expertblogs of Wikipedia. Feiten onthouden, begrip opbouwen en bronidentiteit onthouden zijn verschillende uitkomsten.

Er ontbreekt nog robuust causaal bewijs dat gebruikers na AI-zoeksynthese structureel slechter onthouden **welke** bronnen, auteurs en contexten achter het antwoord lagen.

## 4. Bevindingen over bronbereik en kennisproductie

### 4.1 Minder verkeer is niet hetzelfde als minder kennisproductie

Het bewijs ondersteunt verlies van bronbezoek, maar niet de algemene bewering dat AI-synthese reeds aantoonbaar redacties, makersinkomen, onderzoek of publieke kennisproductie laat verdwijnen. Verkeer is geen omzetmaat; omzet is geen productiemaat; productievolume is geen maat voor kwaliteit of pluraliteit.

De oorspronkelijke KAND-015 moet daarom worden gesplitst:

- **bereik:** rechtstreeks meetbaar en voldoende onderbouwd;
- **erkenning:** afzonderlijk meten via zichtbare attributie en bronherkenning;
- **verdienvermogen:** sectorspecifieke downstream-hypothese;
- **duurzame kennisproductie:** een verdere, nog onbewezen causale stap.

### 4.2 Linkende aggregatie kan juist bereik scheppen

De sluiting van Google News in Spanje leidde in een difference-in-differences-onderzoek tot 8–14% minder bezoeken aan Spaanse nieuwswebsites, vooral bij kleinere uitgevers. Dit toont het marktuitbreidingseffect van een intermediair die naar bronnen verwijst. Die bevinding kan niet rechtstreeks worden overgezet naar een antwoordintermediair die bronbezoek vervangt, maar weerlegt wel de algemene stelling dat iedere tussenlaag bereik vernietigt.

### 4.3 Het verval van nieuwsmarkten begon ruim vóór generatieve AI

Nieuwsorganisaties verloren al vóór de huidige AI-golf grote delen van advertentie- en abonnementsinkomsten. Generatieve AI kan nieuwe druk toevoegen, maar mag niet als hoofdoorzaak van een ouder en multifactorieel marktprobleem worden gepresenteerd.

### 4.4 Paywalls en crawlerblokkades zijn reacties met trade-offs

Paywalls kunnen bereik verkleinen, maar abonnementen en netto-inkomsten verhogen. Crawlerblokkades zijn sinds de generatieve-AI-golf sterk toegenomen. Een audit van 14.000 domeinen vond snelle groei van AI-specifieke beperkingen en inconsistenties tussen robots.txt en gebruiksvoorwaarden. Dit bewijst een krimpend AI-datacommons en gebrekkige protocollen voor hergebruikstoestemming, niet automatisch een krimpend menselijk kennisaanbod.

KAND-016 blijft daarom een reactie- en trade-offlens, geen bewezen worteloorzaak.

### 4.5 Licenties tonen zowel mogelijkheid als machtsongelijkheid

De officiële Australische evaluatie vond meer dan dertig overeenkomsten tussen platforms en nieuwsorganisaties die zonder het onderhandelingsregime waarschijnlijk niet waren gesloten. Vertrouwelijkheid maakt effecten op eerlijke verdeling en duurzame journalistiek moeilijk controleerbaar; kleinere partijen bleven vaker zonder overeenkomst. Ook latere licentiemarkten concentreren zich vooral bij grote rechthebbenden. Dit ondersteunt een vraagstuk van onderhandelingsmacht, niet de algemene stelling dat ieder gebruik zonder klik extractief is.

## 5. Bevindingen over synthetische productie en verificatie

### 5.1 Synthetische productie kan de schaal van beïnvloeding vergroten

Een quasiexperimentele studie van een aan Rusland verbonden propagandawebsite vond dat de invoering van generatieve AI samenging met een grotere hoeveelheid en bredere variatie van desinformatie, zonder verlies van ervaren overtuigingskracht. Een grootschalige studie van meer dan vijftien miljoen artikelen vond na de introductie van ChatGPT een duidelijke stijging van gedetecteerde synthetische artikelen, vooral op kleine en misinformatiewebsites.

Dit toont capaciteit en feitelijk gebruik in specifieke ecosystemen. Het bewijst niet dat synthetische inhoud inmiddels het grootste deel van het internet vormt.

### 5.2 Bots zijn een versterkend mechanisme, niet de enige oorzaak

Onderzoek vond dat bots vroeg in de verspreidingsketen onevenredig laagwaardige bronnen deelden en menselijke hershares konden uitlokken. Ander grootschalig onderzoek vond echter dat bots ware en onware berichten ongeveer even sterk versnelden en dat menselijke deelkeuzes het verschil in verspreiding beter verklaarden.

Daarom wordt KAND-021 niet behouden als “het internet staat vol bots”. De houdbare bijdrage is dat geautomatiseerde actoren signalen van populariteit, consensus en menselijke aanwezigheid kunnen nabootsen of versterken terwijl ontvangers hun oorsprong niet altijd betrouwbaar kunnen beoordelen.

### 5.3 Detectie is mogelijk, maar niet algemeen betrouwbaar

In preregistreerde experimenten konden deelnemers verschillende politieke deepfakes duidelijk beter dan kansniveau herkennen, vooral met audiovisuele aanwijzingen. Tegelijk verschillen prestaties sterk per techniek, modaliteit en waarschuwing. Automatische bot- en synthetische-contentdetectoren kennen bovendien aanzienlijke generalisatie- en foutproblemen.

Provenance, metadata, watermerken en detectie kunnen elkaar aanvullen, maar geen enkel middel stelt zelfstandig waarheid vast. Cryptografische herkomst kan aantonen welke actor een verklaring over oorsprong of bewerking ondertekende; zij bewijst niet dat de inhoud feitelijk juist is.

### 5.4 Een algemene vertrouwenscrisis is niet aangetoond

Misinformatie is reëel en kan in specifieke contexten ernstige schade veroorzaken. Representatieve gedragsdata laten echter zien dat blootstelling aan onbetrouwbare websites gemiddeld vaak een klein en sterk geconcentreerd deel van het informatiedieet vormt. Experimentele effecten op houding en gedrag zijn heterogeen; een enkele blootstelling heeft vaak geen of slechts beperkte gevolgen.

KAND-022 wordt daarom vernauwd tot verificatie-asymmetrie. “Desintegratie van gedeelde epistemologie” blijft een mogelijke systeemconsequentie waarvoor afzonderlijk bewijs nodig is.

## 6. Bevindingen over model collapse en synthetische trainingsdata

### 6.1 Model collapse bestaat binnen specifieke condities

Shumailov et al. tonen theoretisch en experimenteel dat modellen bij recursieve vervanging van echte data door modeluitvoer informatie over de oorspronkelijke verdeling verliezen. De zeldzame staarten verdwijnen vroeg; bij verdere recursie kan sterke degradatie ontstaan.

### 6.2 Collapse is niet onvermijdelijk

Gerstgrasser et al. bevestigen degradatie bij vervanging, maar vinden over meerdere modeltypen dat accumulatie van eerdere echte en synthetische data de fout begrensd houdt. Ander onderzoek laat zien dat zorgvuldig geselecteerde echte data en verificatie de dynamiek verder kunnen veranderen.

### 6.3 Synthetische data kunnen waardevol zijn

Self-Instruct verbeterde een basismodel sterk met gegenereerde en gefilterde instructiedata. Ook buiten taalmodellen kan gerichte synthetische aanvulling zeldzame of ondervertegenwoordigde gevallen beter representeren.

De maximale claim is dus niet “synthetische data vervuilen kennis”, maar:

> Ongecontroleerde recursieve vervanging van oorspronkelijke gegevens door gegenereerde afgeleiden kan distributie-informatie en modelkwaliteit verliezen.

Dat is een technisch data-lineage- en trainingsrisico. De sociale extrapolaties naar verlies van minderheidskennis, betekenis of werkelijkheid zijn nog niet aangetoond.

## 7. Bevindingen over creatie en collectieve diversiteit

### 7.1 Individuele winst en collectieve convergentie kunnen samengaan

In een experiment met korte verhalen verbeterden AI-ideeën gemiddeld de beoordeelde creativiteit, schrijfkwaliteit en aantrekkelijkheid, vooral bij minder creatieve schrijvers. Tegelijk leken AI-geholpen verhalen onderling meer op elkaar. Een grote observationele studie van miljoenen kunstwerken vond na AI-adoptie meer productie en waardering, een daling van gemiddelde nieuwheid en tegelijk een stijging van de meest vernieuwende uitkomsten.

### 7.2 Convergentie is ontwerp- en contextafhankelijk

Een dynamisch experiment vond bij hoge blootstelling aan AI-ideeën juist meer collectieve ideeëndiversiteit. Verschillende modellen, persona's, bronsets, variatieprikkels en menselijke selectie kunnen convergentie verminderen of omkeren.

### 7.3 Culturele modelbias is nog geen bewezen cultuurhomogenisering

Meertalige studies vinden dat modellen culturele voorkeuren en dominante perspectieven kunnen reproduceren. Dat is een relevant mechanisme, maar bewijst niet dat menselijke culturen reeds duurzaam naar één vorm convergeren.

KAND-037 blijft daarom emerging en wordt niet geformuleerd als algemene aantasting van taal, cultuur of collectieve denkkracht.

## 8. Claim–bron–tegenbewijs-matrix

| Claim | Ondersteunend bewijs | Tegenbewijs of grens | Voorlopig oordeel |
|---|---|---|---|
| AI-zoeksynthese vermindert direct bronbezoek. | Pew; Agarwal & Sen. | Queryselectie bij Pew; aanbieder rapporteert meer gebruik en waardevollere resterende klikken. | Sterk voor specifieke interfaces. |
| Generatieve antwoorden behouden niet automatisch volledige en correcte bronsteun. | Liu et al.; Strauss et al. | Systemen verschillen en veranderen snel; OpenScholar laat expertniveau zien. | Sterk als conditioneel ontwerpprobleem. |
| Minder klikken veroorzaakt reeds algemeen minder onafhankelijke kennisproductie. | Uitgeverssignalering; eerste verkeersstudies. | Geen complete causale keten; marktverval ouder; aggregatoren kunnen bereik vergroten. | Onvoldoende; downstream-hypothese. |
| Paywalls en crawlerblokkades bewijzen enclosure van menselijke kennis. | Longpre et al. tonen snel stijgende AI-beperkingen. | Paywalls kunnen productie financieren; AI-crawlerblokkade sluit menselijk bezoek niet noodzakelijk uit. | Reactie/trade-off, geen wortelprobleem. |
| Generatieve AI vergroot schaal van propaganda en synthetische publicatie. | Wack et al.; Hanley & Durumeric. | Specifieke ecosystemen; geen betrouwbare internetbrede denominator. | Middelsterk en contextgebonden. |
| Synthetische of geautomatiseerde herkomst is voor ontvangers altijd onherkenbaar. | Detectie- en provenancebeperkingen. | Mensen herkennen sommige deepfakes goed; meerdere mitigaties bestaan. | Te absoluut; verificatie-asymmetrie behouden. |
| Misinformatie heeft het gemiddelde informatiedieet overgenomen. | Ernstige casussen en ongelijke verspreiding. | Blootstelling gemiddeld klein en geconcentreerd in representatieve studies. | Verwerpen als algemene claim. |
| Recursieve synthetische training veroorzaakt onvermijdelijk model collapse. | Shumailov et al. onder vervangingscondities. | Accumulatie, echte data, filtering en verificatie kunnen collapse voorkomen. | Verwerpen als onvermijdelijk; technisch risico behouden. |
| Generatieve AI homogeniseert menselijke cultuur. | Doshi & Hauser; culturele modelbias. | Individuele en piekcreativiteit kunnen stijgen; tegenexperiment vindt meer diversiteit. | Emerging, sterk vernauwen. |

## 9. Beoordeling van de oorspronkelijke kandidaten

| Kandidaat | Behandeling | Motivering |
|---|---|---|
| KAND-013 | Opsplitsen; synthese zelf verwerpen als probleem. | Synthese kan efficiëntie, feitelijke herinnering en onderzoekskwaliteit verbeteren. Alleen vervanging zonder gelijkwaardige provenance en bronrelatie is problematisch. |
| KAND-014 | Behouden als meetbaar mechanisme/direct effect. | Nul-klik en minder bronverkeer zijn onderbouwd, maar een niet-klik is niet vanzelf schade. |
| KAND-015 | Opsplitsen. | Bereik is aantoonbaar; erkenning moet apart worden gemeten; inkomen en kennisproductie blijven sectorspecifieke downstream-hypothesen. |
| KAND-016 | Herclassificeren als reactie- en trade-offlens. | Paywalls en crawlerblokkades kunnen beschermen of financieren en tegelijk toegang beperken. |
| KAND-017 | Verwerpen als zelfstandig probleem. | Toenemend synthetisch gebruik of mogelijke dataschaarste is een trend/driver, geen onvermijdelijk probleem. |
| KAND-018 | Behouden als technisch risico, niet als charterprobleem. | Collapse treedt op bij specifieke recursieve trainingscondities en is mitigeerbaar. |
| KAND-019 | Onderbrengen bij KAND-018. | Statistisch tailverlies is onderbouwd; verlies van menselijke minderheidskennis is nog een sociale extrapolatie. |
| KAND-020 | Verwerpen als zelfstandig probleem. | Prestatieverlies is gevolg van specifieke trainingskeuzes; betekenis- en werkelijkheidsdegradatie zijn te breed. |
| KAND-021 | Opsplitsen en invoegen in kandidaat 5B. | Bots en synthetische ruis zijn productie- en amplificatiemechanismen; internetbrede dominantie is niet bewezen. |
| KAND-022 | Vernauwen tot kandidaat 5B. | Oncontroleerbare herkomst bij schaalbare productie is houdbaar; een algemene crisis van perceptie en sociaal vertrouwen niet. |
| KAND-023 | Buiten deze familie herplaatsen. | Gedragssturing hoort bij dossier 004; zichtbaarheid en regelmacht kruisen kandidaat 5A en familie 1, maar vormen hier geen nieuwe wortel. |
| KAND-024 | Verwerpen als zelfstandig probleem; behouden als toepassing/indicator. | Desinformatie is een inhouds- en aanvalscategorie met vele oorzaken, geen enkelvoudige wortel. |
| KAND-025 | Behouden en vernauwen tot actieve kandidaat 5A. | Claimgebonden bronsteun en context zijn niet automatisch aanwezig; sterke provenance is wel technisch mogelijk. |
| KAND-037 | Behouden als emerging risico 5D. | Kortetermijnconvergentie bestaat naast productiviteits- en creativiteitswinst; brede cultuurverarming is niet bewezen. |

## 10. Wat dit dossier uitdrukkelijk niet beweert

Dit dossier beweert niet dat:

- synthese, samenvatting of een nul-klik op zichzelf schadelijk is;
- alle AI-antwoorden slechte of verzonnen citaties bevatten;
- gebruikers altijd de oorspronkelijke bron moeten bezoeken;
- iedere maker recht heeft op verkeer, betaling of eigendom van ieder afgeleid inzicht;
- generatieve AI de historische neergang van nieuwsmarkten heeft veroorzaakt;
- paywalls of crawlerblokkades per definitie tegen het publieke belang zijn;
- synthetische inhoud noodzakelijk onwaar of kwalitatief inferieur is;
- menselijke herkomst een garantie voor waarheid vormt;
- het internet voornamelijk uit bots, desinformatie of “AI slop” bestaat;
- model collapse bij iedere inzet van synthetische data optreedt;
- menselijk taalgebruik, cultuur of creativiteit reeds algemeen homogeniseert;
- technische provenance automatisch waarheid, legitimiteit of kwaliteit vaststelt.

## 11. Falsificatie- en grenstoetsen

### Voor actieve kandidaat 5A — Bronrelatie

De kandidaat geldt niet voor een systeem of context wanneer onafhankelijke audits aantonen dat:

1. materiële beweringen vrijwel volledig en correct claimgebonden worden geciteerd;
2. iedere bewering direct naar passage, auteur, datum, versie en context voert;
3. onzekerheid en conflicterende bronnen zichtbaar blijven;
4. gebruikers onjuiste of onvoldoende ondersteunde claims minstens even goed herkennen als bij directe bronzoeking;
5. deze eigenschappen standhouden over domeinen, talen, tijd en modelupdates.

### Voor actieve kandidaat 5B — Oncontroleerbare herkomst

De kandidaat verzwakt wanneer representatieve veldstudies aantonen dat:

1. ontvangers in normaal gebruik oorsprong, actor en manipulatie betrouwbaar herkennen;
2. platformoverschrijdende provenance intact blijft en werkelijk onderscheidingsvermogen verbetert;
3. geautomatiseerde productie of verspreiding geen materieel schaalvoordeel voor misleiding oplevert;
4. verificatie-instrumenten zonder onevenredige fouten, uitsluiting of algemene verdenking van echte inhoud werken.

### Voor onderzoeksrisico 5C — Bronbereik

De downstream-hypothese wordt pas een onderbouwd probleem wanneer langdurig en voor bedrijfsmodel gecorrigeerd onderzoek laat zien dat minder bronverkeer leidt tot materieel verlies van:

- erkenning, inkomsten of opdrachten;
- redactionele of onderzoekscapaciteit;
- productie van moeilijk vervangbare bronkennis;
- pluraliteit of open toegankelijkheid.

Zij verzwakt wanneer resterende bezoeken waardevoller zijn, alternatieve financiering het verlies compenseert of productie en pluraliteit niet afnemen.

### Voor emerging risico 5D — Creatieve convergentie

De kandidaat verzwakt wanneer preregistreerde studies over meerdere talen, culturen, media en langere perioden geen daling of juist stijging van collectieve diversiteit vinden, of wanneer het effect bij realistische interactieve workflows en diversiteitsgericht ontwerp verdwijnt.

## 12. Voorlopig bewijsoordeel

| Onderdeel | Oordeel |
|---|---|
| AI-antwoordsynthese vermindert bronklikken | Hoog voor onderzochte zoekinterfaces |
| Synthese levert snelheid, toegankelijkheid en soms betere feitelijke recall | Hoog |
| Generatieve citaties zijn zonder audit volledig en correct | Weerlegd als algemene aanname |
| Ontwerp met sterke claimgebonden provenance is technisch mogelijk | Hoog |
| Langetermijnverlies van bronherinnering door synthese | Onvoldoende |
| Minder bronverkeer | Hoog als direct effect; causaliteit steeds beter onderbouwd |
| Minder inkomsten of kennisproductie door AI-synthese | Laag/onvoldoende en sectorspecifiek |
| Schaalvergroting van synthetische propaganda/productie | Middelmatig-hoog in specifieke ecosystemen |
| Internetbrede dominantie door bots of synthetische ruis | Onvoldoende |
| Algemene crisis van sociaal vertrouwen door synthetische inhoud | Onvoldoende |
| Model collapse bij indiscriminerende recursieve vervanging | Hoog binnen geteste condities |
| Onvermijdelijke model collapse bij synthetische data | Weerlegd |
| Kortetermijnconvergentie van creatieve output | Middelmatig en contextafhankelijk |
| Duurzame homogenisering van taal, cultuur of collectieve denkkracht | Onvoldoende |

## 13. Gevolgen voor de voorlopige probleemkaart

De oude familie 5 wordt vervangen door:

1. **5A — Niet-herleidbare bronbasis bij vervangende antwoordsynthese** — actief; KAND-025 als kern, KAND-013/014 als mechanismen.
2. **5B — Oncontroleerbare herkomst van schaalbaar geproduceerde inhoud** — actief maar begrensd; KAND-022 als kern, KAND-021/024 als mechanismen of toepassingen.
3. **5C — Ontkoppeling van kennisconsumptie en bronbereik** — onderzoeksrisico; bereik onderbouwd, verdere economische en kennisgevolgen open.
4. **5D — Conditionele convergentie van collectieve creatie** — emerging; KAND-037, zonder brede cultuurclaim.

KAND-017–020 worden niet als zelfstandige probleemtakken opgenomen. KAND-023 blijft verdeeld over gedragssturing, intermediaire macht en zichtbaarheid. KAND-016 blijft zichtbaar als reactie- en trade-offlens.

## 14. Bronnen

### Synthese, bronrelatie en leren

- Pew Research Center (2025), [Google users are less likely to click on links when an AI summary appears in the results](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/).
- Agarwal & Sen (2026), [The Impact of Google AI Overviews on Publisher Traffic and User Experience](https://doi.org/10.2139/ssrn.6513059). Working paper.
- Liu, Zhang & Liang (2023), [Evaluating Verifiability in Generative Search Engines](https://doi.org/10.18653/v1/2023.findings-emnlp.467).
- Strauss et al. (2026), [The attribution crisis in LLM search results](https://doi.org/10.1017/dap.2026.10064).
- Kim et al. (2025), [Fostering Appropriate Reliance on Large Language Models](https://doi.org/10.1145/3706598.3714020).
- Melumad & Yun (2025), [Experimental evidence of the effects of large language models versus web search on depth of learning](https://doi.org/10.1093/pnasnexus/pgaf316).
- Karell et al. (2025), [Research on factual recall after AI summaries](https://doi.org/10.1177/08944393251409744).
- Asai et al. (2026), [Synthesizing scientific literature with retrieval-augmented language models](https://doi.org/10.1038/s41586-025-10072-4).

### Bronbereik, economie en toegang

- Calzada & Gil (2020), [What Do News Aggregators Do?](https://doi.org/10.1287/mksc.2019.1150).
- Chiou & Tucker (2017), [Content aggregation by platforms](https://doi.org/10.1111/jems.12207).
- Pattabhiramaiah, Sriram & Manchanda (2019), [Paywalls and digital news consumption](https://doi.org/10.1177/0022242918815163).
- Longpre et al. (2024), [Consent in Crisis: The Rapid Decline of the AI Data Commons](https://papers.nips.cc/paper_files/paper/2024/hash/c3738949a80306cc48a8ea8ba0560f9d-Abstract-Datasets_and_Benchmarks_Track.html).
- Australian Treasury (2022), [Review of the News Media and Digital Platforms Mandatory Bargaining Code](https://treasury.gov.au/publication/p2022-343549).
- UK Government (2026), [Report on Copyright and Artificial Intelligence](https://www.gov.uk/government/publications/report-and-impact-assessment-on-copyright-and-artificial-intelligence/report-on-copyright-and-artificial-intelligence).

### Synthetische productie, bots en verificatie

- Wack et al. (2025), [Generative propaganda](https://doi.org/10.1093/pnasnexus/pgaf083).
- Hanley & Durumeric (2024), [Machine-Made Media](https://doi.org/10.1609/icwsm.v18i1.31333).
- Shao et al. (2018), [The spread of low-credibility content by social bots](https://doi.org/10.1038/s41467-018-06930-7).
- Vosoughi, Roy & Aral (2018), [The spread of true and false news online](https://doi.org/10.1126/science.aap9559).
- Groh et al. (2024), [Human detection of political speech deepfakes](https://doi.org/10.1038/s41467-024-51998-z).
- Guess, Nyhan & Reifler (2020), [Exposure to untrustworthy websites in the 2016 US election](https://doi.org/10.1038/s41562-020-0833-x).
- NIST (2024), [Reducing Risks Posed by Synthetic Content](https://doi.org/10.6028/NIST.AI.100-4).
- C2PA (2025), [C2PA Explainer and Specification 2.2](https://c2pa.org/specifications/specifications/2.2/explainer/Explainer.html).

### Trainingsdynamiek en collectieve creatie

- Shumailov et al. (2024), [AI models collapse when trained on recursively generated data](https://doi.org/10.1038/s41586-024-07566-y).
- Gerstgrasser et al. (2024), [Is Model Collapse Inevitable?](https://openreview.net/forum?id=5B2K4LRgmz).
- Wang et al. (2023), [Self-Instruct](https://doi.org/10.18653/v1/2023.acl-long.754).
- Doshi & Hauser (2024), [Generative AI enhances individual creativity but reduces the collective diversity of novel content](https://doi.org/10.1126/sciadv.adn5290).
- Zhou & Lee (2024), [Generative artificial intelligence, human creativity, and art](https://doi.org/10.1093/pnasnexus/pgae052).
- Ashkinaze et al. (2025), [How AI Ideas Affect the Creativity, Diversity, and Evolution of Human Ideas](https://doi.org/10.1145/3715928.3737481).
- Naous et al. (2024), [Cultural bias in multilingual language models](https://doi.org/10.18653/v1/2024.acl-long.862).

## 15. Lokale relaties

- [Voorlopige probleemkaart](PROVISIONAL_PROBLEM_MAP.md)
- [Probleemdossier 001 — geconcentreerde digitale bemiddelingsmacht](PROBLEM_DOSSIER_001_CONCENTRATED_DIGITAL_INTERMEDIATION.md)
- [Probleemdossier 004 — gedragssturing, AI-afhankelijkheid en synthetische relaties](PROBLEM_DOSSIER_004_AUTONOMY_DECOMPOSITION.md)
- [Kandidatenlonglist](../02_overdrachtsdocumenten/KANDIDATENLONGLIST.md)
- [Onderzoeksprotocol](RESEARCH_PROTOCOL.md)

## 16. Versiegeschiedenis

| Versie | Datum | Wijziging |
|---|---|---|
| 0.3 | 2026-08-08 | Alle interne werklabels gesynchroniseerd met de probleemkaart en baseline: 5A, 5B, 5C en 5D. |
| 0.2 | 2026-08-08 | Probleemzinnen ontdaan van oplossingsvoorschriften; 5A en 5B in begrijpelijker Nederlands en met behoud van hun onderlinge scheidslijn vastgelegd. |
| 0.1 | 2026-08-08 | Eerste volledige ontleding van bronrelaties, bronbereik, synthetische productie, model collapse, desinformatie en creatieve convergentie. |

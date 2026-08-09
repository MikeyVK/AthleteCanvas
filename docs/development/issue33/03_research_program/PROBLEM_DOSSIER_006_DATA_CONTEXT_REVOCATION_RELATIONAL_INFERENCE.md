<!-- C:\1Voudig\99_Programming\ypsia\docs\development\issue33\03_research_program\PROBLEM_DOSSIER_006_DATA_CONTEXT_REVOCATION_RELATIONAL_INFERENCE.md -->
<!-- template=research version=8b7bb3ab created=2026-08-08T17:35Z updated= -->
# Probleemdossier 006 — Context, herroepbaarheid en relationele gegevensmacht

| Veld | Waarde |
|---|---|
| Status | PRELIMINARY |
| Versie | 0.2 |
| Laatst bijgewerkt | 2026-08-08 |
| Onderzoeksfase | Inhoudelijk bronnenonderzoek en ontleding |
| Primaire kandidaten | KAND-008 en KAND-026–032 |
| Overgenomen materiaal | Tracking- en toestemmingsbevindingen uit dossier 003 |
| Voorlopig oordeel | De oorspronkelijke gegevensfamilie opsplitsen |
| Actieve kandidaten | Context- en doeloverschrijdend datagebruik; niet-doorgewerkte correctie of beëindiging; voorspellingen over mensen uit gegevens van anderen |
| Verworpen brede claims | Alle toestemming is schijn; ieder hergebruik is schadelijk; AI-training is principieel onverenigbaar met gegevensbescherming; modellen zijn inherent onuitwisbaar; iedere algoritmische groep heeft één collectief privacyrecht |

## 1. Doel en onderzoeksvraag

De voorlopige probleemkaart bracht KAND-008 en KAND-026–032 samen onder **contextoverschrijdend, persistent en relationeel datagebruik zonder effectieve controle**. Die formulering is te breed voor het Single Responsibility Principle (SRP). Zij vermengt drie verschillende vragen:

1. mag informatie voor een andere context, actor, ontvanger of doel worden gebruikt;
2. kan een geldige correctie, intrekking of verwijdering aantoonbaar doorwerken in kopieën en afgeleiden;
3. kan informatie van anderen iemand profileerbaar maken die zelf niet deelnam.

Dit dossier onderzoekt welke vragen als zelfstandig probleem kunnen blijven bestaan. Het kiest geen eigendomsmodel, gegevensarchitectuur of juridisch eindantwoord en wijzigt de vastgestelde onderzoeksmethodiek niet.

## 2. Voorlopige ontleding

### 2.1 Actieve kandidaat 6A — Context- en doeloverschrijdend datagebruik

> Digitale systemen kunnen gegevens die binnen één relatie of voor één doel zijn verkregen koppelen, doorgeven of gebruiken voor een wezenlijk andere relatie, ontvanger of beslissing, terwijl voor die contextverschuiving geen afzonderlijk toetsbare en inhoudelijk toereikende rechtvaardiging bestaat.

Voorzienbaarheid, begrijpelijkheid en betwistbaarheid bepalen mede de ernst en de beschikbare bescherming, maar zijn niet de causale kern van 6A. Een concrete beslissing die niet effectief kan worden betwist, hoort bij 7A.

Niet iedere gegevenskoppeling is een schending. De toets betreft ten minste:

- wie informatie verstrekt, over wie zij gaat en wie haar ontvangt;
- het gegevenstype en de gevoeligheid die uit de combinatie ontstaat;
- het oorspronkelijke en nieuwe doel;
- bewaartermijn, verdere verstrekking en transformatie;
- noodzaak, evenredigheid, publieke of private baten en mogelijke schade;
- transparantie, controle, onafhankelijke toetsing en daadwerkelijk verhaal.

Gebruikersverwachtingen zijn empirisch bewijs, maar geen volledige morele maatstaf. Een gebruik wordt niet gerechtvaardigd doordat een meerderheid het verwacht of een lokale praktijk het normaal vindt. Gelijke menselijke waardigheid en bescherming blijven grenzen aan contextuele variatie.

KAND-008 en KAND-030 vormen samen de kern. De eerder onder KAND-002/003 onderzochte tracking- en toestemmingsmechanismen verhuizen hierheen.

### 2.2 Actieve kandidaat 6B — Niet-doorgewerkte correctie of beëindiging van persoonsgegevensgebruik

> Een geldige correctie of beëindiging van persoonsgegevensgebruik werkt niet door wanneer kopieën en nog tot de persoon herleidbare afleidingen elders blijven worden gebruikt, of wanneer de verantwoordelijke ondanks een toepasselijke verantwoordingsplicht niet kan aantonen dat die verwerking is aangepast of gestopt.

Ontbrekende herleidbaarheid van gegevens, ontvangers en modelversies is een belangrijk uitvoerings- en bewijsmechanisme, maar niet zelfstandig de schade. De actieve kern vereist voortgezette personenspecifieke verwerking of het niet kunnen afleggen van een toepasselijk verschuldigde verantwoording na een geldige aanspraak.

Deze kandidaat beweert niet dat iedere statistische invloed moet verdwijnen. Hij geldt alleen waar een geldige aanspraak bestaat en een afgeleide representatie nog identificeerbare, extraheerbare of operationeel personenspecifieke informatie bevat of gebruikt. Werkelijk anonieme aggregaten en gerechtvaardigde wettelijke uitzonderingen vallen niet automatisch binnen de claim.

Het controledeel van KAND-026 levert de kern. KAND-027–029 beschrijven technische mechanismen en verificatieproblemen.

### 2.3 Actieve kandidaat 6C — Voorspellingen over mensen uit gegevens van anderen

> Gegevens van anderen kunnen worden gebruikt om iemands identiteit, gevoelige kenmerken of beslisrelevante risico's af te leiden die over die persoon worden toegepast of blootgesteld, zonder dat die persoon zelf gegevens heeft verstrekt of de afleiding praktisch kan kennen, corrigeren of betwisten.

De kandidaat geldt niet voor iedere populatiestatistiek. Een casus moet aantonen dat gegevens van anderen materiële extra informatiewinst leveren én leiden tot blootstelling, surveillance of ander relevant gebruik, terwijl effectieve bescherming of verhaal ontbreekt.

Dit is de versmalde relationele kern van KAND-032. Een algemeen privacyrecht voor iedere door een model geconstrueerde groep wordt niet aangenomen.

### 2.4 Waarom drie kandidaten

Een red-teamroute adviseerde 6B als mechanisme onder 6A te plaatsen en 6C voorlopig emerging te houden. Dit dossier houdt de drie routes afzonderlijk omdat hun tegenfeitelijke toetsen verschillen:

- 6A kan bestaan zonder verwijderingsverzoek: het nieuwe gebruik was vanaf het begin ongerechtvaardigd;
- 6B kan bestaan binnen hetzelfde legitieme doel: een latere geldige herroeping werkt niet door;
- 6C kan bestaan zonder dat de niet-deelnemer ooit zelf een informatiestroom is begonnen.

6C krijgt wel een lager bewijsvertrouwen dan 6A: het mechanisme is sterk aangetoond, maar internetbrede prevalentie en concrete gevolgen zijn minder breed gemeten.

## 3. Bevindingen over context, tracking en toestemming

### 3.1 Contextoverschrijdende verzameling is geen hypothetisch randverschijnsel

De FTC onderzocht negen grote sociale- en videodiensten op basis van wettelijke informatievorderingen. De bedrijven verzamelden gegevens binnen en buiten hun diensten, ontvingen informatie van databrokers, verwerkten gegevens over niet-gebruikers, leidden kenmerken af, deelden breed en gebruikten informatie in algoritmen en AI. Bijna geen van de onderzochte diensten bood integrale controle over al die toepassingen. De steekproef vertegenwoordigt niet het hele internet, maar bestrijkt meerdere zeer grote ecosystemen.

Onafhankelijke metingen versterken dit patroon. Englehardt en Narayanan maten tracking en synchronisatie over één miljoen websites. Binns en collega's vonden derdepartijtrackers in het merendeel van 959.000 onderzochte Android-apps, met een klein aantal partijen dat in zeer veel apps voorkwam.

### 3.2 Toestemming is ontwerpgevoelig, maar niet altijd betekenisloos

Nouwens en collega's vonden bij 680 veelgebruikte toestemmingsinterfaces dat slechts 11,8% aan hun minimale wettelijke criteria voldeed. Het weglaten van een weigermogelijkheid op het eerste scherm verhoogde acceptatie met 22–23 procentpunt. Utz en collega's vonden in drie veldexperimenten met meer dan 80.000 unieke gebruikers dat positie, keuzestructuur en framing de uitkomst substantieel veranderden.

Matte, Bielova en Santos vonden bovendien websites waar een toestemmingssysteem toestemming registreerde zonder geldige keuze of na weigering. Dit bewijst dat een klikregistratie niet automatisch een betrouwbare voorkeur vastlegt.

Het tegenbewijs is belangrijk: mensen kunnen onder symmetrische omstandigheden werkelijk instemmen en onderzoek naar genomische gegevensdeling laat brede bereidheid tot gecontroleerd hergebruik zien. De houdbare conclusie is daarom niet dat toestemming altijd schijn is, maar dat individuele keuze geen voldoende waarborg vormt wanneer informatie, ontvangers, doelen en downstreamgebruik niet overzienbaar zijn.

### 3.3 Context is empirisch meetbaar

Martin en Shilton lieten 1.915 deelnemers 77.480 mobiele scenario's beoordelen. Verwachtingen veranderden voorspelbaar met actor, gegevenstype, toepassingscontext en gebruik. Apthorpe en collega's vonden vergelijkbare verschillen bij 1.731 deelnemers en 3.840 smart-home-informatiestromen.

Deze studies meten oordelen en geen morele waarheid. Zij onderbouwen wel dat “de gebruiker heeft gegevens gedeeld” onvoldoende beschrijft welke verdere stromen passend zijn.

### 3.4 Concrete contextverschuiving kan gevoelige schade creëren

In officiële procedures stelde de FTC onder meer vast of aan dat:

- GoodRx gezondheids- en medicatiegegevens met advertentieplatforms deelde, in strijd met eerdere beloften;
- X-Mode precieze locatiegegevens verkocht waarmee bezoeken aan klinieken, gebedshuizen en opvanglocaties konden worden gevolgd;
- Cambridge Analytica gegevens van tientallen miljoenen Facebookvrienden verzamelde en voor kiezersprofilering gebruikte, terwijl die vrienden niet met de app hadden geïnterageerd.

Dit zijn specifieke zaken, geen bewijs dat ieder datagebruik dezelfde schade veroorzaakt. Zij tonen wel dat een doel- en ontvangersverschuiving materiële belangen kan raken.

## 4. Bevindingen over herroeping, afgeleiden en modellen

### 4.1 Verwijdering bij de bron is niet hetzelfde als beëindiging van de keten

De FTC-audit uit 2024 vond uiteenlopende en vaak onvolledige bewaarbeleidsregels. Sommige bedrijven gebruikten “soft deletion”, behielden gegevens zolang een algemeen bedrijfsdoel bestond of verwijderden niet alle gegevens na een gebruikersverzoek. Bekende ontvangers, back-ups, gedeelde datasets en afgeleide systemen maken aantoonbare ketenbeëindiging organisatorisch moeilijk.

Dit is het maatschappelijke deel van 6B: niet de rekentijd van één algoritme, maar het ontbreken van een controleerbare keten waarlangs een geldige verandering kan doorwerken.

### 4.2 Modellen kunnen trainingsgegevens onthouden, maar doen dat niet uniform

Carlini en collega's extraheerden honderden letterlijke trainingsfragmenten uit GPT-2, waaronder publiek beschikbare persoonsgegevens. Grotere modellen en herhaalde fragmenten bleken kwetsbaarder. Membership-inferenceonderzoek toont daarnaast dat trainingslidmaatschap in bepaalde modellen en dreigingsmodellen kan lekken.

Daartegenover staat sterk begrenzend bewijs:

- deduplicatie vermindert memorisatie en bestaande extractieaanvallen sterk;
- volledige hertraining zonder het record vormt een krachtige referentie voor exacte verwijdering;
- Ginart, Guo en Bourtoule demonstreren voor begrensde modelklassen efficiënte of certificeerbare verwijdering;
- huidige unlearningtests kunnen worden misleid of alleen zichtbaar gedrag onderdrukken, waardoor onafhankelijke verificatie nog onvolwassen is.

Daarom zijn KAND-027–029 geen natuurwetten en geen drie zelfstandige problemen.

### 4.3 Niet ieder model is blijvend persoonsgebonden

De EDPB stelt dat anonimiteit van AI-modellen per geval moet worden beoordeeld. Een model is niet automatisch anoniem doordat bronrecords zijn verwijderd, maar ook niet automatisch persoonsgegeven doordat ooit persoonsgegevens zijn gebruikt. Identificatie- en extractiekans, redelijk beschikbare aanvalsmiddelen, documentatie en technische waarborgen zijn bepalend.

De absolute stelling van KAND-031—onrechtmatige brondata besmetten noodzakelijk het hele model en vereisen altijd volledige vernietiging—wordt daarom verworpen.

### 4.4 De-identificatie kent risico's én werkbare vormen

Vier tijd- en locatiepunten identificeerden in een dataset van 1,5 miljoen personen 95% van de mobiliteitssporen. Rocher en collega's tonen eveneens dat combinaties van demografische kenmerken hoge heridentificatiekansen kunnen geven. Zulke resultaten weerleggen “namen verwijderen is anonimiseren”.

Zij bewijzen niet dat veilige statistiek onmogelijk is. Differentiële privacy, privacybehoudende recordkoppeling, toegangscontrole en andere technieken kunnen bruikbare analyse mogelijk maken. Iedere techniek kent echter aannames en een privacy–nutafweging die expliciet moet worden beheerd.

## 5. Bevindingen over relationele inferentie

### 5.1 Sociale contacten maken niet-deelnemers voorspelbaar

Garcia toonde met historische Friendster-data dat netwerkstructuur en gegevens van gebruikers seksuele oriëntatie en relatiestatus van toenmalige niet-gebruikers boven toeval konden voorspellen. Bagrow, Liu en Mitchell berekenden dat berichten van acht à negen contacten vrijwel dezelfde theoretisch beschikbare voorspelbaarheid over iemands activiteit konden leveren als de eigen berichtgeschiedenis.

Die 95% betreft een informatie-theoretische bovengrens ten opzichte van beschikbare voorspelbaarheid, niet 95% foutloze persoonsvoorspelling.

### 5.2 Genetische gegevens zijn structureel relationeel

Erlich en collega's onderzochten 1,28 miljoen consumentengenomen. Voor personen van Europese afkomst gaf ongeveer 60% van zoekopdrachten een derdegraadsverwant of nauwere match. Familieleden kunnen iemand dus identificeerbaar maken zonder dat die persoon zelf DNA heeft gedeeld. De populatiebeperking verhindert een universele extrapolatie van het percentage, maar niet het relationele mechanisme.

### 5.3 Een individuele keuze kan miljoenen anderen raken

De Cambridge Analytica-zaak is een concreet voorbeeld: gegevens van ongeveer 250.000–270.000 directe Amerikaanse appgebruikers werden gecombineerd met gegevens van naar schatting 50–65 miljoen Facebookvrienden. Die vrienden hadden geen interactie met de app. Dit laat zien dat relationele informatiewinst niet alleen een laboratoriummogelijkheid is.

### 5.4 Groepsprivacy wordt niet als universeel antwoord aangenomen

Veel algoritmisch samengestelde groepen hebben geen gezamenlijke identiteit, vertegenwoordiging of gedeeld belang. Iedere modelcategorie tot rechtssubject verheffen kan groepen juist essentialiseren, interne verschillen uitwissen en een classificatie van de gegevensbeheerder legitimeren.

Groepsuitkomsten zoals discriminatoire advertentiedistributie en proxybias blijven belangrijk, maar worden primair onderzocht bij familie 7 over digitale beslismacht en ongelijkheid. Voor dit dossier blijft 6C beperkt tot de blootstelling van niet-deelnemers door relationele gegevens.

## 6. Baten en sterk tegenbewijs

### 6.1 Gegevenskoppeling kan aantoonbare publieke waarde hebben

Gezondheidsgegevens uit dossiers, registers, claims en sterftebestanden kunnen gezamenlijk ziekteverloop, behandeling en volksgezondheid zichtbaar maken. Privacybehoudende recordkoppeling wordt reeds gebruikt in meerdere nationale onderzoeksnetwerken. Genomische deelnemers blijken in sommige studies bereid tot brede maar gecontroleerde gegevensdeling.

Daarom is dataminimalisatie geen bevel om iedere informatiestroom te stoppen en is contextverschuiving niet automatisch onrechtmatig of schadelijk.

### 6.2 Inferentie is niet hetzelfde als schade

Fraudedetectie, epidemiologie en populatiestatistiek berusten noodzakelijk op aggregatie en inferentie. RAPPOR en Prio laten zien dat populatie-inzicht mogelijk is zonder iedere individuele bijdrage centraal prijs te geven.

Voor 6C is alleen statistische voorspelbaarheid daarom onvoldoende. Er moet relevante blootstelling of toepassing én een beschermings- of verhaalslacune zijn.

### 6.3 Controle kan daadwerkelijk werken

Individuele rechten en goede governance kunnen voldoende zijn wanneer de verantwoordelijke vindbaar is, afleidingen zichtbaar zijn, gegevensketens herleidbaar blijven en toegang, correctie, bezwaar en verhaal werkelijk uitvoerbaar zijn. Het probleem is dus geen menselijke onmacht tegenover iedere dataverwerking, maar aantoonbare gevallen waarin de gegevensketen deze mogelijkheden structureel ondergraaft.

## 7. Beoordeling van de oorspronkelijke kandidaten

| Kandidaat | Herclassificatie | Voorlopig oordeel |
|---|---|---|
| KAND-008 | Kern van 6A | Behouden na vernauwing; aggregatie alleen is geen schending. |
| KAND-026 | Juridische en architecturale spanning | Kruist 6A en 6B; geen universele incompatibiliteit tussen AI-training en gegevensbescherming. |
| KAND-027 | Technisch mechanisme achter 6B | Lokalisatie en verwijdering zijn moeilijk, niet principieel onmogelijk. |
| KAND-028 | Oplossingsbeperking | Werkelijke afweging tussen garantie, nut en rekenkosten; geen zelfstandig probleem. |
| KAND-029 | Conditioneel technisch risico en verificatietest | Membership inference bewijst geen algemene reconstructie of mislukte verwijdering. |
| KAND-030 | Kernmechanisme van 6A | Alleen ongerechtvaardigde of onverenigbare doelverschuiving telt. |
| KAND-031 | Verworpen absolute gevolgtrekking | Modelvernietiging kan soms proportioneel zijn, maar volgt niet automatisch. |
| KAND-032 | Kern van 6C | Relationeel deel behouden; brede groepsrechtclaim niet overnemen. |

## 8. Claim–bron–tegenbewijs-matrix

| Claim | Dragend bewijs | Sterkste grens of tegenbewijs | Oordeel |
|---|---|---|---|
| Grote digitale diensten verzamelen en gebruiken gegevens over meerdere contexten. | FTC 6(b); Englehardt; Binns. | Geen representatieve meting van het hele internet; sommige verwerking is noodzakelijk. | Hoog voor onderzochte ecosystemen. |
| Individuele toestemming geeft betrouwbare end-to-end controle. | Formele toestemmingsmechanismen. | Nouwens; Utz; Matte; FTC tonen ontwerpgevoeligheid en downstream-onzichtbaarheid. | Weerlegd als algemene aanname. |
| Context verandert wat mensen passend vinden. | Martin & Shilton; Apthorpe. | Verwachting is geen volledige normatieve rechtvaardiging. | Hoog als empirisch patroon. |
| Een bronrecord wissen stopt alle afgeleide verwerking. | Geldt in eenvoudige, beheerste systemen. | FTC-retentiebevindingen; modelmemorisation; ontvangerkopieën. | Weerlegd als algemene aanname. |
| Machine-unlearning is onmogelijk. | Moeilijkheid bij diffuse gewichten en kwetsbare evaluaties. | Hertraining; Ginart; Guo; Bourtoule. | Weerlegd. |
| Ieder getraind model blijft persoonsgegeven. | Extractie is bij sommige modellen mogelijk. | EDPB vereist beoordeling per geval; anonimisering kan slagen. | Weerlegd. |
| Andermans gegevens kunnen niet-deelnemers profileerbaar maken. | Garcia; Bagrow; Erlich; Cambridge Analytica. | Nauwkeurigheid, populatie en gevolg verschillen sterk per casus. | Middel-hoog. |
| Iedere algoritmische groep heeft een uniform collectief privacybelang. | Conceptuele groepsprivacyliteratuur. | Dynamische groepen missen vaak identiteit, vertegenwoordiging en gedeeld belang. | Onvoldoende en normatief riskant. |
| Gegevenskoppeling is per definitie schadelijk. | Specifieke misbruikzaken. | Gezondheidsonderzoek, fraudedetectie, statistiek en privacytechniek leveren reële baten. | Weerlegd. |

## 9. Operationele drempels

### Voor 6A

Een casus telt pas wanneer een materiële verandering plaatsvindt in context, doel, actor, ontvanger, bewaartermijn of transformatie én de nieuwe stroom onvoldoende gerechtvaardigd, transparant of betwistbaar is. Alleen onverwachtheid of impopulariteit is niet genoeg.

### Voor 6B

Een casus vereist:

1. een geldige correctie, intrekking, bezwaar- of verwijderingsgrond;
2. een downstreamkopie of afgeleide die nog identificeerbare, extraheerbare of personenspecifiek gebruikte informatie bevat;
3. falende uitvoering of ontbrekend onafhankelijk bewijs dat de aanspraak door de relevante keten werkte.

### Voor 6C

Een casus vereist:

1. materiële extra identificatie- of voorspellingskracht uit gegevens van anderen;
2. blootstelling, surveillance of ander relevant gebruik over de niet-deelnemer;
3. geen effectieve mogelijkheid tot kennisneming, correctie, weigering of verhaal.

Voor een afzonderlijke collectieve schadeclaim is bovendien een aantoonbaar gedeeld belang en meetbaar collectief gevolg nodig. Een modelcluster alleen is onvoldoende.

## 10. Wat dit dossier uitdrukkelijk niet beweert

- Privacy betekent niet dat informatie nooit mag stromen.
- Toestemming is niet altijd ongeldig of waardeloos.
- Iedere nieuwe gegevensbestemming is niet automatisch function creep.
- Ieder model onthoudt of openbaart trainingsgegevens niet in gelijke mate.
- Een geldige verwijderingsaanspraak is niet absoluut en vereist niet altijd modelvernietiging.
- Statistische kennis over een populatie is niet automatisch schade.
- Relationele gegevens geven één familielid of contact geen exclusief eigendomsrecht over gedeelde feiten.
- Groepen worden niet als minderwaardig, homogeen of onbeweeglijk behandeld.

## 11. Falsificatie- en grenstoetsen

### 6A verzwakt wanneer

- hergebruik aantoonbaar binnen dezelfde gerechtvaardigde context en doelbinding blijft;
- de nieuwe stroom noodzakelijk, evenredig, transparant en effectief betwistbaar is;
- representatieve audits geen betekenisvolle contextoverschrijdende verwerking vinden;
- symmetrische keuzes stabiel en aantoonbaar geïnformeerd blijven bij gewijzigde presentatie.

### 6B verzwakt wanneer

- organisaties op relevante schaal alle datasets, ontvangers en modelversies kunnen traceren;
- een geldige verandering binnen redelijke tijd aantoonbaar door alle toepasselijke ketens werkt;
- aangepaste modellen onder vooraf vastgelegde extractie- en membershiptests niet te onderscheiden zijn van een model dat de gegevens nooit zag;
- resterende representaties werkelijk anoniem zijn of niet langer personenspecifiek worden gebruikt.

### 6C verzwakt wanneer

- gegevens van relaties geen relevante extra voorspellings- of identificatiekracht leveren;
- afleidingen niet tot relevante blootstelling of toepassing leiden;
- ook niet-deelnemers consequent effectieve individuele bescherming en remedies hebben;
- privacybehoudende aggregatie de relationele spillover op operationele schaal wegneemt.

## 12. Voorlopig bewijsoordeel

| Onderdeel | Oordeel |
|---|---|
| Contextoverschrijdende tracking en aggregatie in grote digitale ecosystemen | Hoog |
| Contextafhankelijkheid van privacyverwachtingen | Hoog |
| Manipuleerbaarheid en onvolledigheid van toestemmingsinterfaces | Hoog |
| Iedere toestemming is schijn | Weerlegd |
| Concrete gevoelige doel- en ontvangersverschuiving | Hoog in specifieke officiële zaken |
| Internetbrede prevalentie van materieel ongerechtvaardigd hergebruik | Middel |
| Organisatorische downstream-verwijderingskloof | Middel-hoog in onderzochte diensten |
| Extractie of membership inference uit ieder model | Weerlegd |
| Technische mogelijkheid van begrensde, certificeerbare verwijdering | Hoog |
| Robuuste onafhankelijke unlearningverificatie voor complexe modellen | Emerging/onvolwassen |
| Relationele inferentie over niet-deelnemers | Hoog als technisch en empirisch mechanisme |
| Internetbrede materiële relationele schade | Middel |
| Universeel groepsprivacyrecht voor modelgroepen | Onvoldoende |
| Legitieme maatschappelijke baten van gegevenskoppeling | Hoog |

## 13. Gevolgen voor de voorlopige probleemkaart

De oude familie 6 wordt vervangen door:

1. **6A — Context- en doeloverschrijdend datagebruik** — actief; KAND-008 en KAND-030 als kern, met tracking en toestemmingsontwerp als mechanismen.
2. **6B — Niet-doorgewerkte correctie of beëindiging van persoonsgegevensgebruik** — actief maar smaller en met lager vertrouwen; het controledeel van KAND-026 als kern, KAND-027–029 als mechanismen en toetsingskennis.
3. **6C — Voorspellingen over mensen uit gegevens van anderen** — actief met lager bewijsvertrouwen dan 6A; versmalde KAND-032.

KAND-028 blijft een oplossingsbeperking. KAND-031 blijft als gecorrigeerde, verworpen hypothese traceerbaar. Brede groepsschade wordt niet als zelfstandig probleem vastgesteld; discriminatoire groepsuitkomsten worden bij familie 7 getoetst.

## 14. Bronnen

### Context, tracking en toestemming

- [FTC, *A Look Behind the Screens* (2024)](https://www.ftc.gov/system/files/ftc_gov/pdf/Social-Media-6b-Report-9-11-2024.pdf)
- [FTC, *Data Brokers: A Call for Transparency and Accountability* (2014)](https://www.ftc.gov/reports/data-brokers-call-transparency-accountability-report-federal-trade-commission-may-2014)
- [Englehardt & Narayanan, *Online Tracking: A 1-million-site Measurement and Analysis*](https://doi.org/10.1145/2976749.2978313)
- [Binns e.a., *Third Party Tracking in the Mobile Ecosystem*](https://doi.org/10.1145/3201064.3201089)
- [Nouwens e.a., *Dark Patterns after the GDPR*](https://doi.org/10.1145/3313831.3376321)
- [Utz e.a., *(Un)informed Consent*](https://doi.org/10.1145/3319535.3354212)
- [Matte, Bielova & Santos, consent-measurement study](https://doi.org/10.1109/SP40000.2020.00076)
- [Martin & Shilton, mobile privacy expectations](https://doi.org/10.1080/01972243.2016.1153012)
- [Apthorpe e.a., smart-home informational norms](https://doi.org/10.1145/3214262)
- [Nissenbaum, *Privacy as Contextual Integrity*](https://digitalcommons.law.uw.edu/wlr/vol79/iss1/10/)

### Concrete officiële zaken

- [FTC, GoodRx health-data enforcement](https://www.ftc.gov/news-events/news/press-releases/2023/02/ftc-enforcement-action-bar-goodrx-sharing-consumers-sensitive-health-info-advertising)
- [FTC, X-Mode sensitive-location order](https://www.ftc.gov/news-events/news/press-releases/2024/04/ftc-finalizes-order-x-mode-successor-outlogic-prohibiting-it-sharing-or-selling-sensitive-location)
- [FTC, Cambridge Analytica opinion](https://www.ftc.gov/business-guidance/blog/2019/12/commission-issues-opinion-cambridge-analytica-case)

### Herroeping, anonimisering en modellen

- [EDPB, Opinion 28/2024 on AI models](https://www.edpb.europa.eu/system/files/documents/2024-12/edpb_opinion_202428_ai-models_en.pdf)
- [Carlini e.a., *Extracting Training Data from Large Language Models*](https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting)
- [Kandpal e.a., deduplication and memorization](https://proceedings.mlr.press/v162/kandpal22a.html)
- [Ginart e.a., *Making AI Forget You*](https://proceedings.neurips.cc/paper/2019/hash/cb79f8fa58b91d3af6c9c991f63962d3-Abstract.html)
- [Guo e.a., *Certified Data Removal from Machine Learning Models*](https://proceedings.mlr.press/v119/guo20c.html)
- [Bourtoule e.a., *Machine Unlearning*](https://doi.org/10.1109/SP40001.2021.00019)
- [Zhang e.a., external verification of machine unlearning](https://proceedings.mlr.press/v235/zhang24h.html)
- [de Montjoye e.a., *Unique in the Crowd*](https://doi.org/10.1038/srep01376)
- [Rocher e.a., re-identification in incomplete datasets](https://doi.org/10.1038/s41467-019-10933-3)
- [NIST SP 800-188, de-identifying government datasets](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-188.pdf)

### Relationele gegevens en tegenbewijs

- [Garcia, *Leaking privacy and shadow profiles*](https://doi.org/10.1126/sciadv.1701172)
- [Bagrow, Liu & Mitchell, social prediction limits](https://doi.org/10.1038/s41562-018-0510-5)
- [Erlich e.a., genomic identity inference](https://doi.org/10.1126/science.aau4832)
- [Friehe, Gerhards & Weber, privacy externalities experiment](https://doi.org/10.1016/j.joep.2025.102830)
- [Mittelstadt, *From Individual to Group Privacy*](https://doi.org/10.1007/s13347-017-0253-7)
- [Erlingsson e.a., RAPPOR](https://doi.org/10.1145/2660267.2660348)
- [Corrigan-Gibbs & Boneh, Prio](https://www.usenix.org/conference/nsdi17/technical-sessions/presentation/corrigan-gibbs)
- [Data linkage across healthcare sectors](https://doi.org/10.1038/s43856-025-00769-y)
- [Randomized trial of consent for genomic data sharing](https://pmc.ncbi.nlm.nih.gov/articles/PMC3203320/)

## 15. Lokale relaties

- [Voorlopige probleemkaart](PROVISIONAL_PROBLEM_MAP.md)
- [Kandidatenlonglist](../02_overdrachtsdocumenten/KANDIDATENLONGLIST.md)
- [Claim–bron–tegenbewijs-matrix](../02_overdrachtsdocumenten/CLAIM_BRON_TEGENBEWIJS_MATRIX.md)
- [Probleemdossier 003](PROBLEM_DOSSIER_003_DATA_VALUE_LABOR_DECOMPOSITION.md)
- [Probleemdossier 004](PROBLEM_DOSSIER_004_AUTONOMY_DECOMPOSITION.md)
- [Onderzoeksprotocol](RESEARCH_PROTOCOL.md)

## 16. Versiegeschiedenis

| Versie | Datum | Auteur | Wijziging |
|---|---|---|---|
| 0.2 | 2026-08-08 | Agent | Horizontale SRP-audit verwerkt: 6A substantief begrensd, 6B op voortgezette of niet-verantwoorde verwerking gericht en 6C in begrijpelijk Nederlands geformuleerd. |
| 0.1 | 2026-08-08 | Agent | Eerste bron- en tegenbewijsronde; familie 6 ontbonden in drie begrensde kandidaten. |

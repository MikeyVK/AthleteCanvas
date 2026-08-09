# Probleemdossier 009 — Gedeelde afhankelijkheden en herstelvermogen

**Status:** PRELIMINARY  
**Version:** 0.2  
**Last updated:** 2026-08-08  
**Evidence cut-off:** 2026-08-08  
**Method:** `RESEARCH_PROTOCOL.md` 0.1  
**Source set:** oorspronkelijke kandidaten KAND-046–055

## 1. Doel en onderzoeksvraag

Dit dossier onderzoekt welke zelfstandige problemen overeind blijven binnen de brede familie over infrastructuurconcentratie, ketenafhankelijkheid, cascade-uitval en herstel. De toets vermijdt de aanname dat centralisatie, schaal, een buitenlandse leverancier of open source op zichzelf schadelijk is.

De werklabels zijn voorlopige topologielabels en nog geen definitieve Charter-P-identificaties.

## 2. Voorlopige ontleding

### 2.1 Actieve kandidaat 9A — Gedeelde digitale storingsafhankelijkheid zonder onafhankelijke uitwijkmogelijkheid

> Meerdere essentiële digitale functies kunnen door één gebeurtenis tegelijk uitvallen wanneer zij dezelfde onderliggende leverancier, component, updateketen, beheer- of autoriteitslaag of fysieke route gebruiken en tijdens de verstoring niet tijdig naar een werkelijk onafhankelijke vervanger kunnen uitwijken.

De probleemkern is niet het aantal leveranciers of centralisatie op zichzelf, maar een gedeelde uitvalsoorzaak in combinatie met onvoldoende onafhankelijke uitwijkmogelijkheid. Twee commercieel verschillende diensten zijn niet onafhankelijk wanneer zij dezelfde identiteit, DNS, certificaatautoriteit, route, updateketen of fysieke locatie delen. Geplande beëindiging of migratie onder normale omstandigheden hoort bij kandidaat 2; 9A betreft gelijktijdige uitval en uitwijking binnen een vooraf bepaalde verstoringstermijn.

### 2.2 Actieve kandidaat 9B — Meefalende nood- en herstelmiddelen

> Een essentiële digitale functie is niet zelfstandig bestand tegen verstoring wanneer de middelen voor noodbedrijf, authenticatie, bediening, waarneming, communicatie en herstel door dezelfde fout kunnen uitvallen als de primaire dienst.

Noodcontinuïteit en herstel blijven hier één verantwoordelijkheid omdat zij dezelfde tegenfeitelijke vraag delen: blijven de middelen die een primaire uitval moeten opvangen buiten die uitvalsoorzaak functioneren? Een dienst kan geconcentreerd maar goed bestand tegen verstoring zijn. Omgekeerd kan een verspreid systeem falen wanneer nood- en herstelmiddelen dezelfde afhankelijkheden gebruiken. Daarom is 9B niet slechts een gevolg van 9A.

### 2.3 Onderzoeksrisico 9C — Stewardshipcapaciteit van breed hergebruikte open-sourcecomponenten

> Bij sommige zeer breed hergebruikte open-sourcecomponenten kan de gegarandeerde onderhouds-, beveiligings- en incidentresponscapaciteit achterblijven bij hun transitieve afhankelijkheidsbereik.

Dit is een plausibele en relevante afhankelijkheidsvorm, maar blijft **RESEARCH_RISK/HOLD**. De algemene claim dat open source structureel ondergefinancierd of onveilig is, wordt niet door de huidige bronnen gedragen. De kwestie verklaart nog geen zelfstandige schade naast 9A/9B en blijft een onderzoeksrisico totdat bereik, capaciteit en materiële uitkomsten systematischer zijn vastgesteld.

## 3. Waarom 9A en 9B afzonderlijk blijven

- **9A vraagt:** bestaat een gedeelde afhankelijkheid en kan tijdig naar een werkelijk onafhankelijke vervanger worden overgeschakeld?
- **9B vraagt:** kan de essentiële functie tijdens en na verstoring veilig degraderen, lokaal doorwerken, bestuurd en geobserveerd blijven en aantoonbaar herstellen?

Het eerste betreft topologie en substitutie; het tweede continuïteit en herstel. Een architectuur kan op één van beide toetsen slagen en op de andere falen.

## 4. Bewijs voor 9A — gedeelde afhankelijkheid

De Britse CMA vond in haar cloudonderzoek dat AWS en Microsoft ieder ongeveer 30–40% van de Britse IaaS-markt bedienden en dat jaarlijks minder dan 1% van de klanten van hoofdprovider wisselde. Technische en commerciële barrières beperkten multi-cloud en overstap. Dit ondersteunt afhankelijkheid in specifieke cloudmarkten, niet de claim dat het gehele internet van twee bedrijven afhangt. De in 2026 gemelde verbeterstappen tonen bovendien dat de situatie veranderbaar is.

Internetmetingsonderzoek vond dat een groot aandeel van populaire websites kritisch afhankelijk was van een kleine groep externe DNS-, CDN- en certificaatdiensten. De berekende mogelijkheid dat enkele aanbieders grote delen tegelijk kunnen raken is topologisch bewijs van potentiële blast radius, geen meting dat zulke uitval frequent of onvermijdelijk plaatsvindt.

Concrete incidenten tonen verschillende mechanismen:

- de Fastly-storing van 8 juni 2021 raakte ongeveer 85% van het netwerkverkeer; herstel tot ongeveer 95% volgde binnen 49 minuten;
- een AWS US-EAST-1-storing in december 2021 trof interne monitoring, DNS, authenticatie, control planes en het publieke status- en supportpad, waardoor herstel en communicatie dezelfde failure domain deelden;
- de CrowdStrike-update van juli 2024 trof volgens Microsoft ongeveer 8,5 miljoen Windowsapparaten — minder dan 1% van alle Windowsmachines, maar met brede sectorale impact;
- SolarWinds verspreidde een gecompromitteerde update naar ongeveer 18.000 klanten, terwijl slechts een kleinere groep vervolgens gericht werd geëxploiteerd.

Deze incidenten tonen mogelijke gemeenschappelijke foutpaden. Zij bewijzen niet dat schaal of gedeelde software altijd tot systeemrisico leidt.

## 5. Bewijs voor 9B — continuïteit en herstel

De AWS-casus laat zien waarom een formele redundantieclaim onvoldoende is wanneer authenticatie, observability, ondersteuning en herstelbediening dezelfde storing delen. De operationele vraag is niet alleen of replica's bestaan, maar of mensen de dienst buiten het getroffen failure domain kunnen zien, besturen en herstellen.

Tegenvoorbeelden laten juist zien hoe isolatie de impact begrenst. Tijdens de Cloudflare-storing van november 2023 faalden onder meer control-plane- en analysetaken, terwijl de kern van het verkeers- en beveiligingspad grotendeels bleef functioneren. Fastly herstelde een zeer brede storing relatief snel. Deze voorbeelden ondersteunen 9B als toetsbare ontwerp- en governancevraag, niet als algemene conclusie dat geconcentreerde infrastructuur onherstelbaar is.

Herstelvermogen moet daarom blijken uit destructieve oefeningen en waarneembare uitkomsten: veilig behouden minimumfunctie, onafhankelijke authenticatie en bediening, herstelduur, dataverlies, reconciliatie en communicatie. SLA-tekst of een tweede regio alleen is geen voldoende bewijs.

## 6. Open-source stewardship als begrensde onderzoekslijn

Onderzoek naar npm-afhankelijkheden laat zien dat een klein aantal maintainers transitief zeer veel pakketten kon beïnvloeden. De Linux Foundation/Harvard Census II bracht veelgebruikte componenten en de moeilijkheid van afhankelijkheidsinventarisatie in kaart. Log4Shell toont dat één breed hergebruikte component een uitzonderlijk groot respons- en patchbereik kan hebben.

Dit bewijs ondersteunt transitief bereik, maar nog niet de algemene causaliteit *vrijwillig onderhoud → onvoldoende kwaliteit → maatschappelijke schade*. Recent onderzoek vindt geen eenvoudige relatie tussen gangbare duurzaamheidsindicatoren en softwarekwaliteit. De kandidaat blijft daarom opkomend en wordt pas actief wanneer afhankelijkheidsbereik, gegarandeerde responscapaciteit en materiële uitkomsten gezamenlijk zijn aangetoond.

## 7. Sterk tegenbewijs en legitieme baten

### 7.1 Centralisatie kan betrouwbaarheid en veiligheid verbeteren

Schaal kan professionele beveiliging, redundantie, snelle patching, gespecialiseerde incidentrespons en geografische spreiding financieren. De DNS-root functioneert bijvoorbeeld met twaalf onafhankelijke operatoren en meer dan vijftienhonderd anycast-instanties: een logisch gecentraliseerde functie hoeft operationeel geen enkelvoudig failure domain te zijn.

### 7.2 Diversiteit is niet gratis

Extra leveranciers en technologieën vergroten ook configuratiecomplexiteit, aanvalsvlak, beheerlast en de kans op uiteenlopende beveiligingsniveaus. NIST behandelt diversiteit als één mogelijke cyberresilience-techniek die expliciet tegen kosten en nieuwe risico's moet worden afgewogen.

### 7.3 Cloudafhankelijkheid is niet automatisch systeemrisico

De Financial Stability Board identificeerde in 2019 zowel voordelen als mogelijke concentratierisico's en vond toen geen onmiddellijk financieel-stabiliteitsrisico. De juiste claim is dus conditioneel en domeinspecifiek.

### 7.4 Eigendom of vestigingsland is geen schadeproxy

Niet-Europees eigendom kan rechtsmacht-, continuïteits- of beleidsrisico's beïnvloeden, maar is op zichzelf geen aantoonbare schade. De toets moet gaan over feitelijke controle, afdwingbaarheid, gegevenstoegang, exporteerbaarheid, substitutie en continuïteit.

## 8. Beoordeling van de oorspronkelijke kandidaten

| Oorspronkelijke kandidaat | Oordeel | Plaats in de topologie |
|---|---|---|
| KAND-046 | Splitsen | Operationele/juridische afhankelijkheid onder 9A; geografisch eigendom alleen geen schade |
| KAND-047 | Niet actief | Onderzoeksrisico/HOLD onder 9A en 9B |
| KAND-048 | Geen zelfstandige kandidaat | Incidentvoorbeeld |
| KAND-049 | Verplaatsen/kruisverwijzen | Lock-inmechanisme onder familie 2, versterkt 9A |
| KAND-050 | Geen zelfstandig probleem | Oplossingsbeperking: diversiteit kan complexiteit en risico vergroten |
| KAND-051 | Verplaatsen/kruisverwijzen | Economisch adoptie- en overstapmechanisme onder familie 2 |
| KAND-052 | Behouden en vernauwd | Wortelkandidaat 9A |
| KAND-053 | Geen zelfstandige kandidaat | Cascaderend mechanisme onder 9A |
| KAND-054 | Geen zelfstandige kandidaat | Risicoversterker/gevolg van afhankelijkheidskoppeling |
| KAND-055 | Behouden en vernauwd | Wortelkandidaat 9B |

## 9. Claim–bron–tegenbewijs-matrix

| Claim | Dragend bewijs | Sterkste tegenbewijs of beperking | Voorlopig oordeel |
|---|---|---|---|
| Gedeelde failure domains kunnen meerdere essentiële functies tegelijk raken | Internettopologie; CMA; AWS/Fastly/CrowdStrike/SolarWinds | Veel studies meten potentiële reach; schaal kan redundantie en security financieren | Hoog voor mechanisme; conditioneel voor probleem |
| Formele redundantie kan falen wanneer herstelpaden dezelfde afhankelijkheden delen | AWS-postmortem; Cloudflare-isolatie als vergelijking | Snelle Fastly-recovery; sterke interne isolatie kan risico begrenzen | Middel-hoog |
| Open-source stewardshipcapaciteit blijft soms achter bij transitief bereik | npm-netwerk; Census II; Log4Shell | Geen eenvoudige relatie tussen maintainermaatstaven en kwaliteit; professionele open-sourceprojecten bestaan | Opkomend/HOLD |
| Buitenlands eigendom is op zichzelf een infrastructuurschade | Jurisdictie- en beleidsrisico's | Eigendom voorspelt geen storing, exporteerbaarheid of herstel | Niet behouden |

## 10. Operationele drempels

### Voor 9A

Een beoordeling moet ten minste vastleggen:

- welke functie aantoonbaar essentieel is en welke minimumuitkomst behouden moet blijven;
- de volledige directe en transitieve afhankelijkheidsketen voor code, updates, signing, DNS, certificaten, identiteit, control plane, monitoring, support, fysieke routes en rechtsmacht;
- welke afhankelijkheden werkelijk verschillende failure domains vormen;
- feitelijke overstaptijd, data-export, functionaliteitsverlies, kosten en contractuele belemmeringen;
- of failover onafhankelijk is van dezelfde cloud, identity provider, DNS-, CA-, update- of fysieke infrastructuur;
- historische incidentcorrelatie en maximale aantoonbare blast radius;
- welke schaal-, beveiligings- en betrouwbaarheidsbaten tegenover de afhankelijkheid staan.

### Voor 9B

Vereist zijn vooraf bepaalde minimumfuncties en meetbare uitkomsten:

- percentage veilig behouden functionaliteit en duur van lokale/offline werking;
- onafhankelijke authenticatie, bediening, communicatie en observability;
- MTTD, MTTR, RTO en RPO, met werkelijk dataverlies en herstelduur;
- destructieve failover- en hersteltests buiten het primaire failure domain;
- veilige degradatie, autorisatie en reconciliatie na herstel;
- aantoonbare menselijke bevoegdheid en informatie om tijdens uitval te handelen.

### Voor 9C

Activering vereist gezamenlijk bewijs van hoog transitief bereik, onvoldoende gegarandeerde onderhouds- en incidentresponscapaciteit, een materiële kwetsbaarheids- of continuïteitsuitkomst en gebrek aan een tijdig substituut. Populariteit of weinig maintainers alleen volstaat niet.

## 11. Wat dit dossier uitdrukkelijk niet beweert

- dat centralisatie, standaardisatie of schaal inherent fragiel is;
- dat marktaandeel een voldoende maat voor maatschappelijke uitval is;
- dat multi-cloud automatisch onafhankelijke continuïteit oplevert;
- dat iedere buitenlandse leverancier een soevereiniteits- of continuïteitsprobleem vormt;
- dat open source structureel onveilig of ondergefinancierd is;
- dat iedere storing een systeemcrisis of permanente schade veroorzaakt;
- dat maximale technische diversiteit altijd veiliger is.

## 12. Falsificatie- en grenstoetsen

### 9A verzwakt wanneer

- end-to-end afhankelijkheidsmetingen aantonen dat essentiële functies geen gedeelde failure domains hebben;
- een functioneel gelijkwaardige vervanger binnen de vooraf vereiste tijd onafhankelijk kan worden geactiveerd zonder disproportioneel verlies;
- grootschalige incidenten aantoonbaar lokaal blijven en geen gecorreleerde uitval veroorzaken;
- schaalvoordelen het vergelijkbare alternatief aantoonbaar veiliger en betrouwbaarder maken zonder betekenisvolle exit of controle te verminderen.

### 9B verzwakt wanneer

- destructieve, onafhankelijke oefeningen herhaaldelijk aantonen dat de minimumfunctie veilig degradeert en binnen RTO/RPO herstelt;
- authenticatie, bediening, observability, communicatie en herstel buiten het primaire failure domain blijven functioneren;
- dataverlies, reconciliatie- en veiligheidsrisico's binnen vooraf vastgestelde grenzen blijven;
- incidentdata geen additionele schade door gedeelde herstelafhankelijkheden laten zien.

### 9C verzwakt wanneer

Breed hergebruikte componenten aantoonbaar voldoende gegarandeerde responscapaciteit, meerdere bevoegde maintainers, reproduceerbare builds, tijdige herstelroutes en werkbare substituten hebben, en afhankelijkheidsbereik niet samenhangt met materiële achterstanden of schade.

## 13. Voorlopig bewijsoordeel

| Kandidaat | Materialiteit | Bewijssterkte | Rootness | Status |
|---|---|---|---|---|
| 9A — Gedeelde digitale storingsafhankelijkheid zonder onafhankelijke uitwijkmogelijkheid | Hoog bij essentiële en breed gedeelde functies | Hoog voor mechanisme; middel-hoog voor actuele omvang per domein | Hoog | ACTIVE — PROVISIONAL |
| 9B — Meefalende nood- en herstelmiddelen | Hoog bij essentiële functies | Middel-hoog | Hoog en orthogonaal aan 9A | ACTIVE — PROVISIONAL |
| 9C — Stewardshipcapaciteit van breed hergebruikte open-sourcecomponenten | Potentieel hoog | Middel voor bereik; onvoldoende voor algemene causaliteit | Geen zelfstandige rootness | RESEARCH_RISK — HOLD |

## 14. Gevolgen voor de voorlopige probleemkaart

1. De brede infrastructuurfamilie wordt vervangen door twee actieve kandidaten: 9A en 9B.
2. KAND-047 blijft zichtbaar als onderzoeksrisico 9C onder 9A/9B, maar telt niet mee als actief probleem.
3. KAND-049 en KAND-051 blijven onder familie 2 en krijgen alleen een kruisrelatie naar 9A.
4. Soevereiniteit wordt niet gelijkgesteld aan lokaal of Europees eigendom; feitelijke controle, substitutie en continuïteit zijn beslissend.

## 15. Bronnen

### Afhankelijkheid en concentratie

- UK Competition and Markets Authority, *Cloud services market investigation* (2025): <https://www.gov.uk/cma-cases/cloud-services-market-investigation>
- CMA, *Summary of final decision* (2025): <https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf>
- Kashaf, Sekar & Agarwal, *Analyzing Third Party Service Dependencies in Modern Web Services*, IMC 2020: <https://doi.org/10.1145/3419394.3423664>
- Doan et al., *The Web's Sixth Sense*, ACM TOIT 2022: <https://doi.org/10.1145/3503158>
- OECD, *Vulnerabilities in the semiconductor supply chain*: <https://www.oecd.org/en/publications/vulnerabilities-in-the-semiconductor-supply-chain_6bed616f-en.html>
- ITU, *International Advisory Body for Submarine Cable Resilience*: <https://www.itu.int/en/ITU-T/extcoop/cable-resilience/Pages/default.aspx>

### Incidenten en herstel

- Fastly, *Summary of June 8 outage* (2021): <https://www.fastly.com/blog/summary-of-june-8-outage>
- AWS, *Summary of the AWS Service Event in the Northern Virginia Region* (2021): <https://aws.amazon.com/message/12721/>
- Cloudflare, *Post mortem on Cloudflare control plane and analytics outage* (2023): <https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/>
- Microsoft, *Helping our customers through the CrowdStrike outage* (2024): <https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/>
- CrowdStrike, *Channel File 291 Incident Root Cause Analysis* (2024): <https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/>
- U.S. GAO, *SolarWinds Cyberattack Demands Significant Federal and Private-Sector Response*, GAO-21-594T: <https://www.gao.gov/products/gao-21-594t>
- Financial Stability Board, *Third-party dependencies in cloud services* (2019): <https://www.fsb.org/2019/12/third-party-dependencies-in-cloud-services-considerations-on-financial-stability-implications/>
- NIST SP 800-160 Vol. 2 Rev. 1, *Developing Cyber-Resilient Systems*: <https://doi.org/10.6028/NIST.SP.800-160v2r1>

### Open-source afhankelijkheden

- Zimmermann et al., *Small World with High Risks: A Study of Security Threats in the npm Ecosystem*, USENIX Security 2019: <https://www.usenix.org/conference/usenixsecurity19/presentation/zimmerman>
- Linux Foundation & Harvard LISH, *Census II of Free and Open Source Software*: <https://www.linuxfoundation.org/research/census-ii-of-free-and-open-source-software-application-libraries>
- CISA, *Apache Log4j Vulnerability Guidance*: <https://www.cisa.gov/news-events/news/apache-log4j-vulnerability-guidance>
- Alami, Pardo & Linåker, *How do maintainers perceive the sustainability of open source software?*, Empirical Software Engineering 2024: <https://doi.org/10.1007/s10664-024-10529-6>

## 16. Lokale relaties

- `RESEARCH_PROTOCOL.md`
- `PROVISIONAL_PROBLEM_MAP.md`
- `PROBLEM_DOSSIER_001_POWER_CONCENTRATION.md`
- `PROBLEM_DOSSIER_002_EFFECTIVE_EXIT.md`
- `PROBLEM_DOSSIER_005_KNOWLEDGE_COMMONS_SYNTHETIC_INTEGRITY.md`

## 17. Versiegeschiedenis

| Versie | Datum | Wijziging |
|---|---|---|
| 0.2 | 2026-08-08 | Geplande exit van storingsuitwijking gescheiden, 9B als één meefalende incidentbeheersingskern verduidelijkt en 9C als research risk/HOLD geclassificeerd. |
| 0.1 | 2026-08-08 | Eerste inhoudelijke beoordeling; twee actieve kandidaten, één opkomende subkandidaat, tegenbewijs en falsificatievoorwaarden vastgelegd. |

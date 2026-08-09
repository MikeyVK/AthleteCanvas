# Bewijsgetrouwe audit van het teruggevonden Ypsia-onderzoek

**Auditdatum:** 2026-08-06  
**Scope:** lokale artefacten; geen nieuw webonderzoek en geen inhoudelijke verificatie van externe URL's  
**Doel:** vaststellen welke onderzoeksinhoud exact is teruggevonden, welke probleemkandidaten en claims in de bestanden staan, hoe de genummerde verwijzingen zijn gebruikt, welke bewijszwakten al uit de lokale set blijken en wat niet als exact herstel mag worden gepresenteerd.

## 0. Onderzochte bestanden en auditlabels

Deze audit leest de volgende drie bestanden als één bewijsset:

1. [`../00_teruggevonden_exact/Kritiek_op_het_huidige_internet_tekstextractie.txt`](../00_teruggevonden_exact/Kritiek_op_het_huidige_internet_tekstextractie.txt);
2. [`../00_teruggevonden_exact/BRONNENREGISTER.md`](../00_teruggevonden_exact/BRONNENREGISTER.md);
3. [`../00_teruggevonden_exact/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.1.md`](../00_teruggevonden_exact/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.1.md).

Waar nodig is uitsluitend voor integriteitscontrole ook de lokaal aanwezige PDF `Kritiek_op_het_huidige_internet.pdf` gelezen. De bronbestanden zijn niet gewijzigd.

De volgende labels worden hieronder gebruikt:

| Label | Betekenis in deze audit |
|---|---|
| **[AUD-E] exact lokaal bewijs** | De bewering kan rechtstreeks worden gecontroleerd in een ongewijzigd lokaal bestand of via een hash. |
| **[AUD-T] exacte tekst, onvolledige provenance** | De formulering staat exact in het huidige dossier, maar de oorspronkelijke onderzoeksactiviteit of bewaarde conversatie waaruit zij afkomstig zou zijn, is niet in deze bewijsset aanwezig. |
| **[AUD-I] audit-inferentie** | Dit is een voorzichtige gevolgtrekking uit structuur, citatiepatroon, titel, domein of interne tegenspraak; geen extern geverifieerde inhoudelijke conclusie. |
| **[AUD-O] open / niet verifieerbaar** | De lokale set bevat onvoldoende materiaal om de claim, broninhoud of herkomst zelfstandig te controleren. |

De labels van het ruwe dossier (`A` tot en met `D`) worden niet stilzwijgend gelijkgesteld aan deze auditlabels. Een tekst kan bijvoorbeeld exact als passage in DOS-001 staan, terwijl de daarin genoemde oorspronkelijke onderzoeksronde niet exact is teruggevonden.

## 1. Hoofdconclusie

1. **[AUD-E] Het oorspronkelijke PDF-artefact is als bytes exact aanwezig.** Het bestand telt twintig pagina's en heeft SHA-256 `be96a1803d17bc4cec4f7d7b2181d642e0af337230601a00c4324662e7e84162`. Deze hash komt overeen met zowel het Bronnenregister als DOS-001.
2. **[AUD-E] De tekstextractie is exact reproduceerbaar uit de aanwezige PDF.** Een lokale uitvoering van `pdftotext -layout` op de PDF leverde byte voor byte dezelfde tekst op, met SHA-256 `196ba0ac53d17c9b895d3cd785633beef1632a42abe7eeb17537ab12124b407c`.
3. **[AUD-I] De PDF kan daarom exact als het nu teruggevonden onderzoeksartefact worden aangeduid, maar niet zonder aanvullend extern ijkpunt als bewezen identiek aan iedere eerdere of oorspronkelijke versie.** Er is geen oudere, onafhankelijk vastgelegde hash of provenance-log in deze bewijsset.
4. **[AUD-E] De oorspronkelijke bibliografie telt 79 genummerde vermeldingen.** In de hoofdtekst worden 43 verschillende nummers zichtbaar gebruikt; 36 nummers staan wel in de literatuurlijst maar zijn niet als citatiemarker in de hoofdtekst aangetroffen.
5. **[AUD-I] De audit beoordeelt het oorspronkelijke dossier als inhoudelijk asymmetrisch.** Pagina's 1–8 behandelen vooral diagnose; vanaf digitale soevereiniteit verschuift het zwaartepunt naar beleids-, organisatie- en architectuuroplossingen. De structurele observatie is controleerbaar, maar de functie-indeling blijft een audit-inferentie. Dit maakt het dossier een rijke hypothesekaart, maar niet vanzelf een categorisch volledige probleeminventaris.
6. **[AUD-E/AUD-T] DOS-001 bewaart een omvangrijke en bruikbare samenvatting van de aanvullende ronde, inclusief twintig expliciete nieuwe kandidaat-problemen, vijf verdiepende thema's, drie claimcorrecties en negen aanvullende bronverwijzingen.** De tekst hiervan is exact aanwezig, maar de zoekopdrachten, bronnotities, tussenredeneringen, tegenargumenten en volledige gespreksinhoud waaruit dit zou zijn afgeleid, zijn niet lokaal geborgd.
7. **[AUD-E] DOS-001 is dus geen volledig ruw onderzoeksarchief.** Het document vermeldt dit zelf uitdrukkelijk in de status, doelomschrijving en sectie 11. Het is een overdrachtsdossier en integriteitswaarschuwing, geen reproduceerbaar onderzoekslogboek.

## 2. Artefactintegriteit en exacte herstelstatus

| Artefact | Lokale controle | Wat exact kan worden gezegd | Wat niet exact kan worden gezegd |
|---|---|---|---|
| PDF, 579.240 bytes, 20 pagina's | SHA-256 komt overeen met register en DOS-001 | De nu aanwezige PDF is ongewijzigd en identificeerbaar als één exact artefact. | Zonder eerder extern manifest kan niet worden bewezen dat dit de enige of allereerste oorspronkelijke versie was. |
| Tekstextractie, 54.096 bytes | SHA-256 klopt; identiek aan nieuwe `pdftotext -layout`-uitvoer | Dit is een exact reproduceerbare afgeleide tekstweergave van de aanwezige PDF. | Het is geen semantisch foutloze transcriptie: tabellen, kophiërarchie, URL-regelafbrekingen, superscriptstatus en paginaovergangen zijn platgeslagen. |
| Bibliografie 1–79 | Volledig aanwezig in PDF en extractie | Nummer, titeltekst en weergegeven locator zijn behouden zoals door de PDF-extractor gelezen. | De externe publicaties zelf zijn niet lokaal bewaard; bereikbaarheid, versie, auteurschap en precieze inhoud zijn niet vanuit deze set controleerbaar. |
| `BRONNENREGISTER.md` | Exact huidig Markdown-bestand; bevat hashes van PDF en extractie | De lokale bronnen en negen later geregistreerde online vindplaatsen zijn als huidige registertekst teruggevonden. | Het register bewijst niet dat de negen online bronnen daadwerkelijk volledig zijn gelezen; het bevat geen download, snapshot, citaat, pagina of leesnotitie. |
| DOS-001 v0.1 | Exact huidig Markdown-bestand | De huidige samenvattingen, correcties, kandidaten en bewaargaten zijn woordelijk beschikbaar. | Hun kwalificatie als `B — Letterlijk teruggevonden` kan niet per passage onafhankelijk worden geaudit, omdat het onderliggende gesprek/projectdocument niet in deze drie-bestandenset zit. |

### Belangrijke nuance over de tekstextractie

**[AUD-E]** De extractie is technisch exact als uitvoer van `pdftotext -layout`, maar bevat onder meer form-feedtekens, door regelafbreking gesplitste URL's en een visueel gereconstrueerde tabel. Een later systeem moet daarom de PDF als primaire lokale bron blijven behandelen en de tekstextractie als zoekindex. Het woord “exact” mag hier niet worden gelezen als “editorieel perfecte platte tekst”.

## 3. Documentstructuur van het oorspronkelijke dossier

Onderstaande hiërarchie is rechtstreeks uit de PDF/extractie afgeleid. Paginanummers verwijzen naar de PDF; de functieomschrijving is een audit-inferentie.

| Niveau | Titel zoals teruggevonden | Pagina | Functie |
|---|---|---:|---|
| Titel | **Het Kantelpunt van het Internet: Een Diepgaande Analyse van Soevereiniteit, Privacy en Eigenaarschap in het Tijdperk van AI** | 1 | Kader en hoofdthese |
| Hoofddeel | **De Pathologie van het Huidige Internet: Datamonopolies en Waarde-extractie** | 1 | Politiek-economische diagnose |
| Subdeel | **Bewakingskapitalisme en Techno-feodalisme** | 1–2 | Data-extractie, gedragssturing en machtsasymmetrie |
| Subdeel | **Erosie van Contextuele Integriteit** | 2 | Privacy, contextverlies en autonomie |
| Subdeel | **Platformverval en de 'Enshittification'-Cyclus** | 2–3 | Lock-in en verschuivende waarde-extractie |
| Hoofddeel | **De Ontwrichting door Generatieve AI: Van Curatie naar Synthese** | 3 | AI als versterker van bestaande problemen |
| Subdeel | **Generative Engine Optimization (GEO) en het Nul-Klik Internet** | 3–4 | Bronverkeer, uitgeverseconomie en enclosure |
| Subdeel | **Model Collapse en de Gevolgen van Recursieve Synthese** | 5 | Synthetische trainingsdata en informatiedegradatie |
| Subdeel | **De 'Dead Internet Theory' als Realiteit** | 5–6 | Bots, synthetische ruis en epistemisch vertrouwen |
| Hoofddeel | **Privacy en Eigenaarschap in de AI-Cyclus: Een Juridische en Technische Impasse** | 6 | AVG, wissing en modeltraining |
| Subdeel | **De Limieten van 'Machine Unlearning'** | 6–7 | Technische beperkingen van verwijdering |
| Subdeel | **Regelgevend Antwoord: De EDPB-Richtlijnen en Algoritmische Destructie** | 7–8 | Juridische duiding en zeer stellige gevolgtrekking |
| Hoofddeel | **De Herovering: Digitale Soevereiniteit als Geopolitieke en Maatschappelijke Noodzaak** | 8–9 | Overgang van diagnose naar oplossingsrichting |
| Subdeel | **De Europese Investering: EDIC Digital Commons** | 9–10 | Institutionele en publieke infrastructuur |
| Subdeel | **Waardengedreven Digitaliseren en 'MijnBureau' (Nederland)** | 10 | Nationaal beleids- en implementatievoorbeeld |
| Hoofddeel | **De Architectuur van Eigenaarschap: De 'Public Stack' en Decentrale Protocollen** | 10–11 | Architectonisch antwoord |
| Subdeel | **Datasoevereiniteit via de Datakluis: Solid** | 10–11 | Data-applicatiescheiding en datakluizen |
| Subdeel | **Sociale Decentralisatie: Fediverse, AT Protocol en Matrix** | 11–13 | Protocolvergelijking |
| Subdeel | **Voorbij Techniek: Data als Arbeid** | 13–14 | Coöperatieve/economische machtscorrectie |
| Hoofddeel | **Conclusie: Een Nieuw Digitaal Sociaal Contract** | 14–15 | Synthese en normatieve oproep |
| Bijlage | **Geciteerd werk** | 15–20 | 79 genummerde vermeldingen |

## 4. Alle identificeerbare probleemkandidaten uit het oorspronkelijke dossier

De codes `ORIG-xx` zijn uitsluitend auditcodes en **geen** voorstellen voor permanente constitutionele `P`-nummers. “Expliciet” betekent dat het dossier het verschijnsel zelf als schade, crisis, impasse of kwetsbaarheid beschrijft. “Impliciet” betekent dat het probleem vooral uit een voorgestelde oplossing of randopmerking moet worden afgeleid.

### 4.1 Politieke economie, macht en autonomie

| Auditcode | Probleemkandidaat | Vindplaats | Genummerde verwijzingen in de betreffende passage | Status |
|---|---|---|---|---|
| ORIG-01 | Hypercommercialisering en concentratie van datastromen, identiteit en digitale publieke ruimte bij enkele multinationals | p.1, inleiding | 1 | Expliciet [AUD-E] |
| ORIG-02 | Bewakingskapitalistische extractie van menselijke ervaring, gedrag en metadata | p.1–2 | 5, 6, 8 | Expliciet [AUD-E] |
| ORIG-03 | Onteigening van gebruikersrechten via complexe/onleesbare voorwaarden | p.2 | 7 aan het einde van het vierstadia-argument | Expliciet [AUD-E] |
| ORIG-04 | Gedragsmodificatie en aantasting van keuzevrijheid door voorspellende en sturende systemen | p.2 | 7; later 5 | Expliciet [AUD-E] |
| ORIG-05 | Private epistemische macht: bedrijven bepalen toegang tot kennis zonder publieke controle | p.2 | 7 | Expliciet [AUD-E] |
| ORIG-06 | Techno-feodale data- en waardepacht; gebruikers leveren digitale arbeid zonder gelijkwaardige macht | p.2 en p.13–14 | 10; later 78 | Expliciet [AUD-E] |
| ORIG-07 | Lock-in, ontbrekende interoperabiliteit en kunstmatig hoge overstapkosten | p.2–3 | 15 en 2; de slotclaim op p.2 na 10 is niet apart geciteerd | Expliciet [AUD-E] |
| ORIG-08 | Schending van contextuele integriteit door cross-contextaggregatie en schaduwprofielen | p.2 | 12 | Expliciet [AUD-E] |
| ORIG-09 | Platformverval: waarde verschuift van gebruikers naar adverteerders en uiteindelijk aandeelhouders | p.2–3 | 15 | Expliciet [AUD-E] |
| ORIG-10 | Degradatie van gebruikerservaring en verlies van dataportabiliteit binnen maatschappelijk onmisbare platforms | p.3 | 2 | Expliciet [AUD-E] |

### 4.2 Kennis, open web en generatieve AI

| Auditcode | Probleemkandidaat | Vindplaats | Verwijzingen | Status |
|---|---|---|---|---|
| ORIG-11 | Verschuiving van verwijzende curatie naar platformgebonden synthese van antwoorden | p.3 | 5, 17 | Expliciet [AUD-E] |
| ORIG-12 | Nul-klikbemiddeling: afnemende noodzaak om originele bronnen te bezoeken | p.3–4 | 17, 21 | Expliciet [AUD-E]; statistiek later gecorrigeerd in DOS-001 |
| ORIG-13 | Verdamping van bereik en verdienmodellen van makers, nieuwsmedia en onafhankelijke onderzoekers | p.4 | 17, 21; sterke causale slotclaims zonder afzonderlijke primaire bron | Expliciet [AUD-E] |
| ORIG-14 | Digitale enclosure: blokkeren van crawlers en verplaatsing van informatie achter betaalmuren | p.4 | 23 | Expliciet [AUD-E] |
| ORIG-15 | Toenemende inzet van synthetische trainingsdata wegens vermeende uitputting van menselijke data | p.5 | 24 | Expliciet [AUD-E] |
| ORIG-16 | Model collapse door indiscriminerende recursieve training | p.5 | 26, 27 | Expliciet [AUD-E]; onvermijdelijkheid later gecorrigeerd |
| ORIG-17 | Verlies van statistische “tails”, nuances, uitzonderingen en minderheidskennis | p.5 | 27 | Expliciet [AUD-E] |
| ORIG-18 | Cascaderende prestatie- en betekenisdegradatie bij verdere recursie | p.5 | 27, 31 | Expliciet [AUD-E] |
| ORIG-19 | Overvloed aan bots en synthetische ruis waardoor menselijke/authentieke signalen moeilijk herkenbaar worden | p.5–6 | 32, 33 | Expliciet [AUD-E] |
| ORIG-20 | Crisis van perceptie, verificatie en sociaal vertrouwen; desintegratie van gedeelde epistemologie | p.6 | 32 | Expliciet [AUD-E] |

### 4.3 Privacy, recht en gegevenscontrole

| Auditcode | Probleemkandidaat | Vindplaats | Verwijzingen | Status |
|---|---|---|---|---|
| ORIG-21 | Spanning tussen grootschalige AI-training en dataminimalisatie, doelbinding en gegevenswissing | p.6 | 38 | Expliciet [AUD-E]; juridische absoluutheid later gecorrigeerd |
| ORIG-22 | Moeilijkheid om individuele informatie/invloed in modelgewichten te lokaliseren, verwijderen en aantoonbaar te verifiëren | p.6–7 | 38, 42 | Expliciet [AUD-E] |
| ORIG-23 | Onmogelijke of moeilijk verenigbare doelen van unlearning: vergeten, modelnut en rekenefficiëntie | p.7 | 40 | Expliciet [AUD-E], maar zwak bronanker |
| ORIG-24 | Restinformatie en reconstructierisico via membership-inferenceaanvallen | p.7 | 38 | Expliciet [AUD-E] |
| ORIG-25 | Function creep: een getraind systeem krijgt later een ander doel | p.7 | 44 | Expliciet [AUD-E] |
| ORIG-26 | “Gecontamineerde modellen” en de stelling dat onrechtmatige brondata het hele productieve model onrechtmatig maakt | p.7–8 | 44 en 38 | Expliciet [AUD-E]; DOS-001 verwerpt de absolute formulering |

### 4.4 Soevereiniteit, infrastructuur en institutionele afhankelijkheid

| Auditcode | Probleemkandidaat | Vindplaats | Verwijzingen | Status |
|---|---|---|---|---|
| ORIG-27 | Geopolitieke en operationele afhankelijkheid van niet-Europese techmonopolies, cloud, chips en leveranciers | p.8–9 | 45, 46, 48 | Expliciet [AUD-E] |
| ORIG-28 | Onderfinanciering en onderhoudsafhankelijkheid van open-source basisinfrastructuur | p.9–10 | 55 | Expliciet [AUD-E] |
| ORIG-29 | Overheidsafhankelijkheid van gesloten samenwerkingsplatforms, met kwetsbaarheid en problemen voor archivering/Woo | p.10 | 4 | Expliciet [AUD-E] |
| ORIG-30 | Verstrengeling van data, identiteit en applicatie in gesloten datasilo's | p.10–11 | 64 en 65 dragen vooral het voorgestelde antwoord; de probleemzin zelf heeft geen eigen marker | Expliciet [AUD-E], bewijs indirect |
| ORIG-31 | Schaalbaarheids-, complexiteits-, authenticatie- en adoptieproblemen van een decentrale datakluisarchitectuur | p.11 | 65 | Expliciet als beperking van oplossing [AUD-E] |
| ORIG-32 | Gebrek aan economische prikkel voor bedrijven om naar gebruikerscontrole te migreren | p.11 | 65 | Expliciet als adoptiebarrière [AUD-E] |
| ORIG-33 | Ongecompenseerde data-arbeid en zwakke collectieve onderhandelingsmacht tegenover AI-ontwikkelaars/datamonopsonies | p.13–14 | 78 | Expliciet [AUD-E] |
| ORIG-34 | Substantiële economische en ecologische kosten van volledige hertraining van modellen | p.6 | 38 | Alleen kort genoemd; impliciete probleemkandidaat [AUD-E/AUD-I] |

### 4.5 Wat het oorspronkelijke dossier niet systematisch als probleem onderzoekt

**[AUD-I]** De volgende onderwerpen komen niet als zelfstandig uitgewerkt probleemveld naar voren, ook al raken losse zinnen eraan: procedurele rechtsbescherming, algoritmische ongelijkheid, digitale uitsluiting, kinderen, synthetische intimiteit, arbeidsmanagement, e-waste, water- en materiaalgebruik, rebound, herstelvermogen, gecorreleerd falen, belangen van toekomstige generaties en gedwongen digitalisering door de staat. Dat oordeel sluit aan bij DOS-001, maar is hier ook rechtstreeks controleerbaar aan de structuur van de oorspronkelijke tekst.

## 5. Alle expliciete probleemkandidaten uit DOS-001

De formuleringen hieronder zijn **[AUD-T] exact als huidige dossierinhoud**. Hun status als letterlijk teruggevonden resultaat van een eerdere onderzoeksronde is zonder onderliggende conversatie/bronnotities niet onafhankelijk te bevestigen.

### 5.1 Nieuwe kandidaten per lacunelens

| Domein | Kandidaat zoals vastgelegd | Geborgde bron-ID's in DOS-001 | Lokale bewijsstatus |
|---|---|---|---|
| Mens en cognitie | Cognitieve uitbesteding en vaardigheidsverlies | SRC-105 | Alleen URL/DOI en samenvatting; geen lokale publicatie of paginotitie |
| Mens en cognitie | Verdringing van zelfstandig oordeel door AI-autoriteit | Geen afzonderlijke bron toegewezen | Open |
| Mens en cognitie | Exploitatie van de ontwikkelingsasymmetrie van kinderen | SRC-106 | Alleen URL en samenvatting |
| Mens en cognitie | Synthetische intimiteit en afhankelijkheid | Geen voldoende bron; dossier vraagt herverificatie | Open |
| Mens en cognitie | Homogenisering van menselijke creatie en collectieve denkkracht | Geen voldoende bron; dossier vraagt herverificatie | Open |
| Democratie/recht | Digitale macht zonder procedurele rechtsbescherming | SRC-104 | Eén kaderverdrag als brede institutionele basis; geen claimnotitie |
| Democratie/recht | Algoritmische reproductie van ongelijkheid | SRC-104 | Idem; tweede onafhankelijke bron ontbreekt |
| Democratie/recht | Digitale uitsluiting van rechten en deelname | SRC-104 | Idem; causale afbakening ontbreekt |
| Democratie/recht | Algoritmische onderwerping van arbeid | SRC-104 | Idem; specifieke arbeidsbron ontbreekt |
| Democratie/recht | Grensoverschrijdende macht zonder gelijkwaardige democratische orde | SRC-104 | Idem; specifieke machtsanalyse ontbreekt |
| Ecologie/toekomst | Ontkende fysieke materialiteit van het digitale systeem | SRC-107, SRC-108 | Twee brede officiële/synthesebronnen geregistreerd; geen lokale kopieën |
| Ecologie/toekomst | Extractieve hardwareketens | SRC-108 slechts gedeeltelijk relevant volgens dossier | Specifieke bron voor sociale/ecologische ketenclaim ontbreekt |
| Ecologie/toekomst | E-waste en korte levenscycli | SRC-108 | Eén dataset/monitor geregistreerd |
| Ecologie/toekomst | Rebound | Geen specifieke bron toegewezen | Open |
| Ecologie/toekomst | Geografische en sociale afwenteling | SRC-107/108 slechts breed | Claimgerichte bron ontbreekt |
| Ecologie/toekomst | Intergenerationele vastlegging | Geen specifieke empirische/normatieve bron toegewezen | Open |
| Technische weerbaarheid | Kwetsbare digitale afhankelijkheden | SRC-109 | Eén beleidsanalyse geregistreerd |
| Technische weerbaarheid | Ketenaanvallen en gecorreleerd falen | SRC-109 | Tweede onafhankelijke bron en afbakening ontbreken |
| Technische weerbaarheid | Centrale uitvalspunten | SRC-109 | Idem |
| Technische weerbaarheid | Ontbrekend herstel- en continuïteitsvermogen | SRC-109 | Idem |

### 5.2 Als verdieping, mechanisme of gevolg vastgelegde thema's

DOS-001 classificeert de volgende vijf onderwerpen voorlopig niet als nieuwe hoofdcategorie, maar als verdieping van bestaande kritiek:

1. aandachtsexploitatie;
2. recommender systems;
3. desinformatie;
4. bronverlies;
5. synthetische ruis.

**[AUD-T]** Het dossier houdt expliciet open dat consolidatie alsnog kan aantonen dat een onderwerp een zelfstandig machtsmechanisme of unieke fundamentele schade bevat.

### 5.3 Voorlopige probleemtopologie

DOS-001 noemt acht consolidatiedomeinen, uitdrukkelijk zonder permanente `P`-nummers:

1. digitale macht en politieke economie;
2. menselijke autonomie, cognitie en ontwikkeling;
3. kennis en informatie-integriteit;
4. democratie, procedurele rechtsbescherming en gelijkheid;
5. arbeid, verdeling en institutionele afhankelijkheid;
6. materiële en ecologische gevolgen;
7. technische weerbaarheid en structurele afhankelijkheid;
8. toekomstige generaties en belangen zonder stem.

De verwachting van “ongeveer tien tot vijftien probleemfamilies” wordt in DOS-001 zelf correct aangeduid als werkhypothese en niet als onderzoeksuitkomst.

## 6. Claim–referentiekaart van de oorspronkelijke hoofdtekst

Deze tabel inventariseert alle inhoudelijke citatieclusters in de hoofdtekst. De marker is het nummer dat letterlijk achter een woord of zin staat; de audit bevestigt niet dat de externe bron de hele claim werkelijk draagt.

| Sectie / claimcluster | Gebruikte nummers | Interne auditbevinding |
|---|---:|---|
| Internet veranderde van decentraal/publiek naar hypergecommercialiseerd en gemonopoliseerd | 1 | Eén normatief Waag-rapport draagt meerdere brede historische en empirische claims. |
| Generatieve AI vergroot centralisatie, extractie en autonomieverlies | 5 | Fast Company-opiniestuk/essay volgens titel; zwak als enige basis voor systeemclaim. |
| Definitie bewakingskapitalisme en menselijke ervaring als grondstof | 5, 6 | 6 is een HBS-pagina over Zuboffs boek, niet zichtbaar het boek zelf. |
| Extractie van interacties/metadata zonder democratische controle | 8 | ResearchGate-vermelding; lokale set bevat geen publicatie of kwaliteitsmetadata. |
| Vier stadia van extractie, onteigening, gedragsmodificatie en epistemische coup | 7 | Eén marker aan einde van een uitgebreide reconstructie; onduidelijk welke deelclaims letterlijk uit bron 7 komen. |
| Techno-feodalisme, digitale horigen en data als pacht | 10 | Academische PDF-locator; marktcorrectie- en uitstapclaim erna heeft geen eigen bron. |
| Contextuele integriteit | 12 | Sterke conceptuele bronvermelding; toepassing op holistische schaduwprofielen wordt met dezelfde marker gedragen. |
| Contextverlies als aanval op autonomie | 5 | Secundair essay in plaats van directe empirische onderbouwing. |
| Enshittification als structureel en “onvermijdelijk” mechanisme | 15 | Bron 15 is een Reddit-discussie en geen primaire Doctorow-bron; “onvermijdelijk” is een sterke universele claim. |
| Cyclus van waardeverschuiving; dataportabiliteit en onontkoombare afhankelijkheid | 15, 2 | Bron 2 is journalistiek interview; 15 blijft Reddit. |
| Van “surveillance capitalism which curates” naar “which creates” | 5 | Passende herkomst voor geciteerd perspectief mogelijk, maar geen onafhankelijke systeemtoets. |
| Traditionele zoekarchitectuur, RAG/answer engines en nul-klikmechanisme | 17 | Eén ResearchGate-item draagt definities, techniek, gedrag en economie. |
| 58% AI-samenvattingen, 80% zero-click, 15–25% verkeersdaling | 21 | Bron 21 is volgens bibliografie een marketingblog met “98+ statistics”; tabel noemt daarbinnen Pew en Bain zonder die primaire stukken apart te registreren. DOS-001 corrigeert de 58%-interpretatie. |
| Voorspelde daling traditioneel zoekverkeer met 25% richting 2026 | 17 | De tabel noemt Gartner, maar marker 17 verwijst niet naar een Gartner-publicatie. Dit is citation substitution. |
| GEO-transitie en structurering voor LLM-citatie | 17, 18 | 18 is een Jasper.ai-gids; commerciële context. |
| Crawlerblokkades en informatie achter paywalls | 23 | Bron 23 is een commerciële GEO-gids; causale en empirische dekking onzeker. |
| Menselijke data raakt “uitgeput”; noodgedwongen synthetische training | 24 | Bron 24 blijkt uit titel/URL een arXiv-item; formulering is zeer stellig. |
| Nature-studie zou model collapse “aantonen” | 26 | Bron 26 is juist “A Note on Shumailov et al.”; de originele Nature/PubMed-vermelding 30 staat in bibliografie maar wordt niet geciteerd. |
| Twee fasen en onomkeerbare degeneratie van model collapse | 27 | ResearchGate-kopie van de studie; DOS-001 nuanceert onvermijdelijkheid en mitigatie door originele menselijke data. |
| Handgeschreven-cijferexperiment en maatschappelijke extrapolatie | 31 | Bron 31 is een Transparency Coalition-artikel, niet de genoemde oorspronkelijke New York Times-publicatie. Medische/historische extrapolatie is niet afzonderlijk onderbouwd. |
| Dead Internet als plausibele, academisch hergeformuleerde realiteit | 32 | Eén OCAD-openresearchdocument; dossier gebruikt zeer stellige taal. |
| AI-slop maakt authentieke menselijke signalen onherkenbaar | 33 | Bron 33 is een Hacker News-item over een door agents gebouwde C-compiler en is op titel evident niet passend. |
| Crisis van perceptie en desintegratie van gedeelde epistemologie | 32 | Normatief/diagnostisch argument, geen brede empirische bewijsbasis zichtbaar. |
| AVG-beginselen, recht op wissing en technische tegenstelling met LLM's | 38 | Bron 38 is een TechPolicy.Press-essay, niet de AVG of officiële toezichttekst. |
| Informatie diffuus in parameters; alleen volledige hertraining garandeert wissing | 38 | Zeer absolute technische claim; door DOS-001 expliciet gecorrigeerd als te stellig. |
| Machine unlearning als discipline en benaderende verwijdering | 38, 42 | 42 is een specifieke arXiv-preprint over pruning/sparse models; generaliseerbaarheid niet lokaal toetsbaar. |
| “Onmogelijke driehoek” van vergeten, nut en efficiëntie | 40 | Bron 40 is een trainings/lesplanwebsite, geen primaire technische studie. |
| MIA kan verwijderde kennis vaak reconstrueren; unlearning is riskante AVG-strategie | 38 | Technische en juridische claims steunen op hetzelfde opiniestuk. |
| EDPB Opinion 28/2024 en stringente belangenafweging/function creep | 44 | Bron 44 is een consultancy-uitleg; de officiële EDPB-bron staat niet als nummer in deze passage. |
| Hoge anonimiseringsdrempel en uitoefening rechten | 39, 44 | 39 is CNIL en institutioneler; precieze claimdekking kan zonder bronkopie niet worden vastgesteld. |
| Gecontamineerd model en volledige algoritmische destructie | 38, 44 | DOS-001 corrigeert deze gevolgtrekking aan de hand van later geregistreerde officiële EDPB-bron SRC-103. |
| Definitie en gelaagdheid van digitale soevereiniteit | 45 | Peer-reviewed ogende Taylor & Francis-locator; lokale inhoud ontbreekt. |
| Technologische soevereiniteit/EU-afhankelijkheid | 46 | Officiële EPRS-briefing. |
| Afbakening digitale, technologische en datasoevereiniteit | 48 | Academische/conferentiepublicatie via International Data Spaces. |
| EU-kwetsbaarheid door cloud, ransomware en desinformatie | 46 | Eén brede beleidsbriefing voor uiteenlopende oorzaken. |
| Oprichting, deelnemers en rol DC-EDIC | 52, 53 | Officiële EU- en nationale digitale-overheidslocators; precieze datering niet lokaal geverifieerd. |
| Onderfinanciering open source en veiligheidsrisico | 55 | OpenSourceWerken-bijlage; broninhoud niet lokaal. |
| STF en “100-Day Challenges” | 54 | Open Future Foundation, geen officiële programmadocumentatie in lokale set. |
| Nederlandse Werkagenda en publieke waarden | 58, 60 | Overheidsvindplaatsen; relatief sterke bronklasse. |
| MijnBureau, afhankelijkheid en Woo-problemen | 4 | Eén ODI-nieuwsbericht draagt veel product- en beleidsclaims. |
| Public Stack-lagen en publieke waarden | 3 | Eigen project-/organisatiebeschrijving, geschikt voor zelfdefinitie maar niet voor aangetoonde effectiviteit. |
| Solid-oorsprong en architectuur | 64, 65 | 64 is Inrupt (belanghebbende leverancier); 65 is een technische publicatie. |
| Vlaamse use-cases en “grootschalige, toekomstbestendige” infrastructuur | 68 | Inrupt-case study, dus belanghebbende vendorbron; bronnen 69/70 zijn wel geregistreerd maar niet gebruikt. |
| ActivityPub-standaard, netwerk en governance | 72, 73, 74 | Mix van academisch governanceartikel, white paper en gespecialiseerde blog. |
| AT Protocol: draagbaarheid en algoritmische keuze | 74 | Alleen Fediverse Report-artikel als marker; claims over volledige scheiding en switchbaarheid zijn sterke systeemclaims. |
| Matrix: state sync, E2EE en overheidsadoptie | 77 | Bron 77 is een persoonlijke protocolvergelijkingsblog. |
| Data als arbeid, coöperaties en collectieve onderhandeling | 78 | AEA Papers and Proceedings-vermelding; relatief passende economische bron. |
| Conclusie herhaalt centrale claims | 5, 17, 27, 3, 65, 74, 38, 4 | De conclusie versterkt taal als “onherroepelijk”, “destructief”, “onomkeerbaar” zonder nieuw tegenbewijs of extra primaire bronnen. |

### 6.1 Gebruikte en ongebruikte nummers

**[AUD-E] Gebruikt in de hoofdtekst (43):** 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 17, 18, 21, 23, 24, 26, 27, 31, 32, 33, 38, 39, 40, 42, 44, 45, 46, 48, 52, 53, 54, 55, 58, 60, 64, 65, 68, 72, 73, 74, 77, 78.

**[AUD-E] Alleen in de bibliografie aangetroffen (36):** 9, 11, 13, 14, 16, 19, 20, 22, 25, 28, 29, 30, 34, 35, 36, 37, 41, 43, 47, 49, 50, 51, 56, 57, 59, 61, 62, 63, 66, 67, 69, 70, 71, 75, 76, 79.

Het tweede feit betekent niet dat deze bronnen tijdens het schrijven niet zijn bekeken; alleen dat in de geëxtraheerde hoofdtekst geen marker naar deze nummers staat.

## 7. Volledige bibliografie-inventaris 1–79

Onderstaande lijst is een **genormaliseerde transcriptie [AUD-E]** van *Geciteerd werk*: harde PDF-regelafbrekingen binnen titels en URL's zijn samengevoegd. Zij is geen externe verificatie. `Ja` in de laatste kolom betekent uitsluitend dat het nummer als marker in de geëxtraheerde hoofdtekst voorkomt.

| Nr. | Vermelding en locator zoals teruggevonden (regelafbrekingen genormaliseerd) | In hoofdtekst |
|---:|---|:---:|
| 1 | *Het internet is stuk* — `https://waag.org/sites/waag/files/2025-02/MarleenStikker-HetInternetIsStuk.pdf` | Ja |
| 2 | *Het internet is stuk, ziet Marleen Stikker: 'Je kunt niet meer uitloggen'* — Vrij Nederland — `https://www.vn.nl/het-internet-is-stuk-marleen-stikker` | Ja |
| 3 | *Public Stack: samen herbouwen we het internet* — PublicSpaces — `https://publicspaces.net/2020/12/16/public-stack/` | Ja |
| 4 | *Digitale soevereiniteit: 'Zonder keuzevrijheid ben je ontzettend kwetsbaar'* — Rijksorganisatie voor Ontwikkeling, Digitalisering en Innovatie — `https://www.rijksorganisatieodi.nl/actueel/nieuws/2026/06/23/digitale-soevereiniteit-zonder-keuzevrijheid-ben-je-ontzettend-kwetsbaar` | Ja |
| 5 | *POV: How generative AI is changing surveillance capitalism* — Fast Company — `https://www.fastcompany.com/90871955/how-generative-ai-is-changing-surveillance-capitalism` | Ja |
| 6 | *The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power* — Faculty & Research/HBS — `https://www.hbs.edu/faculty/Pages/item.aspx?num=56791` | Ja |
| 7 | *Shoshana Zuboff on the Undetectable, Indecipherable World of Surveillance Capitalism* — `https://www.cigionline.org/articles/shoshana-zuboff-undetectable-indecipherable-world-surveillance-capitalism/` | Ja |
| 8 | *Digital surveillance capitalism and cities: data, democracy and activism* — ResearchGate — `https://www.researchgate.net/publication/385789464_Digital_surveillance_capitalism_and_cities_data_democracy_and_activism` | Ja |
| 9 | *The Geopolitics of Surveillance Capitalism* — Harvard Kennedy School — `https://www.hks.harvard.edu/sites/default/files/2025-10/25_Kilic_Tech_Paper_0.pdf` | Nee |
| 10 | *FEUDALISM RELOADED?* — `https://rucforsk.ruc.dk/ws/files/111169403/Feudalism_Reloaded_Final.pdf` | Ja |
| 11 | *How are Varoufakis' “techno-feudal” platforms different in any way from supermarkets and malls?* — Reddit r/Marxism — `https://www.reddit.com/r/Marxism/comments/1qsbbjl/how_are_varoufakis_technofeudal_platforms/` | Nee |
| 12 | *101 PRIVACY AS CONTEXTUAL INTEGRITY Helen Nissenbaum — I. INTRODUCTION* — Applied Cryptography Group — `https://crypto.stanford.edu/portia/papers/RevnissenbaumDTP31.pdf` | Ja |
| 13 | *Technology as uncharted territory: Contextual integrity and the notion of AI as new ethical ground* — arXiv — `https://arxiv.org/pdf/2412.05130?` | Nee |
| 14 | *AI's Regulatory Challenge: Avoiding the Pitfalls of Past Mistakes* — `https://journals.library.columbia.edu/index.php/stlr/blog/view/583` | Nee |
| 15 | *Cory Doctorow explains the “enshitification” of internet platforms ...* — Reddit r/medicine — `https://www.reddit.com/r/medicine/comments/10hyf7m/cory_doctorow_explains_the_enshitification_of/` | Ja |
| 16 | *The Dual Decays of Enshittification* — TechPolicy.Press — `https://www.techpolicy.press/the-dual-decays-of-enshittification/` | Nee |
| 17 | *Generative Engine Optimization (GEO): The Mechanics, Strategy, and Economic Impact of the Post-Search Era* — ResearchGate — `https://www.researchgate.net/publication/398120277_Generative_Engine_Optimization_GEO_The_Mechanics_Strategy_and_Economic_Impact_of_the_Post-Search_Era` | Ja |
| 18 | *What is Generative Engine Optimization? GEO vs AEO vs SEO Guide 2026* — Jasper.ai — `https://www.jasper.ai/blog/geo-aeo` | Ja |
| 19 | *Generative Engine Optimization (GEO) explained* — Evergreen Media — `https://www.evergreen.media/en/guide/generative-engine-optimization/` | Nee |
| 20 | *What is Generative Engine Optimization (GEO) and how does it differ from SEO?* — Contentful — `https://www.contentful.com/blog/generative-engine-optimization-seo/` | Nee |
| 21 | *98+ Generative Engine Optimization (GEO) Statistics for 2026 [Expert Analysis]* — `https://marketingltb.com/blog/statistics/generative-engine-optimization-statistics/` | Ja |
| 22 | *[2509.08919] Generative Engine Optimization: How to Dominate AI Search* — arXiv — `https://arxiv.org/abs/2509.08919` | Nee |
| 23 | *Generative Engine Optimization (GEO): The 2026 Guide to AI Search Visibility* — LLMrefs — `https://llmrefs.com/generative-engine-optimization` | Ja |
| 24 | *1 Introduction* — arXiv — `https://arxiv.org/html/2503.03150v2` | Ja |
| 25 | *Position: Model Collapse Does Not Mean What You Think* — arXiv — `https://arxiv.org/pdf/2503.03150` | Nee |
| 26 | *[2410.12954] A Note on Shumailov et al. (2024): “AI Models Collapse When Trained on Recursively Generated Data”* — arXiv — `https://arxiv.org/abs/2410.12954` | Ja |
| 27 | *AI models collapse when trained on recursively generated data* — ResearchGate — `https://www.researchgate.net/publication/382526401_AI_models_collapse_when_trained_on_recursively_generated_data` | Ja |
| 28 | *Model collapse* — Wikipedia — `https://en.wikipedia.org/wiki/Model_collapse` | Nee |
| 29 | *Author Correction: AI models collapse when trained on recursively generated data* — ResearchGate — `https://www.researchgate.net/publication/390064111_Author_Correction_AI_models_collapse_when_trained_on_recursively_generated_data` | Nee |
| 30 | *AI models collapse when trained on recursively generated data* — PubMed — `https://pubmed.ncbi.nlm.nih.gov/39048682/` | Nee |
| 31 | *How AI systems trained on AI-generated data lead to erosion and collapse* — Transparency Coalition — `https://www.transparencycoalition.ai/news/this-is-how-ai-erosion-and-collapse` | Ja |
| 32 | *Between the Self and Signal: The Dead Internet & a Crisis of Perception* — OCAD Open Research — `https://openresearch.ocadu.ca/id/eprint/4676/1/Between%20the%20Self%20and%20Signal%20__%20The%20Dead%20Internet%20%26%20a%20Crisis%20of%20Perception.pdf` | Ja |
| 33 | *We tasked Opus 4.6 using agent teams to build a C Compiler* — Hacker News — `https://news.ycombinator.com/item?id=46903616` | Ja |
| 34 | *Digital Psychology: Introducing a Conceptual Impact Model and the Future of Work* — ResearchGate — `https://www.researchgate.net/publication/386006471_Digital_Psychology_Introducing_a_Conceptual_Impact_Model_and_the_Future_of_Work` | Nee |
| 35 | *The practical ethics of bias reduction in machine translation: why domain adaptation is better than data debiasing* — ResearchGate — `https://www.researchgate.net/publication/349849963_The_practical_ethics_of_bias_reduction_in_machine_translation_why_domain_adaptation_is_better_than_data_debiasing` | Nee |
| 36 | *Generative AI* — Wikipedia — `https://en.wikipedia.org/wiki/Generative_AI` | Nee |
| 37 | *Environmental Impacts of AI* — Oxford Academic — `https://academic.oup.com/edited-volume/63015/chapter/565953510?login=false` | Nee |
| 38 | *The Right to Be Forgotten Is Dead: Data Lives Forever in AI* — TechPolicy.Press — `https://www.techpolicy.press/the-right-to-be-forgotten-is-dead-data-lives-forever-in-ai/` | Ja |
| 39 | *Ensuring and facilitating the exercise of data subjects' rights* — CNIL — `https://www.cnil.fr/en/ensuring-and-facilitating-exercise-data-subjects-rights` | Ja |
| 40 | *Machine Unlearning and the Right to Erasure* — Transformational Leadership Training — `https://www.marvinuehara.com/ai-literacy-lesson-plans/ai-privacy-governance/machine-unlearning-and-the-right-to-erasure` | Ja |
| 41 | *AI-Complex Algorithms and effective Data Protection Supervision — Effective implementation of data subjects' rights* — EDPB — `https://www.edpb.europa.eu/system/files/2025-01/d2-ai-effective-implementation-of-data-subjects-rights_en.pdf` | Nee |
| 42 | *The Right to be Forgotten in Pruning: Unveil Machine Unlearning on Sparse Models* — arXiv — `https://arxiv.org/html/2507.18725v1` | Ja |
| 43 | *Supporting Trustworthy AI Through Machine Unlearning* — PMC/NIH — `https://pmc.ncbi.nlm.nih.gov/articles/PMC11390766/` | Nee |
| 44 | *EDPB Issues New Guidelines on AI Systems and Personal Data — Key Changes for EU Organisations* — Measured Collective — `https://measuredcollective.com/edpb-ai-models-personal-data-gdpr-guidance/` | Ja |
| 45 | *Attributes of Digital Sovereignty: A Conceptual Framework* — Taylor & Francis — `https://www.tandfonline.com/doi/full/10.1080/14650045.2025.2521548` | Ja |
| 46 | *Digital sovereignty for Europe* — European Parliament — `https://www.europarl.europa.eu/RegData/etudes/BRIE/2020/651992/EPRS_BRI(2020)651992_EN.pdf` | Ja |
| 47 | *Data sovereignty: A review* — `https://d-nb.info/1282975056/34` | Nee |
| 48 | *A Delimitation of Data Sovereignty from Digital and Technological Sovereignty* — International Data Spaces — `https://internationaldataspaces.org/wp-content/uploads/dlm_uploads/Hellmeier-et-al_A-Delimitation-of-Data-Sovereignty-from-Digital-and-Technological-Sovereignty_ECIS-2023.pdf` | Ja |
| 49 | *A Delimitation of Data Sovereignty from Digital and Technological Sovereignty* — ResearchGate — `https://www.researchgate.net/publication/370060138_A_Delimitation_of_Data_Sovereignty_from_Digital_and_Technological_Sovereignty` | Nee |
| 50 | *Will the real data sovereign please stand up? An EU policy response to sovereignty in data spaces* — WUR eDepot — `https://edepot.wur.nl/670804` | Nee |
| 51 | *Leveraging the Interplay of AI Act and DMA for Sovereign EU Defence Applications* — `https://eugovlab.com/leveraging-the-interplay-of-ai-act-and-dma-for-sovereign-eu-defence-applications/` | Nee |
| 52 | *European Digital Infrastructure Consortium — EDIC* — European Commission — `https://digital-strategy.ec.europa.eu/en/policies/edic` | Ja |
| 53 | *EC launches DC-EDIC to strengthen digital sovereignty* — NL Digital Government — `https://www.nldigitalgovernment.nl/news/ec-launches-dc-edic-to-strengthen-digital-sovereignty/` | Ja |
| 54 | *Public Digital Infrastructure* — Open Future Foundation — `https://openfuture.eu/our-work/public-digital-infrastructure/` | Ja |
| 55 | *Digital Commons European Digital Infrastructure Consortium* — Opensourcewerken — `https://opensourcewerken.nl/attachment/entity/ac99644d-ca8b-4e71-9a07-33b22d3fa6c4` | Ja |
| 56 | *Digital Commons EDIC* — `https://digital-commons-edic.eu/` | Nee |
| 57 | *What the launch of the Digital Commons EDIC means for Digital Europe Programme projects* — DEDEP.eu — `https://dedep.eu/news/what-launch-digital-commons-edic-means-digital-europe-programme-projects` | Nee |
| 58 | *Werkagenda Waardengedreven Digitaliseren* — Digitale Overheid — `https://www.digitaleoverheid.nl/document/werkagenda-waardengedreven-digitaliseren/` | Ja |
| 59 | *Werkagenda Waardengedreven digitaliseren* — Open Overheid — `https://www.open-overheid.nl/documenten/2023/03/31/werkagenda-waardengedreven-digitaliseren` | Nee |
| 60 | *Kamerstuk 26643, nr. 940* — Overheid.nl — `https://zoek.officielebekendmakingen.nl/kst-26643-940.html` | Ja |
| 61 | *De nieuwe Werkagenda Waardengedreven Digitaliseren* — NLdigital — `https://www.nldigital.nl/nieuws/de-nieuwe-werkagenda-waardengedreven-digitaliseren/` | Nee |
| 62 | *Aan Staatssecretaris van Koninkrijksrelaties en Digitalisering — Van Digitale Samenleving 2 — Verzending Kamerbrief en Werkagenda ...* — Tweede Kamer — `https://www.tweedekamer.nl/downloads/document?id=2022D45424` | Nee |
| 63 | *Public Stack: het alternatieve internet* — Waag Futurelab — `https://waag.org/nl/project/public-stack-het-alternatieve-internet/` | Nee |
| 64 | *About Solid Project — Tim Berners-Lee* — Inrupt — `https://www.inrupt.com/solid` | Ja |
| 65 | *Solid: A Platform for Decentralized Social Applications Based on Linked Data* — Essam Mansour — `http://emansour.com/research/lusail/solid_protocols.pdf` | Ja |
| 66 | *Exploring Decentralized Computing Using Solid and IPFS for Social Media Applications* — ScholarWorks@UARK — `https://scholarworks.uark.edu/cgi/viewcontent.cgi?article=1137&context=csceuht` | Nee |
| 67 | *Solid Pods: A Promising Approach to Enhance Users' Perception of Data Transparency and Control* — Oxford Academic — `https://academic.oup.com/iwc/advance-article/doi/10.1093/iwc/iwaf017/8110646` | Nee |
| 68 | *Flanders Government strengthens a trusted data economy with Inrupt's Enterprise Solid Server* — Inrupt — `https://www.inrupt.com/case-study/flanders-strengthens-trusted-data-economy` | Ja |
| 69 | *Vertrouwen by Design* — Vlaanderen.be — `https://www.vlaanderen.be/vertrouwen-by-design` | Nee |
| 70 | *Towards a Research Agenda for Personal Data Spaces: Synthesis of a Community Driven Process* — Biblio UGent — `https://backoffice.biblio.ugent.be/download/8765470/8765480` | Nee |
| 71 | *Making personal data Solid* — Trinity College Dublin dissertation — `https://publications.scss.tcd.ie/theses/diss/2022/TCD-SCSS-DISSERTATION-2022-043.pdf` | Nee |
| 72 | *Can This Platform Survive? Governance Challenges for the Fediverse* — International Journal of Communication — `https://ijoc.org/index.php/ijoc/article/viewFile/22254/4864` | Ja |
| 73 | *Open Risk White Paper — Connecting the Dots: Tensor Representations of ActivityPub Networks* — `https://www.openriskmanagement.com/post-media/2024/02/OpenRiskWP15_020224.pdf` | Ja |
| 74 | *A conceptual model of ATProto and ActivityPub* — The Fediverse Report — `https://fediversereport.com/a-conceptual-model-of-atproto-and-activitypub/` | Ja |
| 75 | *A Comparative Analysis of Decentralized Social Protocols* — Justin McAfee / 1kxnetwork / Medium — `https://medium.com/1kxnetwork/a-comparative-analysis-of-decentralized-social-protocols-84914d9fca83` | Nee |
| 76 | *An evidence-based and critical analysis of the Fediverse decentralization promises* — arXiv — `https://arxiv.org/html/2408.15383v1` | Nee |
| 77 | *Social media protocols comparison* — Paul Stephen Borile — `https://www.paulstephenborile.com/2024/11/social-media-protocols-comparison/` | Ja |
| 78 | *Should We Treat Data as Labor? Moving beyond “Free”* — IDEAS/RePEc — `https://ideas.repec.org/a/aea/apandp/v108y2018p38-42.html` | Ja |
| 79 | *A database of AI and algorithmic management in collective bargaining agreements* — UNI Europa — `https://www.uni-europa.org/news/a-database-of-ai-and-algorithmic-management-in-collective-bargaining-agreements/` | Nee |

### 7.1 Bibliografische integriteitswaarschuwingen

- **[AUD-E]** De geëxtraheerde PDF splitst meerdere URL's midden in woorden. De genormaliseerde links hierboven zijn audittranscripties; voor bewijsarchivering hoort iedere locator opnieuw tegen de PDF en de werkelijke bron te worden gecontroleerd.
- **[AUD-I]** Enkele titel/URL-combinaties suggereren dubbele representaties van dezelfde publicatie: 24/25; 27/30 en mogelijk 29; 48/49.
- **[AUD-E]** Referentie 33 is op titel evident inhoudelijk niet passend bij de claim over “AI slop”.
- **[AUD-E/AUD-I]** Primaire of institutionelere vermeldingen zijn geregeld ongebruikt terwijl secundaire varianten wel de claim dragen: 30 tegenover 26/27; 41 en 43 tegenover 38/40/44; 69/70 tegenover vendorbron 68; 76 tegenover blog 74/77.

## 8. Aanvullende bronnen SRC-101–SRC-109

Deze negen vermeldingen staan exact in `BRONNENREGISTER.md`. Alleen de locator en een korte gebruiksomschrijving zijn lokaal bewaard; er zijn geen lokale bronbestanden, citaten of paginanotities.

| ID | Bron en locator | Functie volgens register/DOS-001 | Exact herstelbare inhoud |
|---|---|---|---|
| SRC-101 | Nature, *AI models collapse when trained on recursively generated data* — `https://www.nature.com/articles/s41586-024-07566-y` | Nuanceert model collapse: specifieke condities, niet ieder model | Alleen bibliografische verwijzing en huidige samenvatting; niet de gelezen brontekst |
| SRC-102 | Pew Research Center, AI-samenvattingen en doorklikgedrag — `https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/` | Corrigeert 58%; noemt 18% zoekopdrachten en daling 15% naar 8% | Cijfers exact als DOS-001-tekst, maar geen lokaal rapport/snapshot |
| SRC-103 | EDPB, AI-modellen en AVG — `https://www.edpb.europa.eu/news/edpb-opinion-on-ai-models-gdpr-principles-support-responsible-ai_en` | Corrigeert absolute verwijderings-/destructieclaim; casuïstische beoordeling | Alleen samenvatting en URL |
| SRC-104 | Raad van Europa, Framework Convention on AI — `https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence` | Brede basis voor mensenrechten, gelijkheid, transparantie, toezicht en betwistbaarheid | Alleen brede gebruiksnotitie; geen artikelkoppeling |
| SRC-105 | PNAS, DOI `10.1073/pnas.2422633122` — `https://doi.org/10.1073/pnas.2422633122` | Leren ondersteunen versus denkwerk overnemen | Geen titel, citaat, methodenotitie of lokale studie in register |
| SRC-106 | OECD, *How's Life for Children in the Digital Age?* — `https://www.oecd.org/en/publications/2025/05/how-s-life-for-children-in-the-digital-age_c4a22655.html` | Bescherming en handelingsvermogen van kinderen | Alleen syntheseomschrijving en URL |
| SRC-107 | IEA, *Energy and AI* — `https://www.iea.org/reports/energy-and-ai/executive-summary%C2%A0` | Energiegebruik datacenters en lokale concentratie | DOS-001 bewaart 415 TWh (2024) en circa 945 TWh (2030); bronpagina niet lokaal |
| SRC-108 | ITU/UNITAR, *Global E-waste Monitor 2024* — `https://www.itu.int/pub/D-GEN-E_WASTE.01-2024` | Materiële voetafdruk en e-waste | Alleen titel, rol en URL; geen cijfers of pagina's vastgelegd |
| SRC-109 | OECD, *Enhancing the Resilience of Communication Networks* — `https://www.oecd.org/en/publications/2025/05/enhancing-the-resilience-of-communication-networks_a47d78a1.html` | Redundantie, herstelvermogen en continuïteit | Alleen brede syntheseomschrijving en URL |

**[AUD-E]** Het Bronnenregister noemt de bronnen “geraadpleegd”. Deze handeling is niet reproduceerbaar uit de lokale set: er is geen querylog, downloadtijd, contenthash, websnapshot of bronnotitie. De correcte overdrachtsformulering is daarom: *deze bronnen zijn in het register als geraadpleegde bronnen geregistreerd; de bijbehorende ruwe leesactiviteit is niet exact geborgd*.

## 9. Voornaamste claim-/bewijszwakten die lokaal aantoonbaar zijn

### 9.1 Bronlagen zijn vermengd

**[AUD-E]** De 79 vermeldingen combineren boeken-/faculteitspagina's, peer-reviewed ogende artikelen, preprints, officiële overheidsbronnen, project- en leverancierspagina's, opiniestukken, marketingblogs, Reddit, Hacker News, Wikipedia, ResearchGate-landingspagina's, persoonlijke blogs en aggregators. In de tekst wordt niet systematisch aangegeven welke claim een primaire empirische bron, een conceptueel werk, een beleidskader, een zelfbeschrijving of slechts context heeft.

### 9.2 Citation substitution en secundaire doorverwijzing

**[AUD-E]** Meerdere passages noemen een gezaghebbende actor of studie, maar de eigen marker verwijst naar een andere laag:

- de tabel noemt Pew en Bain, maar verwijst voor beide naar marketingaggregator 21;
- de tabel noemt Gartner, maar gebruikt marker 17;
- de Nature-studie wordt geïntroduceerd met marker 26, een “Note on” de studie, terwijl de PubMed-vermelding 30 ongebruikt blijft;
- het Bhatia/NYT-experiment wordt gedragen door 31, een Transparency Coalition-artikel;
- EDPB-claims worden voornamelijk gedragen door consultancybron 44 en essay 38, terwijl officiële 41 niet wordt gebruikt;
- Doctorows mechanisme wordt gedragen door een Reddit-thread (15), niet een primaire Doctorow-publicatie.

### 9.3 Eén evidente inhoudelijke mismatch

**[AUD-E]** Bron 33 (*We tasked Opus 4.6 using agent teams to build a C Compiler*) wordt gebruikt bij de stelling dat AI-slop authentieke menselijke signalen moeilijk onderscheidbaar maakt. Op basis van titel en context is dit een duidelijke mismatch die vóór enig hergebruik moet worden verwijderd of vervangen.

### 9.4 Te absolute of universele formuleringen

**[AUD-E]** De tekst gebruikt onder meer “structureel en onvermijdelijk”, “onomkeerbare fase”, “noodgedwongen”, “onomkeerbare degeneratie”, “feitelijk onmogelijk”, “de enige volstrekt effectieve manier”, “nooit gelijktijdig” en “volledige algoritmische destructie”. DOS-001 corrigeert drie centrale versies hiervan al:

1. model collapse is conditioneel en mitigeerbaar, niet het onvermijdelijke lot van ieder model;
2. de 58%-zoekclaim was verkeerd geïnterpreteerd;
3. de EDPB schrijft geen algemene automatische vernietiging van onrechtmatig getrainde modellen voor.

**[AUD-I]** Deze correcties tonen dat ook andere absolute formuleringen systematisch als hypotheses moeten worden hergetoetst.

### 9.5 Probleem- en oplossingsbewijs lopen door elkaar

**[AUD-E/AUD-I]** Vanaf p.8 gebruikt het dossier het bestaan van beleidsinitiatieven en protocollen geregeld als bewijs dat de voorgestelde normatieve richting haalbaar of noodzakelijk is. Zelfbeschrijvingen van Public Stack, Inrupt/Solid, DC-EDIC, ActivityPub/ATProto/Matrix en MijnBureau zeggen wel wat de oplossing beoogt, maar bewijzen niet zelfstandig dat zij de diagnose oplossen, grootschalig werken, machtsverschuiving voorkomen of geen nieuwe afhankelijkheid introduceren.

### 9.6 Belanghebbende bronnen dragen effectiviteitsclaims

**[AUD-E]** Inrupt-bronnen 64 en 68 dragen respectievelijk de beschrijving van Solid en de Vlaamse succes-/toekomstbestendigheidsclaims. PublicSpaces/Waag dragen de Public Stack-zelfdefinitie. Zulke bronnen zijn geschikt om ontwerpintentie en projectstatus te documenteren, maar hebben onafhankelijke evaluatie nodig voor effectiviteit.

### 9.7 Claimgranulariteit ontbreekt

**[AUD-E]** Eén marker staat vaak aan het einde van een alinea met meerdere causale, empirische en normatieve deelclaims. Daardoor is niet controleerbaar welk deel de bron werkelijk ondersteunt. Dit geldt onder meer voor verwijzingen 7, 15, 17, 27, 38, 44, 65, 68 en 74.

### 9.8 Het aanvullende dossier bewaart samenvattingen, geen bewijsobjecten

**[AUD-E]** DOS-001 koppelt bij meerdere nieuwe kandidaten één brede bron aan een hele lens en erkent zelf dat tweede onafhankelijke bronnen, causale afbakening, tegenbewijs, citaten en paginaverwijzingen ontbreken. Vooral AI-autoriteit, synthetische intimiteit, creatieve homogenisering, rebound, afwenteling en intergenerationele vastlegging hebben nog geen specifieke bronkoppeling.

### 9.9 Asymmetrie en oplossingsgestuurde selectie

**[AUD-I]** Het oorspronkelijke dossier onderzoekt zeer diep die problemen waarop datasoevereiniteit, open protocollen en Public Stack als antwoord kunnen worden gepresenteerd. Andere constitutioneel relevante schademechanismen werden pas in de aanvullende ronde zichtbaar. Dit suggereert een oplossingsgestuurde zoekasymmetrie en is een reden om de oorspronkelijke tekst als hypothesekaart, niet als complete taxonomie, te behandelen.

## 10. Wat exact is teruggevonden en wat niet

### 10.1 Verantwoord als “exact teruggevonden” te benoemen

- de huidige twintigpagina-PDF als identificeerbaar byte-artefact met bovengenoemde SHA-256;
- de huidige `pdftotext -layout`-extractie als exact reproduceerbare afgeleide van die PDF;
- de volledige hoofdtekst, koppen, tabellen en bibliografie zoals zij in dat artefact staan;
- de 79 bibliografienummers en de zichtbare nummermarkers in de hoofdtekst;
- het huidige Bronnenregister als werkregister 0.1;
- DOS-001 v0.1 als exact huidige overdrachtstekst, inclusief eigen waarschuwingen en lacunes;
- de formulering van de twintig aanvullende kandidaat-problemen en vijf verdiepende thema's zoals zij nu in DOS-001 staat;
- de drie correcties zoals zij nu in DOS-001 zijn geformuleerd;
- het feit dat negen aanvullende URL/DOI-verwijzingen in het Bronnenregister staan.

### 10.2 Niet verantwoord als “exact teruggevonden” te benoemen

- alle oorspronkelijke zoekvragen, zoekresultaten en browsepaden van de aanvullende ronde;
- de volledige longlist vóór selectie of samenvoeging;
- woordelijke bronnotities, citaten en paginaverwijzingen van SRC-101–109;
- volledige tussenredeneringen, afgewezen hypothesen en classificatiebesluiten;
- het sterkste tegenargument per kandidaat;
- een complete claim–bron–tegenbewijs-matrix;
- bewijs dat iedere als “geraadpleegd” geregistreerde online bron in een specifieke versie volledig is gelezen;
- bewijs dat `B — Letterlijk teruggevonden` per passage werkelijk woordelijk uit de oorspronkelijke conversatie komt, zolang die bewaarde conversatie niet in het overdrachtspakket zit;
- de inhoud van de externe publicaties achter de 79 + 9 locators;
- reproduceerbaarheid van de aanvullende onderzoeksronde;
- categorische volledigheid van het probleemveld;
- wetenschappelijke juistheid van het oorspronkelijke dossier als geheel.

### 10.3 Nauwkeurige overdrachtsformulering

Een bewijsgetrouwe beschrijving luidt:

> Het oorspronkelijke onderzoeksdossier is als PDF en reproduceerbare tekstextractie exact lokaal teruggevonden. De aanvullende onderzoeksronde is niet als volledig onderzoekslogboek teruggevonden; wel is een inhoudelijk rijke, expliciet onvolledige samenvatting bewaard met kandidaat-problemen, drie correcties, aanvullende bronlocators en een inventaris van bewaargaten. Gereconstrueerde vervolgstappen moeten als heronderzoek of reconstructie worden gelabeld.

## 11. Minimale vervolgstappen voor een werkelijk controleerbaar archief

Zonder nieuwe brede onderzoeksronde kan de bewijsintegriteit al sterk worden verhoogd door:

1. de PDF, extractie, het register en DOS-001 samen met een manifest en hashes te bewaren;
2. de 79 URL's te normaliseren en per locator vast te leggen of deze bereikbaar, primair/secundair en inhoudelijk passend is;
3. van SRC-101–109 lokale snapshots of toegestane bronkopieën, titel/auteur/datum, inhoudshash en paginanotities te bewaren;
4. per oorspronkelijke en aanvullende probleemkandidaat één kernclaim te formuleren en iedere bron aan precies die claim te koppelen;
5. evidente mismatches en secundaire substituties eerst te repareren, met name 15, 21, 26, 31, 33, 38, 40, 44, 68 en 77;
6. iedere absolute claim om te zetten in een toetsbare, conditionele formulering totdat primair bewijs haar sterkte rechtvaardigt;
7. voor iedere kandidaat het beste tegenbewijs en de belangrijkste onzekerheid vast te leggen;
8. bij iedere toekomstige reconstructie datum, onderzoeker/agent, zoekvraag, bronselectie en beslisreden expliciet te registreren;
9. pas daarna kandidaat-problemen te consolideren tot constitutionele probleemfamilies en permanente `P`-nummers toe te kennen.

## 12. Auditbesluit

**[AUD-E]** Het teruggevonden pakket bevat een exact oorspronkelijk onderzoeksartefact en een veelbelovende aanvullende inhoudssamenvatting. **[AUD-E]** Het bevat niet het volledige ruwe aanvullende onderzoek. **[AUD-I]** De juiste status is daarom: *sterke overdrachtsbasis met exact geborgde oorspronkelijke bron en transparant gemarkeerde reconstructiegaten*. Het pakket is voldoende om elders inhoudelijk verder te gaan zonder vanaf nul te beginnen, maar onvoldoende om te stellen dat alle eerdere onderzoeksactiviteiten exact, reproduceerbaar en brongebonden zijn overgedragen.

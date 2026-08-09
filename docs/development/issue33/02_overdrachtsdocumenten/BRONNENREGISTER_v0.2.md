# Ypsia — Bronnenregister internetkritiek

**Status:** werkregister 0.2  
**Datum:** 2026-08-06  
**Functie:** vindplaats en identiteitsregister van de exact geborgde bronartefacten, de 79 oorspronkelijke locators en alle aanvullende bronnen die in de bewaarde of nieuwe onderzoeksrondes een claim of claimgrens dragen.

## 1. Leeswijzer

Dit register vervangt de bronnotities niet. Een rij bewijst alleen dat een bron is geïdentificeerd en waar de specifieke leesnotitie staat. De inhoudelijke claim, beperking, sterkste tegenargument en classificatiehint staan in de genoemde werknotitie.

De broncodes in de ruwe notities (`HMD`, `ER`, `TR`, `FG`, `CD`, `ST`, `ID` en `HXD`) blijven als lokale onderzoekscodes zichtbaar. De stabiele `SRC`-code hieronder is de overkoepelende bronidentiteit. Eén publicatie kan daarom meerdere werknotitiecodes hebben, maar slechts één `SRC`-code.

## 2. Exacte lokale bronartefacten

| ID | Bestand | Functie | SHA-256 |
|---|---|---|---|
| `SRC-001` | `00_teruggevonden_exact/Kritiek_op_het_huidige_internet.pdf` | Primaire lokale kopie van het oorspronkelijke twintigpagina-dossier. | `be96a1803d17bc4cec4f7d7b2181d642e0af337230601a00c4324662e7e84162` |
| `SRC-002` | `00_teruggevonden_exact/Kritiek_op_het_huidige_internet_tekstextractie.txt` | Reproduceerbare `pdftotext -layout`-zoekindex van SRC-001. | `196ba0ac53d17c9b895d3cd785633beef1632a42abe7eeb17537ab12124b407c` |

## 3. Oorspronkelijke bibliografie 1–79

De 79 vermeldingen uit SRC-001 zijn volledig en met genormaliseerde regelafbrekingen opgenomen in:

- `01_werknotities_heronderzoek/audit_initial_research.md`, §7.

Dezelfde audit registreert in §6 welke 43 nummers zichtbaar in de hoofdtekst worden gebruikt en welke 36 alleen in de bibliografie staan. De oorspronkelijke nummers blijven `O-001` tot en met `O-079` als verwijscode; zij krijgen niet achteraf elk een nieuw `SRC`-nummer zolang de publicatie zelf niet claimgericht opnieuw is beoordeeld.

Belangrijkste integriteitswaarschuwingen:

- bronniveaus lopen uiteen van peer-reviewed en officieel tot commerciële blog, vendorbron, Reddit, Hacker News en Wikipedia;
- verschillende claims verwijzen naar een secundaire samenvatting terwijl de primaire bron wel in de lijst staat;
- `O-033` is op titel inhoudelijk verkeerd gekoppeld aan de claim over synthetische ruis;
- aanwezigheid in de bibliografie is geen bewijs dat een bron de bijbehorende claim werkelijk ondersteunt.

## 4. Eerder geregistreerde aanvullende bronnen

| SRC-ID | Bron | Jaar | Type | Werknotitie / functie |
|---|---|---:|---|---|
| `SRC-101` | [Shumailov e.a., *AI models collapse when trained on recursively generated data*](https://www.nature.com/articles/s41586-024-07566-y) | 2024 | Peer-reviewed Nature-artikel | Correctie van onvermijdelijke model-collapseclaim. |
| `SRC-102` | [Pew Research Center, AI summaries and click-through behaviour](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) | 2025 | Empirisch onderzoeksrapport | Correctie van de 58%-interpretatie en doorklikcijfers. |
| `SRC-103` | [EDPB Opinion 28/2024 over AI-modellen en AVG](https://www.edpb.europa.eu/news/edpb-opinion-on-ai-models-gdpr-principles-support-responsible-ai_en) | 2024 | Officieel toezichtskader | Correctie van absolute vernietigings-/wissingsclaim. |
| `SRC-104` | [Raad van Europa, AI Framework Convention](https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence) | 2024 | Internationaal verdragskader | `HMD-20`, `HXD-04`; rechtsbescherming, democratie en mensenrechten. |
| `SRC-105` | [Bastani e.a., *Generative AI without guardrails can harm learning*](https://doi.org/10.1073/pnas.2422633122) | 2025 | Peer-reviewed gerandomiseerde veldstudie | `HMD-04`; leren tijdens gebruik versus zelfstandige beheersing. |
| `SRC-106` | [OECD, *How’s Life for Children in the Digital Age?*](https://www.oecd.org/en/publications/2025/05/how-s-life-for-children-in-the-digital-age_c4a22655.html) | 2025 | Internationale synthese | Eerdere kinderrechten-/ontwikkelingslens; in nieuw heronderzoek niet als dragende kernbron geselecteerd wegens overlap. |
| `SRC-107` | [IEA, *Energy and AI*](https://www.iea.org/reports/energy-and-ai) | 2025 | Officieel scenario- en modelrapport | `ER-01.1`; energie, lokale concentratie en scenario-onzekerheid. |
| `SRC-108` | [UNITAR/ITU, *Global E-waste Monitor 2024*](https://ewastemonitor.info/the-global-e-waste-monitor-2024/) | 2024 | Officiële statistische monitor | `ER-02.2`; e-waste en gedocumenteerde recycling. |
| `SRC-109` | [OECD, *Enhancing the Resilience of Communication Networks*](https://www.oecd.org/en/publications/2025/05/enhancing-the-resilience-of-communication-networks_a47d78a1.html) | 2025 | Internationale beleidsanalyse | Eerdere weerbaarheidslens; aangevuld met bronnen `SRC-144`–`SRC-148`. |

## 5. Heronderzoek mens, kennis, democratie, arbeid en uitsluiting

Volledige bronnotities: `01_werknotities_heronderzoek/heronderzoek_human_democracy.md`.

| SRC-ID | Werkcode | Bron en vindplaats | Jaar | Type / primaire functie |
|---|---|---|---:|---|
| `SRC-110` | `HMD-01` | [Risko & Gilbert, *Cognitive Offloading*](https://doi.org/10.1016/j.tics.2016.07.002) | 2016 | Peer-reviewed review; uitbesteding als normaal cognitief mechanisme. |
| `SRC-111` | `HMD-02` | [Sparrow, Liu & Wegner, *Google Effects on Memory*](https://doi.org/10.1126/science.1207745) | 2011 | Peer-reviewed experiment; inhoud onthouden versus vindplaats onthouden. |
| `SRC-112` | `HMD-03` | [Lee e.a., *The Impact of Generative AI on Critical Thinking*](https://doi.org/10.1145/3706598.3713778) | 2025 | Peer-reviewed CHI-enquête; inspanning en vertrouwenskalibratie. |
| `SRC-113` | `HMD-05` | [Orben e.a., *Windows of developmental sensitivity to social media*](https://doi.org/10.1038/s41467-022-29296-3) | 2022 | Peer-reviewed longitudinale analyse; kleine, heterogene leeftijdseffecten. |
| `SRC-114` | `HMD-06` | [National Academies, *Social Media and Adolescent Health*](https://doi.org/10.17226/27396) | 2024 | Onafhankelijk consensusrapport; baten, risico’s en ontbreken universele causale conclusie. |
| `SRC-115` | `HMD-07`, `FG-01.3`, `HXD-03` | [VN-Kinderrechtencomité, General Comment No. 25](https://www.ohchr.org/en/documents/general-comments-and-recommendations/general-comment-no-25-2021-childrens-rights-relation) | 2021 | Gezaghebbende maar niet zelfstandig bindende verdragsinterpretatie; ontwikkeling, autonomie, toegang en bescherming. |
| `SRC-116` | `HMD-08` | [Buçinca, Malaya & Gajos, *To Trust or to Think*](https://doi.org/10.1145/3449287) | 2021 | Peer-reviewed experiment; overreliance en cognitieve frictie. |
| `SRC-117` | `HMD-09` | [Logg, Minson & Moore, *Algorithm appreciation*](https://doi.org/10.1016/j.obhdp.2018.12.005) | 2019 | Peer-reviewed experimenten; algoritmisch advies kan extra gewicht krijgen. |
| `SRC-118` | `HMD-10` | [Dietvorst, Simmons & Massey, *Algorithm aversion*](https://doi.org/10.1037/xge0000033) | 2015 | Peer-reviewed experimenten; tegenbewijs tegen blind vertrouwen. |
| `SRC-119` | `HMD-11` | [NIST AI 600-1, Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) | 2024 | Officiële risicotaxonomie; confabulatie en automatiseringsbias. |
| `SRC-120` | `HMD-12` | [Lorenz-Spreen e.a., systematische review digitale media en democratie](https://doi.org/10.1038/s41562-022-01460-1) | 2023 | Peer-reviewed systematische review; gemengde democratische effecten. |
| `SRC-121` | `HMD-13` | [Nyhan e.a., *Like-minded sources on Facebook are prevalent but not polarizing*](https://doi.org/10.1038/s41586-023-06297-w) | 2023 | Peer-reviewed veldexperiment; blootstelling verandert, polarisatie niet aangetoond. |
| `SRC-122` | `HMD-14` | [Guess e.a., feed algorithms in an election campaign](https://doi.org/10.1126/science.abp9364) | 2023 | Peer-reviewed veldexperiment; rangschikking en nulbevinding politieke houding. |
| `SRC-123` | `HMD-15` | [UNESCO, Guidelines for the Governance of Digital Platforms](https://www.unesco.org/en/articles/guidelines-governance-digital-platforms?hub=751) | 2023 | Officieel normatief kader; distributiemacht, pluralisme en vrijheid van meningsuiting. |
| `SRC-124` | `HMD-16`, `ST-01.2`, `ST-02.1` | [Alston, *Digital welfare states and human rights*, A/74/493](https://digitallibrary.un.org/record/3834146?ln=en) | 2019 | Officieel VN-rapport; publieke digitale macht, classificatie en toegang. |
| `SRC-125` | `HMD-17` | [Rechtbank Den Haag, SyRI, ECLI:NL:RBDHA:2020:865](https://uitspraken.rechtspraak.nl/details?id=ECLI%3ANL%3ARBDHA%3A2020%3A865) | 2020 | Officiële rechtspraak; transparantie, proportionaliteit en controle. |
| `SRC-126` | `HMD-18` | [HvJ EU, SCHUFA, C-634/21](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A62021CJ0634) | 2023 | Bindende EU-rechtspraak; beslissende doorwerking van scoring. |
| `SRC-127` | `HMD-19` | [HvJ EU, Dun & Bradstreet Austria, C-203/22](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A62022CJ0203) | 2025 | Bindende EU-rechtspraak; betekenisvolle en begrijpelijke uitleg. |
| `SRC-128` | `HMD-21` | [Obermeyer e.a., bias in a population-health algorithm](https://doi.org/10.1126/science.aax2342) | 2019 | Peer-reviewed empirisch onderzoek; kostenproxy en corrigeerbare ongelijkheid. |
| `SRC-129` | `HMD-22` | [Buolamwini & Gebru, *Gender Shades*](https://proceedings.mlr.press/v81/buolamwini18a.html) | 2018 | Peer-reviewed onderzoek; intersectionele foutverschillen. |
| `SRC-130` | `HMD-23` | [NIST SP 1270, Identifying and Managing Bias in AI](https://doi.org/10.6028/NIST.SP.1270) | 2022 | Officiële taxonomie; institutionele, data- en meetbias. |
| `SRC-131` | `HMD-24` | [FRA, *Getting the future right*](https://fra.europa.eu/en/publication/2020/artificial-intelligence-and-fundamental-rights) | 2020 | Officieel kwalitatief onderzoek; grondrechten en institutionele lacunes. |
| `SRC-132` | `HMD-25` | [Wood e.a., *Good Gig, Bad Gig*](https://doi.org/10.1177/0950017018785616) | 2019 | Peer-reviewed mixed methods; flexibiliteit én algoritmische controle. |
| `SRC-133` | `HMD-26` | [OECD, *Algorithmic management in the workplace*](https://doi.org/10.1787/287c13c4-en) | 2025 | Officiële werkgeversenquête; voordelen, risico’s en verantwoordelijkheid. |
| `SRC-134` | `HMD-27` | [OECD, AI surveys of employers and workers](https://doi.org/10.1787/ea0a0fe1-en) | 2023 | Officiële enquêtes; directe tegenevidentie voor uitsluitend negatieve arbeidsthese. |
| `SRC-135` | `HMD-28` | [ITU, Facts and Figures 2025](https://www.itu.int/itu-d/reports/statistics/facts-figures-2025/) | 2025 | Officiële wereldstatistiek; connectiviteitskloof en snelle vooruitgang. |
| `SRC-136` | `HMD-29` | [Eurostat, Skills for the digital age](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Skills_for_the_digital_age) | 2025/2026 | Officiële EU-statistiek; ongelijk verdeelde digitale vaardigheden. |
| `SRC-137` | `HMD-30` | [FRA, toegang van ouderen tot publieke diensten](https://fra.europa.eu/en/publication/2023/older-people-digital-rights) | 2023 | Officiële rechts-/beleidsanalyse; digitale én analoge toegankelijkheid. |
| `SRC-138` | `HMD-31` | [UN DESA, E-Government Survey 2024](https://desapublications.un.org/sites/default/files/publications/2024-09/%28Web%20version%29%20E-Government%20Survey%202024%201392024.pdf) | 2024 | Officiële mondiale index; vooruitgang en inkomensgebonden digitale overheidskloof. |

`SRC-105` is tevens werkcode `HMD-04`; `SRC-104` is tevens `HMD-20`.

## 6. Heronderzoek ecologie, weerbaarheid en grensgebieden

Volledige bronnotities: `01_werknotities_heronderzoek/heronderzoek_ecology_resilience.md`.

| SRC-ID | Werkcode | Bron en vindplaats | Jaar | Type / primaire functie |
|---|---|---|---:|---|
| `SRC-139` | `ER-01.2` | [UNEP, AI end-to-end environmental lifecycle](https://www.unep.org/resources/report/artificial-intelligence-ai-end-end-environmental-impact-full-ai-lifecycle-needs-be) | 2024 | Officiële synthese; volledige AI-levenscyclus en impactcategorieën. |
| `SRC-140` | `ER-01.3` | [ITU, *Measuring what matters*](https://www.itu.int/dms_pub/itu-s/opb/gen/S-GEN-GDA.001-2025-PDF-E.pdf) | 2025 | Officiële methodologische review; meetgaten en systeemgrenzen. |
| `SRC-141` | `ER-02.1` | [UNCTAD, Digital Economy Report 2024](https://doi.org/10.18356/9789213589779) | 2024 | Officieel VN-rapport; materiële ketens en geografische afwenteling. |
| `SRC-142` | `ER-03.1` | [Lange, Pohl & Santarius, ICT en energievraag](https://doi.org/10.1016/j.ecolecon.2020.106760) | 2020 | Peer-reviewed artikel; netto-effect bestaat uit tegengestelde kanalen. |
| `SRC-143` | `ER-03.2` | [Kunkel & Tyfield, digital rebound](https://doi.org/10.1016/j.erss.2021.102295) | 2021 | Peer-reviewed perspective; rebound als onderzoeksmechanisme. |
| `SRC-144` | `TR-01.1` | [UK CMA, Cloud infrastructure services final report](https://assets.publishing.service.gov.uk/media/688b8891fdde2b8f73469544/final_decision_report.pdf) | 2025 | Officiële marktstudie; concentratie en overstapbarrières. |
| `SRC-145` | `TR-01.2` | [FSB, Third-party dependencies in cloud services](https://www.fsb.org/uploads/P091219-2.pdf) | 2019 | Officieel stabiliteitsrapport; collectieve afhankelijkheid en uitwijkbaarheid. |
| `SRC-146` | `TR-01.3` | [Algemene Rekenkamer, *Het Rijk in de cloud*](https://www.rekenkamer.nl/site/binaries/site-content/collections/documents/2025/01/15/het-rijk-in-de-cloud/Het%2BRijk%2Bin%2Bde%2Bcloud.pdf) | 2025 | Officiële Nederlandse audit; kennis, concentratie en continuïteit. |
| `SRC-147` | `TR-02.1` | [NIST SP 800-161 Rev. 1 Update 1](https://doi.org/10.6028/NIST.SP.800-161r1-upd1) | 2024 | Officiële richtlijn; transitieve supply-chainrisico’s. |
| `SRC-148` | `TR-02.2` | [ENISA, Good practices for supply chain cybersecurity](https://www.enisa.europa.eu/sites/default/files/publications/Good%20Practices%20for%20Supply%20Chain%20Cybersecurity.pdf) | 2023 | Officiële EU-studie; ketenincidenten en beheerpraktijken. |
| `SRC-149` | `FG-01.1` | [VN Declaration on Future Generations, A/RES/79/1](https://digitallibrary.un.org/record/4061879?ln=en) | 2024 | Officieel normatief instrument; toekomstige generaties als belangendrager. |
| `SRC-150` | `FG-01.2`, `HXD-01` | [UNESCO Recommendation on the Ethics of AI](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence) | 2021 | Officieel soft law; mens, cultuur, milieu, toekomst en onomkeerbaarheid als lens. |
| `SRC-151` | `CD-01.1` | [Mittelstadt, *From Individual to Group Privacy*](https://doi.org/10.1007/s13347-017-0253-7) | 2017 | Peer-reviewed conceptueel onderzoek; ad-hocgroepen en groepsbehandeling. |
| `SRC-152` | `CD-01.2` | [Mühlhoff, *Predictive privacy*](https://doi.org/10.1177/20539517231166886) | 2023 | Peer-reviewed theorie; voorspellingsmacht over niet-deelnemers. |
| `SRC-153` | `ST-01.1` | [OHCHR, The right to privacy in the digital age, A/HRC/48/31](https://digitallibrary.un.org/record/3946475?ln=en) | 2021 | Officieel VN-rapport; staatsmonitoring, biometrie en AI-risico. |
| `SRC-154` | `ST-02.2` | [Nationale ombudsman, *De burger gaat digitaal*](https://www.nationaleombudsman.nl/uploads/2013170_de_burger_gaat_digitaal.pdf) | 2013 | Officiële ombudsmanstudie; kanaalkeuze en feitelijke toegang. |
| `SRC-155` | `ID-01.1` | [Kaye, Encryption, anonymity and human rights, A/HRC/29/32](https://digitallibrary.un.org/record/798709?ln=en) | 2015 | Officieel VN-rapport; anonimiteit als privacy- en uitingsbelang. |
| `SRC-156` | `ID-01.2` | [W3C DID Core 1.0](https://www.w3.org/TR/did-1.0/) | 2022 | Officiële webstandaard; correlatierisico en pairwise identifiers. |
| `SRC-157` | `ID-01.3` | [NIST SP 800-63C-4](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63C-4.pdf) | 2025 | Officiële richtlijn; federatie, assurance, minimalisatie en onkoppelbaarheid. |

`SRC-107` is tevens `ER-01.1`; `SRC-108` is tevens `ER-02.2`; `SRC-115` is tevens `FG-01.3`; `SRC-124` is tevens `ST-01.2` en `ST-02.1`.

## 7. Dwarsdoorsnijdende kruistoets

Volledige notities en als uitgevoerd geregistreerde zoekvragen: `01_werknotities_heronderzoek/heronderzoek_cross_domain.md`.

| SRC-ID | Werkcode | Bron en vindplaats | Jaar | Functie |
|---|---|---|---:|---|
| `SRC-158` | `HXD-02` | [European Declaration on Digital Rights and Principles](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023C0123(01)) | 2022/2023 | Taxonomische kruistoets: mensgerichtheid, inclusie, keuze, publieke ruimte, veiligheid en duurzaamheid. |
| `SRC-159` | `HXD-05` | [EDPS Opinion on online manipulation and personal data](https://www.edps.europa.eu/sites/default/files/publication/18-03-19_online_manipulation_en.pdf) | 2018 | Bedrijfs- én staatsmonitoring, manipulatie en collectieve democratische belangen. |
| `SRC-160` | `HXD-06` | [De Brouwer, privacy self-management and privacy externalities](https://policyreview.info/articles/analysis/privacy-self-management-and-issue-privacy-externalities-thwarted-expectations-and) | 2020 | Peer-reviewed analyse; individuele datakeuze kan anderen raken. |
| `SRC-161` | `HXD-07` | [EDPS Opinion on coherent enforcement in the age of big data](https://www.edps.europa.eu/sites/default/files/publication/16-09-23_bigdata_opinion_en.pdf) | 2016 | Collectieve waarden naast individuele gegevensbescherming. |
| `SRC-162` | `HXD-08` | [Europese Commissie, toepassing EU-Handvest in 2021](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52021DC0819) | 2021 | Gelijke toegang tot publieke diensten en belang van alternatieve toegang. |
| `SRC-163` | `HXD-09` | [Europees Parlement, digitalisering van EU-administratieve diensten](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52023IP0426) | 2024 | Analoge alternatieven, menselijke contactpunten en toegankelijkheid als aanbeveling. |

`HXD-01` is `SRC-150`; `HXD-03` is `SRC-115`; `HXD-04` is `SRC-104`.

## 8. Dossiers en afgeleide documenten

| ID | Bestand | Functie |
|---|---|---|
| `DOS-001` | `00_teruggevonden_exact/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.1.md` | Exact bewaarde aanvullende samenvatting en integriteitswaarschuwing. |
| `DOS-002` | `02_overdrachtsdocumenten/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.2.md` | Overdrachtsindex van exacte laag, reconstructie en heronderzoek. |
| `AUD-001` | `01_werknotities_heronderzoek/audit_initial_research.md` | Bewijsgetrouwe audit van lokale artefacten, 79 bronnen en oorspronkelijke claims. |
| `HER-001` | `01_werknotities_heronderzoek/heronderzoek_human_democracy.md` | Ruwe bronnotities mens/kennis/democratie/arbeid/uitsluiting. |
| `HER-002` | `01_werknotities_heronderzoek/heronderzoek_ecology_resilience.md` | Ruwe bronnotities ecologie/weerbaarheid/grensgebieden. |
| `HER-003` | `01_werknotities_heronderzoek/heronderzoek_cross_domain.md` | Ruwe normatieve kruistoets. |

Geen dossier, audit of afgeleid document telt zelfstandig mee als externe bewijsbron.

## 9. Status en beperkingen

- De externe publicaties zijn in dit pakket als locator en gedetailleerde bronnotitie bewaard, niet als volledige lokale websnapshot.
- Een URL kan later veranderen; DOI, documentcode, ECLI of officiële publicatiecode heeft waar beschikbaar voorrang.
- Een brede synthese, statistiek, uitspraak of normatief kader ondersteunt alleen de specifieke claim die in de bronnotitie staat.
- Brononafhankelijkheid wordt per kandidaat beoordeeld; twee documenten van dezelfde studie of dezelfde onderliggende dataset tellen niet automatisch als twee bewijsgronden.
- `SRC`-registratie is geen inhoudelijke goedkeuring van een kandidaatprobleem.

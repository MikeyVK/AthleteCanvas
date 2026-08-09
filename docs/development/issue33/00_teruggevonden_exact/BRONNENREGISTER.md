# Ypsia — Bronnenregister

**Status:** werkregister 0.1  
**Aangemaakt:** 6 augustus 2026  
**Functie:** vindplaats van alle bronartefacten die op dit moment in de werkruimte aanwezig zijn, plus de verifieerbare online bronnen die in de aanvullende onderzoeksronde zijn geraadpleegd.

## Leeswijzer

Dit register onderscheidt bron**bestanden** van bron**verwijzingen**. Alleen bestanden die in de werkruimte aanwezig waren, zijn hier als lokale kopie opgenomen. Online publicaties worden als stabiele URL of DOI geregistreerd; zij zijn niet zonder meer als lokale kopie gearchiveerd.

Het oorspronkelijke dossier bevat zelf een literatuurlijst van 79 verwijzingen. Die complete oorspronkelijke lijst staat in het lokale dossier, onder *Geciteerd werk*, en is via de tekstextractie doorzoekbaar. Dit register vervangt die lijst niet, maar maakt haar vindbaar en voegt de later gebruikte aanvullende bronnen toe.

## 1. Lokale bronbestanden

| ID | Logische naam | Bestand | Herkomst / inhoud |
|---|---|---|---|
| SRC-001 | Kritiek op het huidige internet — bron-PDF | [Kritiek_op_het_huidige_internet.pdf](01_oorspronkelijk_onderzoek/Kritiek_op_het_huidige_internet.pdf) | Oorspronkelijk Ypsia-onderzoeksdossier; bevat de analyse en de bibliografie met 79 verwijzingen. |
| SRC-002 | Kritiek op het huidige internet — tekstextractie | [Kritiek_op_het_huidige_internet_tekstextractie.txt](01_oorspronkelijk_onderzoek/Kritiek_op_het_huidige_internet_tekstextractie.txt) | Doorzoekbare tekstweergave van SRC-001, inclusief de literatuurlijst. Afgeleid bestand; SRC-001 blijft de primaire lokale kopie. |

### Integriteitscontrole

| Bestand | SHA-256 |
|---|---|
| `Kritiek_op_het_huidige_internet.pdf` | `be96a1803d17bc4cec4f7d7b2181d642e0af337230601a00c4324662e7e84162` |
| `Kritiek_op_het_huidige_internet_tekstextractie.txt` | `196ba0ac53d17c9b895d3cd785633beef1632a42abe7eeb17537ab12124b407c` |

## 2. Aanvullende onderzoeksronde

| ID | Logische naam | Soort | Verifieerbare vindplaats | Gebruik in onderzoek |
|---|---|---|---|---|
| SRC-101 | Model collapse bij recursief getrainde AI | Peer-reviewed onderzoek | [Nature](https://www.nature.com/articles/s41586-024-07566-y) | Nuancering: reëel risico bij specifieke trainingscondities, niet onvermijdelijk voor ieder model. |
| SRC-102 | AI-samenvattingen en doorklikgedrag | Empirisch onderzoeksrapport | [Pew Research Center](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) | Controle van claims over AI-zoekresultaten, bronverkeer en bronverlies. |
| SRC-103 | GDPR en AI-modellen | Toezichtskader | [European Data Protection Board](https://www.edpb.europa.eu/news/edpb-opinion-on-ai-models-gdpr-principles-support-responsible-ai_en) | Nuancering van recht op gegevenswissing, anonimiteit en AI-modellen. |
| SRC-104 | Mensenrechten, democratie en AI | Internationaal juridisch kader | [Council of Europe — Framework Convention on AI](https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence) | Onderbouwing voor rechtsbescherming, gelijkheid, transparantie, toezicht en betwistbaarheid. |
| SRC-105 | AI-gebruik, denken en leren | Peer-reviewed onderzoek | [PNAS, DOI 10.1073/pnas.2422633122](https://doi.org/10.1073/pnas.2422633122) | Onderbouwing voor onderscheid tussen leerondersteuning en overname van denkwerk. |
| SRC-106 | Kinderen in het digitale tijdperk | Internationale synthese | [OECD](https://www.oecd.org/en/publications/2025/05/how-s-life-for-children-in-the-digital-age_c4a22655.html) | Bescherming én handelingsvermogen van kinderen als afzonderlijke constitutionele zorg. |
| SRC-107 | Energie en AI | Internationale analyse | [IEA — Energy and AI](https://www.iea.org/reports/energy-and-ai/executive-summary%C2%A0) | Onderbouwing voor energiegebruik en geconcentreerde lokale effecten van datacenters. |
| SRC-108 | Mondiale e-waste | Internationale dataset / monitor | [ITU/UNITAR — Global E-waste Monitor 2024](https://www.itu.int/pub/D-GEN-E_WASTE.01-2024) | Onderbouwing voor materiële voetafdruk, hardwareketens en afvalstromen. |
| SRC-109 | Weerbaarheid van communicatienetwerken | Internationale beleidsanalyse | [OECD](https://www.oecd.org/en/publications/2025/05/enhancing-the-resilience-of-communication-networks_a47d78a1.html) | Onderbouwing voor redundantie, herstelvermogen en continuïteit. |

## 3. Status en beperking

- Dit is een **bronregister**, geen bewijsmatrix. Een latere bewijsmatrix koppelt per probleemfamilie een specifieke kernclaim aan minimaal twee onafhankelijke bronnen.
- De 79 verwijzingen in SRC-001 zijn nog niet afzonderlijk beoordeeld op onafhankelijkheid, primaire status of actuele geldigheid.
- De negen aanvullende bronnen hierboven zijn genoemd in de afgeronde gerichte onderzoeksronde en zijn daarom expliciet geregistreerd.
- Nieuwe bronnen krijgen een opvolgend `SRC`-nummer en worden eerst hier geregistreerd, voordat zij een claim in een onderzoeksverslag dragen.

## 4. Onderzoeks- en herkomstdossiers

| ID | Logische naam | Bestand | Functie |
|---|---|---|---|
| DOS-001 | Ruw onderzoeksdossier internetkritiek v0.1 | [Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.1.md](02_aanvullend_onderzoek/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.1.md) | Bundelt de teruggevonden inhoud van de aanvullende onderzoeksronde en markeert per onderdeel of deze exact, letterlijk, samengevat of alleen via heronderzoek herstelbaar is. |

DOS-001 is geen primaire bron en telt niet mee voor het bronminimum. Het is een overdrachts- en integriteitsdocument dat voorkomt dat latere reconstructies ongemerkt als oorspronkelijke onderzoeksbevinding worden behandeld.

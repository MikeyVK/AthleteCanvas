# Ypsia — pakketmanifest onderzoeksarchief

**Pakketversie:** 0.2  
**Vastgelegd op:** 2026-08-06  
**Functie:** bestandsidentiteit, rol en integriteitscontrole van het overdrachtspakket vastleggen.

## Integriteitsmodel

- `MANIFEST.sha256` bevat het SHA-256-hashrecord van ieder pakketbestand behalve zichzelf.
- Het hashbestand bevat na voltooiing 27 records; samen met `MANIFEST.sha256` telt het pakket 28 bestanden.
- `MANIFEST.sha256` kan zichzelf niet betrouwbaar hashen zonder een oneindige zelfverwijzing en is daarom de enige bewuste uitzondering.
- De drie bestanden in de compatibiliteitspaden zijn byte-identieke kopieën. Zij houden relatieve links in het ongewijzigde historische `BRONNENREGISTER.md` werkend en voegen geen nieuwe onderzoeksinhoud toe.

Verificatie vanaf de pakketroot:

```bash
sha256sum -c MANIFEST.sha256
```

## Bestandsregister

| Pad | Versie of status | Rol |
|---|---|---|
| `START_HERE.md` | pakket 0.2 | Primaire leeswijzer, status en hervatvolgorde. |
| `CODEX_HERVATINSTRUCTIE.md` | pakket 0.2 | Opdracht- en grensinstructie voor een volgende Codex-omgeving. |
| `INTEGRATIE_IN_PROJECTMAP.md` | pakket 0.2 | Veilige integratie naast de zeven actuele lokale projectbestanden. |
| `MANIFEST.md` | pakket 0.2 | Semantisch bestandsregister en verificatie-instructie. |
| `MANIFEST.sha256` | gegenereerd na definitieve QA | Machineleesbare SHA-256-records; hash van dit bestand zelf bewust uitgesloten. |
| `00_teruggevonden_exact/BRONNENREGISTER.md` | exact teruggevonden v0.1 | Historisch bronnenregister; ongewijzigd. |
| `00_teruggevonden_exact/Kritiek_op_het_huidige_internet.pdf` | exact teruggevonden | Primaire twintigpagina-bron-PDF. |
| `00_teruggevonden_exact/Kritiek_op_het_huidige_internet_tekstextractie.txt` | exact teruggevonden | Byte-reproduceerbare `pdftotext -layout`-zoekindex van de PDF. |
| `00_teruggevonden_exact/Projectmap_bestandslijst_2026-08-06.png` | aangeleverd 2026-08-06 | Bewijs van namen en aanwezigheid van zeven lokale projectbestanden; geen inhoudsbewijs. |
| `00_teruggevonden_exact/Ypsia_Charter_v3.0_teruggevonden_contextkopie.md` | teruggevonden contextkopie | Constitutionele context; niet automatisch de actuele lokale versie. |
| `00_teruggevonden_exact/Ypsia_Constitutionele_Inventaris.md` | exact teruggevonden v0.1 | Lege/voorbereidende inventarisstructuur; niet inhoudelijk ingevuld. |
| `00_teruggevonden_exact/Ypsia_Constitutionele_Onderzoeksmethodiek.md` | exact teruggevonden v0.1 | Onderzoeksmethode, fasen, bewijsdrempels en stopregel. |
| `00_teruggevonden_exact/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.1.md` | exact teruggevonden v0.1 | Historische overdrachtsmomentopname; bewust ongewijzigd. |
| `00_teruggevonden_exact/01_oorspronkelijk_onderzoek/Kritiek_op_het_huidige_internet.pdf` | compatibiliteitskopie | Byte-identieke kopie van de primaire PDF voor historische relatieve links. |
| `00_teruggevonden_exact/01_oorspronkelijk_onderzoek/Kritiek_op_het_huidige_internet_tekstextractie.txt` | compatibiliteitskopie | Byte-identieke kopie van de primaire tekstextractie voor historische relatieve links. |
| `00_teruggevonden_exact/02_aanvullend_onderzoek/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.1.md` | compatibiliteitskopie | Byte-identieke kopie van v0.1 voor de historische relatieve link. |
| `01_werknotities_heronderzoek/README.md` | heronderzoek 2026-08-06 | Routekaart van de ruwe heronderzoekslaag. |
| `01_werknotities_heronderzoek/audit_initial_research.md` | audit 2026-08-06 | Artefact-, structuur-, bron- en herstelbaarheidsaudit. |
| `01_werknotities_heronderzoek/heronderzoek_cross_domain.md` | heronderzoek 2026-08-06 | Dwarsdoorsnijdende normatieve kruistoets en grensgebieden. |
| `01_werknotities_heronderzoek/heronderzoek_ecology_resilience.md` | heronderzoek 2026-08-06 | Ecologie, ketens, weerbaarheid, toekomst en collectieve schade. |
| `01_werknotities_heronderzoek/heronderzoek_human_democracy.md` | heronderzoek 2026-08-06 | Cognitie, ontwikkeling, kennis, democratie, recht, arbeid en uitsluiting. |
| `02_overdrachtsdocumenten/BESLISLOGBOEK.md` | v0.2 | Traceerbare procesbesluiten, alternatieven en niet-besluiten. |
| `02_overdrachtsdocumenten/BRONNENREGISTER_v0.2.md` | v0.2 | Genormaliseerde koppeling van oorspronkelijke en aanvullende bronnen. |
| `02_overdrachtsdocumenten/CLAIM_BRON_TEGENBEWIJS_MATRIX.md` | v0.2 | 28 voorlopige bewijsclusters met tegenbewijs en open bewijsopgaven. |
| `02_overdrachtsdocumenten/KANDIDATENLONGLIST.md` | v0.2 | Best-effortinventaris van 63 tijdelijke signalen; geen permanente `P`-IDs. |
| `02_overdrachtsdocumenten/ONDERZOEKLOGBOEK_2026-08-06.md` | v0.2 | Zelfregistratie van audit- en zoekactiviteiten en begrensd stopbesluit. |
| `02_overdrachtsdocumenten/OPEN_GATEN_EN_RED_TEAMSTATUS.md` | v0.2 | Historische bewaargaten, actuele bewijsleemten en red-teamstatus. |
| `02_overdrachtsdocumenten/Ypsia_Ruw_Onderzoeksdossier_Internetkritiek_v0.2.md` | v0.2 | Centrale inhoudelijke overdracht en huidige onderzoeksstatus. |

## Vaste primaire hashes

De twee eerder geregistreerde en opnieuw gecontroleerde primaire hashes zijn:

| Bestand | SHA-256 |
|---|---|
| `00_teruggevonden_exact/Kritiek_op_het_huidige_internet.pdf` | `be96a1803d17bc4cec4f7d7b2181d642e0af337230601a00c4324662e7e84162` |
| `00_teruggevonden_exact/Kritiek_op_het_huidige_internet_tekstextractie.txt` | `196ba0ac53d17c9b895d3cd785633beef1632a42abe7eeb17537ab12124b407c` |

Alle overige exacte hashes staan in `MANIFEST.sha256`.

# Ypsia Constitutionele Inventaris

Status: Actief werkdocument  
Versie: 0.1  
Laatste update: 2026-08-05

## Doel van dit document

De Constitutionele Inventaris is het centrale werkdocument voor het identificeren, onderzoeken en ordenen van de zelfstandige bouwstenen van de Ypsia-grondwet.

De inventaris is nadrukkelijk geen lineaire keten waarin één probleem automatisch leidt tot precies één doel, architectonisch antwoord, recht, verbod of toets. De constitutionele orde van Ypsia vormt een netwerk van veel-op-veelrelaties. Eén probleem kan meerdere beschermingen noodzakelijk maken, terwijl één recht of verbod verschillende problemen tegelijk kan adresseren.

Iedere bouwsteen wordt daarom eerst zelfstandig beschreven. Relaties worden pas vastgelegd nadat de betrokken bouwstenen voldoende zijn onderzocht. Vanuit deze relaties kunnen later gerichte matrices en Mermaid-diagrammen worden opgebouwd.

Dit document ondersteunt het schrijven en toetsen van het Charter, maar vervangt het Charter niet. Alleen tekst die uitdrukkelijk in het Charter wordt opgenomen, heeft constitutionele status.

## Werkwijze

1. We inventariseren één categorie en één bouwsteen tegelijk.
2. Iedere bouwsteen krijgt een permanent en uniek ID.
3. De formulering van een bouwsteen mag tijdens het onderzoek veranderen; het ID blijft gelijk.
4. Een vervallen bouwsteen behoudt zijn ID en krijgt de status `Vervallen`. Een ID wordt nooit opnieuw gebruikt.
5. Relaties worden niet impliciet uit de plaats van een bouwsteen afgeleid, maar later afzonderlijk en expliciet vastgelegd.
6. Diagrammen en matrices zijn afgeleide visualisaties. De inventaris blijft de inhoudelijke bron van waarheid.

## Identificatie

| Code | Categorie | Betekenis |
|---|---|---|
| `P` | Fundamenteel probleem | Een structurele ontsporing of bedreiging die Ypsia erkent. |
| `M` | Mandaat | Een doel of opdracht die uit de aanleiding voortvloeit. |
| `A` | Architectonisch antwoord | Een structurele eigenschap waarmee Ypsia een mandaat uitvoerbaar maakt. |
| `B` | Positief beginsel | Een actieve constitutionele verplichting waaraan Ypsia moet voldoen. |
| `R` | Onvervreemdbaar recht | Een bescherming die iedere gebruiker of andere erkende rechthebbende bezit. |
| `V` | Constitutioneel verbod | Een absolute grens die Ypsia niet mag overschrijden. |
| `T` | Constitutionele toets | Een vraag of criterium waarmee een beslissing wordt beoordeeld. |

IDs bestaan uit de categorieletter en een nummer van twee cijfers, bijvoorbeeld `P01`, `A03` of `V12`.

## Statussen

| Status | Betekenis |
|---|---|
| `Te onderzoeken` | De bouwsteen is gesignaleerd, maar nog niet inhoudelijk onderzocht. |
| `In bespreking` | De betekenis, afbakening of noodzaak wordt onderzocht. |
| `Concept` | Er ligt een voorlopige formulering die nog niet definitief is. |
| `Vastgesteld` | De bouwsteen is inhoudelijk goedgekeurd voor verdere verwerking. |
| `Vervallen` | De bouwsteen wordt niet verder gebruikt, maar blijft voor de historie zichtbaar. |

## Bouwstenen

| ID | Categorie | Werktitel | Kernomschrijving | Charterdeel | Status | Bron | Open vragen |
|---|---|---|---|---|---|---|---|

## Relaties en visualisaties

Relaties tussen bouwstenen worden later in een afzonderlijk relatieoverzicht vastgelegd. Iedere relatie verbindt een bron-ID met een doel-ID en krijgt een eigen type, toelichting en status. Hierdoor kunnen meerdere problemen naar hetzelfde recht verwijzen en kan één architectonisch antwoord verschillende rechten tegelijk waarborgen.

Op basis van dat relatieoverzicht kunnen onder meer de volgende weergaven worden gegenereerd:

- probleem ↔ mandaat;
- mandaat ↔ architectuur;
- probleem ↔ recht of verbod;
- architectuur ↔ recht of verbod;
- recht of verbod ↔ constitutionele toets;
- spanningen en versterkende relaties tussen beginselen;
- integrale Mermaid-diagrammen van de constitutionele orde.

De vorm van het relatieoverzicht en de toegestane relatietypen worden pas vastgesteld wanneer de eerste bouwstenen voldoende zijn uitgewerkt.

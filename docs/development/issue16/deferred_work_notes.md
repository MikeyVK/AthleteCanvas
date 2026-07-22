# Deferred Work Notes - Epic 16

Dit document verzamelt alle goedkeurde wijzigingen die in Epic 1 (Data Fundament) en Epic 18 (Waitlist) moeten worden doorgevoerd in hun respectievelijke branches, om strict de Git Branch Hygiene te respecteren. Bij het inchecken van die Epics moeten deze refactors als allereerste worden doorgevoerd.

## Epic 1 (Data Fundament) - docs/development/issue1/research.md

### Finding 2 & Finding 4 (PostgreSQL & Vector Storage)
- **Aanpassing in Finding 2**: PostgreSQL is niet alleen de relationele store, maar dankzij `pgvector` de *enige* store voor alle data. SQLite vervalt.
- **Isolatielaag**: We implementeren PostgreSQL Row-Level Security (RLS) gebaseerd op `user_uuid` als de fundamentele isolatielaag voor zowel relationele data als vectoren. Dit vervangt de eerdere dynamische context switches in applicatiecode.
- **Aanpassing in Finding 4**: ChromaDB (en de voorgestelde per-user collections) wordt volledig gedeprecateerd. We gebruiken één gecentraliseerde `user_embeddings` tabel in PostgreSQL.
- **Vector Indexering**: Geen HNSW index (om post-filtering recall loss te voorkomen), maar een standaard B-Tree index op `user_uuid` gevolgd door een Exact Cosine Distance flat scan.
- **Hiërarchische Vector Rollups & RAG**: Vector data wordt hiërarchisch opgeslagen (Micro, Meso, Macro) door background workers. Deze workers krijgen toegang via een uniform `data_shares` model.
- **Deterministische Serialisatie**: Gestructureerde data wordt eerst via rigide Jinja2 templates naar tekst omgezet, voordat ze door de static `all-MiniLM-L6-v2` model worden gehaald. Dit voorkomt coordinate drift.
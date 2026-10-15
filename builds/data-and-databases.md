# Data and databases: community builds with Jev

12 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/data-and-databases).

## [A data analyst agent with Jev as the reviewer](https://x.com/Sumanth_077/status/2107800513681182737)
By [Sumanth](https://x.com/Sumanth_077), 2026-10-07

A plain-English data agent that checks its own work.

How Jev is used: Qwen writes the SQL and explains results, Jev acts as the review layer, and Vercel's eve runs the loop and the human approval flow.

## [jev4pg: semantic operators for PostgreSQL](https://github.com/Sheltercosmo/jev4pg)
By [Shelter Zhou](https://github.com/Sheltercosmo), 2026-09-23

41 Jev-powered operators for filtering, extracting, ranking and matching data in PostgreSQL.

How Jev is used: Natural-language queries in English and Chinese run as Jev judgements, with caching and reviewable fallbacks.

## [laya-jev-GraphRAG: an agentic layer for your graph database](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG)
By [muneendra](https://github.com/bodepudimuneendra-netizen), 2026-09-23

A graph-database-agnostic GraphRAG framework with a swappable decision layer.

How Jev is used: The decision layer can use local Laya or cloud Jev, so the graph database keeps its role and the framework adds the choices.

## [JEV DataOps: choose what data to keep, then fine-tune](https://github.com/RenaGao/jev-dataops)
By [Rena Gao](https://github.com/RenaGao), 2026-09-21

An open-source workbench for selecting and scoring data for a training run.

How Jev is used: Jev decides which records to keep, then the tool fine-tunes a model and compares results, saving every decision, split and report.

## [DocJev: fast document classification and splitting](https://github.com/jerryjliu/docjev)
By [Jerry Liu](https://github.com/jerryjliu), 2026-09-19

A library, command-line tool and local app that classify and split PDF, Word and PowerPoint document packets.

How Jev is used: Local text extraction feeds Jev, which predicts a document's category or the boundaries between documents using rules written in plain language.

## [Jev on the Venice API: 24,000 Hacker News posts](https://x.com/sabrinaesaquino/status/2101102660997017747)
By [Sabrina](https://x.com/sabrinaesaquino), 2026-09-19

A demo classifying Hacker News posts into 12 categories.

How Jev is used: The author reports about two minutes for 24,000 posts.

## [tax-doc-classifier: sorting tax document pages with Jev](https://github.com/kyotofin/tax-doc-classifier)
By [Kyoto](https://github.com/kyotofin), 2026-09-18

A classifier that labels each page of a tax document as one of 261 IRS forms and 7 page kinds.

How Jev is used: One request per page goes to Jev, which returns probabilities. The authors report 100% classification of their own corpus at about $0.001 per page, 34 times cheaper and 6 times faster than their earlier language-model pipeline.

## [An image classifier with OCR and Jev](https://x.com/fayazara/status/2100953838891192789)
By [Fayaz Ahmed](https://x.com/fayazara), 2026-09-18

A small tool that sorts images by what they contain.

How Jev is used: The author reports about 900 images categorised in 40 seconds.

## [pg_typesafe: Jev from PostgreSQL](https://github.com/giuliosmall/pg_typesafe)
By [Giulio Piccolo](https://github.com/giuliosmall), 2026-09-17

A pre-alpha PostgreSQL extension that calls Jev from SQL.

How Jev is used: Exposes Jev's choice, yes/no and score questions as SQL functions for classification work inside the database.

## [pg-jev: ask your Postgres tables questions in plain language](https://github.com/realZachi/pg-jev)
By [mahmoud](https://github.com/realZachi), 2026-09-17

A PostgreSQL extension that filters, ranks and classifies rows with conditions written in everyday words.

How Jev is used: Every row is judged by Jev, which returns calibrated probabilities, so there is no index, embedding or vector column to maintain.

## [Classifying company invoices for accounting](https://x.com/iagolast/status/2100694100160745746)
By [iagolast](https://x.com/iagolast), 2026-09-17

A use case showing Jev sorting invoices into accounting categories.

How Jev is used: The author, writing in Spanish, says a company's invoices can be reviewed and classified in seconds.

## [neo4jev: navigating a graph](https://github.com/jexp/neo4jev)
By [Michael Hunger](https://github.com/jexp), 2026-09-16

A demo that walks a Neo4j graph one hop at a time toward a goal.

How Jev is used: At each node, the outgoing relationships become Jev choices, and a yes/no question in the same call asks whether the goal has been reached.


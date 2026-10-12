# Data and databases: community builds with Jev

6 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/data-and-databases).

## [jev4pg: semantic operators for PostgreSQL](https://github.com/Sheltercosmo/jev4pg)
By [Shelter Zhou](https://github.com/Sheltercosmo), 2026-09-23

41 Jev-powered operators for filtering, extracting, ranking and matching data in PostgreSQL.

How Jev is used: Natural-language queries in English and Chinese run as Jev judgements, with caching and reviewable fallbacks.

## [Jev for DuckDB](https://github.com/prasanthj/duckdb-jev)
By [Prasanth Jayachandran](https://github.com/prasanthj), 2026-09-20

A native DuckDB extension for classification and scoring from SQL.

How Jev is used: Batches up to 1,000 independent Jev judgements per request and streams results directly into queries.

## [Jevflake: Jev inside Snowflake](https://github.com/KranzL/Jevflake)
By [KranzL](https://github.com/KranzL), 2026-09-20

A dbt package (and Terraform module) that lets Snowflake ask Jev about your data.

How Jev is used: Creates SQL functions that call Jev, plus dbt macros and tests so answers are stored once and checked like any other model.

## [jevframe: Jev for pandas and Polars](https://github.com/ktaletsk/jevframe)
By [Konstantin Taletskiy](https://github.com/ktaletsk), 2026-09-18

A Python library to classify, analyse sentiment and score DataFrame rows with plain-language questions.

How Jev is used: Each row gets Jev's answer with the full probability distribution, returned as ordinary Series and DataFrames.

## [pg_typesafe: Jev from PostgreSQL](https://github.com/giuliosmall/pg_typesafe)
By [Giulio Piccolo](https://github.com/giuliosmall), 2026-09-17

A pre-alpha PostgreSQL extension that calls Jev from SQL.

How Jev is used: Exposes Jev's choice, yes/no and score questions as SQL functions for classification work inside the database.

## [neo4jev: navigating a graph](https://github.com/jexp/neo4jev)
By [Michael Hunger](https://github.com/jexp), 2026-09-16

A demo that walks a Neo4j graph one hop at a time toward a goal.

How Jev is used: At each node, the outgoing relationships become Jev choices, and a yes/no question in the same call asks whether the goal has been reached.


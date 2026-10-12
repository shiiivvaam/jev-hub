# Search and ranking: community builds with Jev

5 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/search-and-ranking).

## [Jev Reranker: choose what your LLM reads](https://github.com/shinpr/jev-reranker)
By [shinpr](https://github.com/shinpr), 2026-09-20

A command-line reranker that drops search results with no usable evidence.

How Jev is used: Reads candidates as JSON, has Jev rerank or extract the relevant passages, and passes metadata through unchanged.

## [Hearth: rental search across four marketplaces](https://github.com/Nancy-Chauhan/hearth-jev-rental-search)
By [Nancy Chauhan](https://github.com/Nancy-Chauhan), 2026-09-20

An agent that searches Craigslist, Facebook Marketplace, Redfin and Zillow from one request.

How Jev is used: Jev drives a real Chrome browser step by step and judges which listings match; it only reads, never messages or transacts.

## [jev-align: AI functions from your feedback](https://github.com/sutro-sh/jev-align)
By [Sutro](https://github.com/sutro-sh), 2026-09-19

An experimental CLI that builds calibrated AI functions from human labels.

How Jev is used: Finds the examples Jev is unsure about, asks you to label them, and improves the function's questions automatically.

## [Jev Search](https://x.com/fatwang2ai/status/2100653998378516518)
By [fatwang2](https://x.com/fatwang2ai), 2026-09-17

A free, open-source search engine you query in plain language.

How Jev is used: Jev decides where to search for each question and ranks the results that come back from the search API.

## [hev reranker](https://github.com/hev/reranker)
By [Adam Hevenor](https://github.com/hev), 2026-09-17

Uses Jev as a calibrated reranker for search results.

How Jev is used: One call carries the query and up to 30 documents; Jev returns a relevance probability for each, usable to sort and to cut off.


# Jev for re-ranking search results

Yes. A fast search such as keyword matching builds a shortlist, and Jev then scores every shortlisted result against the query and puts the best first. In TypeSafe's cookbook on 3,565 court-opinion passages, re-ranking a 30-result keyword shortlist raised the share of queries with the right passage in first place from 5% to 18%, and in the top ten from 38% to 62%.

**Fit:** Strong fit

**Good when**
- Your search finds roughly the right documents but often not the best one first.
- Relevance depends on meaning, not shared words: legal, support or product search.
- You can keep the shortlist small (tens of results, not thousands).

**Avoid when**
- Your keyword search already puts the right result first most of the time.
- You need to score millions of documents per query. Re-rank a shortlist, not the whole index.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`search-reranking.json`](./search-reranking.json):

```json
{
  "model": "jev-latest",
  "state": "Query: When can a court refuse to enforce an arbitration clause in an employment contract?\nCandidate: ...the clause was unconscionable because the employee had no meaningful opportunity to negotiate its terms...",
  "questions": {
    "relevance": {
      "type": "score",
      "instructions": "How well does this passage answer the query?",
      "criteria": [
        "Unrelated",
        "Same topic, does not answer",
        "Partly answers",
        "Answers the query"
      ]
    }
  }
}
```

## How to wire it in
1. Run your fast search (the cookbook uses BM25 keyword search) and keep a shortlist; the cookbook keeps 30.
2. Send Jev the query and one candidate at a time with one Score question.
3. Sort the shortlist by the score and show the top results.
4. Cache scores for popular queries so you do not pay twice.

## Common mistakes
- Re-ranking cannot rescue a result the fast search missed. If the right document is not on the shortlist, widen the shortlist.
- Describe every level of the score in words; the scale is the whole definition of relevance.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/search-reranking

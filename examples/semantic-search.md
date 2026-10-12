# Jev for semantic search

Partly. Jev can't search a catalogue on its own, but it works well as a re-ranker: once a conventional search returns 50 or so candidates, Jev scores how well each one matches the query so the best rise to the top. One builder used this to search property listings from a plain-English brief.

**Fit:** Good fit

**Good when**
- Queries are written in natural language, not keywords.
- A conventional search already produces a shortlist of candidates.
- Each result has a short text description Jev can read.

**Avoid when**
- You need to search millions of items directly. Jev evaluates one item at a time, so narrow the list first.
- Results are mostly images.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`semantic-search.json`](./semantic-search.json):

```json
{
  "model": "jev-latest",
  "state": "Search: \"Quiet 2-bedroom near a park, under $3,000, allows a dog\"\nListing: 2 bed / 1 bath apartment, $2,850 a month. Two blocks from Riverside Park. Top-floor unit, no shared walls. Cats only.",
  "questions": {
    "match": {
      "type": "score",
      "instructions": "How well does this listing match what the person asked for?",
      "criteria": [
        "Not a match",
        "Partly matches",
        "Good match",
        "Exactly what they asked for"
      ]
    },
    "breaks_requirement": {
      "type": "noul",
      "instructions": "Does this listing break a hard requirement in the search, such as price, pets or number of bedrooms?"
    }
  }
}
```

## How to wire it in
1. Run your normal search first (keyword or vector search) and keep the top 50–100 results.
2. Send Jev the person's search plus one result at a time, and ask both questions in the same request.
3. Drop anything with breaks_requirement ≥ 0.5, then sort the rest by the match score.
4. Show the top results. Cache answers for popular searches so you don't pay twice.

## Common mistakes
- Costs multiply: every search checks many results. Price it in the calculator with results per month, not searches per month.
- Two-word searches give Jev little to judge. For short searches, a normal search may do just as well.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/semantic-search

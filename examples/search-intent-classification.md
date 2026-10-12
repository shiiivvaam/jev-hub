# Jev for SEO search-intent classification

Yes. Search intent is a textbook Choice question with four well-known classes: informational, commercial, transactional and navigational. Run a keyword export through Jev and get intent plus a relevance score per keyword, for under a cent per 1,000.

**Fit:** Strong fit

**Good when**
- You work with keyword exports of thousands of rows.
- You want to cluster keywords by intent before writing anything.

**Avoid when**
- You need search volume or difficulty. That data comes from SEO tools, not a model.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`search-intent-classification.json`](./search-intent-classification.json):

```json
{
  "model": "jev-latest",
  "state": {
    "keyword": "jev api pricing per million tokens",
    "site": "A resource site for developers building with Jev"
  },
  "questions": {
    "intent": {
      "type": "choice",
      "instructions": "What is the searcher's main intent?",
      "criteria": {
        "informational": "Wants to learn or understand something",
        "commercial": "Comparing options before a purchase",
        "transactional": "Ready to buy, sign up or download",
        "navigational": "Looking for a specific site or page"
      }
    },
    "relevance": {
      "type": "score",
      "instructions": "How relevant is this keyword to the site described?",
      "criteria": [
        "Off-topic",
        "Loosely related",
        "Relevant",
        "Core topic"
      ]
    }
  }
}
```

## How to wire it in
1. Export keywords from your SEO tool as CSV.
2. Send each keyword with a one-line site description as state.
3. Drop keywords with relevance < 1.5, then group the rest by intent to plan pages.

## Common mistakes
- Mixed-intent keywords are common. Use the probabilities, not just the top choice — a 58/34 split tells you the page should serve both.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/search-intent-classification

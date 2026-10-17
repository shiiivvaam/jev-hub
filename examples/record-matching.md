# Jev for matching duplicate records

Yes. For each candidate pair, one Score question with three levels (different, possibly related, same) decides whether to leave the records apart, ask a person or merge them, and a few yes/no questions in the same request show which fields disagree. In TypeSafe's cookbook on 450 beer-catalogue pairs, 360 were left unlinked, 40 merged and 50 sent to a curator.

**Fit:** Good fit

**Good when**
- Two sources describe the same things in different words: catalogues, CRMs, supplier lists.
- A wrong merge is expensive, so you want a middle option that goes to a person.
- A cheap first pass has already picked the pairs worth checking.

**Avoid when**
- Records share a reliable ID. Match on the ID in code.
- You need every pair in two large lists compared. Narrow the candidates first, then let Jev judge.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`record-matching.json`](./record-matching.json):

```json
{
  "model": "jev-latest",
  "state": "Record A: Harbour Amber Ale · Northgate Brewing · American Amber · 5.5%\nRecord B: Northgate Harbour Amber - Pomegranate Edition · Northgate Brewing Co. · Fruit Beer · 5.5%",
  "questions": {
    "same": {
      "type": "score",
      "instructions": "Do these two records describe the same product?",
      "criteria": [
        "Different product",
        "Related, but possibly not the same",
        "Same product"
      ]
    },
    "brewery_matches": {
      "type": "noul",
      "instructions": "Do the two records name the same brewery?"
    },
    "style_matches": {
      "type": "noul",
      "instructions": "Do the two records describe the same style?"
    },
    "strength_matches": {
      "type": "noul",
      "instructions": "Do the two records give the same alcohol content?"
    }
  }
}
```

## How to wire it in
1. Use a cheap first pass (shared words, blocking keys) to pick candidate pairs.
2. Send each pair with one three-level Score and a yes/no question per field you care about.
3. Merge only at the top level, leave the bottom level apart, and send the middle to a person with the field answers attached.
4. Write the middle level carefully: it decides which pairs reach a person.

## Common mistakes
- Variants and special editions are the hard cases. Name them in the middle level so they reach a person instead of being merged.
- A wrong merge spreads: every fact about either record now describes both. Lean toward review when unsure.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/record-matching

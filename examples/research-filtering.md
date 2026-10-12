# Jev for research and news filtering

Yes. Relevance filtering is a natural Score question: describe what you care about, and Jev rates each abstract or headline against it. One public run classified 1,018 research papers for about 8 cents at a 256 ms median response time.

**Fit:** Strong fit

**Good when**
- You follow a feed (arXiv, RSS, news) that is mostly noise for you.
- You can describe your interests in a paragraph.
- Titles and abstracts are enough to judge relevance.

**Avoid when**
- You need summaries of what you keep. That's a language model's job.
- Relevance depends on reading full papers; cost rises with input length.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`research-filtering.json`](./research-filtering.json):

```json
{
  "model": "jev-latest",
  "state": "Title: Calibrated Early-Exit Classifiers for Low-Latency Routing\nAbstract: We study confidence calibration for small classifiers that route requests between models, and show that temperature scaling on 2k labeled examples cuts misroutes by 31%...",
  "questions": {
    "relevance": {
      "type": "score",
      "instructions": "How relevant is this to a team building cheap, fast AI routing and classification in production?",
      "criteria": [
        "Irrelevant",
        "Tangential",
        "Relevant",
        "Must read"
      ]
    },
    "topic": {
      "type": "choice",
      "instructions": "What is the main topic?",
      "criteria": {
        "routing": "Model routing and cascades",
        "evaluation": "Benchmarks, evals, calibration",
        "training": "Training methods and data",
        "applications": "Applied systems and case studies",
        "other": "Something else"
      }
    },
    "practical": {
      "type": "noul",
      "instructions": "Does this include results a practitioner could apply this month?"
    }
  }
}
```

## How to wire it in
1. Pull new items from your feeds once a day.
2. Send title + abstract (or headline + first paragraph) as state.
3. Keep items with relevance ≥ 2; put practical ≥ 0.6 at the top of your digest.
4. Rewrite the relevance instructions whenever your focus changes — it's the only tuning you need.

## Common mistakes
- Very broad interests make everything "relevant". Be specific about what you don't want.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/research-filtering

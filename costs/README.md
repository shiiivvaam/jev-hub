# What Jev costs

Jev (TypeSafe AI) lists **$0.042 per million input tokens**, with no charge for output tokens (checked 22 September 2026). A request can carry up to 64,000 tokens, counting the state and all questions together. These are TypeSafe's published figures and can change: check [their docs](https://docs.typesafe.ai/api).

## The formula

When you send several questions about the same input in one request (batched), the input is read once:

```
tokens per item = state tokens + (questions x tokens per question)
cost per item   = tokens per item / 1,000,000 x 0.042
```

If you send one question per request instead, the state is sent again with every question, so the cost is higher.

## Typical workloads

Estimates from list price, using typical sizes for each job (the calculator on the site lets you set your own): https://jevhub.io/calculator

| Use case | Items per month | Tokens per item | Cost per 1,000 items | Per month |
|---|---:|---:|---:|---:|
| [lead scoring](https://jevhub.io/use-cases/lead-scoring) | 3,000 | 460 | $0.02 | $0.06 |
| [email triage](https://jevhub.io/use-cases/email-triage) | 20,000 | 580 | $0.02 | $0.49 |
| [support ticket routing](https://jevhub.io/use-cases/support-ticket-routing) | 15,000 | 510 | $0.02 | $0.32 |
| [content moderation](https://jevhub.io/use-cases/content-moderation) | 100,000 | 270 | $0.01 | $1.13 |
| [research and news filtering](https://jevhub.io/use-cases/research-filtering) | 30,000 | 500 | $0.02 | $0.63 |
| [SEO search-intent classification](https://jevhub.io/use-cases/search-intent-classification) | 50,000 | 160 | $0.0067 | $0.34 |
| [ad and creative classification](https://jevhub.io/use-cases/ad-classification) | 5,000 | 300 | $0.01 | $0.06 |
| [semantic search](https://jevhub.io/use-cases/semantic-search) | 50,000 | 250 | $0.01 | $0.53 |
| [agent and browser decisions](https://jevhub.io/use-cases/agent-decisions) | 200,000 | 1,060 | $0.04 | $8.90 |
| [LLM guardrails](https://jevhub.io/use-cases/llm-guardrails) | 100,000 | 550 | $0.02 | $2.31 |
| [checking citations](https://jevhub.io/use-cases/citation-checking) | 20,000 | 760 | $0.03 | $0.64 |
| [filtering RAG passages](https://jevhub.io/use-cases/rag-passage-filtering) | 120,000 | 510 | $0.02 | $2.57 |
| [re-ranking search results](https://jevhub.io/use-cases/search-reranking) | 300,000 | 300 | $0.01 | $3.78 |
| [matching duplicate records](https://jevhub.io/use-cases/record-matching) | 50,000 | 280 | $0.01 | $0.59 |
| [classifying documents into many categories](https://jevhub.io/use-cases/document-classification) | 10,000 | 2,700 | $0.11 | $1.13 |
| [extracting dates, emails and amounts](https://jevhub.io/use-cases/data-extraction) | 30,000 | 680 | $0.03 | $0.86 |

Data files: [`use-case-costs.csv`](./use-case-costs.csv) and [`use-case-costs.json`](./use-case-costs.json).

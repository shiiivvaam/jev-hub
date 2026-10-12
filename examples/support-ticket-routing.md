# Jev for support ticket routing

Yes. Routing a ticket to a queue is a textbook Choice question, and TypeSafe's own docs use this example. In an independent test, 8-way routing cost about 1.5 cents per 1,000 tickets, roughly five times less than small language models.

**Fit:** Strong fit

**Good when**
- You have three or more queues and tickets regularly land in the wrong one.
- Keyword-based routing rules keep breaking.
- You want early warning on angry or at-risk customers.

**Avoid when**
- You have a single support queue, so there's nothing to route.
- You need a reply sent to the customer. That's a text-generation job.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`support-ticket-routing.json`](./support-ticket-routing.json):

```json
{
  "model": "jev-latest",
  "state": "Ticket #88213 — Plan: Business\n\"I've been locked out since the SSO change this morning. Three people on my team can't log in and we have a client demo at 2pm.\"",
  "questions": {
    "queue": {
      "type": "choice",
      "instructions": "Which team should handle this ticket?",
      "criteria": {
        "billing": "Payments, invoices, refunds, plan changes",
        "account_access": "Login, SSO, passwords, permissions",
        "bug": "Something in the product is broken",
        "how_to": "Questions about using a feature",
        "feedback": "Feature requests and general feedback"
      }
    },
    "frustration": {
      "type": "score",
      "instructions": "How frustrated is the customer?",
      "criteria": [
        "Calm",
        "Mildly annoyed",
        "Frustrated",
        "Angry or threatening to leave"
      ]
    },
    "blocking": {
      "type": "noul",
      "instructions": "Is the customer completely blocked from using the product?"
    }
  }
}
```

## How to wire it in
1. Call Jev when the ticket is created, before any agent sees it.
2. Assign the queue automatically when confidence ≥ 0.7; leave the rest in a triage queue.
3. Raise priority when blocking ≥ 0.6 or frustration ≥ 2.5.
4. Log Jev's answer next to the queue the ticket was finally closed in — that's your free accuracy dataset.

## Common mistakes
- Overlapping queues ("technical" vs "bug") confuse people and Jev alike. Make criteria mutually exclusive.
- Choice questions with many options add tokens per option. 77-way routing cost ~2.6× more than 8-way in the same test.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/support-ticket-routing

# Jev for email triage

Yes. Email triage is the most widely reproduced Jev workload: one request per email can assign a category, rate urgency and flag whether a human needs to see it. An open-source project reports 1,000 emails triaged in about a minute for around 3 cents.

**Fit:** Strong fit

**Good when**
- You or your team spend real time deciding what to open first.
- Your categories are stable (for example: needs reply, updates, promotions, sales, spam).
- A human stays in the loop for anything consequential.

**Avoid when**
- You want replies drafted. Jev can't generate text; pair it with a language model for the emails that need one.
- Your privacy obligations don't allow sending email content to a third-party API.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`email-triage.json`](./email-triage.json):

```json
{
  "model": "jev-latest",
  "state": "From: Dana Lee <dana@acme.io>\nSubject: Invoice #4471 charged twice\nBody: Hi, our card was charged twice for March. Can you refund the duplicate today? Our finance close is tomorrow.",
  "questions": {
    "category": {
      "type": "choice",
      "instructions": "What kind of email is this?",
      "criteria": {
        "needs_reply": "A person expecting a response from us",
        "updates": "Notifications, receipts, product updates",
        "promotions": "Marketing and newsletters",
        "sales": "Someone selling to us",
        "spam": "Unwanted or suspicious mail"
      }
    },
    "urgency": {
      "type": "score",
      "instructions": "How time-sensitive is this email for us?",
      "criteria": [
        "Whenever",
        "This week",
        "Today",
        "Within the hour"
      ]
    },
    "needs_human": {
      "type": "noul",
      "instructions": "Does this email involve money, legal risk or an upset customer?"
    }
  }
}
```

## How to wire it in
1. Send sender, subject and the first ~1,500 characters of the body as state. Long threads cost more and rarely change the answer.
2. Ask all questions in one request per email.
3. Apply labels automatically; only surface needs_reply mail with urgency ≥ 2 as a notification.
4. Anything with needs_human ≥ 0.5 goes to a person, whatever the category.

## Common mistakes
- Newsletters that look personal are the most common misclassification. Add an example of one to the promotions criterion.
- Test on a de-identified sample first and check the provider's data retention settings before running a live inbox.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/email-triage

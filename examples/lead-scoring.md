# Jev for lead scoring

Yes. Lead scoring is one of Jev's strongest fits: send the lead record, score it for fit, estimate buying intent and route it, all in one request. Public runs report scoring hundreds of leads in seconds for a few cents.

**Fit:** Strong fit

**Good when**
- You get more inbound leads than your team can read, and most are low value.
- Your ideal customer profile fits in a few plain sentences.
- You want a ranked queue for reps, not a fully automated decision on who gets contacted.

**Avoid when**
- You need a written rationale for each score. Jev returns scores and probabilities, not explanations.
- The score depends on data Jev can't see, such as CRM deal history, and you can't include it in the input.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`lead-scoring.json`](./lead-scoring.json):

```json
{
  "model": "jev-latest",
  "state": {
    "name": "Priya Raman",
    "title": "Head of RevOps",
    "company": "Northwind Logistics (420 employees)",
    "source": "Pricing page form",
    "message": "We're replacing our routing rules for ~3k inbound leads/month. Need something live this quarter."
  },
  "questions": {
    "fit": {
      "type": "score",
      "instructions": "How well does this lead match our ideal customer: B2B companies of 100–2,000 employees with a sales or RevOps team?",
      "criteria": [
        "No fit",
        "Weak fit",
        "Plausible fit",
        "Strong fit",
        "Ideal customer"
      ]
    },
    "intent": {
      "type": "noul",
      "instructions": "Is this person actively looking to buy or implement a solution soon?",
      "criteria": {
        "true": "Mentions a timeline, budget, active evaluation or a concrete project.",
        "false": "Browsing, researching, a student, or a vendor pitching us."
      }
    },
    "route": {
      "type": "choice",
      "instructions": "Who should handle this lead?",
      "criteria": {
        "sales": "A potential customer worth a sales conversation",
        "nurture": "A potential customer who is early; add to nurture",
        "partner": "An agency, reseller or integration partner",
        "other": "Job seeker, vendor, spam or not a buyer"
      }
    }
  }
}
```

## How to wire it in
1. Send each new lead as JSON state with all three questions in one request, so the lead is read once.
2. Route to sales when intent ≥ 0.7 and fit ≥ 3; send to nurture below that.
3. Send low-confidence route answers (confidence < 0.6) to a human review list.
4. Every month, compare 50 Jev decisions with what your team would have done and adjust the wording of the criteria.

## Common mistakes
- Vague criteria produce vague scores. "Good lead" is not a rubric; "B2B, 100–2,000 employees, has a RevOps team" is.
- Don't send fields you wouldn't want a vendor to see. Strip phone numbers and anything you don't need for the decision.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/lead-scoring

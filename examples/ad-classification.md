# Jev for ad and creative classification

Yes, for text. Jev can tag each ad by angle, rate hook strength and check it against your policy list in a single request, which makes it practical to label thousands of competitor or historical ads.

**Fit:** Good fit

**Good when**
- You're analysing a large library of your own or competitors' ads.
- You want consistent tags so you can compare angles against performance.

**Avoid when**
- The creative is image- or video-only with little text.
- You want new ad copy generated.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`ad-classification.json`](./ad-classification.json):

```json
{
  "model": "jev-latest",
  "state": "Platform: Meta — Headline: \"Stop losing leads at 2am\" — Primary text: \"Your form fills don't sleep. Route every inbound lead in under a second and wake up to a sorted pipeline. Free 14-day trial.\"",
  "questions": {
    "angle": {
      "type": "choice",
      "instructions": "What is the main persuasion angle?",
      "criteria": {
        "pain": "Leads with a problem or fear",
        "outcome": "Leads with a result or benefit",
        "proof": "Leads with testimonials, numbers or logos",
        "offer": "Leads with a discount, trial or deal",
        "curiosity": "Leads with a question or tease"
      }
    },
    "hook": {
      "type": "score",
      "instructions": "How strong is the first line as a scroll-stopping hook?",
      "criteria": [
        "Weak",
        "Average",
        "Strong",
        "Exceptional"
      ]
    },
    "claims_risk": {
      "type": "noul",
      "instructions": "Does the ad make a specific claim that could need substantiation (numbers, guarantees, health or income claims)?"
    }
  }
}
```

## How to wire it in
1. Collect ads (yours from the ad manager, competitors' from public ad libraries) into a sheet.
2. Run the three questions per ad and join the results to spend and CTR.
3. Look for angles that are overused by competitors and underused by you.

## Common mistakes
- Hook strength is subjective. Calibrate the rubric on 20 ads your team has already judged.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/ad-classification

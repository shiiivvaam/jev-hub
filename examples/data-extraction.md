# Jev for extracting dates, emails and amounts

Yes, in a specific way: Jev chooses, and code does the rest. For values such as emails, phone numbers and amounts, a pattern match finds the candidates and Jev picks the one the question asks for, so it cannot invent a value. For dates, Jev reads the parts the text names (month, day, year or 'next Thursday') and code builds and checks the date. Both are TypeSafe cookbooks.

**Fit:** Good fit

**Good when**
- Documents contain several values of the same kind and the right one depends on the words around it.
- A wrong digit is costly, so the value must be copied exactly from the text.
- Dates appear in mixed forms, including relative ones such as 'tomorrow'.

**Avoid when**
- The document has a fixed layout. A parser is cheaper and exact.
- You need free-form text extracted (a summary, a reason). Jev picks from options; it does not write.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`data-extraction.json`](./data-extraction.json):

```json
{
  "model": "jev-latest",
  "state": "From: Billing <billing@acme.io>\nReply-To: dana.lee@gmail.com\nBody: Please send the receipt to my personal address, not the billing alias. Total due: $1,315.50. Credit applied: -$84.50.",
  "questions": {
    "receipt_address": {
      "type": "choice",
      "instructions": "Which address should the receipt be sent to?",
      "criteria": [
        "billing@acme.io",
        "dana.lee@gmail.com",
        "none"
      ]
    },
    "total_due": {
      "type": "choice",
      "instructions": "Which amount is the total due?",
      "criteria": [
        "$1,315.50",
        "-$84.50",
        "none"
      ]
    }
  }
}
```

## How to wire it in
1. Find every candidate value with a pattern match tuned to over-find, and remove duplicates.
2. Ask Jev a Choice whose options are those candidates, plus 'none'.
3. Copy the chosen value exactly and normalise it in code (for example a phone number to international format).
4. For dates, ask for the parts the text names and let code build the date, counting from today for relative dates.

## Common mistakes
- Jev can only pick what the pattern found. If a value is missing from the options, widen the pattern.
- Never let Jev do calendar arithmetic. TypeSafe lists date comparison as a known weak spot.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/data-extraction

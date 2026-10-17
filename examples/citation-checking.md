# Jev for checking citations

Yes, with a little code around it. A string match first catches quotes that do not exist in the source. Then one Jev Choice question per citation reads the quoted section and decides whether it supports the claim, contradicts it or does not address it. In TypeSafe's own cookbook, all four planted failures among eight citations were caught.

**Fit:** Strong fit

**Good when**
- An LLM writes answers or reports with citations to documents you hold.
- A wrong citation is costly: legal, medical, financial or technical writing.
- You want people to check only the doubtful citations, not all of them.

**Avoid when**
- You do not have the source documents. Jev can only judge a quote against the text you send it.
- Quotes are loosely paraphrased. An exact string match marks those as made up, so you would need fuzzy matching first.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`citation-checking.json`](./citation-checking.json):

```json
{
  "model": "jev-latest",
  "state": "Claim: The \"exp\" claim is required in every JSON Web Token.\nQuoted section (RFC 7519, 4.1.4): The \"exp\" (expiration time) claim identifies the expiration time on or after which the JWT MUST NOT be accepted for processing. ... Use of this claim is OPTIONAL.",
  "questions": {
    "verdict": {
      "type": "choice",
      "instructions": "Does the quoted section support the claim?",
      "criteria": {
        "supports": "The section states or directly implies the claim",
        "contradicts": "The section says the opposite of the claim",
        "unsupported": "The section does not address the claim"
      }
    }
  }
}
```

## How to wire it in
1. Normalise spaces and quote marks, then look for each quote in the source as plain text. A quote that is not there is fabricated, with no model call needed.
2. Send the claim plus the section the quote came from to Jev as one Choice question.
3. Accept the verdict when confidence is at or above your threshold (the cookbook uses 0.8); below it, a person confirms.
4. Start with a high threshold and lower it as you see how Jev does on your own documents.

## Common mistakes
- A quote can be real and still not back the claim. That is why the string match alone is not enough.
- The cookbook splits an RFC by its section numbers; documents of another shape need their own splitting.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/citation-checking

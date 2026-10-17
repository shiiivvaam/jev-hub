# Jev for classifying documents into many categories

Yes, and its confidence tells you which answers to trust. In TypeSafe's cookbook, 60 company annual reports were classified into 75 industry groups with one Choice question each. A confidence cutoff of 0.9 split them in half: the confident half was right 90% of the time, the other half 40%, and reporting that half one level up the hierarchy raised it to 70%.

**Fit:** Good fit

**Good when**
- Your categories form a hierarchy, so an unsure answer can fall back to the broader group.
- There are many categories (Jev's Choice takes up to 255 options).
- A broad but right label is more useful than a precise but wrong one.

**Avoid when**
- Every document must get a precise label with no review. Plan for the unsure half.
- Your labels are not described anywhere. Each option needs words that describe what belongs in it.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`document-classification.json`](./document-classification.json):

```json
{
  "model": "jev-latest",
  "state": "Item 1. Business. We operate 140 branches across three states, taking deposits and making commercial and residential real-estate loans...",
  "questions": {
    "group": {
      "type": "choice",
      "instructions": "Which industry group best describes the business this company runs today?",
      "criteria": {
        "depository_institutions": "Banks, savings institutions and credit unions",
        "insurance_carriers": "Life, health, property and casualty insurers",
        "business_services": "Software, advertising, staffing and other services to businesses",
        "chemicals": "Chemicals, plastics, drugs and allied products"
      }
    }
  }
}
```

## How to wire it in
1. Describe each category by what falls inside it, not only by its name.
2. Send one document with one Choice question over all the categories.
3. Keep the label when confidence is high (the cookbook uses 0.9).
4. Below the cutoff, report the broader parent category instead; it follows from the same answer, so there is no second call.

## Common mistakes
- Hard documents look like easy ones from the label alone. Read the confidence, not just the winning option.
- Send the part of the document that describes the business, not the whole filing.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/document-classification

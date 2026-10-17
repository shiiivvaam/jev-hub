# Jev Hub

Everything about Jev in one place: use cases, real costs, a free cost calculator, community builds and dated news. This repo holds the ready-to-run examples, cost data and the directory of community builds behind [jevhub.io](https://jevhub.io).

**Jev** is TypeSafe AI's decision model. It answers a defined question about some input with a typed value and a probability, instead of writing text. It is made by [TypeSafe AI](https://typesafe.ai).

> Jev Hub is an independent project. It is not affiliated with TypeSafe AI.

## Contents

- [What is Jev, in plain English](#what-is-jev-in-plain-english)
- [Jev terms explained](#jev-terms-explained)
- [How a request works](#how-a-request-works)
- [Writing questions that give useful answers](#writing-questions-that-give-useful-answers)
- [Turning confidence into actions](#turning-confidence-into-actions)
- [What Jev can't do](#what-jev-cant-do)
- [Where the name comes from](#where-the-name-comes-from)
- [Quickstart](#quickstart)
- [Use cases and ready-to-run examples](#use-cases-and-ready-to-run-examples)
- [What Jev costs](#what-jev-costs)
- [What people are building](#what-people-are-building)
- [News and comparisons](#news-and-comparisons)
- [Data files](#data-files)

## What is Jev, in plain English

Jev is a decision model made by TypeSafe AI, released on 15 September 2026. It does one job: it reads some input and answers questions about it by choosing from answers you have defined in advance. It never writes text.

A language model such as GPT, Claude or Gemini answers "Is this email urgent?" with a paragraph that your code then has to read and interpret. Jev answers with one of your options, for example `urgent`, plus a probability for each option. Your code can act on that directly, without parsing anything.

Because it skips text generation, Jev is fast (TypeSafe reports 70 to 500 ms per request) and cheap ($0.042 per million input tokens, output free). That makes it practical to run a decision on every email, ticket or lead instead of a sample.

It is built for the small decisions software makes thousands of times a day: which team gets this ticket, is this lead worth a call, is this post spam, should a person look at this. It is not built for chat, writing, summaries or code.

## Jev terms explained

**Decision model.** A model that returns a choice from a fixed set of answers instead of generating text. Jev was the first widely used one.

**System One model.** TypeSafe's name for this kind of model, after Daniel Kahneman's *Thinking, Fast and Slow*: System 1 is fast and intuitive, System 2 slow and deliberate. Text-generating models are the deliberate kind; Jev is built for the fast kind.

**State.** The input you want a decision about: an email, a support ticket, a lead record, a list of page elements. It can be plain text, a JSON object or a list of text items. Text by default: image input is experimental (TypeSafe, since 14 October), and there is no audio or video.

**Question.** One thing you want decided about the state. A request can carry several questions, and each one gets its own answer.

**Question ID.** The name you give a question, such as `category` or `urgency`. It comes back as the key for that answer in the response. The model never sees it, so the full question has to be in the instructions.

**Instructions.** The question itself, in plain words: "What kind of email is this?"

**Criteria.** The answers a question accepts, and what each one means. Writing clear criteria is most of the work of using Jev well.

**Choice.** A question type that picks one option from a list you define (up to 255 options), such as which team should handle a ticket. Each option has a name and a short description.

**Score.** A question type that places the state on an ordered scale you describe in words (2 to 10 levels), such as Whenever / This week / Today / Within the hour. The returned score is probability-weighted, so it can land between two levels: 2.31 means "mostly Today, with some chance of Within the hour".

**Noul.** A question type for yes/no statements. It returns the probability that the statement is true, for example "Does this email need a human?". You can say what counts as true and as false to handle edge cases.

**Probabilities.** For Choice and Score answers, Jev returns a probability for every option, not just the winner. A 0.91 / 0.05 / 0.04 split is a clear answer; 0.45 / 0.44 is a close call.

**Confidence.** A single number from 0 to 1 that sums up how clear the answer is: 1 when all the probability sits on one option, 0 when it is spread evenly. Choice and Score answers carry it; Noul answers don't, because the Noul value is already a probability.

**Calibration.** The idea that a confidence of 0.9 should be right about 90% of the time. TypeSafe says Jev is trained for it. Check it on your own data before relying on it.

**Threshold.** The confidence level you choose for acting automatically. Above it, your code acts; below it, the item goes to a person or a larger model. Set a higher bar for actions that are costly to get wrong.

**Batching.** Sending all the questions about one input in a single request. The state is read once, so three questions cost little more than one.

**Tokens.** The units Jev bills by, roughly four characters of text each. You pay for input tokens only: the state plus your questions and criteria.

**Model name.** You send `jev-latest`, an alias for the current version, or pin a version such as `jev-1.13.0` so results don't change under you.

**Limits.** Up to 64,000 tokens per request in total, and 32,000 for the state plus the longest single question.

**Playground.** TypeSafe's page for trying Jev in the browser: paste an input, add a question, see the probabilities. No code needed.

**API.** How software calls Jev: one `POST` request to `https://api.typesafe.ai/v1/systemone`, with your TypeSafe API key as a Bearer token.

**Python SDK.** TypeSafe's Python package (`pip install typesafe-sdk`, Python 3.10 or later). It reads `TYPESAFE_API_KEY` from the environment and uses `jev-latest` by default.

**Agent skill.** A package that teaches a coding agent the Jev API, so the agent can write the integration for you (`npx skills add typesafe-ai/skills --skill typesafe-ai`).

**Gateways.** Besides TypeSafe's own API, Jev is available through the Vercel AI Gateway, OpenRouter and LiteLLM.

## How a request works

A request has three parts: the model, the state and a map of questions.

```json
{
  "model": "jev-latest",
  "state": "From: Dana Lee <dana@acme.io>\nSubject: Invoice #4471 charged twice\nBody: Our card was charged twice for March. Can you refund the duplicate today? Our finance close is tomorrow.",
  "questions": {
    "category": {
      "type": "choice",
      "instructions": "What kind of email is this?",
      "criteria": {
        "needs_reply": "A person expecting a response from us",
        "updates": "Notifications, receipts, product updates",
        "promotions": "Marketing and newsletters",
        "spam": "Unwanted or suspicious mail"
      }
    },
    "needs_human": {
      "type": "noul",
      "instructions": "Does this email involve money, legal risk or an upset customer?"
    }
  }
}
```

Each answer comes back under the question ID you chose. The values below are illustrative; the shape follows TypeSafe's API reference.

```json
{
  "model": "jev-1.13.0",
  "answers": {
    "category": {
      "type": "choice",
      "choice": "needs_reply",
      "confidence": 0.84,
      "probabilities": { "needs_reply": 0.91, "updates": 0.05, "promotions": 0.03, "spam": 0.01 }
    },
    "needs_human": { "type": "noul", "noul": 0.88 }
  },
  "usage": { "input_tokens": 212, "output_tokens": 31 }
}
```

`choice` is the selected option and `probabilities` gives one probability per option. `noul` is the probability that the statement is true. `usage` reports the input tokens you are billed for.

## Writing questions that give useful answers

1. **Pick the type from what you will do with the answer.** Send it somewhere (a queue, a folder, a label): Choice. Sort or rank by it: Score. Gate on it (block, escalate, flag): Noul. If a Choice has options like low, medium, high, use a Score: the order carries information.
2. **Make Choice options clearly different.** A careful person should be able to tell every option apart. Describe each one in a few words, and add an `other` option so Jev isn't forced into a wrong bucket. Every description is billed as input, so only list options you will act on differently.
3. **Describe every Score level in words.** The levels are your rubric. Write them so two people would put the same item at the same level. Four or five levels is usually enough.
4. **Ask a Noul about one thing.** "Is this spam or abusive?" is two questions; split it. Use the optional true and false criteria for edge cases.
5. **Batch questions about the same input** and name them by what they decide (`queue`, `urgency`), because those names come back as keys.
6. **Keep the state small.** It is usually most of the bill. Send the fields the decision needs: an email's subject and first few hundred words usually decide the category; the visible element list, not raw HTML.

## Turning confidence into actions

Don't act on the top answer alone. A simple pattern that holds up:

- Act automatically when the answer is clear (for example confidence of 0.7 or more, or a Noul of 0.8 or more).
- Send the uncertain middle to a person.
- Log what the person decided next to what Jev said.
- After a few hundred items, adjust the thresholds using that log.

TypeSafe's own example sends anything below 0.5 to a person, and its guidance says thresholds should scale with the cost of being wrong: a destructive action needs a higher bar than a read-only one. Before trusting any setup, label 50 to 100 real items yourself and compare.

## What Jev can't do

- **No text.** No replies, summaries, explanations or code. That stays with a language model.
- **Closed answer sets.** It only chooses from options you define, so you need to know them in advance.
- **No reasoning shown.** You get the decision and its confidence, not why.
- **Text first.** Image input is experimental and not meant for production; no audio or video.
- **It can still be wrong.** The answer is always a valid option, but not always the right one. That is what confidence is for.

Most teams run Jev alongside a language model rather than instead of one: Jev handles the high-volume judgments (route, score, flag, verify) and the language model handles the work that needs words.

## Where the name comes from

According to the launch post by TypeSafe's founder, Diogo Almeida, the name comes from the Jevons paradox. In 1865 the economist William Stanley Jevons observed that as steam engines burned coal more efficiently, Britain burned more coal, not less, because the engines became worth using everywhere. The bet behind Jev is the same: make a decision cheap enough, and software will make millions of them.

## Quickstart

One request, in curl, Python or Node, with no dependencies: [`quickstart/`](./quickstart). You bring your own TypeSafe API key. Nothing here calls Jev for you.

## Use cases and ready-to-run examples

Each page has a working request, when Jev fits, when to avoid it and the usual mistakes.

| Use case | Fit | Example |
|---|---|---|
| [lead scoring](https://jevhub.io/use-cases/lead-scoring) | Strong fit | [request and notes](./examples/lead-scoring.md) |
| [email triage](https://jevhub.io/use-cases/email-triage) | Strong fit | [request and notes](./examples/email-triage.md) |
| [support ticket routing](https://jevhub.io/use-cases/support-ticket-routing) | Strong fit | [request and notes](./examples/support-ticket-routing.md) |
| [content moderation](https://jevhub.io/use-cases/content-moderation) | Good fit | [request and notes](./examples/content-moderation.md) |
| [research and news filtering](https://jevhub.io/use-cases/research-filtering) | Strong fit | [request and notes](./examples/research-filtering.md) |
| [SEO search-intent classification](https://jevhub.io/use-cases/search-intent-classification) | Strong fit | [request and notes](./examples/search-intent-classification.md) |
| [ad and creative classification](https://jevhub.io/use-cases/ad-classification) | Good fit | [request and notes](./examples/ad-classification.md) |
| [semantic search](https://jevhub.io/use-cases/semantic-search) | Good fit | [request and notes](./examples/semantic-search.md) |
| [agent and browser decisions](https://jevhub.io/use-cases/agent-decisions) | Partial fit | [request and notes](./examples/agent-decisions.md) |
| [LLM guardrails](https://jevhub.io/use-cases/llm-guardrails) | Strong fit | [request and notes](./examples/llm-guardrails.md) |
| [checking citations](https://jevhub.io/use-cases/citation-checking) | Strong fit | [request and notes](./examples/citation-checking.md) |
| [filtering RAG passages](https://jevhub.io/use-cases/rag-passage-filtering) | Strong fit | [request and notes](./examples/rag-passage-filtering.md) |
| [re-ranking search results](https://jevhub.io/use-cases/search-reranking) | Strong fit | [request and notes](./examples/search-reranking.md) |
| [matching duplicate records](https://jevhub.io/use-cases/record-matching) | Good fit | [request and notes](./examples/record-matching.md) |
| [classifying documents into many categories](https://jevhub.io/use-cases/document-classification) | Good fit | [request and notes](./examples/document-classification.md) |
| [extracting dates, emails and amounts](https://jevhub.io/use-cases/data-extraction) | Good fit | [request and notes](./examples/data-extraction.md) |

## What Jev costs

Jev lists **$0.042 per million input tokens**, with no charge for output (checked 22 September 2026). A typical email costs a fraction of a cent to classify. The formula, a cost table for 16 typical workloads and CSV/JSON data are in [`costs/`](./costs). Set your own volume in the [cost calculator](https://jevhub.io/calculator).

## What people are building

249 community projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one.

**Curated picks**

- [Voice-controlled computer use for the Mac](https://x.com/instantricecook/status/2100814590300889426) by [Andy Gao](https://x.com/instantricecook): Dictate a command and the Mac starts acting on it before the sentence is finished.
- [jevmeter: a live BS meter for any video](https://x.com/chetaslua/status/2100473581251748216) by [Chetaslua](https://x.com/chetaslua): Scores every sentence of a video against a set of yes/no questions and renders the result as an on-screen meter.
- [JEV: how it works and what you can build](https://www.youtube.com/watch?v=o1CogAtWdBk) by [Riley Brown](https://www.youtube.com/@rileybrownai): Riley Brown walks through how Jev works and builds with it on screen.
- [Hide posts on X with plain-language rules](https://x.com/marcelpociot/status/2100520134481735729) by [Marcel Pociot](https://x.com/marcelpociot): A browser extension that collapses posts on X matching rules written in everyday language.
- [Model router](https://x.com/ephraimduncan/status/2100454070536351824) by [Duncan](https://x.com/ephraimduncan): Sends each request to whichever model suits it best.
- [Jev Router on OpenRouter](https://x.com/OpenRouter/status/2103610898690855161) by [OpenRouter](https://x.com/OpenRouter): A packaged router on OpenRouter that picks the model and reasoning effort for each request.
- [jev-drone: a camera-only autonomous drone](https://x.com/RomanSlack1/status/2100335978229690683) by [Roman Slack](https://x.com/RomanSlack1): A simulated quadrotor that flies an obstacle course using only its onboard camera.
- [Jev: the ultimate classification model?](https://www.youtube.com/watch?v=X117w2Rark8) by [Sam Witteveen](https://www.youtube.com/@samwitteveenai): Sam Witteveen tests Jev on a range of classification tasks and looks at how it differs from LLMs.
- [Fast app testing with OpenCode](https://x.com/Neriousy/status/2100287208166969746) by [Filip](https://x.com/Neriousy): A demo of an AI agent clicking through an app under test at high speed.
- [Jev Review: staged code review](https://github.com/devagrawal09/jev-review) by [Dev Agrawal](https://github.com/devagrawal09): A code-review workflow for diffs or whole codebases, with a quiet local dashboard.
- [jevgrep: find code by asking what it does](https://github.com/dzhng/jevgrep) by [David Zhang](https://github.com/dzhng): A CLI that points coding agents at the right files for an unfamiliar task.
- [What is Jev and how to use it?](https://www.youtube.com/watch?v=ZgXej_9isxY) by [Codevolution](https://www.youtube.com/@Codevolution): A developer tutorial on what Jev is and how to call it from an application.
- [jgrep: grep where the pattern is a description](https://github.com/keltokhy/jgrep) by [keltokhy](https://github.com/keltokhy): Filters lines of text by meaning, for example 'a user is getting frustrated' in a live log.
- [Jevmail: open-source Gmail triage](https://github.com/fazlerocks/jevmail) by [Syed Fazle Rahman](https://github.com/fazlerocks): Sorts a Gmail inbox into Needs reply, Updates, Promos, Sales and Spam, read-only and running locally.
- [Jev plays Super Mario Bros.](https://github.com/fhshaik/typesafe-mario) by [fhshaik](https://github.com/fhshaik): An agent that plays the original Super Mario Bros. from emulator data, not screenshots.
- [Shapeshift: an input that becomes what you mean](https://github.com/anishfn/shapeshift) by [Anish Gupta](https://github.com/anishfn): One text box that turns into an event card, checklist, timer, bill splitter and more as you type.

**Browse by topic**

- [Coding agents](./builds/coding-agents.md) (27)
- [Code search](./builds/code-search.md) (11)
- [Computer and browser use](./builds/computer-and-browser-use.md) (22)
- [Voice control](./builds/voice-control.md) (9)
- [Email and messages](./builds/email-and-messages.md) (9)
- [Content and social](./builds/content-and-social.md) (29)
- [Search and ranking](./builds/search-and-ranking.md) (9)
- [Agent memory](./builds/agent-memory.md) (6)
- [Model routing](./builds/model-routing.md) (12)
- [Data and databases](./builds/data-and-databases.md) (12)
- [Trading and finance](./builds/trading-and-finance.md) (6)
- [Games and simulations](./builds/games-and-simulations.md) (16)
- [Hiring](./builds/hiring.md) (2)
- [Home and devices](./builds/home-and-devices.md) (7)
- [Safety and moderation](./builds/safety-and-moderation.md) (7)
- [SDKs and integrations](./builds/sdks-and-integrations.md) (17)
- [Tutorials](./builds/tutorials.md) (21)
- [Explainers](./builds/explainers.md) (27)

Filter and search them all at [jevhub.io/builds](https://jevhub.io/builds). Made something with Jev? [Submit a build](https://jevhub.io/builds/submit).

## News and comparisons

- 2026-10-15: [Jev 1.14 can read images. Should you care?](https://jevhub.io/updates/jev-1-14-images-box-and-longer-context)
- 2026-10-13: [How Jack & Jill cut screening costs 88% with Jev](https://jevhub.io/updates/jack-and-jill-cuts-screening-costs-88-percent-with-jev)
- 2026-10-12: [Jev just got three big rivals](https://jevhub.io/updates/openai-aws-cloudflare-release-decision-models)
- 2026-10-12: [TypeSafe raises $870M: what it means for Jev](https://jevhub.io/updates/typesafe-raises-870-million-series-a)
- [Jev vs OpenAI's Decisions API](https://jevhub.io/jev-vs-openai-decisions-api)
- [Jev vs open models](https://jevhub.io/jev-vs-open-decision-models)
- [Jev vs Laya](https://jevhub.io/jev-vs-laya)
- [Jev vs ChatGPT, Claude and other LLMs](https://jevhub.io/jev-vs-llms)
  - [Jev vs ChatGPT](https://jevhub.io/jev-vs-chatgpt)
  - [Jev vs Claude](https://jevhub.io/jev-vs-claude)
  - [Jev vs Gemini](https://jevhub.io/jev-vs-gemini)

Every article is dated, links its sources and says which claims are the companies' own.

## Data files

Machine-readable, regenerated from the site: [`data/builds.json`](./data/builds.json), [`data/use-cases.json`](./data/use-cases.json), [`data/updates.json`](./data/updates.json), [`costs/use-case-costs.json`](./costs/use-case-costs.json).

## Licence

[MIT](./LICENSE). Project descriptions are Jev Hub's own wording; every project belongs to its author. Prices and limits belong to TypeSafe AI and can change.

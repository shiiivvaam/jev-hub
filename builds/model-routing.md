# Model routing: community builds with Jev

7 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/model-routing).

## [Model router](https://x.com/ephraimduncan/status/2100454070536351824)
By [Duncan](https://x.com/ephraimduncan), 2026-09-17

Sends each request to whichever model suits it best.

How Jev is used: Jev reads the incoming request and chooses the model from a list; the request is then forwarded to that model.

## [Jev Router on OpenRouter](https://x.com/OpenRouter/status/2103610898690855161)
By [OpenRouter](https://x.com/OpenRouter), 2026-09-25

A packaged router on OpenRouter that picks the model and reasoning effort for each request.

How Jev is used: Before each turn, Jev scores the prompt on difficulty and precision and checks whether a cheaper or stronger model fits, balancing quality, speed and cost.

## [jev-router for Claude Code and Codex](https://github.com/dirien/jev-router)
By [Engin Diri](https://github.com/dirien), 2026-09-24

A local proxy that picks a fast, balanced or frontier model for each turn of a coding session.

How Jev is used: When you send a new message, Jev decides which tier the work needs, while the router avoids switches that would waste the prompt cache.

## [Codex Sift: the cheapest model that can do the turn](https://github.com/romanmeclazcke/codex-sift)
By [Roman Meclazcke](https://github.com/romanmeclazcke), 2026-09-19

Routes each Codex turn to the cheapest model lane that should handle it.

How Jev is used: On every user turn, Jev judges how hard the request is before Codex spends premium quota on it.

## [Automatic model choice for image and video generation](https://x.com/higgsfield_ai/status/2101024623370567913)
By [Higgsfield AI](https://x.com/higgsfield_ai), 2026-09-18

Picks the best-suited image or video model for each prompt on the Higgsfield API.

How Jev is used: Jev evaluates the prompt and selects the most fitting generation model from Higgsfield's catalogue.

## [Agent Router: pick the right coding agent for a task](https://x.com/nidhisinghattri/status/2100617830890885415)
By [Nidhi Singh](https://x.com/nidhisinghattri), 2026-09-17

A command-line tool that chooses the coding agent, model and effort level for a task, then launches it.

How Jev is used: Fixed rules filter your subscriptions by quota; Jev ranks what's left for the task and picks the effort. The chosen agent (Cursor, Claude Code, Codex or OpenCode) starts in a Herdr pane.

## [Criteria-based model routing](https://x.com/eve/status/2100430918762832180)
By [eve](https://x.com/eve), 2026-09-17

Very fast model routing driven by criteria you define.

How Jev is used: Jev scores each request against the routing criteria and the highest-scoring model handles it.


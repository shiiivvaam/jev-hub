# Model routing: community builds with Jev

12 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/model-routing).

## [Model router](https://x.com/ephraimduncan/status/2100454070536351824)
By [Duncan](https://x.com/ephraimduncan), 2026-09-17

Sends each request to whichever model suits it best.

How Jev is used: Jev reads the incoming request and chooses the model from a list; the request is then forwarded to that model.

## [Jev Router on OpenRouter](https://x.com/OpenRouter/status/2103610898690855161)
By [OpenRouter](https://x.com/OpenRouter), 2026-09-25

A packaged router on OpenRouter that picks the model and reasoning effort for each request.

How Jev is used: Before each turn, Jev scores the prompt on difficulty and precision and checks whether a cheaper or stronger model fits, balancing quality, speed and cost.

## [Astra-Ares: adaptive reasoning effort for Codex](https://github.com/miuuyy/Astra-Ares)
By [vechen](https://github.com/miuuyy), 2026-09-22

A reference implementation that adjusts how hard GPT-6 reasons during Codex tasks.

How Jev is used: Jev decides how much reasoning effort each step needs, to reduce token use. The author describes it as an experimental early preview that runs a patched Codex CLI.

## [Clonk: launching agents on a canvas instantly](https://x.com/0xPaulius/status/2101312576252481785)
By [Paulius 🏴‍☠️](https://x.com/0xPaulius), 2026-09-19

An agent orchestrator that skips the slow language-model loop for routing.

How Jev is used: Jev launches agents on a canvas instantly, which the author credits for making it fast.

## [Automatic model choice for image and video generation](https://x.com/higgsfield_ai/status/2101024623370567913)
By [Higgsfield AI](https://x.com/higgsfield_ai), 2026-09-18

Picks the best-suited image or video model for each prompt on the Higgsfield API.

How Jev is used: Jev evaluates the prompt and selects the most fitting generation model from Higgsfield's catalogue.

## [Hermes Jev Skills: a second brain for the small decisions](https://github.com/kerpopule/hermes-jev-skills)
By [Steve Darlow](https://github.com/kerpopule), 2026-09-18

Skills that give coding agents a cheap, fast judge for decisions such as which model should answer.

How Jev is used: Jev handles model routing, memory, compaction, skill selection and browser actions for Hermes agents, and the skills also work with Claude Code and Codex.

## [JevRouter: a lightweight router for models, tools and subagents](https://github.com/BillionsBobby/JevRouter)
By [BillionsBobby](https://github.com/BillionsBobby), 2026-09-18

A router that treats models, subagents, skills, tools and plugins as one candidate set.

How Jev is used: Jev answers one typed Choice question about which should handle the next step, and the router enforces availability, permissions, risk and confirmation around the answer.

## [A Slack agent made twice as fast](https://x.com/johnyeo_/status/2100987661926252737)
By [John Yeo](https://x.com/johnyeo_), 2026-09-18

A write-up of speeding up a Slack agent.

How Jev is used: Jev first classifies the best skill, tool and parameters for the prompt before handing it to the agent, which the authors say made it twice as fast.

## [Agent Router: pick the right coding agent for a task](https://x.com/nidhisinghattri/status/2100617830890885415)
By [Nidhi Singh](https://x.com/nidhisinghattri), 2026-09-17

A command-line tool that chooses the coding agent, model and effort level for a task, then launches it.

How Jev is used: Fixed rules filter your subscriptions by quota; Jev ranks what's left for the task and picks the effort. The chosen agent (Cursor, Claude Code, Codex or OpenCode) starts in a Herdr pane.

## [Criteria-based model routing](https://x.com/eve/status/2100430918762832180)
By [eve](https://x.com/eve), 2026-09-17

Very fast model routing driven by criteria you define.

How Jev is used: Jev scores each request against the routing criteria and the highest-scoring model handles it.

## [Jev as a chief of staff for bots](https://x.com/milindlabs/status/2100515910754750741)
By [Milind S](https://x.com/milindlabs), 2026-09-17

An agent orchestration demo where Jev picks the right teammate for a task.

How Jev is used: Jev reads the task, wakes the right agent and gives each the right model, on OpenMausBot.

## [jev-router: model routing for Claude Code and Codex](https://github.com/gargpratyush/jev-router)
By [Pratyush Garg](https://github.com/gargpratyush), 2026-09-16

A command-line wrapper that picks a fast or strong model for each turn.

How Jev is used: Jev sends simple work to the fast tier and difficult work to the strong tier, while each tool keeps its own interface, sessions and login.


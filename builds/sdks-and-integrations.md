# SDKs and integrations: community builds with Jev

17 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/sdks-and-integrations).

## [stuntd: a local proxy that learns your typed decisions](https://github.com/bladedevoff/stuntd)
By [BladeDev](https://github.com/bladedevoff), 2026-09-23

A self-hosted proxy that records the typed decisions an app makes and learns to answer them itself.

How Jev is used: It speaks the Jev System One protocol and OpenAI's Decisions API, so an app can point at it instead of a hosted model.

## [A 404 page that fixes your typos](https://x.com/haaarshsingh/status/2102755111244046418)
By [Harsh Singh](https://x.com/haaarshsingh), 2026-09-23

A 404 page that redirects to the page you meant.

How Jev is used: Built with Jev, it works out the correct address from the mistyped one.

## [System One for TypeScript: write the decision once](https://github.com/iamaamir/system-one)
By [Aamir khan](https://github.com/iamaamir), 2026-09-22

A small provider-neutral TypeScript runtime for bounded AI decisions.

How Jev is used: Code uses the same choice, noul and score calls and can run on Jev, a local model or any compatible endpoint.

## [Jeview: see every Jev call live](https://github.com/andududu/jeview)
By [Mihai Ionescu](https://github.com/andududu), 2026-09-21

A local gateway that records and visualises every Jev call your code makes.

How Jev is used: Point your Jev client at Jeview; it forwards each call with your key, stores it locally and draws it on a live map.

## [System One for Apple Foundation Models](https://github.com/peterfriese/system-one-foundation-models)
By [Peter Friese](https://github.com/peterfriese), 2026-09-21

A Swift bridge that brings decision models into Apple's Foundation Models framework.

How Jev is used: Evaluates typed Swift structs and enums against app state using Jev, or an on-device model when offline.

## [Jev workflow builder: a multiplayer demo](https://github.com/CTNicholas/jev-workflow-builder)
By [Chris Nicholas](https://github.com/CTNicholas), 2026-09-21

A demo of a collaborative workflow builder for Jev built with Liveblocks.

How Jev is used: You wire Jev and language models together, call the workflow through a REST API, preview test runs and see other people's cursors.

## [Spring AI TypeSafe](https://github.com/spring-ai-community/spring-ai-typesafe)
By [Spring AI Community](https://github.com/spring-ai-community), 2026-09-20

A Java client for Jev with Spring AI integrations.

How Jev is used: Uses Jev as a model-as-judge, a guardrail, a retrieval post-processor and a tool index inside Spring AI.

## [Jimothy: turn your Jev usage into small local classifiers](https://github.com/AndrewPrifer/jimothy)
By [Andrew Prifer](https://github.com/AndrewPrifer), 2026-09-20

A tool that trains small, very fast classifiers from Jev-compatible examples.

How Jev is used: The trained classifier runs locally in a browser or Node.js, so repeated judgments no longer need an API call.

## [Jev × WebMCP Chrome extension](https://github.com/sdras/jev-webmcp-extension)
By [Sarah Drasner](https://github.com/sdras), 2026-09-19

Turns what you type into WebMCP tool calls on the current page.

How Jev is used: Jev reads the page's tool schemas and predicts the tool and its arguments as you type, with confidence and latency shown.

## [jevcache: a decision cache](https://github.com/hyperspaceai/jevcache)
By [HyperspaceAI](https://github.com/hyperspaceai), 2026-09-18

Caches Jev decisions locally so repeated questions are free and replayable in CI.

How Jev is used: Treats each decision as a function of model, questions and input, and memoises it; your key never leaves your machine.

## [ruby_decision_model](https://github.com/obie/ruby_decision_model)
By [Obie Fernandez](https://github.com/obie), 2026-09-18

A Ruby gem for decision models such as Jev, with no runtime dependencies.

How Jev is used: One client talks to Jev through OpenRouter by default or TypeSafe's API directly.

## [Jev Chat: a command bar that calls tools without an LLM](https://github.com/w3cj/jev-chat)
By [CJ](https://github.com/w3cj), 2026-09-18

A chat-shaped command bar that calls real tools while no language model writes anything.

How Jev is used: Each turn a classifier picks what was asked, which tool, which argument values and whether to confirm, and code builds the reply from the tools' own data.

## [hono-jev-router: route requests by meaning](https://github.com/yusukebe/hono-jev-router)
By [Yusuke Wada](https://github.com/yusukebe), 2026-09-18

An experimental router for the Hono web framework.

How Jev is used: You describe a request in plain words and Jev decides which description fits the incoming request.

## [Website to App: turn a URL into a native mobile app](https://x.com/chddaniel/status/2100919415554617537)
By [Daniel Ch](https://x.com/chddaniel), 2026-09-18

A service that builds a native mobile app from a website address.

How Jev is used: Jev decides how to rebuild the site as a native app, then a shipping tool submits it to the app stores. The team says it has used it internally for iOS and Android apps.

## [Jev MCP server for agent harnesses](https://x.com/jkudish/status/2100413576284712999)
By [Joey Kudish](https://x.com/jkudish), 2026-09-17

A proof-of-concept MCP server that adds Jev to an existing agent setup.

How Jev is used: Agents call it to check claims against evidence, screen content before it enters their context and rank candidates by meaning.

## [System One Connector: Jev as an MCP tool](https://github.com/itsmostafa/system-one-connector)
By [Mostafa](https://github.com/itsmostafa), 2026-09-17

An MCP connector that gives Claude Code, Codex and other agents direct access to Jev.

How Jev is used: The agent asks a question such as whether something is urgent or which team owns it and gets back a number or an option it can use in an if statement.

## [SemDecide: decisions for Unix pipelines and CI](https://github.com/sharziki/semdecide)
By [Sharvil Saxena](https://github.com/sharziki), 2026-09-16

Pipe in text and get a predicate, route, score or filtered stream with a stable exit code.

How Jev is used: Jev answers the semantic question; SemDecide handles the parsing, retries and confidence thresholds.


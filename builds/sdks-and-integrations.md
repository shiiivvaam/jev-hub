# SDKs and integrations: community builds with Jev

22 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/sdks-and-integrations).

## [llm-typesafe: Jev in Simon Willison's LLM](https://github.com/simonw/llm-typesafe)
By [Simon Willison](https://github.com/simonw), 2026-09-22

A plugin that adds Jev to the LLM command-line tool.

How Jev is used: Ask yes/no, choice or score questions about any text from the terminal and get Jev's typed answer.

## [go-jev: Go SDK and CLI](https://github.com/mattn/go-jev)
By [mattn](https://github.com/mattn), 2026-09-23

A Go SDK for Jev with a command-line tool for Unix pipelines.

How Jev is used: Wraps Jev's yes/no, choice and score questions in idiomatic Go types.

## [Jeview: see every Jev call live](https://github.com/andududu/jeview)
By [Mihai Ionescu](https://github.com/andududu), 2026-09-21

A local gateway that records and visualises every Jev call your code makes.

How Jev is used: Point your Jev client at Jeview; it forwards each call with your key, stores it locally and draws it on a live map.

## [System One for Apple Foundation Models](https://github.com/peterfriese/system-one-foundation-models)
By [Peter Friese](https://github.com/peterfriese), 2026-09-21

A Swift bridge that brings decision models into Apple's Foundation Models framework.

How Jev is used: Evaluates typed Swift structs and enums against app state using Jev, or an on-device model when offline.

## [Spring AI TypeSafe](https://github.com/spring-ai-community/spring-ai-typesafe)
By [Spring AI Community](https://github.com/spring-ai-community), 2026-09-20

A Java client for Jev with Spring AI integrations.

How Jev is used: Uses Jev as a model-as-judge, a guardrail, a retrieval post-processor and a tool index inside Spring AI.

## [Jev Spring Boot starter](https://github.com/danvega/jev-spring-boot-starter)
By [Dan Vega](https://github.com/danvega), 2026-09-20

One dependency to ask Jev typed questions from a Spring Boot app.

How Jev is used: Add the starter, set an API key and inject a JevClient.

## [Jevalyn: decisions in your Rails app](https://github.com/Ray-Hughes/jevalyn)
By [Raymond Hughes](https://github.com/Ray-Hughes), 2026-09-20

A Rails-native wrapper that puts Jev decisions into your app's control flow.

How Jev is used: Declare a decision class with questions and a confidence threshold, then evaluate it inside a request in about the time of a database query.

## [jev: a semantic if statement for the terminal](https://github.com/shaharia-lab/jev-cli)
By [Shaharia Lab](https://github.com/shaharia-lab), 2026-09-19

A command-line tool that turns Jev's answers into exit codes, JSON and MCP tools.

How Jev is used: Ask a typed question about any text and branch on the probability in shell scripts, CI jobs or agents.

## [PHP SDK for Jev](https://github.com/sanmai/typesafe-ai-php)
By [Alexey Kopytko](https://github.com/sanmai), 2026-09-19

A PHP client for Jev, installable with Composer.

How Jev is used: Build a request with a fluent interface and get one typed answer per question.

## [Jev × WebMCP Chrome extension](https://github.com/sdras/jev-webmcp-extension)
By [Sarah Drasner](https://github.com/sdras), 2026-09-19

Turns what you type into WebMCP tool calls on the current page.

How Jev is used: Jev reads the page's tool schemas and predicts the tool and its arguments as you type, with confidence and latency shown.

## [JevForm: a form that decides what to ask next](https://x.com/TamirSPIRITT/status/2101079101997982037)
By [Tamir](https://x.com/TamirSPIRITT), 2026-09-18

A form that branches on its own, choosing the next question from the answers so far.

How Jev is used: Instead of hand-written if/then logic, Jev picks the next question. The interface is rendered with Vercel's json-render.

## [jevals: a local workbench for Jev requests](https://x.com/Dayhaysoos/status/2100968892591968320)
By [Nick DeJesus](https://x.com/Dayhaysoos), 2026-09-18

A local tool for testing Jev requests and checking whether results improve over time.

How Jev is used: Lets you build and mix yes/no, choice and score requests, run them against Jev and compare the answers.

## [jevcache: a decision cache](https://github.com/hyperspaceai/jevcache)
By [HyperspaceAI](https://github.com/hyperspaceai), 2026-09-18

Caches Jev decisions locally so repeated questions are free and replayable in CI.

How Jev is used: Treats each decision as a function of model, questions and input, and memoises it; your key never leaves your machine.

## [ruby_decision_model](https://github.com/obie/ruby_decision_model)
By [Obie Fernandez](https://github.com/obie), 2026-09-18

A Ruby gem for decision models such as Jev, with no runtime dependencies.

How Jev is used: One client talks to Jev through OpenRouter by default or TypeSafe's API directly.

## [AI Provider for Jev (WordPress)](https://github.com/soderlind/ai-provider-for-jev)
By [Per Søderlind](https://github.com/soderlind), 2026-09-18

Connects WordPress to Jev for structured decisions.

How Jev is used: Exposes choice, score and yes/no questions to WordPress plugins and themes.

## [Jev MCP server for agent harnesses](https://x.com/jkudish/status/2100413576284712999)
By [Joey Kudish](https://x.com/jkudish), 2026-09-17

A proof-of-concept MCP server that adds Jev to an existing agent setup.

How Jev is used: Agents call it to check claims against evidence, screen content before it enters their context and rank candidates by meaning.

## [Easy-Jev: an interactive Jev demo](https://x.com/rory_builds/status/2100606378184171682)
By [Rory Garton-Smith](https://x.com/rory_builds), 2026-09-17

A demo anyone can try: change the inputs and watch the classifications update in real time.

How Jev is used: Each change sends the new input to Jev and shows the returned probabilities live.

## [A syntax highlighter for any language](https://x.com/imarikchakma/status/2100587614927741435)
By [Arik Chakma](https://x.com/imarikchakma), 2026-09-17

Highlights code in any language, including one the author made up.

How Jev is used: Jev classifies each token into a highlighting category instead of relying on a grammar file.

## [GPT vs Jev, side by side](https://x.com/nerdytanay/status/2100465397267144815)
By [Tanay](https://x.com/nerdytanay), 2026-09-17

A live tool comparing GPT and Jev on the same task.

How Jev is used: Runs the same decision through both and reports money spent, time taken and tokens used.

## [Jev for Elixir OTP](https://github.com/dannote/jev)
By [Danila Poyarkov](https://github.com/dannote), 2026-09-17

Use Jev from Elixir as a peer process you pattern-match on.

How Jev is used: You reply to Jev from a GenServer and its answer arrives as a message, with routing expressed through clause order.

## [jev-mcp: Jev as MCP tools](https://github.com/rashedInt32/jev-mcp)
By [Rashed Parvez](https://github.com/rashedInt32), 2026-09-17

An MCP server and Claude Code plugin that exposes Jev's judgements as tools.

How Jev is used: Agents can classify, score, check and batch-ask, and see Jev's full probabilities rather than a bare label.

## [SemDecide: decisions for Unix pipelines and CI](https://github.com/sharziki/semdecide)
By [Sharvil Saxena](https://github.com/sharziki), 2026-09-16

Pipe in text and get a predicate, route, score or filtered stream with a stable exit code.

How Jev is used: Jev answers the semantic question; SemDecide handles the parsing, retries and confidence thresholds.


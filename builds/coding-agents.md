# Coding agents: community builds with Jev

27 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/coding-agents).

## [Jev Review: staged code review](https://github.com/devagrawal09/jev-review)
By [Dev Agrawal](https://github.com/devagrawal09), 2026-09-16

A code-review workflow for diffs or whole codebases, with a quiet local dashboard.

How Jev is used: Code orchestrates the review; Jev handles bounded judgements at each stage: a risk matrix, file profiles, evidence selection and severity scores.

## [A client follow-up agent with Jev matching requests](https://x.com/akshay_pachaar/status/2109909532352917658)
By [Akshay 🚀](https://x.com/akshay_pachaar), 2026-10-13

An agent built on an open harness that matches client requests to the right GitHub issue.

How Jev is used: The author reports 40 requests matched as accurately as when Opus made every match, with decision cost about 150 times lower.

## [Jev plugin for DeepSeek Harness](https://github.com/luobosibing2/dsh-jev-plugin)
By [CHENG YIZHOU](https://github.com/luobosibing2), 2026-09-27

A native DeepSeek Harness plugin with twelve Jev-powered features.

How Jev is used: Jev selects skills and files, supervises tasks, filters tool output and assists with single-operation approvals; each feature can be switched on separately.

## [Building with TypeSafe Jev: patterns from 150+ projects](https://github.com/aaddrick/building-with-typesafe-jev)
By [Aaddrick](https://github.com/aaddrick), 2026-09-26

An unofficial skill that teaches coding agents to design for Jev, with prior art from community projects.

How Jev is used: Gives the agent typed-question patterns and links to 150+ community builds sorted by how they use Jev, each with a code sketch.

## [Quicksilver: hand bulk judgement calls to Jev](https://github.com/UditAkhourii/quicksilver)
By [Udit Akhouri](https://github.com/UditAkhourii), 2026-09-25

A Claude Code skill that offloads 'which of these matter?' questions to Jev.

How Jev is used: Instead of reading hundreds of files or log lines, Claude asks Jev to sort them and gets back a shortlist with confidence. The author reports 86% fewer Claude tokens on a 12-task benchmark.

## [Claude x Jev: Jev sorts, Claude writes](https://github.com/charlesdove977/claude-x-jev)
By [Charles Dove](https://github.com/charlesdove977), 2026-09-25

A free Claude Code skill that pairs Jev's fast decisions with Claude's writing.

How Jev is used: Commands let Jev classify, pre-sort items so Claude reads only the uncertain ones, and run a quick safety check before tool calls.

## [mu: a coding agent with a judgment kernel](https://github.com/qybaihe/mu)
By [qybaihe](https://github.com/qybaihe), 2026-09-22

A coding agent that hands its routine judgment calls to a small, fast model.

How Jev is used: Jev acts as the judge for decision points such as what stays in context, whether a command is safe and when the work is done, so the large model spends its effort on the code.

## [JevHarness: let a language model write a harness for Jev](https://github.com/TianyuCodings/JevHarness)
By [Tianyu](https://github.com/TianyuCodings), 2026-09-21

A framework where a language model writes a task-specific harness around Jev, then the harness runs without it.

How Jev is used: The harness turns observations into features, builds Jev questions and criteria, and combines the answers into actions. It can be improved with rewards and full execution traces.

## [Jev DSH: a decision plugin for agent harnesses](https://github.com/Devin-AXIS/jev-dsh-decision)
By [Devin-AXIS](https://github.com/Devin-AXIS), 2026-09-20

A plugin that brings Jev's structured decisions to DeepSeek Harness, OpenCode and Codex.

How Jev is used: Jev helps choose tools, skills and task owners and rates the quality of the output, while the original agent keeps planning and executing. The page is mostly in Chinese.

## [jev-use: let Jev take the steps that need no text](https://github.com/shitianfang/jev-use)
By [shitianfang](https://github.com/shitianfang), 2026-09-19

A plugin for Claude Code, Codex and Pi that hands decision-only steps to Jev.

How Jev is used: When a step only needs a decision, Jev takes it; when text must be written, the LLM takes over. The author measures about 230 ms and $0.02 per 1,000 judgements.

## [Jev Code Reviewer: review behaviour, not just diffs](https://github.com/egma-ai/jev-code-reviewer)
By [egma ai](https://github.com/egma-ai), 2026-09-19

A command-line reviewer and agent skill that ranks each change in a review as P0, P1 or P2.

How Jev is used: Jev prioritises what deserves human attention and only P0 changes show by default, while OpenAI explains the changes in plain language.

## [jev-pruner: trim long command output](https://github.com/tamaratran/jev-pruner)
By [tamara tran](https://github.com/tamaratran), 2026-09-18

A Claude Code plugin that trims noisy Bash output before the model reads it.

How Jev is used: Short output passes through untouched; for long output, Jev picks the lines that matter so later turns carry less noise.

## [jev-gateway: Jev chooses the tool, your LLM does the rest](https://github.com/vinilana/jev-gateway)
By [Vinicius Lana](https://github.com/vinilana), 2026-09-18

A local gateway for coding agents that asks Jev which tool to call.

How Jev is used: When the agent is about to choose a tool, the gateway asks Jev instead of the expensive reasoning model. Everything else goes to the usual model, and it works with Codex, Claude Code, OpenCode and Kilo.

## [jev-rules: only the rules that matter, per prompt](https://github.com/EliaAlberti/jev-rules)
By [Elia Alberti](https://github.com/EliaAlberti), 2026-09-18

A Claude Code add-on that shows Claude only the standing rules that apply to each prompt.

How Jev is used: Jev decides which of your rules are relevant to the current request.

## [End-to-end testing with agents and Jev](https://x.com/o_kwasniewski/status/2100966838905585687)
By [Oskar](https://x.com/o_kwasniewski), 2026-09-18

An open-source framework for running end-to-end tests with agents.

How Jev is used: It supports web and mobile and uses Jev for the decisions.

## [A prompt box that picks the agent, model and computer](https://x.com/sawyerhood/status/2100994779291259187)
By [Sawyer Hood](https://x.com/sawyerhood), 2026-09-18

A personal tool that fills in the fields of a prompt box automatically.

How Jev is used: Jev picks the agent, model, computer and folder; a major rewrite goes to a large model with Claude Code and iOS changes run on one of his Macs.

## [Stanley: a Jev-first coding agent](https://github.com/devagrawal09/stanley-code)
By [Dev Agrawal](https://github.com/devagrawal09), 2026-09-17

A command-line tool for checking and understanding code changes, described in plain words.

How Jev is used: Jev routes each request to a workflow; the workflow gathers evidence and asks Jev small fixed-choice questions, and code makes the final call. A general agent is only used as a fallback.

## [Jev Review: quality scores for coding agents](https://github.com/NiazMorshed2007/jev-review)
By [Niaz Morshed](https://github.com/NiazMorshed2007), 2026-09-17

A local MCP server that gives coding agents continuous quality scores while they work.

How Jev is used: Jev scores code on independent dimensions such as correctness, complexity, tests and security; the agent stays responsible for fixing what scores low.

## [SkillRanker: the right skill for the next step](https://github.com/Dicklesworthstone/skillranker)
By [Jeff Emanuel](https://github.com/Dicklesworthstone), 2026-09-17

A Rust CLI that ranks an agent's installed skills for the next step of a session.

How Jev is used: Jev evaluates the agent's live context against the available skills; SkillRanker adds session hooks, safeguards and local feedback.

## [Semantic tool routing for the Pi agent](https://github.com/TheoOliveira/pi-jev)
By [Theo Oliveira](https://github.com/TheoOliveira), 2026-09-17

Activates only the tools and skills a Pi agent needs for the current prompt.

How Jev is used: Jev matches the prompt against registered tools and skill files, and is also exposed for typed yes/no, choice and score questions.

## [Building with Jev: an agent skill](https://github.com/dbreunig/building-with-jev-skill)
By [Drew Breunig](https://github.com/dbreunig), 2026-09-17

A skill that helps coding agents write and improve programs that call Jev.

How Jev is used: Covers question design, state structure, confidence thresholds and diagnosing questions that answer wrongly or with low confidence.

## [Foreman: a supervisor for coding agents](https://github.com/thruwire/foreman)
By [ThruWire](https://github.com/thruwire), 2026-09-17

An agent supervisor that watches coding agents at work and decides what they should do next.

How Jev is used: It runs on decision models, supporting Jev and OpenAI's Decisions API, and can supervise workers such as Codex and OpenCode on a ticket or specification.

## [skillbox: a self-hosted skills library for agents](https://github.com/kitze/skillbox)
By [kitze 🚀](https://github.com/kitze), 2026-09-17

A versioned skills library for AI agents that serves skills over MCP.

How Jev is used: It offers optional Jev recommendations for which skill an agent should use.

## [jev-mcp: Jev as tools for coding agents](https://github.com/burnigtm/jev-mcp)
By [burnigtm](https://github.com/burnigtm), 2026-09-17

A local MCP server that gives Cursor, Codex and other clients typed Jev judgments.

How Jev is used: It routes the next step and decides whether a partner model is needed, while the host agent still edits files and runs commands.

## [pi-jev: a decision layer for the Pi agent](https://github.com/y0usaf/pi-jev)
By [Sami Ansari](https://github.com/y0usaf), 2026-09-16

Adds Jev to the Pi coding agent as a gate on risky tool calls and a fast way to ask typed questions.

How Jev is used: Jev judges bash, write and edit calls before they run, reads command output, and answers the agent's own questions through a jev_ask tool.

## [VexJoy Agent: routing plain-English requests to specialist agents](https://github.com/notque/vexjoy-agent)
By [notque](https://github.com/notque), 2026-09-15

A toolkit of agents, skills and hooks that turns a plain request into the right workflow.

How Jev is used: Its /do command uses Jev for intelligent routing, then gates the work with reviews and tests.

## [Canny: no 'done' without evidence](https://github.com/qkal/Canny)
By [Qkal](https://github.com/qkal), 2026-09-11

A supervision layer for Claude Code and Codex that won't let an agent finish on an unproven claim.

How Jev is used: Deterministic hooks keep a ledger of what the agent actually did and make the decisions; Jev advises on the judgement calls.


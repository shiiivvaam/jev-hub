# Coding agents: community builds with Jev

20 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/coding-agents).

## [Jev Review: staged code review](https://github.com/devagrawal09/jev-review)
By [Dev Agrawal](https://github.com/devagrawal09), 2026-09-16

A code-review workflow for diffs or whole codebases, with a quiet local dashboard.

How Jev is used: Code orchestrates the review; Jev handles bounded judgements at each stage: a risk matrix, file profiles, evidence selection and severity scores.

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

## [Gatekeeper: route requests to the right agent or skill](https://github.com/AgriciDaniel/gatekeeper)
By [Agrici Daniel](https://github.com/AgriciDaniel), 2026-09-23

Decides which AI agent or skill should handle a request before your AI guesses.

How Jev is used: YAML rules handle what code can decide; Jev answers the remaining 'which handler owns this?' question as a typed choice, and confidence bands turn it into a verdict.

## [jev-harness: propose, ask, decide](https://github.com/TypeSafeAI/jev-harness)
By [TypeSafe Community](https://github.com/TypeSafeAI), 2026-09-22

A research-stage coding harness where an LLM proposes and Jev reviews.

How Jev is used: An LLM proposes one action, Jev answers four narrow questions about it, and code produces evidence for the host to act on. Maintained by a community organisation independent of TypeSafe.

## [Auto-Guard: check every tool call before it runs](https://x.com/roshanchandna/status/2101419433415581797)
By [Roshan Chandna](https://x.com/roshanchandna), 2026-09-19

An open-source guard that stops a coding agent's dangerous commands and lets safe ones through.

How Jev is used: Jev reviews each tool call before execution; the demo shows it blocking a credentials delete while allowing a routine build cleanup.

## [jev-use: let Jev take the steps that need no text](https://github.com/shitianfang/jev-use)
By [shitianfang](https://github.com/shitianfang), 2026-09-19

A plugin for Claude Code, Codex and Pi that hands decision-only steps to Jev.

How Jev is used: When a step only needs a decision, Jev takes it; when text must be written, the LLM takes over. The author measures about 230 ms and $0.02 per 1,000 judgements.

## [jev-pruner: trim long command output](https://github.com/tamaratran/jev-pruner)
By [tamara tran](https://github.com/tamaratran), 2026-09-18

A Claude Code plugin that trims noisy Bash output before the model reads it.

How Jev is used: Short output passes through untouched; for long output, Jev picks the lines that matter so later turns carry less noise.

## [Stanley: a Jev-first coding agent](https://github.com/devagrawal09/stanley-code)
By [Dev Agrawal](https://github.com/devagrawal09), 2026-09-17

A command-line tool for checking and understanding code changes, described in plain words.

How Jev is used: Jev routes each request to a workflow; the workflow gathers evidence and asks Jev small fixed-choice questions, and code makes the final call. A general agent is only used as a fallback.

## [Jev Review: quality scores for coding agents](https://github.com/NiazMorshed2007/jev-review)
By [Niaz Morshed](https://github.com/NiazMorshed2007), 2026-09-17

A local MCP server that gives coding agents continuous quality scores while they work.

How Jev is used: Jev scores code on independent dimensions such as correctness, complexity, tests and security; the agent stays responsible for fixing what scores low.

## [Auto mode for the Pi coding agent](https://github.com/jomatsu/pi-jev-auto-mode)
By [Jo Matsuda](https://github.com/jomatsu), 2026-09-17

Auto-approves routine bash, write and edit calls in Pi and fails closed when unsure.

How Jev is used: Jev judges each tool call semantically; if a decision can't be made, the call is blocked rather than allowed.

## [Smart command approvals for Hermes Agent](https://github.com/anpicasso/hermes-jev-approvals)
By [Angello Picasso](https://github.com/anpicasso), 2026-09-17

Replaces Hermes Agent's command reviewer with Jev: approve, deny or ask the user.

How Jev is used: One request asks six typed questions in parallel. The author reports 8.7x faster reviews and 4.4x fewer prompts on 153 real commands.

## [SkillRanker: the right skill for the next step](https://github.com/Dicklesworthstone/skillranker)
By [Jeff Emanuel](https://github.com/Dicklesworthstone), 2026-09-17

A Rust CLI that ranks an agent's installed skills for the next step of a session.

How Jev is used: Jev evaluates the agent's live context against the available skills; SkillRanker adds session hooks, safeguards and local feedback.

## [Semantic tool routing for the Pi agent](https://github.com/TheoOliveira/pi-jev)
By [Theo Oliveira](https://github.com/TheoOliveira), 2026-09-17

Activates only the tools and skills a Pi agent needs for the current prompt.

How Jev is used: Jev matches the prompt against registered tools and skill files, and is also exposed for typed yes/no, choice and score questions.

## [Jevify: teach your agent when to use Jev](https://github.com/altryne/jevify)
By [Alex Volkov](https://github.com/altryne), 2026-09-17

An agent skill that finds work a fast decision model can handle and helps design the questions.

How Jev is used: Makes Jev the default for bulk judgements such as selecting passages, ranking candidates and checking items, so the agent reasons only over what Jev selects.

## [Building with Jev: an agent skill](https://github.com/dbreunig/building-with-jev-skill)
By [Drew Breunig](https://github.com/dbreunig), 2026-09-17

A skill that helps coding agents write and improve programs that call Jev.

How Jev is used: Covers question design, state structure, confidence thresholds and diagnosing questions that answer wrongly or with low confidence.

## [pi-jev: a decision layer for the Pi agent](https://github.com/y0usaf/pi-jev)
By [Sami Ansari](https://github.com/y0usaf), 2026-09-16

Adds Jev to the Pi coding agent as a gate on risky tool calls and a fast way to ask typed questions.

How Jev is used: Jev judges bash, write and edit calls before they run, reads command output, and answers the agent's own questions through a jev_ask tool.

## [Canny: no 'done' without evidence](https://github.com/qkal/Canny)
By [Qkal](https://github.com/qkal), 2026-09-11

A supervision layer for Claude Code and Codex that won't let an agent finish on an unproven claim.

How Jev is used: Deterministic hooks keep a ledger of what the agent actually did and make the decisions; Jev advises on the judgement calls.


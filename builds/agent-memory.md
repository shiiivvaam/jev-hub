# Agent memory: community builds with Jev

6 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/agent-memory).

## [jevmem: say it once to Claude Code](https://github.com/Avinash-jetwani/jevmem)
By [Avinash Jetwani](https://github.com/Avinash-jetwani), 2026-09-22

Saves decisions and rules from Claude Code chats and brings the relevant ones back next session.

How Jev is used: Jev picks which saved notes apply and checks commands and edits against your saved rules before they run.

## [Jev-Mem: agent memory with a fast controller](https://github.com/libingzheren/Jev-Mem)
By [Bingzhe Li](https://github.com/libingzheren), 2026-09-20

A research project separating frequent memory decisions from deeper reasoning.

How Jev is used: A Jev-style controller organises memories and guides retrieval; a language model writes the final answer. Published with a paper.

## [fast-jev-compaction: smarter context compaction for Claude Code](https://github.com/tamaratran/fast-jev-compaction)
By [tamara tran](https://github.com/tamaratran), 2026-09-17

A Claude Code plugin that replaces the usual compaction summary with decisions about which tool calls to keep.

How Jev is used: Jev scores every tool call and result in one request. Stale ones are dropped or truncated, and everything kept stays word for word, so nothing is rewritten.

## [compact-adviser: should you run /compact now?](https://github.com/kunchenguid/compact-adviser)
By [Kun Chen](https://github.com/kunchenguid), 2026-09-17

An agent plugin that answers one question: is it safe to compact this session?

How Jev is used: Jev judges whether the session is at a boundary where compaction is safe, then hints at it or, on Pi and Claude Code if you opt in, runs it for you.

## [winnow: a context sieve for Claude Code](https://github.com/GhalebDweikat/winnow)
By [Ghaleb Dweikat](https://github.com/GhalebDweikat), 2026-09-16

A plugin that judges every large tool result before it enters Claude's context.

How Jev is used: Blocks the judge is confident you don't need are replaced with a short stub and a key that restores the full text on demand.

## [ThoughtDAG: a canvas for AI conversations, with Jev retrieval](https://github.com/chenxiachan/thoughtdag)
By [Xia Chen](https://github.com/chenxiachan), 2026-09-15

An infinite-canvas app where AI conversations branch into a graph and the wires carry the context.

How Jev is used: An optional Jev decision layer helps identify topics and rank relevant excerpts from earlier agent sessions and canvases, and your chosen language model writes the answer. The authors report a median of 391 ms for Jev in a small relevance pilot.


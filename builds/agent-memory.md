# Agent memory: community builds with Jev

4 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/agent-memory).

## [jevmem: say it once to Claude Code](https://github.com/Avinash-jetwani/jevmem)
By [Avinash Jetwani](https://github.com/Avinash-jetwani), 2026-09-22

Saves decisions and rules from Claude Code chats and brings the relevant ones back next session.

How Jev is used: Jev picks which saved notes apply and checks commands and edits against your saved rules before they run.

## [Jev-Mem: agent memory with a fast controller](https://github.com/libingzheren/Jev-Mem)
By [Bingzhe Li](https://github.com/libingzheren), 2026-09-20

A research project separating frequent memory decisions from deeper reasoning.

How Jev is used: A Jev-style controller organises memories and guides retrieval; a language model writes the final answer. Published with a paper.

## [Jev Recall: retrieve memories by relevance](https://github.com/samdotmak/jev-recall)
By [Samarth Makhija](https://github.com/samdotmak), 2026-09-19

Picks the most relevant memories for an AI assistant's query.

How Jev is used: Jev answers one yes/no relevance question per memory, all in a single request.

## [invalidate: let agents un-remember](https://github.com/chopratejas/invalidate)
By [Tejas Chopra](https://github.com/chopratejas), 2026-09-19

Ends an agent's stored facts when new evidence contradicts them.

How Jev is used: Every fact gets a lease; Jev judges whether new events invalidate it, so outdated memories stop being used.


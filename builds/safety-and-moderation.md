# Safety and moderation: community builds with Jev

7 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/safety-and-moderation).

## [CAPTCHA rebuilt with Jev](https://x.com/jarekceborski/status/2103071312323158512)
By [Jarek](https://x.com/jarekceborski), 2026-09-24

A bot check based on how you fill in a form.

How Jev is used: The browser measures the behaviour, the server turns it into plain sentences and Jev decides person or bot. The author published a blog post with the source code.

## [Finding sensitive files on a file share](https://x.com/_xpn_/status/2102739497829961734)
By [Adam Chester 🏴‍☠️](https://x.com/_xpn_), 2026-09-23

A security demo where Jev picks out sensitive files.

How Jev is used: The author says Jev is very quick at it.

## [jevals: evals and guardrails for agents](https://github.com/openlayer-ai/jevals)
By [Openlayer](https://github.com/openlayer-ai), 2026-09-20

Runs evals and guardrails on every agent trace instead of using an LLM judge.

How Jev is used: All the checks for a trace go to Jev in one request costing a few thousandths of a cent, fast enough to run inside the agent loop.

## [Jev as a Judge with Comet Opik](https://github.com/patchy631/jev-as-judge)
By [Akshay Pachaar](https://github.com/patchy631), 2026-09-20

An auditable example that evaluates refund-support traces with Jev and records the result as an Opik experiment.

How Jev is used: It replays ten synthetic support traces, including invented policies and a prompt-injection attempt, and runs deterministic checks first.

## [Jev Arena: Jev against DeepSeek on the same comments](https://github.com/NanmiCoder/jev-arena)
By [程序员阿江-Relakkes](https://github.com/NanmiCoder), 2026-09-19

A tool that compares two models' speed, cost and labels on the same batch of comments.

How Jev is used: It imports CSV or Excel, replays the run and writes offline reports. The author reports 10,000 comments done in 203 seconds for $0.84 with Jev against 824 seconds for an estimated $1.50 with DeepSeek, with Jev slightly lower on accuracy. The page is mostly in Chinese.

## [Fraud detection: Jev first, Kimi for the uncertain cases](https://x.com/nutlope/status/2100614659690713543)
By [Hassan](https://x.com/nutlope), 2026-09-17

A pipeline that classifies emails with Jev and sends unsure ones to a larger model.

How Jev is used: The author reports 100 emails classified in 1.42 seconds, and 96 of 100 correct for about $0.07 once uncertain cases went to Kimi K3.

## [Jev Detector: a fast AI-slop checker](https://x.com/jozef_gherman/status/2100627898436571555)
By [Jozef](https://x.com/jozef_gherman), 2026-09-17

A free tool that scans text for AI slop.

How Jev is used: The author reports about 10,000 words scanned in about two seconds, with no sign-up.


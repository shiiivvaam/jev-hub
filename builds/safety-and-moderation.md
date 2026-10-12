# Safety and moderation: community builds with Jev

3 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/safety-and-moderation).

## [SpamLens: spam protection for WordPress](https://github.com/veronalabs/spamlens)
By [VeronaLabs](https://github.com/veronalabs), 2026-09-21

Filters spam from WordPress comments, product reviews and Contact Form 7.

How Jev is used: Comments Jev is confident are spam go to the spam folder; borderline ones are held for moderation; it never approves anything on its own.

## [jevals: evals and guardrails for agents](https://github.com/openlayer-ai/jevals)
By [Openlayer](https://github.com/openlayer-ai), 2026-09-20

Runs evals and guardrails on every agent trace instead of using an LLM judge.

How Jev is used: All the checks for a trace go to Jev in one request costing a few thousandths of a cent, fast enough to run inside the agent loop.

## [Telegram anti-spam bot](https://github.com/backmeupplz/jev_antispam_bot)
By [Nikita Kolmogorov](https://github.com/backmeupplz), 2026-09-18

A minimal Telegram bot that deletes spam from group chats.

How Jev is used: Jev judges whether each message is spam; only high-confidence matches are deleted.


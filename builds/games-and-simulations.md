# Games and simulations: community builds with Jev

17 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/games-and-simulations).

## [jev-drone: a camera-only autonomous drone](https://x.com/RomanSlack1/status/2100335978229690683)
By [Roman Slack](https://x.com/RomanSlack1), 2026-09-16

A simulated quadrotor that flies an obstacle course using only its onboard camera.

How Jev is used: Jev runs at about 2.5 times a second and decides what the current situation means; time-critical flight control stays in ordinary code. The author built the first version in 15 minutes for 10 cents.

## [Jev plays Super Mario Bros.](https://github.com/fhshaik/typesafe-mario)
By [fhshaik](https://github.com/fhshaik), 2026-09-16

An agent that plays the original Super Mario Bros. from emulator data, not screenshots.

How Jev is used: Game memory is turned into a compact description of Mario, enemies and terrain, and Jev chooses one legal controller action at a time.

## [clash-jev: a Clash Royale bot](https://github.com/bytelabs-oss/clash-jev)
By [bytelabs](https://github.com/bytelabs-oss), 2026-09-21

Plays Clash Royale on a real Android phone with no trained game policy.

How Jev is used: Computer vision turns the live screen into a game state once a second; Jev picks a strategy and a card in about 135 ms.

## [jevman: Pac-Man driven by Jev](https://github.com/joch/jevman)
By [Johnny Chadda](https://github.com/joch), 2026-10-04

Watch Jev play Pac-Man, or play against Jev controlling the ghosts.

How Jev is used: A side panel shows each of Jev's decisions with its probabilities, latency and the running cost.

## [Laya vs Jev arena](https://github.com/PromptEngineer48/laya-vs-jev-arena)
By [Prompt Engineer](https://github.com/PromptEngineer48), 2026-09-21

Two decision models race in Snake and fight in a Mortal Kombat-style arena.

How Jev is used: Both models get the same input and typed questions, so the only difference between the sides is the model; every move is a real decision.

## [jev-leftpad](https://github.com/f/jev-leftpad)
By [Fatih Kadir Akın](https://github.com/f), 2026-09-21

Left-pads a string using a model call. For reasons.

How Jev is used: A deliberately absurd npm package: Jev chooses how many spaces to add from a list of options.

## [AI chess lab](https://github.com/dperezcabrera/ai-chess-lab)
By [David Pérez Cabrera](https://github.com/dperezcabrera), 2026-09-21

LLMs, decision models and people play chess in the browser, with every move, second and dollar recorded.

How Jev is used: Jev picks moves through Vercel AI Gateway or OpenRouter, and Stockfish analyses the games in the browser.

## [Pac-Man where every move is Jev's](https://x.com/NesanSelvan04/status/2100844705588347238)
By [Nesan Selvan](https://x.com/NesanSelvan04), 2026-09-18

A Pac-Man game in which each step is decided by Jev.

How Jev is used: On every tile Jev receives Pac-Man's surroundings and returns a direction, a strategy, a danger score and flags such as trapped or committed.

## [Playable video game NPCs](https://x.com/dparksdev/status/2100949987571974537)
By [David Parks](https://x.com/dparksdev), 2026-09-18

Game characters you can direct: explore, gather resources or build a house, then override them mid-task.

How Jev is used: Jev chooses each NPC's next action; the choices and their probabilities are shown live.

## [Where should a burning ship go?](https://x.com/carlosmarcialt/status/2100979161196052855)
By [Carlos Marcial](https://x.com/carlosmarcialt), 2026-09-18

An app that asks Jev where a ship in distress should head, or where a troubled plane should land.

How Jev is used: Vessels and aircraft come from real AIS and ADS-B traffic feeds; Jev picks the destination from the available options.

## [Zero-shot control of a real robotic arm](https://x.com/zaidbul/status/2100949713138729135)
By [Zaid Bulbul](https://x.com/zaidbul), 2026-09-18

Jev controlling a physical robotic arm with no trained policy.

How Jev is used: Jev chooses the arm's next move from a set of options at each step, outside of any simulation.

## [Jev self-driving sim](https://github.com/vinilana/live-jev)
By [Vinicius Lana](https://github.com/vinilana), 2026-09-18

A top-down autonomous car simulation that runs in the browser.

How Jev is used: About every 200 ms the car's sensor readings go to Jev with four questions (lane, speed and more), and the car executes the answers.

## [Jev plays Pokémon Red](https://github.com/milanboers/jev-plays-pokemon)
By [Milan Boers](https://github.com/milanboers), 2026-09-17

A small autonomous agent for Pokémon Red on a Game Boy emulator.

How Jev is used: Each turn the game is described as text (dialog, map, party, objective); Jev answers typed questions and code turns them into button presses.

## [TypeSafe experiments: from support messages to a 3D car](https://github.com/kavehmz/typesafe-playground)
By [Kaveh Mousavi Zamani](https://github.com/kavehmz), 2026-09-17

Interactive experiments with real Jev calls, including a self-driving car in a 3D world.

How Jev is used: Each experiment makes the inputs and Jev's judgements visible, including hesitation and mistakes.

## [Should AI kill us all?](https://github.com/hellogumbo/should-ai-kill-us-all)
By [GUMBO](https://github.com/hellogumbo), 2026-09-17

A site that asks Jev the question every ten minutes, using the actual headlines.

How Jev is used: Jev can only choose, not explain, so it reads the news and picks an answer with a probability.

## [JevGPT: a chatbot from a model that can't write](https://github.com/Bewinxed/jevgpt)
By [Omar Al Matar](https://github.com/Bewinxed), 2026-09-17

A chat client built on a model that doesn't generate text.

How Jev is used: The conversation is the state, the question is 'next word?', and the options are a 20,000-word dictionary; Jev answers one word at a time.

## [Jev plays StarCraft](https://github.com/phyous/tsai-sc)
By [Philip Youssef](https://github.com/phyous), 2026-09-16

Jev completes the first combat mission of the original StarCraft shareware campaign.

How Jev is used: Jev controls the game through keyboard and mouse actions, and every action's probability is recorded alongside a game recording.


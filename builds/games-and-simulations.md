# Games and simulations: community builds with Jev

16 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/games-and-simulations).

## [jev-drone: a camera-only autonomous drone](https://x.com/RomanSlack1/status/2100335978229690683)
By [Roman Slack](https://x.com/RomanSlack1), 2026-09-16

A simulated quadrotor that flies an obstacle course using only its onboard camera.

How Jev is used: Jev runs at about 2.5 times a second and decides what the current situation means; time-critical flight control stays in ordinary code. The author built the first version in 15 minutes for 10 cents.

## [Jev plays Super Mario Bros.](https://github.com/fhshaik/typesafe-mario)
By [fhshaik](https://github.com/fhshaik), 2026-09-16

An agent that plays the original Super Mario Bros. from emulator data, not screenshots.

How Jev is used: Game memory is turned into a compact description of Mario, enemies and terrain, and Jev chooses one legal controller action at a time.

## [Jevspresso: Jev as a barista](https://x.com/DavidKPiano/status/2106407550845600200)
By [David K 🎹](https://x.com/DavidKPiano), 2026-10-03

A state-machine demo where XState decides what is possible and Jev decides the next move.

How Jev is used: You can order in plain language or break things and watch Jev cope.

## [Luna plans, Jev acts: playing poker](https://x.com/browser_use/status/2102980499614658580)
By [Browser Use](https://x.com/browser_use), 2026-09-24

A demo from Browser Use pairing a planner model with Jev as the actor.

How Jev is used: Luna sets the plan and Jev makes the moves in a poker game.

## [ldraw-nova: an agent that builds LEGO models](https://github.com/anteloc/ldraw-nova)
By [Carlos Antelo](https://github.com/anteloc), 2026-09-23

Agent tooling that takes a model idea and produces an LDraw LEGO model.

How Jev is used: The agents are built with GPT and Claude models and use Jev for fast decisions. The output includes the LDraw source, 3D and VR views and an editable Blender file.

## [LeJudge: plain-English rules for a world-model planner](https://x.com/AbdelStark/status/2102675806027755724)
By [abdel](https://x.com/AbdelStark), 2026-09-23

An experiment putting Jev inside a JEPA world-model planner.

How Jev is used: The planner imagines 300 futures, each is described in words, Jev answers whether it breaks the rule and code adds a penalty. No LLM is involved.

## [JEV-Star: real-time StarCraft II control](https://github.com/sc2musa/Jev_Star)
By [Weiyu Ma (马纬彧)](https://github.com/sc2musa), 2026-09-22

A research project on real-time StarCraft II macro control, plus Jev and GPT micromanagement.

How Jev is used: The repository has a paper, five macro configurations and videos of complete games at original speed.

## [jev-leftpad](https://github.com/f/jev-leftpad)
By [Fatih Kadir Akın](https://github.com/f), 2026-09-21

Left-pads a string using a model call. For reasons.

How Jev is used: A deliberately absurd npm package: Jev chooses how many spaces to add from a list of options.

## [Laya vs Jev: two models play the T-Rex game](https://github.com/virajbhartiya/laya-vs-jev)
By [Viraj Bhartiya](https://github.com/virajbhartiya), 2026-09-21

A side-by-side game where a local Laya model and hosted Jev both play Chrome's T-Rex.

How Jev is used: It shows each model's choices, response times, survival streaks and crash replays on a shared course.

## [Minecraft agent: a language-model planner with Jev at the controls](https://github.com/rmalde/minecraft-agent)
By [rmalde](https://github.com/rmalde), 2026-09-20

An agent that plays Minecraft Java 1.16.5 and aims to beat the Ender Dragon.

How Jev is used: A GPT model plans and Jev selects the player actions. The author reports a run completing in 8 minutes 43 seconds.

## [jev-paint: paintings from Jev's pixel probabilities](https://github.com/achimala/jev-paint)
By [Anshu Chimala](https://github.com/achimala), 2026-09-18

A small local app that turns Jev's probability distributions into paintings.

How Jev is used: Jev returns pixel probabilities, which the app renders into images in the browser.

## [Jev plays Smash Bros against itself](https://x.com/maubaron/status/2100738237237002706)
By [Mau Baron](https://x.com/maubaron), 2026-09-18

A demo where Jev controls all four characters in a fighting game.

How Jev is used: The author reports over 22 million tokens for the match at a cost of a couple of cents, with decisions in a fraction of a second.

## [Generating game levels in real time with Jev](https://x.com/HugoDuprez/status/2100953089003921543)
By [Hugo Duprez](https://x.com/HugoDuprez), 2026-09-18

A game-development experiment where Jev produces levels as you play.

How Jev is used: The author argues that faster, cheaper structured output could matter for game development.

## [JevPilot: a driving simulator with a Jev autopilot](https://github.com/standardagents/jevpilot)
By [Standard Agents](https://github.com/standardagents), 2026-09-17

A playable Three.js driving simulator with Tesla Autopilot-like behaviour.

How Jev is used: Jev makes the driving decisions through a hosted endpoint that requires a login. The project offers a small amount of free Jev play credit.

## [Jev plays Subway Surfers, 50 games at once](https://x.com/_MaxBlade/status/2100634359099232678)
By [Max Blade](https://x.com/_MaxBlade), 2026-09-17

A demo of Jev playing a fast arcade game and running 50 games at once.

How Jev is used: The author reports the run cost less than a cent and notes that Jev does not replace large reasoning models.

## [Jev plays Slay the Spire 2](https://x.com/coolish/status/2100570517954838897)
By [paulwei](https://x.com/coolish), 2026-09-17

A demo of Jev playing a card game faster than a human can follow.

How Jev is used: The author, writing in Chinese, reports about 0.7 seconds of thinking per action, compared with a slower run using GPT-6 Astra.


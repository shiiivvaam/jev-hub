# Computer and browser use: community builds with Jev

22 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/computer-and-browser-use).

## [Fast app testing with OpenCode](https://x.com/Neriousy/status/2100287208166969746)
By [Filip](https://x.com/Neriousy), 2026-09-16

A demo of an AI agent clicking through an app under test at high speed.

How Jev is used: Jev makes the step-by-step choices of what to click next, so the testing agent doesn't wait on a large model for every action.

## [Jevry: a desktop browser that acts on a task](https://github.com/michaelswissa/jevry)
By [Michael Swissa](https://github.com/michaelswissa), 2026-09-24

An open-source desktop browser that carries out website tasks, cited research and supported games.

How Jev is used: Actions are visible and can be stopped or redirected, and results are grounded in the page.

## [CodexQA Jev Browser](https://github.com/openqa-cn/jev-browser)
By [OpenQA](https://github.com/openqa-cn), 2026-09-23

Browser automation for checking code after it's written, without sending screenshots to a vision model.

How Jev is used: Controls are found from an index of the page and Jev chooses which one to use; part of the CodexQA set of agent skills.

## [jev-ui-test: UI tests in plain language](https://github.com/buer2233/jev-ui-test)
By [buer](https://github.com/buer2233), 2026-09-22

A UI test framework where test cases are written as sentences and run with pytest.

How Jev is used: A browser agent runs each test, and Jev scores the candidate elements to choose every action, with no selectors or site scripts. The author measures about 458 ms per decision.

## [system1-agents: agents powered by decision models](https://github.com/ThinkFlowLab/system1-agents)
By [ThinkFlowLab](https://github.com/ThinkFlowLab), 2026-09-22

A set of ready-made agents for browser use, computer use, games and robotics.

How Jev is used: Claude Code or Codex runs a prebuilt agent or builds a new one on Jev, Laya or Cua-S1. The authors report up to 6 times faster and 25 times cheaper than a chat model at the same score.

## [A Chrome side panel that drives WebMCP tools with Jev](https://x.com/sarah_edo/status/2102025642862600634)
By [Sarah Drasner](https://x.com/sarah_edo), 2026-09-21

A Chrome extension that operates a site's WebMCP tools from a side panel.

How Jev is used: On every keystroke Jev picks the right tool, fills in the arguments and says how sure it is. The demo does grocery shopping.

## [Smart copy and paste, powered by Jev](https://x.com/marcus_lowe/status/2101476399488160013)
By [Marcus Lowe](https://x.com/marcus_lowe), 2026-09-20

A demo where copy and paste understands what you are doing.

How Jev is used: Marcus Lowe built it with Jev and describes it as a glimpse of computer interactions being rewritten.

## [jev-use: say it, and your Mac does it](https://github.com/savka777/jev-use)
By [Sav](https://github.com/savka777), 2026-09-19

Voice and typed computer use for macOS that reads the screen without screenshots.

How Jev is used: The app reads the screen through the Accessibility tree and Jev picks the next on-screen action.

## [Jev Desktop for Codex](https://github.com/yikangy873-gif/jev-desktop)
By [yikangy873-gif](https://github.com/yikangy873-gif), 2026-09-19

Adds a bounded decision loop to Codex's computer use for browser tabs and Mac apps.

How Jev is used: Codex sets the goal and allowed actions, Jev selects an operation and target in one request, and Computer Use performs it.

## [Jev Browser Use: Jev clicks, Codex checks](https://github.com/wy-coliney/jev-browser-use)
By [coliney](https://github.com/wy-coliney), 2026-09-18

A browser skill that hands navigation, clicks and scrolling to Jev while Codex keeps text input and the final check.

How Jev is used: The authors report browser operations about 5 to 10 times faster in their own EZCollegeApp workflows.

## [Keystroke oracle: a launcher that reads intent](https://x.com/dabit3/status/2100756930054504776)
By [nader dabit](https://x.com/dabit3), 2026-09-18

A predictive app launcher that re-ranks results on every keystroke.

How Jev is used: Jev reads intent, so typing the pdf I just downloaded puts the newest PDF on top. It is the first of Nader Dabit's Jev experiments.

## [A used-goods hunter built with Playwright and Jev](https://x.com/AlanDaitch/status/2100757989212754085)
By [Alan Daitch](https://x.com/AlanDaitch), 2026-09-18

An agent that searches second-hand listings and acts on them.

How Jev is used: The author, writing in Spanish, reports about 26 listings a minute at roughly 406 ms a decision, with a total search cost of $0.00085, including messaging sellers when details are missing.

## [Cline's Jev browser plugin](https://x.com/cline/status/2101056078872256935)
By [Cline](https://x.com/cline), 2026-09-18

A plugin that gives Jev a browser inside Cline.

How Jev is used: Install jev-browser from the plugin marketplace, add a Vercel AI Gateway key and ask for a browser task; Cline launches Chrome in the background.

## [jev-browser: fast, cheap browser use with Jev](https://github.com/jkudish/jev-browser)
By [Joey Kudish](https://github.com/jkudish), 2026-09-17

A tool that drives a real headless browser through an MCP server, command line or library.

How Jev is used: Jev picks one action per step from the page's clickable, typeable and selectable elements and scores how likely the goal is met or the run is stuck. Code owns the loop.

## [fastbrowse: a fast browser agent with cited answers](https://github.com/agent-labs-dev/fastbrowse)
By [Agent Labs](https://github.com/agent-labs-dev), 2026-09-17

A browser agent that runs locally or in a cloud browser and returns cited answers or validated data.

How Jev is used: Jev picks from indexed page controls, so it cannot click something that was never on the page, while a language model reads and plans.

## [Stagehand with Jev: browser use for a tenth of a cent](https://x.com/kylejeong/status/2100622054945095934)
By [Kyle Jeong](https://x.com/kylejeong), 2026-09-17

A fast browser-use loop built with Stagehand.

How Jev is used: The page's accessibility tree goes to Jev as state, Jev picks the next action and Stagehand carries it out. The authors report a task costing $0.001.

## [A Wikipedia link-walking agent with Jev](https://x.com/mormonnegro/status/2100408498446111031)
By [Mormon Negro](https://x.com/mormonnegro), 2026-09-17

A demo of an agent navigating with Jev and headless Chromium.

How Jev is used: It walks from the Café page to Inteligencia artificial by following links. The author, writing in Spanish, reports completing it in 20 seconds.

## [fx.sh: agentic browsing in a Chrome extension](https://x.com/razaanstha/status/2100645675591520612)
By [RaZaan](https://x.com/razaanstha), 2026-09-17

A Chrome extension that lets agents browse and click in your own browser.

How Jev is used: Decision-making by Jev, with Vercel AI Gateway.

## [jev-browser: an LLM plans, Jev decides](https://github.com/Ying-Kai-Liao/jev-browser)
By [Ying-Kai Liao](https://github.com/Ying-Kai-Liao), 2026-09-16

Browser automation as a library, CLI and MCP server.

How Jev is used: For each step, one Jev request picks the element, the action and the value, and checks whether the step is done, blocked or about to do something irreversible. Playwright performs it.

## [Jev Ultrafast: a browser agent that picks each click](https://github.com/browser-use/jev-ultrafast)
By [Browser Use](https://github.com/browser-use), 2026-09-16

A browser agent from the Browser Use team that works toward a goal one fast step at a time.

How Jev is used: Jev picks an operation and an element from an indexed list of page controls, and a small language model writes text only when text has to be typed. The authors report a Zürich to London flight search on Google Flights in 7.1 seconds.

## [typesafe-computer-use: Mac computer use for a fraction of a cent a step](https://github.com/awlevin/typesafe-computer-use)
By [Aaron Levin](https://github.com/awlevin), 2026-09-16

A tool that drives a Mac toward a goal typed in plain English.

How Jev is used: The screen is read with OCR and a small classifier picks the next action. A writing model is called only when a text field needs free text. The author reports about $0.0002 per step.

## [TipTour: a local computer-use companion for the Mac](https://github.com/milind-soni/tiptour-macos)
By [Milind Soni](https://github.com/milind-soni), 2026-09-15

A macOS menu bar companion that carries out click-based tasks you type.

How Jev is used: In its Jev mode, Jev chooses from controls detected locally on the screen, and the app executes and validates each action.


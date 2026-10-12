# Computer and browser use: community builds with Jev

10 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/computer-and-browser-use).

## [Fast app testing with OpenCode](https://x.com/Neriousy/status/2100287208166969746)
By [Filip](https://x.com/Neriousy), 2026-09-16

A demo of an AI agent clicking through an app under test at high speed.

How Jev is used: Jev makes the step-by-step choices of what to click next, so the testing agent doesn't wait on a large model for every action.

## [Flick: fast computer use for MCP agents](https://github.com/bgivenb/flick-computer-use)
By [Given Borthwick](https://github.com/bgivenb), 2026-09-24

A local MCP server that carries out whole browser and macOS goals.

How Jev is used: Your agent supplies the goal and completion conditions; Flick runs the observe, decide, act loop with Jev and returns the result.

## [CodexQA Jev Browser](https://github.com/openqa-cn/jev-browser)
By [OpenQA](https://github.com/openqa-cn), 2026-09-23

Browser automation for checking code after it's written, without sending screenshots to a vision model.

How Jev is used: Controls are found from an index of the page and Jev chooses which one to use; part of the CodexQA set of agent skills.

## [jev-ui-test: UI tests in plain language](https://github.com/buer2233/jev-ui-test)
By [buer](https://github.com/buer2233), 2026-09-22

A UI test framework where test cases are written as sentences and run with pytest.

How Jev is used: A browser agent runs each test, and Jev scores the candidate elements to choose every action, with no selectors or site scripts. The author measures about 458 ms per decision.

## [jev-use: say it, and your Mac does it](https://github.com/savka777/jev-use)
By [Sav](https://github.com/savka777), 2026-09-19

Voice and typed computer use for macOS that reads the screen without screenshots.

How Jev is used: The app reads the screen through the Accessibility tree and Jev picks the next on-screen action.

## [Jev Desktop for Codex](https://github.com/yikangy873-gif/jev-desktop)
By [yikangy873-gif](https://github.com/yikangy873-gif), 2026-09-19

Adds a bounded decision loop to Codex's computer use for browser tabs and Mac apps.

How Jev is used: Codex sets the goal and allowed actions, Jev selects an operation and target in one request, and Computer Use performs it.

## [Jev for Chrome](https://github.com/chy4pro/jev-for-chrome)
By [chy4pro](https://github.com/chy4pro), 2026-09-18

A Chrome extension that drives the tab you're looking at.

How Jev is used: Jev picks the next click, keystroke or dropdown value in a few hundred milliseconds. A community port of Browser Use's jev-ultrafast.

## [jev-mobile: an Android agent](https://github.com/Friedjof/jev-mobile)
By [Friedjof Noweck](https://github.com/Friedjof), 2026-09-17

An autonomous Android sub-agent that carries out tasks on a connected phone.

How Jev is used: A worker observes the screen, Jev chooses among technically valid actions, and the result is verified; Jev never generates coordinates or code.

## [jev-browser: an LLM plans, Jev decides](https://github.com/Ying-Kai-Liao/jev-browser)
By [Ying-Kai Liao](https://github.com/Ying-Kai-Liao), 2026-09-16

Browser automation as a library, CLI and MCP server.

How Jev is used: For each step, one Jev request picks the element, the action and the value, and checks whether the step is done, blocked or about to do something irreversible. Playwright performs it.

## [computer-use-jev: drive macOS apps from Go](https://github.com/paulsmith/computer-use-jev)
By [Paul Smith](https://github.com/paulsmith), 2026-09-16

A Go library for operating native macOS apps.

How Jev is used: Apps are controlled through the Accessibility API, and Jev is the decision maker for which element to act on.


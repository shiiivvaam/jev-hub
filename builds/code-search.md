# Code search: community builds with Jev

11 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/code-search).

## [jevgrep: find code by asking what it does](https://github.com/dzhng/jevgrep)
By [David Zhang](https://github.com/dzhng), 2026-09-26

A CLI that points coding agents at the right files for an unfamiliar task.

How Jev is used: Jev judges relevance across folders, files and declarations, and returns files and verbatim excerpts. The author reports the same 8 of 10 SWE-bench tasks solved at about 30% lower cost.

## [jgrep: grep where the pattern is a description](https://github.com/keltokhy/jgrep)
By [keltokhy](https://github.com/keltokhy), 2026-09-18

Filters lines of text by meaning, for example 'a user is getting frustrated' in a live log.

How Jev is used: Each line becomes one yes/no question to Jev; the author reports about 200 ms and a thousandth of a cent per line.

## [Jevlint: a linter for code taste](https://github.com/codegirl-007/jevlint)
By [codegirl007](https://github.com/codegirl-007), 2026-09-25

A linter that checks code against rules written in plain language.

How Jev is used: It uses Tree-sitter to pull out code units and asks a decision backend such as Jev whether each one passes.

## [JevGrep: code search for agents, CLI and MCP](https://github.com/nassim-arifette/jevgrep)
By [Nassim Arifette](https://github.com/nassim-arifette), 2026-09-20

Finds code by behaviour when an agent doesn't know the file or symbol name.

How Jev is used: Jev scores every eligible code fragment against the question and returns the original excerpts with paths and line numbers.

## [jgrep: grep for what code does](https://github.com/kyu1204/jgrep)
By [MINT](https://github.com/kyu1204), 2026-09-19

Semantic code search with no index or embeddings, plus a mode that picks which tests a diff can affect.

How Jev is used: Jev answers a yes/no question for each piece of code. The author reports scanning a src/ tree in about two seconds for roughly a cent.

## [sys1grep: grep by meaning, across languages](https://github.com/uehaj/sys1grep)
By [UEHARA Junji](https://github.com/uehaj), 2026-09-19

Searches files by meaning and can find English text from a Japanese query, and the reverse.

How Jev is used: Jev scores every line against a meaning; meanings can be combined with AND, OR and NOT.

## [jev-lint: lint what a parser can't check](https://github.com/mizchi/jev-lint)
By [Kotaro Chikuba](https://github.com/mizchi), 2026-09-19

Lint rules written as questions, such as 'does this comment match what the function does?'

How Jev is used: Jev answers each rule's question with a probability, catching mismatches between comments, types and behaviour that ordinary linters miss.

## [oxlint-plugin-jev: lint rules in plain English](https://github.com/wobsoriano/oxlint-plugin-jev)
By [Robert Soriano](https://github.com/wobsoriano), 2026-09-19

An experimental Oxlint plugin where each rule is a yes or no question about code.

How Jev is used: Each match is sent to Jev with the question, and the plugin reports an error when the yes probability clears your cutoff.

## [Shell history suggestions ranked by Jev](https://github.com/mrnugget/jev-shell-history)
By [Thorsten Ball](https://github.com/mrnugget), 2026-09-18

Fish-style autosuggestions for zsh that guess which past command you're typing.

How Jev is used: As you type, Jev looks at your last 100 distinct commands and picks the one you're most likely completing, even when you describe it in words.

## [blink: codebase search with walkers](https://github.com/ellipsis-dev/blink)
By [Ellipsis](https://github.com/ellipsis-dev), 2026-09-16

Searches a codebase with an ensemble of walkers that move through the file tree.

How Jev is used: At each folder, Jev chooses which way to walk toward the file that answers the query.

## [Perch: semantic code linting with decision models](https://github.com/lakeday-org/perch)
By [lakeday-org](https://github.com/lakeday-org), 2026-09-16

A command-line scanner that checks code against meaning-based rules rather than patterns.

How Jev is used: Each code unit is judged by a decision model and decisions are cached, so scanning unchanged code again is free.


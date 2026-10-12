# Trading and finance: community builds with Jev

7 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/trading-and-finance).

## [Warren Duffer: intraday trading on Indian stocks](https://github.com/arimanyus/warrenduffer)
By [arimanyus](https://github.com/arimanyus), 2026-09-22

An experimental intraday bot for Nifty 50 stocks through Zerodha or Kotak.

How Jev is used: Jev classifies and ranks the stocks and decides take-profit; code sizes each trade, places the stop and enforces the loss limit.

## [jev-guard: risk triage for exchange deposits and withdrawals](https://github.com/klauswg/jev-guard)
By [klauswg](https://github.com/klauswg), 2026-09-22

Decides whether a crypto deposit or withdrawal passes automatically, goes to human review or is frozen.

How Jev is used: Jev supplies the risk level and behaviour pattern; thresholds and the final action stay in testable Java code.

## [Polymarket BTC 5-minute trading agent](https://x.com/GabiDev98/status/2102073217670107364)
By [gabidev](https://x.com/GabiDev98), 2026-09-21

A terminal agent for Polymarket's 5-minute Bitcoin up/down markets, dry-run by default.

How Jev is used: Jev judges whether BTC will finish up or down against the window's opening price; the agent either abstains or buys once and holds to resolution.

## [jevymarket: a Polymarket pricing bot](https://github.com/markusbug/jevymarket)
By [Markus Haas](https://github.com/markusbug), 2026-09-20

A Polymarket bot that pairs Jev with a web-search researcher.

How Jev is used: A cheap generative model writes a dated evidence brief; Jev, which has no browsing, prices the market from that brief.

## [jev-trader: market making around Jev](https://github.com/buberlo/jev-trader)
By [buberlo](https://github.com/buberlo), 2026-09-19

A 24/7 market-making system where Jev owns selected judgements, not the whole system.

How Jev is used: Code builds the market state, one Jev call returns six judgements (regime, direction, toxic flow and more), and code applies policy and risk vetoes.

## [TSLA 50-day moving-average experiment](https://x.com/mttcnnng/status/2100971168912048153)
By [Matt](https://x.com/mttcnnng), 2026-09-18

A simple trading rule with Jev in the judgement step.

How Jev is used: Code supplies the facts (price against the 50-day average), Jev supplies a typed judgement, and code decides the action.

## [Jev Trade: a live Hyperliquid desk](https://github.com/aowang-ai/jev-trade)
By [Ao Wang](https://github.com/aowang-ai), 2026-09-17

A trading bot on Hyperliquid across five coins, with a public live view.

How Jev is used: Jev reads the order book every tick and answers buy, sell or hold; the bot places the order.


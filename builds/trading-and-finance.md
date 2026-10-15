# Trading and finance: community builds with Jev

6 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/trading-and-finance).

## [Warren Duffer: intraday trading on Indian stocks](https://github.com/arimanyus/warrenduffer)
By [arimanyus](https://github.com/arimanyus), 2026-09-22

An experimental intraday bot for Nifty 50 stocks through Zerodha or Kotak.

How Jev is used: Jev classifies and ranks the stocks and decides take-profit; code sizes each trade, places the stop and enforces the loss limit.

## [Jev Trade: a live Hyperliquid desk](https://github.com/aowang-ai/jev-trade)
By [Ao Wang](https://github.com/aowang-ai), 2026-09-17

A trading bot on Hyperliquid across five coins, with a public live view.

How Jev is used: Jev reads the order book every tick and answers buy, sell or hold; the bot places the order.

## [Giving Jev $10,000 to trade](https://x.com/abolbuild/status/2100523868913807410)
By [Abol](https://x.com/abolbuild), 2026-09-17

A video experiment where Jev makes trading decisions with real money.

How Jev is used: The author says they gave Jev $10,000 and let it trade.

## [jev-trader: one trade decision per Monad block](https://github.com/jarrodwatts/jev-trader)
By [Jarrod Watts](https://github.com/jarrodwatts), 2026-09-16

A trading bot that asks Jev whether to buy or sell on every block of the Monad chain.

How Jev is used: Jev reads the Kuru MON-USDC order book and answers buy or sell about every 300 ms, and each block posts a post-only limit order on that side. Without a private key it runs as a dry run with simulated fills.

## [QuantDinger: an open-source trading workbench with a Jev option](https://github.com/OpenByteInc/QuantDinger)
By [Open Byte Inc](https://github.com/OpenByteInc), 2026-09-15

A self-hosted stack for turning trading ideas into Python strategies, backtests, paper trading and live execution.

How Jev is used: A Jev pre-trade decision gate checks each proposed trade before it goes ahead, as an alternative to a gate that relies only on a language model.

## [AI Stock: a research workspace with an optional Jev decision engine](https://github.com/EthanAlgoX/AIStock)
By [Ethan](https://github.com/EthanAlgoX), 2026-09-15

A website for researching stocks, comparing investing views and testing strategies with simulated money.

How Jev is used: Jev can act as an optional buy, sell or hold decision engine inside the simulator.


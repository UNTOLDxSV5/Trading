# Trading Projects Repository

## 📌 Why This Repo Matters

This repository is a complete collection of my work toward becoming a quantitative and discretionary trader. It includes:

- Live-tested trading strategies with proven edge
- AI/ML models trained on custom financial datasets
- Risk analysis tools for professional evaluation
- Strategy journals and real-world performance logs
- Research on macroeconomics and market structure

The goal is to demonstrate not just technical skill, but also market intuition and edge discovery — key qualities for a desk trader role.

---

## Overview

This repository contains various projects related to trading strategies, quantitative analysis, and market data validation. The projects are organized into different folders based on their focus areas. Below is an overview of each major folder and project within this repository:

---

## Table of Contents

1. [Core Trading Strategies](#core-trading-strategies)
   1. [ny session momentum analysis](#ny-session-momentum-analysis)
   2. [lstm market direction model](#lstm-market-direction-model)
   3. [volume contraction breakout analysis](#volume-contraction-breakout-analysis)
   4. [Live Results and Backtests](#live-results-and-backtests)
   5. [Research Papers](#research-papers)
   6. [Risk Simulation Monte Carlo](#risk-simulation-montecarlo)
2. [Trading Tools](#trading-tools)
   1. [Comment Classifier Project](#comment-classifier-project)
   2. [Data Validation Project](#data-validation-project)
   3. [Settlement Time Extraction](#settlement-time-extraction)
   4. [Helper Functions](#helper-functions)
3. [Disclaimer](#disclaimer)
4. [Usage](#usage)
5. [Contribution Guidelines](#contribution-guidelines)
6. [License](#license)

---

## Core Trading Strategies

This folder contains my **personal work on trading strategies**, including quantitative models and analysis techniques. Below are the key sub-projects in this folder:

### `ny session momentum analysis`
This sub-project focuses on testing a trading hypothesis where the **momentum** of Asian and London sessions is analyzed to predict the likelihood of momentum following through into the New York session.

- **Key Insight**: I found that there is a **68% chance** that momentum observed during the Asian and London sessions will follow through into the NY session.
- **Data**: This logic was tested using data from **2010 to 2024**, and the model was rigorously backtested to validate the hypothesis.

### `lstm market direction model`
The LSTM model was designed using **hand-derived custom data** (not relying on regular OHLC, volume, etc.). It processes the data and attempts to predict the next trend using **binary classification** (up or down) based on a **sliding window approach**.

- **Win Rate**: The model achieves a **59% win rate**.
- **Issue**: The model suffers from **overfitting** due to insufficient data.
- **Solution**: To address this, a **Generative Adversarial Network (GAN)** model is suggested to produce **synthetic data** for training, as data collection is time-consuming and costly.

### `volume contraction breakout analysis`
This project investigates a commonly cited retail pattern — the “inside candle” — using a quantitative lens. It evaluates price continuation probability following inside bar formations, using volume confirmation and a **1:3 RR rule**.

- **Win Rate**: The strategy provides a base win rate of **38%**.
- **Data**: Backtested across all S&P 500 stocks during the period from **2010 to 2024**.
- **Key Insight**: While the base win rate is 38%, results show promise when combined with volatility filters — and may serve as a secondary confirmation signal in momentum strategies.

### `Live Results and Backtests`
This section contains **personal proof** of my trading performance, including:
- **Phase 1 funded challenge statement** (verifiable)
- **$50 to $621 account flip in 1.5 months**
- **Manual journal for TA-based strategies**

### `Research Papers`
This section includes various **research papers** and **personal blog posts** where I discuss:
- My understanding of **macro economics**.
- Strategies I’ve worked on or studied, along with the insights I’ve gained.
- **Video tutorials** where I explain economic concepts, trading strategies, and other important topics.

### `Risk Simulation Monte Carlo`
The risk simulation folder contains models used to simulate potential **trading scenarios** for my personal account, including:
- **Monte Carlo simulations** that help evaluate the risk of various trading strategies.
- These simulations provide insight into the **real-world risk exposure** and how different strategies would perform in various market conditions.

📄 **Strategy Report (PDF): Reversal Zones v1.0**  
> A documented PDF explaining setup logic, market condition filtering, backtest result, sample trades, and journal analysis.  
**This document is in final iterations and will be updated shortly**.  
[View PDF](link-to-your-PDF)  

---

## Trading Tools

This folder includes various utility projects that assist with data validation, classification, and trade exposure. Below are the key sub-projects in this folder:

### `Comment Classifier Project`
An end-to-end, fully automated project that uses **AI/ML** to classify traders' comments on different commodities.

#### Key Features:
- Automated comment classification
- Uses AI/ML for accurate analysis
- Tailored to trading and commodity markets

---

### `Data Validation Project`
Validates data integrity from both external sources and internal systems to ensure consistency in contract prices (e.g., DFL, CFD, spread) for Brent.

#### Key Features:
- Ensures data consistency
- Validates contract prices (DFL, CFD, spread)
- Focuses on Brent commodity data

---

### `Settlement Time Extraction`
Extracts settlement time data from the source/arbitrator website, especially for non-standard trading days. Allows traders to input a date and retrieve relevant product settlement times and reasons.

#### Key Features:
- Retrieves settlement data on non-standard days
- Provides a dynamic interface for date-based queries
- Displays reasons for any settlement changes

---

### `Helper Functions`
Tools designed to assist traders in understanding their exposure for planned trades. These calculators provide insights into risk management and position sizing.

#### Key Features:
- Assists in calculating trade exposure
- Helps with risk management decisions
- Useful for real-time trading evaluations

---

## Disclaimer

1. Some content might not be viewable directly on GitHub. In such cases, please download the content to view it properly.

---

## Usage

To use any of the projects, follow the installation and usage instructions provided in their respective directories. If no instructions are available, please open an issue to request further documentation.

---

## Contribution Guidelines

Feel free to fork the repository and submit pull requests. For contributions, please follow these steps:

1. Fork this repository.
2. Create a new branch for your changes:  
   `git checkout -b feature-branch`
3. Commit your changes:  
   `git commit -am 'Add new feature'`
4. Push to your branch:  
   `git push origin feature-branch`
5. Open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Trading Projects Repository

## Overview

This repository contains various projects related to trading strategies, quantitative analysis, and market data validation. The projects are organized into different folders based on their focus areas. Below is an overview of each major folder and project within this repository:

---

## Table of Contents

1. [Projects](#projects)
   1. [Trading Folder](#trading-folder)
      1. [Backtesting](#backtesting)
      2. [LSTM Model](#lstm-model)
      3. [Other Proofs](#other-proofs)
      4. [Research Papers](#research-papers)
      5. [Risk Analysis](#risk-analysis)
   2. [Comment Classifier Project](#comment-classifier-project)
   3. [Data Validation Project](#data-validation-project)
   4. [Settlement Time Extraction](#settlement-time-extraction)
   5. [Helper Calculators](#helper-calculators)
2. [Disclaimer](#disclaimer)
3. [Usage](#usage)
4. [Contribution Guidelines](#contribution-guidelines)
5. [License](#license)

---

## Projects

### `Trading` Folder

This folder contains my **personal work on trading strategies, quantitative analysis**, and other **research**. Below are the key sub-projects in this folder:

#### Backtesting
This sub-project focuses on testing a trading hypothesis where the **momentum** of Asian and London sessions is analyzed to predict the likelihood of momentum following through into the New York session.

- **Key Insight**: I found that there is a **68% chance** that momentum observed during the Asian and London sessions will follow through into the NY session.
- **Data**: This logic was tested using data from **2010 to 2024**, and the model was rigorously backtested to validate the hypothesis.

#### LSTM Model
The LSTM model was designed using **hand-derived custom data** (not relying on regular OHLC, volume, etc.). It processes the data and attempts to predict the next trend using **binary classification** (up or down) based on a **sliding window approach**.

- **Win Rate**: The model achieves a **59% win rate**.
- **Issue**: The model suffers from **overfitting** due to insufficient data.
- **Solution**: To address this, a **Generative Adversarial Network (GAN)** model is suggested to produce **synthetic data** for training, as data collection is time-consuming and costly.

#### Other Proofs
This section contains **personal proof** of my trading performance, including:
- **Trading statements** from my **funded account phase 1** and **personal account**, where I flipped my balance from **$50 to $621**.
- **Indian market statements** spanning **two years**.
- **Other accounts' statements** that I consult, as well as my **journals** detailing various trading strategies I’ve worked on and am currently working on.

#### Research Papers
This section includes various **research papers** and **personal blog posts** where I discuss:
- My understanding of **macro economics**.
- Strategies I’ve worked on or studied, along with the insights I’ve gained.
- **Video tutorials** where I explain economic concepts, trading strategies, and other important topics.

#### Risk Analysis
The risk analysis folder contains models used to simulate potential **trading scenarios** for my personal account, including:
- **Monte Carlo simulations** that help evaluate the risk of various trading strategies.
- These simulations provide insight into the **real-world risk exposure** and how different strategies would perform in various market conditions.

---

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

### `Helper Calculators`

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

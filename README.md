# portfolio-optimizer
Portfolio Optimizer is a Streamlit-based web application that helps users optimize their stock portfolios using historical data and the Sharpe Ratio. It supports both global and Indian stock tickers and provides visualizations, expected return, volatility, and Sharpe ratio for the optimal portfolio.


# 📈 Portfolio Optimizer

A Streamlit web app to optimize a stock portfolio using the Sharpe Ratio.  
Supports both Indian (e.g., HDFCBANK.NS) and US/global stocks (e.g., AAPL, MSFT).

## 🔧 Features

- 📥 Fetches historical stock data from Yahoo Finance  
- 📅 Choose custom date range  
- 📊 Calculates:
  - Expected annual return
  - Portfolio volatility
  - Sharpe Ratio
  - Optimal stock weights  
- 📉 Visualizes portfolio allocation

## 📌 How to Use

1. Enter stock tickers separated by comma  
   Example: `AAPL, MSFT, GOOGL, HDFCBANK.NS`  
2. Select start and end dates  
3. Click **Optimize Portfolio**

## 🚀 Run Locally

```bash
git clone https://github.com/TheSangamX/portfolio-optimizer.git
cd portfolio-optimizer
pip install -r requirements.txt
streamlit run streamlit_app.py
🧾 Files Included
streamlit_app.py – Streamlit web app

main.py – (Optional core logic file)

requirements.txt – Required Python packages

README.md – App documentation

📌 Notes
Add .NS suffix for Indian stocks (e.g., TCS.NS, RELIANCE.NS)

App uses Yahoo Finance (via yfinance) for data

Ensure internet connection when fetching live data

Made with ❤️ by Sangam Gupta

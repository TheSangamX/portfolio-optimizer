import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px
from scipy.optimize import minimize

# App Title
st.set_page_config(page_title="📈 Portfolio Optimizer", layout="wide")
st.title("📈 Portfolio Optimizer")
st.markdown("""
Enter stock tickers separated by comma (e.g. `AAPL, MSFT, GOOGL`)  
& for Indian stocks enter suffix as `.NS` (e.g. `RELIANCE.NS, TCS.NS`)
""")

# Sidebar Inputs
with st.sidebar:
    tickers_input = st.text_input("Enter Stock Tickers")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    run_button = st.button("🚀 Optimize Portfolio")

if run_button:
    try:
        tickers = [ticker.strip().upper() for ticker in tickers_input.split(",") if ticker.strip() != ""]

        st.info("📥 Downloading stock data...")
        data = yf.download(tickers, start=start_date, end=end_date)["Close"]

        # Drop rows with any missing values
        data.dropna(axis=0, inplace=True)

        # Calculate daily returns
        returns = data.pct_change().dropna()

        # Optimization Function
        def portfolio_performance(weights, mean_returns, cov_matrix):
            returns = np.sum(mean_returns * weights) * 252
            std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
            sharpe = returns / std
            return -sharpe

        def optimize_portfolio(mean_returns, cov_matrix):
            num_assets = len(mean_returns)
            args = (mean_returns, cov_matrix)
            constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
            bounds = tuple((0, 1) for _ in range(num_assets))
            result = minimize(portfolio_performance, num_assets * [1. / num_assets, ], args=args,
                              method='SLSQP', bounds=bounds, constraints=constraints)
            return result.x

        mean_returns = returns.mean()
        cov_matrix = returns.cov()
        weights = optimize_portfolio(mean_returns, cov_matrix)

        st.success("✅ Portfolio optimized successfully!")

        # Show weights
        st.subheader("📊 Optimized Portfolio Weights:")
        weight_df = pd.DataFrame({"Stock": tickers, "Weight (%)": [round(w * 100, 2) for w in weights]})
        st.dataframe(weight_df, use_container_width=True)

        # Plot allocation
        fig = px.bar(weight_df, x="Stock", y="Weight (%)", color="Stock",
                     title="📊 Portfolio Allocation", text="Weight (%)")
        st.plotly_chart(fig, use_container_width=True)

        # Portfolio Metrics
        port_return = np.sum(mean_returns * weights) * 252
        port_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
        sharpe_ratio = port_return / port_volatility

        st.subheader("📈 Portfolio Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("📈 Expected Return", f"{port_return:.2%}")
        col2.metric("⚠️ Volatility", f"{port_volatility:.2%}")
        col3.metric("📊 Sharpe Ratio", f"{sharpe_ratio:.2f}")

    except Exception as e:
        st.error(f"❌ Something went wrong: {e}")

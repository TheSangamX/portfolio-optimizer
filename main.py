# main.py

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Sample list of stocks
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
data = yf.download(stocks, start="2022-01-01", end="2023-01-01")['Close']
returns = data.pct_change().dropna()

# Portfolio optimization
def portfolio_volatility(weights, mean_returns, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

mean_returns = returns.mean()
cov_matrix = returns.cov()
num_assets = len(stocks)
initial_weights = num_assets * [1. / num_assets]
bounds = tuple((0, 1) for _ in range(num_assets))
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

result = minimize(portfolio_volatility, initial_weights,
                  args=(mean_returns, cov_matrix), method='SLSQP',
                  bounds=bounds, constraints=constraints)

print("Optimized Portfolio Weights:")
for stock, weight in zip(stocks, result.x):
    print(f"{stock}: {weight:.2%}")

# source and reference : https://www.machinelearningplus.com/machine-learning/portfolio-optimization-python-example/
# project name : Portfolio Optimization with Python using Efficient Frontier

# Load package
import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import datetime as dt

# Set range of time
start_time = dt.datetime(year=2021, month=1, day=1)
end_time = dt.datetime(year=2022, month=1, day=3)

# Read data
df = data.DataReader(["AAPL", "NKE", "GOOGL", "AMZN"], "yahoo", start_time, end_time)
df = df["Close"]
df = pd.DataFrame(df)
print(df)

# calculate covariance and correlation
cov_matrix = df.pct_change().apply(lambda x: np.log(1 + x)).cov()
print(f"\n\nCovariance of all stocks \n{cov_matrix}")

# calculate correlation matrix
corr_matrix = df.pct_change().apply(lambda x: np.log(1 + x)).corr()
print(f"\n\nCorrelation of all stocks \n{corr_matrix}")

# portfolio variance
# money allocation -> Apple 10%, Nike 20%, Google 50%, Amazon 20%
weight_allocation = {"AAPL":0.1, "NKE":0.2, "GOOGL":0.5, "AMZN":0.2}
port_var = cov_matrix.mul(weight_allocation, axis=0).mul(weight_allocation, axis=1).sum().sum()
print(f"\n\nPortfolio variance {port_var}")

# portfolio expected return
individual_expectedReturn = df.resample('Y').last().pct_change().mean()
print(f"\n\nEach share gives a return \n{individual_expectedReturn}")

# portfolio return
weight_allocation = [0.1, 0.2, 0.5, 0.2]
port_exp_return = (weight_allocation * individual_expectedReturn).sum()
print(f"\n\nPortfolio expected return {port_exp_return}")

# Volatility is given by the annual standard deviation. Trading day is about 250 day
annual_deviation = df.pct_change().apply(lambda x: np.log(1 + x)).std().apply(lambda x: x * np.sqrt(250))
print(f"\n\nAnnual standard deviation \n{annual_deviation}")

# create table to visualize all asset stock
asset = pd.concat([individual_expectedReturn, annual_deviation], axis=1)
asset.columns = ["Returns", "Volatility"]
print(f"\n\nAsset table \n{asset}")


portf_return = []
portf_volatility = []
portf_weight = []

num_asset = len(df.columns)
num_portfolio = 10000

for portfolio in range(num_portfolio):
    weights = np.random.randint(num_asset)
    weights = weights / np.sum(weights)
    portf_weight.append(weights)
    returns = np.dot(weights, individual_expectedReturn)

    portf_return.append(returns)
    varz = cov_matrix.mul(weights, axis=0).mul(weights, axis=1).sum().sum()
    std_deviation = np.sqrt(varz)
    annual_deviation = std_deviation * np.sqrt(250)

    portf_volatility.append(annual_deviation)

data = {"Return":portf_return, "Volatility":portf_volatility}

for counter, symbol in enumerate(df.columns.tolist()):
    data[symbol + " weight"] = [w[counter] for w in portf_weight]

portfolio = pd.DataFrame(data)
print(f"\n\nPortfolio \n{portfolio}")

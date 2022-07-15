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

# Read data               list ticker   data source    data periode
test = data.DataReader(["TSLA", "AMZN"], "yahoo", start_time, end_time)
test = test["Close"]  # ambil kolom harga closing saja
# test = pd.DataFrame(test, copy=True)  # convert to DataFrame format

# Calculate log of percentage change
tesla = test["TSLA"].pct_change().apply(lambda x: np.log(1 + x))
amazon = test["AMZN"].pct_change().apply(lambda x: np.log(1 + x))
#print(tesla)
#print(amazon)

# Calculate variance of tesla stock
var_tesla = tesla.var()
var_amazon = amazon.var()
print(f"Variance of TSLA stock {var_tesla}")
print(f"Variance of AMZN stock {var_amazon}")

# Calculate volatility of each stock
tsla_vol = np.sqrt(var_tesla * 250)
amzn_vol = np.sqrt(var_amazon * 250)
print(f"TSLA volatility {tsla_vol}, AMZN volatility {amzn_vol}")

# Volatility of both stock
test.pct_change().apply(lambda x: np.log(1 + x)).std().apply(lambda x: x * np.sqrt(250)).plot(kind="bar")
#plt.show()  # uncomment to preview plot diagram

# covariance




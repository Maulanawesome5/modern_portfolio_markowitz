# source and reference : https://www.machinelearningplus.com/machine-learning/portfolio-optimization-python-example/
# project name : Portfolio Optimization with Python using Efficient Frontier

# Load package
import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import datetime as dt

# Set range of time
start_time = dt.datetime(year=2018, month=1, day=1)
end_time = dt.datetime.now()

# Read data               list ticker   data source    data periode
test = data.DataReader(["TSLA", "AMZN"], "yahoo", start_time, end_time)
test = test["Close"]
print(test)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data/TATAPOWER.NS.csv', parse_dates=['Date'], index_col='Date')
print(data)

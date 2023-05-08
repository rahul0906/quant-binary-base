import datetime
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
import utilities.utils as utils
import robin.utils as rutils


api_key = "PKDX1ONV8MASSY7TKAAG"
secret_key = "hvSF9OV0X9IXR6140I6nZcxEgVVOMaQKQoq7hWBo"

data = utils.get_historical_stock_data(api_key, secret_key, "AAPL", start_date=datetime.datetime(2023, 1, 1))
print(data.head())
print("Output")

# data1 = data - data.shift(1)
# print(data1)




# print(rutils.moving_average(data, 2))


# print(rutils.mcginley_dynamic_average(data, 20, 'close', True))

# print(rutils.get_ema(data))

# # print(rutils.supertrend(data))

# print(data.reset_index().index.values)

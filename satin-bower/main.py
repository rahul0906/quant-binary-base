import Supertrend as st
import utilities.utils as utils
import datetime

api_key = "PKDX1ONV8MASSY7TKAAG"
secret_key = "hvSF9OV0X9IXR6140I6nZcxEgVVOMaQKQoq7hWBo"

data = utils.get_historical_stock_data(api_key, secret_key, "AAPL", start_date=datetime.datetime(2019, 1, 1))
# print(data.head())
print("Output")
# st.backtest_supertrend(data, 100000)
# st.backtest_supertrend_with_mcginley(data, investment=100000)
# st.backtest_supertrend_with_ema_and_mcginley(data, investment=100000)
st.triple_bullish_with_ema(data, 100000, multipliers=[12, 11, 10], periods=[3, 2, 1])
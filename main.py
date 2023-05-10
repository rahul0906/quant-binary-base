# Python File to run the functions


import utilities.utils as utils
import utilities.realtime_crypto as rc
import datetime
import asyncio

api_key = "PKDX1ONV8MASSY7TKAAG"
secret_key = "hvSF9OV0X9IXR6140I6nZcxEgVVOMaQKQoq7hWBo"

# data = utils.get_historical_crypto_data(api_key, secret_key, ticker="BTC/USD", start_date=datetime.datetime(2023, 1, 1))
# print(data)


## Implementation of realtime_crypto   # Working Fine
def reed(data):
    print("Function Output : ", data.upper())

rc.full_run(reed)

##



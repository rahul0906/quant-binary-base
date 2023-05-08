import datetime
from alpaca.data import StockHistoricalDataClient, CryptoHistoricalDataClient
from alpaca.data.requests import StockBarsRequest, CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import asyncio
import websockets
import time


def get_historical_stock_data(api_key=None, secret_key=None, ticker=None, start_date=None):
    # Working Fine
    # start_date = datetime.datetime(start_date)
    stock_client = StockHistoricalDataClient(api_key, secret_key)
    stock_data_request = StockBarsRequest(symbol_or_symbols=ticker, timeframe=TimeFrame.Day, start=start_date)
    bars = stock_client.get_stock_bars(stock_data_request)
    return bars.df


def get_realtime_stock_data(api_key=None, secret_key=None, ticker=None):
    # Gotta wait Until Monday
    return None


def get_historical_crypto_data(api_key=None, secret_key=None, ticker=None, start_date=None):
    # Working
    crypto_client = CryptoHistoricalDataClient(api_key, secret_key)
    crypto_data_request = CryptoBarsRequest(symbol_or_symbols=ticker, timeframe= TimeFrame.Day, start= start_date)
    bars = crypto_client.get_crypto_bars(crypto_data_request)
    return bars.df


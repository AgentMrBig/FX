# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:31:02 2020
Used for getting Forex data
@author: Eric Hendrix
"""

import numpy as np
import pandas as pd
from datetime import datetime
import requests
import json
import finnhub


# use your own api key https://finnhub.io/ its free
# oanda forex symbols
FINNHUB_CLIENT = finnhub.Client(api_key="bu76jmf48v6rajd4sij0")
API_TOKEN = 'bu76jmf48v6rajd4sij0'
US30 = 'OANDA:US30_USD'
GBPUSD = 'OANDA:GBP_USD'
XAUUSD = 'OANDA:XAU_USD'
EURUSD = 'OANDA:EUR_USD'
USDJPY = 'OANDA:USD_JPY'
SPX500 = 'OANDA:SPX500_USD'
BTSUSD = 'OANDA:BTC_USD'

candles = ''
df = ''


# This function takes a date string in format 'Dec 25, 2018' and
# returns a timestamp for that date string
def setDateTimestamp(date):
    # Convert strings to datetime.datetime
    time_obj = datetime.strptime(date, '%b %d, %Y')
    # Convert datetime.datetime to timestamp
    time_stamp = datetime.timestamp(time_obj)
    # next I remove the dec by converting from float to int
    time_stamp = int(time_stamp)
    return time_stamp


def convertTimestampToDatetime(timestamp):
    time_Obj = datetime.fromtimestamp(timestamp)

    return time_Obj


def getFinanceData(fromTime, toTime, symbol, period):
    # api call to https://finnhub.io/ getting daily stock candles for netflix
    # in a specified date range
    #nflxData = finnhub_client.stock_candles('nflx', 'D', fromTime_stamp, toTime_stamp)

    # api call to get forex candles
    candles = FINNHUB_CLIENT.forex_candles(symbol, period, fromTime, toTime)
    # r = requests.get('https://finnhub.io/api/v1/forex/candle?symbol=OANDA:EUR_USD&resolution=D&from=1572651390&to=1575243390&token=bu76jmf48v6rajd4sij0')
    # print()
    # print(candles)

    # Forex symbols
    # print(candles)

    # pandas dataframe
    df = pd.DataFrame(candles)

    return df

# Supported resolution includes 1, 5, 15, 30, 60, D, W, M .Some timeframes might not be available depending on the exchange.
# df = getFinanceData(setTime('Dec 25, 2018'),
#                     setTime('Oct 25, 2020'), US30, '60')


def formatMarketData(df):
    # take dataframe, arrange coloumns
    # df = df[['c','h','l','o','t']]
    df = df[['t', 'o', 'h', 'l', 'c', 'v']]

    # Set the index to the date in the dataset and
    # convert the unix time in the data to datetime
    df = df.set_index(pd.to_datetime(df['t'], unit='s'))
    # drop the old unix time column/series
    df = df.drop('t', axis=1)

    return df

# Getting candle data using requsts
# token is API_TOKEN
# resolution REQUIRED Supported resolution includes 1, 5, 15, 30, 60, D, W, M
# Some timeframes might not be available depending on the exchange.
# from REQUIRED UNIX timestamp. Interval initial value.
# to REQUIRED UNIX timestamp. Interval end value.

# Response Attributes:

# o
# List of open prices for returned candles.

# h
# List of high prices for returned candles.

# l
# List of low prices for returned candles.

# c
# List of close prices for returned candles.

# v
# List of volume data for returned candles.

# t
# List of timestamp for returned candles.

# s
# Status of the response. This field can either be ok or no_data.


def getFXCandles(token, symbol, fromTime, toTime, resolution, dataFormat):

    r = ''
    pretty_r = ''
    result = ''
    
    if dataFormat == 'csv':
        r = requests.get('https://finnhub.io/api/v1/forex/candle?symbol={}&resolution={}&from={}&to={}&token={}&format={}'.format(
        symbol, resolution, fromTime, toTime, token, dataFormat))
        result = r.text
    elif dataFormat == 'json':
        r = requests.get('https://finnhub.io/api/v1/forex/candle?symbol={}&resolution={}&from={}&to={}&token={}'.format(
        symbol, resolution, fromTime, toTime, token))
        pretty_r = json.dumps(r.json(), indent=4)
        result = pretty_r
   

    
    return result

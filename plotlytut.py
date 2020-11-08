from numpy.core.multiarray import empty_like
import pandas as pd
import numpy as np
import datetime
import chart_studio.plotly as py
import plotly.tools as tls
import plotly.graph_objects as go
import finnhub_data as fin
import time
import json


# Get market data
# Supported resolution includes 1, 5, 15, 30, 60, D, W, M 
# .Some timeframes might not be available depending on the exchange.

us30_60 = fin.getFXCandles(fin.API_TOKEN, fin.US30, fin.setDateTimestamp('Nov 06, 2020'), fin.setDateTimestamp('Nov 08, 2020'), '60', 'json')

df = pd.read_json(us30_60)
df = df.tail(1)
df_f = fin.formatMarketData(df)

df_c = df_f['c']

# moving averages
short_ema = df_c.ewm(span=2, adjust = False).mean()

long_ema = df_c.ewm(span=7, adjust = False).mean()

df_f['slow'] = short_ema
df_f['fast'] = long_ema

print(df_f.tail())

# Create an interactive candlestick chart
# figure = go.Figure(
#   data = [
#     go.Candlestick(
#       x = df.index,
#       low = df['l'],
#       high = df['h'],
#       close = df['c'],
#       open = df['o'],
#       increasing_line_color = 'green',
#       decreasing_line_color = 'red',
#     )
#   ]
# )

# figure.update_layout(xaxis_rangeslider_visible = False)
# figure.update_layout(
#   title = 'US30 Price',
#   yaxis_title = 'US30 price in US$',
#   xaxis_title = 'Data'
# )

# figure.show()

# Below is the code to get the latest candle at the 00 second on the next minute
# this is a loop which will
# currently fetching all candles for the current day
# TODO: fetch only the latest minute candle 
# drive plotly chart with the candle data to make live chart, figure out how to update
# plotly chart live without reloading the whole chart with .show()
# display seconds till next candle
def chartAdvance():
  on = 1
  s = 0
  prevData = pd.DataFrame({'a' : []})
  newCandleMoment = ''

  while on == 1:
    print(timeStuff())
  
    s = timeStuff()
    time.sleep(1)
    
    if(s == 0):
      # df = fin.getFXCandles(fin.API_TOKEN, fin.US30, fin.setDateTimestamp('Nov 06, 2020'), fin.setDateTimestamp('Nov 06, 2020'), '60', 'csv')

      # df = df.tail(1)
      # df = fin.formatMarketData(df)
      
      us30_60 = fin.getFXCandles(fin.API_TOKEN, fin.US30, fin.setDateTimestamp('Nov 06, 2020'), fin.setDateTimestamp('Nov 08, 2020'), '60', 'json')

      df = pd.read_json(us30_60)
      df = df.tail(1)
      df_f = fin.formatMarketData(df)
      
      short_ema = df_c.ewm(span=2, adjust = False).mean()

      long_ema = df_c.ewm(span=7, adjust = False).mean()

      df_f['slow'] = short_ema
      df_f['fast'] = long_ema


      print("New Candle")
      if prevData.empty == True:
        print("prevData empty!")
        newCandleMoment = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        print("Data was updated at ", newCandleMoment)
        print("Previous data = ", prevData)
        print("new data = ", df_f)
        prevData = df_f
      elif df_f.empty != True:
        if int(df_f['c']) != int(prevData['c']):
          print("dataframes not equal!")
          newCandleMoment = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
          print("Data was updated at ", newCandleMoment)
          print("Previous data = ", prevData)
          print("new data = ", df_f)
          prevData = df_f
  
def timeStuff():
  # currentSecond = datetime.datetime.now() / 60
  
  
  currentTime = datetime.datetime.now().second
  return currentTime
  

chartAdvance()
# print(df.tail())
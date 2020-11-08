import numpy as np
import pandas as pd
import finnhub_data as fin
import csv

def snapshot(resolution):
  f = open('datasets/hourly/btcusd.csv')
  df = fin.getFXCandles(fin.API_TOKEN, fin.BTSUSD, fin.setDateTimestamp('Jan 01, 2010'), fin.setDateTimestamp('Oct 29, 2020'), resolution, 'csv')   
  writer = csv.writer(f)
  writer.writerows(df)
  # df.('datasets/hourly/btcusd.csv')
  f.close()
  

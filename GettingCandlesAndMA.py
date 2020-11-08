import numpy as np
import pandas as pd
from datetime import datetime
import json
import finnhub_data as fin

import matplotlib.pyplot as plt



us30_60 = fin.getFXCandles(fin.API_TOKEN, fin.US30, fin.setDateTimestamp('Jan 01, 2010'), fin.setDateTimestamp('Oct 29, 2020'), '60', 'json')

df = pd.read_json(us30_60)
df_f = fin.formatMarketData(df)

df_c = df_f['c']

# moving averages
short_ema = df_c.ewm(span=2, adjust = False).mean()

long_ema = df_c.ewm(span=7, adjust = False).mean()

df_f['slow'] = short_ema
df_f['fast'] = long_ema

print(df_f.tail())

# def order2ma(data):
#   buy_list = []
#   sell_list = []
#   flag_long = False
#   flag_short = False
  
#   for i in range(0, len(data)):
#     if data['slow'][i] < data['fast'][i] and flag_long == False:
#       buy_list.append(np.nan)
#       sell_list.append(data['c'][i])
#       flag_short = True
#       flag_long = False
#     elif data['slow'][i] > data['fast'][i] and flag_short == False:
#       buy_list.append(data['c'][i])
#       sell_list.append(np.nan)
#       flag_short = False
#       flag_long = True
#     else:
#       buy_list.append(np.nan)
#       sell_list.append(np.nan)
#   return(buy_list, sell_list)

# df_f['Buy'] = order2ma(df_f)[0]
# df_f['Sell'] = order2ma(df_f)[0]
      
# print(df_f.tail())
# plt.figure(figsize=(12.2, 4.5))
# plt.title('Ma Orders Plot', fontsize=18)

# plt.plot(df_f['c'], label='Close Price', color='blue', alpha=0.35)
# plt.plot(short_ema, label='Fast EMA', color='green',alpha=0.35)
# plt.plot(long_ema, label='Slow ema', color='red',alpha=0.35)

# plt.scatter(df_f.index, df_f['Buy'], color='green', marker='^', alpha=1)
# plt.scatter(df_f.index, df_f['Sell'], color='red', marker='v', alpha=1)

# plt.xlabel('Date', fontsize=18)
# plt.ylabel('Close Price', fontsize=18)
# plt.show()




import talib
import requests
import numpy as np


res = requests.get('https://cdlrecognizer.deta.dev/ohlc/btcusdt/5m')
data = res.json()

time,open,high,low,close = [],[],[],[],[]
for dt in data:
    time.append(dt['time'])
    open.append(dt['open'])
    high.append(dt['high'])
    low.append(dt['low'])
    close.append(dt['close'])

result =  talib.CDLDOJISTAR(open=np.array(open),high=np.array(high),low=np.array(low),close=np.array(close))

bullish = [time[li[0]] for li in np.argwhere(result == 100).tolist()]

bearish = [time[li[0]] for li in np.argwhere(result == -100).tolist()]

print(bearish)
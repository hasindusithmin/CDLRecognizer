import json
import talib
import requests
import numpy as np
from fastapi import FastAPI,HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CDLRecognizeAPI")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount('/static',StaticFiles(directory='static'),name='static')


@app.get("/")
def root():
    return FileResponse('index.html')

def gen_candle(dt):
    return {
        'time':int(dt[0]/1000)+19800,
        'open':float(dt[1]),
        'high':float(dt[2]),
        'low':float(dt[3]),
        'close':float(dt[4])
    }

@app.get("/ohlc/{symbol}/{interval}")
def get_ohlc(symbol:str,interval:str):
    symbol,interval = symbol.strip().upper(),interval.strip()
    
    with open('static/symbols.json','r') as symbols:
        if symbol not in json.load(symbols):
            raise HTTPException(status_code=400,detail=f'Invalid symbol :{symbol.lower()}')
        
    with open('static/intervals.json','r') as intervals:
        if interval not in json.load(intervals).values():
            raise HTTPException(status_code=400,detail=f'Invalid interval :{interval}')
        
    url = f'https://www.binance.com/api/v3/klines?symbol={symbol}&interval={interval}'
    res = requests.get(url)
    data = res.json()
    return [gen_candle(dt) for dt in data]

@app.get("/pattern/{symbol}/{interval}/{pattern}")
def get_patterns(symbol:str,interval:str,pattern:str):
    symbol,interval,pattern = symbol.strip().upper(),interval.strip(),pattern.strip().upper()
    
    with open('static/symbols.json','r') as symbols:
        if symbol not in json.load(symbols):
            raise HTTPException(status_code=400,detail=f'Invalid symbol :{symbol.lower()}')
    
    with open('static/intervals.json','r') as intervals:
        if interval not in json.load(intervals).values():
            raise HTTPException(status_code=400,detail=f'Invalid interval :{interval}')
    
    with open('static/pattern.json','r') as patterns:
        if pattern not in json.load(patterns).values():
            raise HTTPException(status_code=400,detail=f'Invalid pattern :{pattern.lower()}')
    
    url = f'https://www.binance.com/api/v3/klines?symbol={symbol}&interval={interval}'
    res = requests.get(url)
    data = res.json()
    data = [gen_candle(dt) for dt in data]
    time,open_,high,low,close = [],[],[],[],[]
    for dt in data:
        time.append(dt['time'])
        open_.append(dt['open'])
        high.append(dt['high'])
        low.append(dt['low'])
        close.append(dt['close'])
    result =  eval(f'talib.{pattern}(open=np.array(open_),high=np.array(high),low=np.array(low),close=np.array(close))')
    
    bullish = [time[li[0]] for li in np.argwhere(result == 100).tolist()]
    bearish = [time[li[0]] for li in np.argwhere(result == -100).tolist()]
    
    return {
        'bullish':bullish,
        'bearish':bearish
    }





    


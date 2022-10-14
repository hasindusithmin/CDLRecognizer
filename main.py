import json
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
    symbol,interval = symbol.upper().strip(),interval.strip()
    with open('static/symbols.json','r') as symbols:
        if symbol not in json.load(symbols):
            raise HTTPException(status_code=404,detail=f'Invalid symbol :{symbol}')
    with open('static/intervals.json','r') as intervals:
        if interval not in json.load(intervals).values():
            raise HTTPException(status_code=404,detail=f'Invalid interval :{interval}')
    url = f'https://www.binance.com/api/v3/klines?symbol={symbol}&interval={interval}'
    res = requests.get(url)
    data = res.json()
    return [gen_candle(dt) for dt in data]






    


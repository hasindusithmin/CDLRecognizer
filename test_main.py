import talib
import requests
import logging
from main import app
import numpy as np
from fastapi.testclient import TestClient


client = TestClient(app)
LOGGER = logging.getLogger(__name__)


def gen_candle(dt):
    return {
        'time':int(dt[0]/1000)+19800,
        'open':float(dt[1]),
        'high':float(dt[2]),
        'low':float(dt[3]),
        'close':float(dt[4])
    }

    
# pytest --log-cli-level=DEBUG
def test_get_ohlc():
    # 1. invalid interval 
    res = client.get('/ohlc/btcusdt/2s')
    assert res.status_code == 400
    assert res.json()['detail'] == 'Invalid interval :2s'
    # 2. invalid symbol 
    res = client.get('/ohlc/btcusd/1s')
    assert res.status_code == 400
    assert res.json()['detail'] == 'Invalid symbol :btcusd'
    # 3. valid data 
    res = client.get('/ohlc/btcusdt/5m')
    assert res.status_code == 200
    url = 'https://www.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m'
    res_ = requests.get(url)
    data = res_.json()
    data.pop()
    body = res.json()
    body.pop()
    assert body == [gen_candle(dt) for dt in data]

def test_get_patterns():
    # 1.invalid symbol 
    res = client.get('/pattern/ethusd/5m/cdldoji')
    assert res.status_code == 400
    assert res.json()['detail'] == 'Invalid symbol :ethusd'
    # 2.invalid interval 
    res = client.get('/pattern/ethusdt/7m/cdldoji')
    assert res.status_code == 400
    assert res.json()['detail'] == 'Invalid interval :7m'
    # 3.invalid pattern 
    res = client.get('/pattern/ethusdt/5m/xxxxx')
    assert res.status_code == 400
    assert res.json()['detail'] == 'Invalid pattern :xxxxx'
    # 4.valid data 
    res = client.get('/pattern/ethusdt/5m/cdldojistar')
    body = res.json()
    assert res.status_code == 200
    res_ = requests.get('https://cdlrecognizer.deta.dev/ohlc/ethusdt/5m')
    data = res_.json()
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
    assert body['bullish'] == bullish
    assert body['bearish'] == bearish

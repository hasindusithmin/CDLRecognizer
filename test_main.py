
import requests
import logging
from main import app
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
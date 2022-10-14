
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_ohlc():
    # 1. invalid interval 
    res = client.get('/ohlc/btcusdt/2s')
    assert res.status_code == 400
    assert res.json()['detail'] == 'Invalid interval :2s'
    # 2. invalid symbol 
    res = client.get('/ohlc/btcusd/1s')
    assert res.status_code == 400
    assert res.json()['detail'] == 'Invalid symbol :btcusd'
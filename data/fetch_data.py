import ccxt

def fetch_binance_data(symbol='BTC/USDT', timeframe='1h', limit=100):
    exchange = ccxt.binance()
    data = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    return data

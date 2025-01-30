import ccxt

def place_order(symbol, order_type, amount):
    exchange = ccxt.binance({
        'apiKey': 'your_api_key',
        'secret': 'your_api_secret'
    })
    if order_type == 'buy':
        return exchange.create_market_buy_order(symbol, amount)
    elif order_type == 'sell':
        return exchange.create_market_sell_order(symbol, amount)

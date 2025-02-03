import ccxt

def place_order(symbol, order_type, amount, stop_loss=0.02, take_profit=0.05):
    last_price = exchange.fetch_ticker(symbol)['last']

    if order_type == 'buy':
        stop_loss_price = last_price * (1 - stop_loss)
        take_profit_price = last_price * (1 + take_profit)
        print(f"Stop-Loss at ${stop_loss_price:.2f}, Take-Profit at ${take_profit_price:.2f}")

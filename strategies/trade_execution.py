import ccxt

def place_order(symbol, order_type, amount, stop_loss=0.02, take_profit=0.05):
    """
    Places an order with stop-loss and take-profit.
    stop_loss: 2% below buy price
    take_profit: 5% above buy price
    """
    last_price = exchange.fetch_ticker(symbol)['last']

    if order_type == 'buy':
        stop_loss_price = last_price * (1 - stop_loss)
        take_profit_price = last_price * (1 + take_profit)
        print(f"Setting Stop-Loss at {stop_loss_price}, Take-Profit at {take_profit_price}")

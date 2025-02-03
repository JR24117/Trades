def moving_average_strategy(data, short_window=5, long_window=20):
    """
    A moving average crossover strategy with optimized parameters.
    :param data: DataFrame containing 'close' prices.
    :param short_window: Short moving average window (default: 5).
    :param long_window: Long moving average window (default: 20).
    :return: Buy/Sell signals.
    """
    data['short_ma'] = data['close'].rolling(window=short_window).mean()
    data['long_ma'] = data['close'].rolling(window=long_window).mean()

    data['signal'] = 0
    data.loc[data['short_ma'] > data['long_ma'], 'signal'] = 1  # Buy
    data.loc[data['short_ma'] <= data['long_ma'], 'signal'] = -1  # Sell

    return data['signal']

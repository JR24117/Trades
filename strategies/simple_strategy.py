def moving_average_strategy(data, short_window=10, long_window=50):
    """
    A simple moving average crossover strategy.
    :param data: DataFrame with 'close' prices.
    :param short_window: Short moving average window.
    :param long_window: Long moving average window.
    :return: Buy/Sell signals.
    """
    data['short_ma'] = data['close'].rolling(window=short_window).mean()
    data['long_ma'] = data['close'].rolling(window=long_window).mean()

    data['signal'] = 0
    data.loc[data['short_ma'] > data['long_ma'], 'signal'] = 1  # Buy
    data.loc[data['short_ma'] <= data['long_ma'], 'signal'] = -1  # Sell

    return data['signal']


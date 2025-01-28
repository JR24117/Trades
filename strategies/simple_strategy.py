def moving_average_strategy(data, short_window=10, long_window=50):
    """
    A simple moving average crossover strategy.
    :param data: A DataFrame containing 'close' prices.
    :param short_window: Window size for the short moving average.
    :param long_window: Window size for the long moving average.
    :return: Buy/Sell signals as a list.
    """
    data['short_ma'] = data['close'].rolling(window=short_window).mean()
    data['long_ma'] = data['close'].rolling(window=long_window).mean()

    data['signal'] = 0
    data.loc[data['short_ma'] > data['long_ma'], 'signal'] = 1
    data.loc[data['short_ma'] <= data['long_ma'], 'signal'] = -1

    return data['signal']

def moving_average_strategy(data, short_window=5, long_window=20):
    """
    A moving average crossover strategy with optimized parameters.
    :param data: DataFrame containing 'close' prices.
    :param short_window: Short moving average window (default: 5).
    :param long_window: Long moving average window (default: 20).
    :return: Buy/Sell signals.
    """

    data['confirmed_signal'] = data['signal'].rolling(2).sum()  # Sum last 2 days

data.loc[data['confirmed_signal'] == 2, 'signal'] = 1  # Only buy if two buy signals in a row
data.loc[data['confirmed_signal'] == -2, 'signal'] = -1  # Only sell if two sell signals in a row


    return data['signal']

import pandas as pd

def rsi_strategy(data, window=14, overbought=70, oversold=30):
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window).mean()

    rs = gain / loss
    data['rsi'] = 100 - (100 / (1 + rs))

    data['signal'] = 0
    data.loc[data['rsi'] < oversold, 'signal'] = 1  # Buy
    data.loc[data['rsi'] > overbought, 'signal'] = -1  # Sell

    return data['signal']


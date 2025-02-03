import json
import pandas as pd
from strategies.simple_strategy import moving_average_strategy

# Load configuration
with open('data/config.json', 'r') as file:
    config = json.load(file)

# Load sample data
data = pd.read_csv('data/sample_data.csv')

# Apply strategy
signals = moving_average_strategy(data)

data[['date', 'signal']].to_csv('signals.csv', index=False)
print("Signals saved to signals.csv")

last_trade_day = None

for index, row in data.iterrows():
    if last_trade_day is None or (row['date'] - last_trade_day).days > 3:
        if row['signal'] == 1:
            place_order(symbol, 'buy', 0.001)
            last_trade_day = row['date']
        elif row['signal'] == -1:
            place_order(symbol, 'sell', 0.001)
            last_trade_day = row['date']

# Print results
print("Signals:")
print(signals)

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

# Print results
print("Signals:")
print(signals)

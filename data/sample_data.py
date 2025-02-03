import pandas as pd
import numpy as np
import os

# Set the output file path dynamically
base_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
output_path = os.path.join(base_dir, "sample_data.csv")  # Save inside 'data/' folder

# Generate sample historical market data
np.random.seed(42)  # Ensure reproducibility

# Simulate 100 days of trading data
dates = pd.date_range(start="2023-01-01", periods=100, freq="D")

# Simulate stock/crypto price movements
initial_price = 100
price_changes = np.random.randn(100) * 2  # Small random fluctuations
close_prices = np.cumsum(price_changes) + initial_price

# Simulate trading volume (random but within a reasonable range)
volume = np.random.randint(1000, 5000, size=100)

# Create a DataFrame
df = pd.DataFrame({
    "date": dates,
    "close": close_prices,
    "volume": volume
})

# Save to CSV
df.to_csv(output_path, index=False)

print(f"✅ Sample data generated successfully! File saved at: {output_path}")


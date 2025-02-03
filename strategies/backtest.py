import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Ensure Python recognizes the parent directory (Trades) as a module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the strategy function
from simple_strategy import moving_average_strategy

# Dynamically locate sample_data.csv
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../data/sample_data.csv")

def backtest(data, initial_balance=10000):
    """
    Simulates trading based on signals and calculates final portfolio balance.
    
    :param data: DataFrame with market data.
    :param initial_balance: Starting capital ($).
    :return: Final portfolio balance.
    """
    balance = initial_balance
    position = 0  # 0 = no position, >0 = holding asset

    for i in range(len(data)):
        signal = data['signal'].iloc[i]
        price = data['close'].iloc[i]

        if signal == 1 and position == 0:  # Buy
            position = balance / price  # Buy as much as possible
            balance = 0
            print(f"BUY at ${price:.2f}")

        elif signal == -1 and position > 0:  # Sell
            balance = position * price  # Sell everything
            position = 0
            print(f"SELL at ${price:.2f}")

    # Final balance calculation
    final_balance = balance + (position * data['close'].iloc[-1])
    print(f"\nFinal Balance: ${final_balance:.2f} (Initial: ${initial_balance:.2f})")
    
    return final_balance

if __name__ == "__main__":
    # Load historical data
    print(f"Loading data from: {data_path}")
    
    try:
        data = pd.read_csv(data_path)

        # Ensure 'date' is a datetime format
        data['date'] = pd.to_datetime(data['date'])

        # Apply trading strategy
        data['signal'] = moving_average_strategy(data)

        # Run backtest
        final_balance = backtest(data)

        # Plot price & signals
        plt.figure(figsize=(12, 6))
        plt.plot(data['date'], data['close'], label='Close Price', color='black')
        plt.scatter(data['date'][data['signal'] == 1], data['close'][data['signal'] == 1], color='green', label='Buy Signal', marker='^', alpha=1)
        plt.scatter(data['date'][data['signal'] == -1], data['close'][data['signal'] == -1], color='red', label='Sell Signal', marker='v', alpha=1)
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title("Backtesting Results")
        plt.legend()
        plt.grid()
        plt.show()

    except FileNotFoundError:
        print(f"❌ Error: Could not find data file at {data_path}")
        print("Make sure `sample_data.csv` exists in the `data/` folder.")

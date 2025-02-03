import os
import pandas as pd
import matplotlib.pyplot as plt
from simple_strategy import moving_average_strategy

# Dynamically construct the correct file path
base_dir = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
data_path = os.path.join(base_dir, "../data/sample_data.csv")  # Construct absolute path

def backtest(data):
    """
    Simulates trading based on signals and calculates profit/loss.
    :param data: DataFrame with market data.
    :return: Final portfolio balance.
    """
    initial_balance = 10000  # Starting capital ($)
    balance = initial_balance
    position = 0  # 0 means no position, 1 means holding asset

    for i in range(len(data)):
        signal = data['signal'].iloc[i]
        price = data['close'].iloc[i]

        if signal == 1 and position == 0:  # Buy signal
            position = balance / price  # Buy asset with all balance
            balance = 0
            print(f"BUY at {price}")

        elif signal == -1 and position > 0:  # Sell signal
            balance = position * price  # Sell everything
            position = 0
            print(f"SELL at {price}")

    final_balance = balance + (position * data['close'].iloc[-1])
    print(f"Final Balance: ${final_balance:.2f}")
    return final_balance

if __name__ == "__main__":
    # Load historical data using absolute path
    data = pd.read_csv(data_path)
    data['signal'] = moving_average_strategy(data)

    # Run backtest
    backtest(data)

    # Plot price & signals
    plt.plot(data['close'], label='Close Price')
    plt.scatter(data.index, data['close'], c=data['signal'], cmap='coolwarm', label='Signals')
    plt.legend()
    plt.show()

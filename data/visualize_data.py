import matplotlib.pyplot as plt

def plot_data(data):
    plt.plot(data['date'], data['close'], label='Close Price')
    plt.plot(data['date'], data['short_ma'], label='Short MA')
    plt.plot(data['date'], data['long_ma'], label='Long MA')
    plt.legend()
    plt.savefig('data/price_chart.png')

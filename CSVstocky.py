import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import organize


# Load historical stock data from CSV file
#stock_name = input('Enter stock ticker name: ')

def ma_create(stock_name):
    file_path = 'stocks/' + stock_name + '.csv'



    data = pd.read_csv(file_path)
    print('This is for the stock:' + stock_name)
    print('\n')

    # Ensure data is sorted by date
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values('Date')

    # Calculate moving averages
    data['50_SMA'] = data['Close'].rolling(window=50).mean()
    data['200_SMA'] = data['Close'].rolling(window=200).mean()

    # Generate buy/sell signals using .loc
    data.loc[50:, 'Signal'] = np.where(data.loc[50:, '50_SMA'] > data.loc[50:, '200_SMA'], 1, 0)
    data['Position'] = data['Signal'].diff()

    # Extract buy/sell signals
    buy_signals = data[data['Position'] == 1].copy()
    sell_signals = data[data['Position'] == -1].copy()

    # Add column to the Dataframe with ticker name for archive records
    if not buy_signals.empty:
        buy_signals.loc[:, 'Ticker'] = stock_name

    if not sell_signals.empty:
        sell_signals.loc[:, 'Ticker'] = stock_name

    # Plotting
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Close'], label='Close Price', color='blue')
    plt.plot(data['Date'], data['50_SMA'], label='50-Day SMA', color='orange')
    plt.plot(data['Date'], data['200_SMA'], label='200-Day SMA', color='red')
    plt.scatter(buy_signals['Date'], buy_signals['Close'], label='Buy Signal', marker='^', color='green', alpha=1)
    plt.scatter(sell_signals['Date'], sell_signals['Close'], label='Sell Signal', marker='v', color='red', alpha=1)
    plt.title('Stock Price with Buy and Sell Signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()

    # Save the plot as an image file
    plt.savefig('graph_images/' +stock_name +'.png')

    # Close the plot to free memory
    plt.close()

    # Display buy/sell signals
    print("Buy Signals:")
    print(buy_signals[['Date', 'Close', '50_SMA', '200_SMA']])

    print("\nSell Signals:")
    print(sell_signals[['Date', 'Close', '50_SMA', '200_SMA']])
    print('\n')

    # Save buy/sell signals to CSV for reference
    buy_signals.to_csv('buy_signals/' + stock_name + '_buy_signals.csv', index=False)
    sell_signals.to_csv('sell_signals/' + stock_name + '_sell_signals.csv', index=False)


    def append_to_master(master_path, signals):
        if os.path.isfile(master_path):
            master_df = pd.read_csv(master_path)
            combined_df = pd.concat([master_df, signals]).drop_duplicates(subset=['Date', 'Ticker'], keep='last')
            combined_df.to_csv(master_path, mode='w', header=True, index=False)
        else:
            signals.to_csv(master_path, mode='w', header=True, index=False)

    # Append to Master buy signals file
    append_to_master('buy_signals/Master_buy_signals.csv', buy_signals)

    # Append to Master sell signals file
    append_to_master('sell_signals/Master_sell_signals.csv', sell_signals)

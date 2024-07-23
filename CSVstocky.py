import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import organize


def rsi_creation(data):


    # Calcutlate Relative Strength Indenx (RSI)
    rs_window = 14
    delta = data['Close'].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=rs_window, min_periods=1).mean()
    avg_loss = loss.rolling(window=rs_window, min_periods=1).mean()

    rs = avg_gain/avg_loss
    rsi = 100 - (100/(1+rs))
    
    data['RSI'] = rsi

    global rsi_recent
    rsi_recent = rsi.iloc[-1]

    return data

def macd_creation(data):

    # Calculates the Moving Average Convergence Divergence (MACD)
    short_macd_ema = data['Close'].ewm(span=12, adjust=False).mean()
    long_macd_ema = data['Close'].ewm(span=26, adjust=False).mean()

    # Calculates the MACD line
    data['MACD'] = short_macd_ema - long_macd_ema

    # Calculates the signal line
    data['MACD_Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()

    # Calculate the MACD Histogram
    data['MACD_Hist'] = data['MACD'] - data['MACD_Signal']

    return data



def ma_create(stock_name):
    file_path = 'stocks/' + stock_name + '.csv'

    data = pd.read_csv(file_path)
    print('This is for the stock:' + stock_name)
    print('\n')

    # Ensure data is sorted by date
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values('Date')
    data.set_index('Date', inplace=True) 

    # Calculate simple moving averages (SMA)
    data['50_SMA'] = data['Close'].rolling(window=50).mean()
    data['200_SMA'] = data['Close'].rolling(window=200).mean()

    # Calculate Exponential Moving Data (EMA)
    data['8_EMA'] = data['Close'].ewm(span=8, adjust=False).mean()
    data['20_EMA'] = data['Close'].ewm(span=20, adjust=False).mean()

    # Generate buy/sell signals using .loc
    data['Signal'] = 0
    data.iloc[50:, data.columns.get_loc('Signal')] = np.where(
        data.iloc[50:, data.columns.get_loc('50_SMA')] > data.iloc[50:, data.columns.get_loc('200_SMA')], 1, 0
    )
    data['Position'] = data['Signal'].diff()

    # Extract buy/sell signals
    buy_signals = data[data['Position'] == 1].copy()
    sell_signals = data[data['Position'] == -1].copy()

    # Add column to the Dataframe with ticker name for archive records
    if not buy_signals.empty:
        buy_signals.loc[:, 'Ticker'] = stock_name

    if not sell_signals.empty:
        sell_signals.loc[:, 'Ticker'] = stock_name

    data = rsi_creation(data)
    data = macd_creation(data)
   
    # Debug: Print out date range to check
    print("Data Date Range: ", data.index.min(), " to ", data.index.max())

    # Plotting
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)


    ax1.plot(data.index, data['Close'], label='Close Price', color='blue')
    ax1.plot(data.index, data['50_SMA'], label='50-Day SMA', color='orange')
    ax1.plot(data.index, data['200_SMA'], label='200-Day SMA', color='red')
    ax1.plot(data.index, data['8_EMA'], label='8-Day EMA', color='pink')
    ax1.plot(data.index, data['20_EMA'], label='20-Day EMA', color='black')
    ax1.scatter(buy_signals.index, buy_signals['Close'], label='Buy Signal', marker='^', color='green', alpha=1)
    ax1.scatter(sell_signals.index, sell_signals['Close'], label='Sell Signal', marker='v', color='red', alpha=1)
    ax1.set_title(stock_name + ' (RSI = ' + str(rsi_recent.round(2)) + ')')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price')
    ax1.legend()
    ax1.grid()

    # Plot MACD data in the second subplot (ax2)
    ax2.plot(data.index, data['MACD'], label='MACD', color='g')
    ax2.plot(data.index, data['MACD_Signal'], label='Signal Line', color='r')
    ax2.bar(data.index, data['MACD_Hist'], label='MACD Hist', color='b', alpha=0.3)
    ax2.set_title('MACD')
    ax2.legend()
    ax2.grid()

    for label in ax2.get_xticklabels():
        label.set_rotation(45)

    # Save the plot as an image file
    plt.tight_layout()
    plt.savefig('graph_images/' +stock_name +'.png')

    # Close the plot to free memory
    plt.close()

    # Display buy/sell signals
    print("Buy Signals:")
    print(buy_signals[['Close', '50_SMA', '200_SMA']])

    print("\nSell Signals:")
    print(sell_signals[['Close', '50_SMA', '200_SMA']])
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


# stock_name = 'AAPL'
# file_path = 'stocks/' + stock_name + '.csv'
# print(rsi_creation(file_path))
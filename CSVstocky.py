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
    print('Creating datapoints for ' + stock_name)
    
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

    data = rsi_creation(data)
    data = macd_creation(data)
   

    # Plotting
    # First Plot: Price and Moving Averages
    fig, ax1 = plt.subplots(figsize=(14, 7))

    ax1.plot(data.index, data['Close'], label='Close Price', color='blue')
    ax1.plot(data.index, data['50_SMA'], label='50-Day SMA', color='orange')
    ax1.plot(data.index, data['200_SMA'], label='200-Day SMA', color='red')
    ax1.plot(data.index, data['8_EMA'], label='8-Day EMA', color='pink')
    ax1.plot(data.index, data['20_EMA'], label='20-Day EMA', color='black')
    ax1.set_title(stock_name + ' (RSI = ' + str(rsi_recent.round(2)) + ')')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price')
    ax1.legend()
    ax1.grid()

    plt.tight_layout()
    plt.savefig('graph_images/' + stock_name + '_price.png')
    plt.close()

    # Second Plot: MACD
    fig, ax2 = plt.subplots(figsize=(14, 7))

    ax2.plot(data.index, data['MACD'], label='MACD', color='g')
    ax2.plot(data.index, data['MACD_Signal'], label='Signal Line', color='r')
    ax2.bar(data.index, data['MACD_Hist'], label='MACD Hist', color='b', alpha=0.3)
    ax2.set_title('MACD for ' + stock_name)
    ax2.set_xlabel('Date')
    ax2.legend()
    ax2.grid()

    for label in ax2.get_xticklabels():
        label.set_rotation(45)

    plt.tight_layout()
    plt.savefig('graph_images/' + stock_name + '_macd.png')
    plt.close()

    




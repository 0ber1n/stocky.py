import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import organize
from datetime import datetime

current_date = datetime.now().strftime('%Y_%m_%d')
current_time = datetime.now().strftime('%H:%M:%S')

def rsi_creation(data, window=14):

    # Calcutlate Relative Strength Indenx (RSI)
    delta = data['Close'].pct_change() * 100

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()

    for i in range(window, len(avg_gain)):
        avg_gain.iloc[i] = ((avg_gain.iloc[i-1] * (window -1)) + gain.iloc[i]) / window
        avg_loss.iloc[i] = ((avg_loss.iloc[i-1] * (window -1)) + loss.iloc[i]) / window

    rs = avg_gain / avg_loss
    rsi = 100 - (100/(1 + rs))

     
    data['RSI'] = rsi

    global rsi_recent
    rsi_recent = data['RSI'].iloc[-1]

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

def calculate_uptick(sma):
    
    last_4_days_sma = sma[-10:]
    
    # Calculate the uptick values 
    uptick_values = last_4_days_sma.diff().fillna(0)
    
    return uptick_values

def trend_identify(df, sma50, sma200, stock_name):
    recent_trend_days = 10

    # Open the file in append mode
    with open('trends/' + current_date +'_trend_analysis_output.txt', 'a') as f:
        df['Recent_Trend'] = df[sma50].diff(periods=1)
        f.write('Recent Trend Calculation for:' + stock_name +'\n')
        f.write(df[['Recent_Trend']].tail(recent_trend_days).to_string())
        f.write('\n\n')

        def trend_direction(value):
            if value > 0:
                return 'Up Trend'
            elif value < 0:
                return 'Down Trend'
            else:
                return 'Sideways Trend'
        
        df['Trend'] = df['Recent_Trend'].apply(trend_direction)
        f.write("Trend Direction Calculation:\n")
        f.write(df[['Trend']].tail(recent_trend_days).to_string())
        f.write('\n\n')

        # Checking the proximity to a possible golden cross
        df['golden_cross_check'] = df[sma200] - df[sma50]
        if df[sma50].iloc[-1] < df[sma200].iloc[-1]:
            df['Getting_Closer'] = df['golden_cross_check'].diff().apply(lambda x: 'Yes' if x < 0 else 'No')
            f.write("Golden Cross Check:\n")
            f.write(df[['golden_cross_check', 'Getting_Closer']].tail(recent_trend_days).to_string())
            f.write('\n\n')
        else:
            # df['Getting_Closer'] = 'Too late to join or time to sell.'
            f.write('Golden Cross Check:\n')
            f.write('Too late to join or time to sell.\n')
            f.write('\n')
        
        f.write('**************************\n')
    
    return df



def ma_create(stock_name):

    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%Y_%m_%d")
    durrent_time = current_datetime.strftime('%H:%M:%S')

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

    data = trend_identify(data,'50_SMA','200_SMA', stock_name)

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
    plt.savefig('graph_images/' + stock_name + '_ma.png')
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
    plt.savefig('graph_images/macd/' + stock_name + '_macd.png')
    plt.close()

    




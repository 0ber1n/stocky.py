import os
from CSVstocky import *
from organize import *
from tickers import *
import time


def menu():

    print('1. Download ALL Historical Data')
    print('2. Download TOP-50 Historical Data')
    print('3. Run Moving Average for ALL stocks')
    print('4. Run Moving Average for TOP-50 stocks')
    print('5. ALL stock Golden Trend')
    print('6. Top-50 full run')

    menu_selection = input("\nEnter a selection from menu: ")

    # Need to add a delay so we don't DOS the yahoo finance servers
    delay = 30
    rounds_until_sleep = 100
    counter = 0

    
    if menu_selection == '1':
        for tickers in all_tickers:
            data_dump(tickers)
            counter += 1
            if counter == rounds_until_sleep:
                print('30 Second delay from download')
                time.sleep(delay)
                counter = 0
        print('All Historical data download complete!')

    elif menu_selection == '2':
        for tickers in fifty_tickers:
            data_dump(tickers)
        print('Top-50 Historical data download complete!')

    elif menu_selection == '3':
        for tickers in all_tickers:
            ma_create(tickers)
        print('All Datapoints created')

    elif menu_selection == '4':
        for tickers in fifty_tickers:
            ma_create(tickers)
        print('Top-50 datapoints created')

    elif menu_selection == '5':
        for tickers in all_tickers:
            data_dump(tickers)
            counter += 1
            if counter == rounds_until_sleep:
                print('5 Second delay from download')
                time.sleep(delay)
                counter = 0
        print('Check folder for Golden Trend')

    elif menu_selection == '6':
        for tickers in fifty_tickers:
            data_dump(tickers)
        for tickers in fifty_tickers:
            ma_create(tickers)
        print('TOP-50 Historical data downloaded and datapoints created')

    elif menu_selection == 'test':
        for tickers in test_tickers:
            data_dump(tickers)
            counter += 1
            if counter == rounds_until_sleep:
                print('5 Second delay from download')
                time.sleep(delay)
                counter = 0
            ma_create(tickers)
        print('All Datapoints created')

    else:
        print('Invalid choice')


def main():
    logo()

    # Check folder structure exists for newly created files
    organize.image_folder_check()
    organize.golden_trend_folder()
    organize.stock_folder_check()
    organize.trends_folder_check()
    organize.initialize_output_file()
    print('\n')

    menu()

    cont = input('\nWould you like to perform another action? (y/n) ')

    # Allows for the program to keep running after a selection is performed
    while cont == 'y':
        menu()
        cont = input('\nWould you like to perform another action? (y/n) ')

    print("Thanks for getting your stocky on, byeeeee")

if __name__ == "__main__":
    main()
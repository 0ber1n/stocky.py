import os
from CSVstocky import *
from organize import *
from tickers import *


def main():

    # Downloads a fresh report of all tickers
    fresh_data = input('Do you need to download fresh csv data?(y/n) ')
    if fresh_data == 'y':
        for tickers in all_tickers:
            data_dump(tickers)
    else:
        pass

    #Check folder structure exists for newly created files
    organize.image_folder_check()
    organize.buy_signal_check()
    organize.sell_signal_check()
    print('\n')


    runAll = input ('do you want to run the rack?(y/n) ')

    if runAll == 'y':
        for tickers in all_tickers:
            ma_create(tickers)
    else:
        runOne = input('Which one do you want to see? ')
        ma_create(runOne)
    
    os.system('cut -d, -f1,12 buy_signals/Master_buy_signals.csv | sort -t, -k1,1r | column -s, -t ')

if __name__ == "__main__":
    main()
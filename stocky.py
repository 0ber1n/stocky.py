import os
from CSVstocky import *
from organize import *
from tickers import *

def menu(menu_selection):
    
    match menu_selection:
        case '1':
            for tickers in all_tickers:
                data_dump(tickers)

        case '2':
            for tickers in all_tickers:
                ma_create(tickers)
                    
        case '3':
            data_dump()
            for tickers in all_tickers:
                ma_create(tickers)
            
        case '4':
            os.system('cut -d, -f1,12 buy_signals/Master_buy_signals.csv | sort -t, -k1,1r | column -s, -t ')
        
        case '5':
            os.system('cut -d, -f1,12 sell_signals/Master_sell_signals.csv | sort -t, -k1,1r | column -s, -t ')

        case _:
            return 'Invalide choice'




def main():

    # NEED to add menu here we go!!!
    logo()


    #Check folder structure exists for newly created files
    organize.image_folder_check()
    organize.buy_signal_check()
    organize.sell_signal_check()
    print('\n')

    print('1. Download Historical Data')
    print('2. Run Moving Average for ALL stocks')
    print('3. Run the rack!')
    print('4. Show the buy signal outputs')
    print('5. Show the sell signal outputs')
    
    menu_selection = input("\nEnter a selection from menu: ")
    menu(menu_selection)
 
    

if __name__ == "__main__":
    main()
import os
from CSVstocky import *
from organize import *
from tickers import *


def menu():

    print('1. Download Historical Data')
    print('2. Run Moving Average for ALL stocks')
    print('3. Run the rack!')

    menu_selection = input("\nEnter a selection from menu: ")

    match menu_selection:
        case '1':
            for tickers in all_tickers:
                data_dump(tickers)
            print('Historical data download complete!')

        case '2':
            os.system('rm trends/*')
            for tickers in all_tickers:
                ma_create(tickers)
            print('Datapoints created')
            
                    
        case '3':
            for tickers in all_tickers:
                data_dump(tickers)
            for tickers in all_tickers:
                ma_create(tickers)
            print('Historical data downloaded and datapoints created')

        case 'sleepy':
            
            for tickers in robinhood_24_hour_stocks:
                data_dump(tickers)
            for tickers in robinhood_24_hour_stocks:
                ma_create(tickers)
            print('Late night trading can start now')
           
        case _:
            return 'Invalide choice'



def main():


    logo()


    #Check folder structure exists for newly created files
    organize.image_folder_check()
    organize.stock_folder_check()
    organize.trends_folder_check()
    print('\n')

    # menu_selection = input("\nEnter a selection from menu: ")
    menu()

    cont = input('\nWould you like to perform another action?(y/n) ')

    # Allows for program to keep running after a selection is performed
    while (cont == 'y'):
        menu()
        cont = input('\nWould you like to perform another action?(y/n) ')
        

    print("Thanks for getting your stocky on, byeeeee")     
 
    

if __name__ == "__main__":
    main()
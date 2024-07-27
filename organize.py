# This is a folder cleanup module to ensure the right folders are created

import os
import matplotlib.pyplot as plt
from datetime import datetime



def image_folder_check():
        
    image_path = 'graph_images'
    macd_path = image_path +'/macd'
    if not os.path.exists(image_path):
        print('Graph images folder does not exist, creating parent folder')
        os.makedirs(image_path)
        print(image_path + ' created')
    if not os.path.exists(macd_path):
        print('MACD folder does not exist, creating folder')
        os.makedirs(image_path + '/macd')
        print(macd_path + ' created')

        
    else: 
        print('Graph folder exists.')

def stock_folder_check():
    stock_path = 'stocks'
    if not os.path.exists(stock_path):
        print('Stocks folder does not exist, creating folder')
        os.makedirs(stock_path)
        print(stock_path + ' created')
        
    else: 
        print('Stocks folder exists.')

def trends_folder_check():
    trends_path = 'trends'
    if not os.path.exists(trends_path):
        print('Trends folder does not exist, creating folder')
        os.makedirs(trends_path)
        print(trends_path + ' created')
        
    else: 
        print('Trends folder exists. Cleaning up now!')
        

def golden_trend_folder():
    image_path = 'graph_images'
    golden_trend_path = image_path + '/golden_trend'
    if not os.path.exists(golden_trend_path):
        print('Golden Trend folder does not exist, creating folder')
        os.makedirs(golden_trend_path)
        print(golden_trend_path + ' created')
        
    else: 
        print('Golden Trend folders exist.')

def initialize_output_file():
    current_date = datetime.now().strftime('%Y-%m-%d')
    output_file = f'trends/{current_date}_trend_analysis_output.txt'

    # Create a new file (overwrite if exists)
    with open(output_file, 'w') as f:
        f.write('Trend Analysis Output\n')
        f.write('**************************\n')
    return output_file


def logo():
    print('''  
  ______  ________   ______    ______   __    __  __      __ 
 /      \|        \ /      \  /      \ |  \  /  \|  \    /  \ 
|  $$$$$$\\$$$$$$$$|  $$$$$$\|  $$$$$$\| $$ /  $$ \$$\  /  $$ 
| $$___\$$  | $$   | $$  | $$| $$   \$$| $$/  $$   \$$\/  $$  
 \$$    \   | $$   | $$  | $$| $$      | $$  $$     \$$  $$   
 _\$$$$$$\  | $$   | $$  | $$| $$   __ | $$$$$\      \$$$$    
|  \__| $$  | $$   | $$__/ $$| $$__/  \| $$ \$$\     | $$     
 \$$    $$  | $$    \$$    $$ \$$    $$| $$  \$$\    | $$     
  \$$$$$$    \$$     \$$$$$$   \$$$$$$  \$$   \$$     \$$     
                                                                    
                     Developed by 0ber1n                                                               
                                                                    
''')
    

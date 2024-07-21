# This is a folder cleanup module to ensure the right folders are created

import os
import matplotlib.pyplot as plt


def image_folder_check():
        
    image_path = 'graph_images'
    if not os.path.exists(image_path):
        print('Graph images folder does not exist, creating folder')
        os.makedirs(image_path)
        print(image_path + ' created')
        
    else: 
        print('Graph folder exists.')
        

def sell_signal_check():
    sell_path = 'sell_signals'
    if not os.path.exists(sell_path):
        print('Sell Signal folder does not exist, creating folder')
        os.makedirs(sell_path)
        print(sell_path + ' created')
        
    else: 
        print('Sell Signal folder exists.')
        

def buy_signal_check():
    buy_path = 'buy_signals'
    if not os.path.exists(buy_path):
        print('Buy Signal folder does not exist, creating folder')
        os.makedirs(buy_path)
        print(buy_path + ' created')
        
    else: 
        print('Buy Signal folder exists.')


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
                                                                    
                                                                    
                                                                    
''')
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
        

def stock_folder_check():
    stock_path = 'stocks'
    if not os.path.exists(stock_path):
        print('Stocks folder does not exist, creating folder')
        os.makedirs(stock_path)
        print(stock_path + ' created')
        
    else: 
        print('Stocks folder exists.')


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
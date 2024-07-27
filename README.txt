Need to write this out more.


$ pyhton3 stocky.py

1. stocky.py is utilized to find the moving average of stocks between the last 200 days compared to the last 50 days.
   This is only one way to analyse known trends, and cannot predict the market accurately.


2. When running stocky.py a check will be made for requried folder structure to save outputs (graph_images, stocks, buy_signals, sell_signals).
   If these do not exist, the script will build them.

2. When the 50 MA goes above the 200 MA, a golden cross, a buy signal will hit meaning to buy. When it goes below, sell.
    use this comand to output the Master file to see the recent buys:

3. The following scripts are required to be in the same directory as stocky.py and are used for cleanup and function:
    -CSVstocky.py
    -organize.py
    -tickers.py

4. To view the graphs with the trends looking pretty, look for them in the graph_images folder. There you will see .png files for each ticker.


    if not os.path.exists(macd_path):
            print('MACD folder does not exist, creating folder')
            os.makedirs(image_path + '/macd')
            print(macd_path + ' created')


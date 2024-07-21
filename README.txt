Need to write this out more.

1. stocky,py is utilized to find the moving average of stocks between the last 200 days compared to the last 50 days.

2. When the 200 day crossed above the 50, a buy signal will hit meaning to buy. When it goes below, sell.
    use this comand to output the Master file to see the recent buys:
    cut -d, -f1,12 buy_signals/Master_buy_signals.csv | sort -t, -k1,1r | column -s, -t

To do:
-maybe move away from downloading csv?

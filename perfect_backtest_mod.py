import ccxt
import numpy as np
import pandas as pd
from datetime import datetime
import time
from matplotlib import pyplot as plt


def get_ohlcv(start, last, symbol, timeframe):

    start = round(datetime.strptime(start, '%Y-%m-%d %H:%M:%S').timestamp()*1000)
    last = round(datetime.strptime(last, '%Y-%m-%d %H:%M:%S').timestamp()*1000)

    with open("binance_key.txt") as f:
        lines = f.readlines()
        api_key = lines[0].strip()
        secret  = lines[1].strip()

    binance = ccxt.binance(config={
        'apiKey': api_key, 
        'secret': secret,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'future'
        }
    })

    dfs = []

    while True:
        btc = binance.fetch_ohlcv(
        symbol=symbol,
        timeframe=timeframe, 
        since=int(start),
        )

        df = pd.DataFrame(data=btc, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
        start = df.iloc[-1]['datetime']
        df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
        df.set_index('datetime', inplace=True)

        dfs.append(df)

        time.sleep(0.1)

        if pd.to_datetime(last, unit='ms') in df.index:
            break


    result = pd.concat(dfs).sort_index()
    result = result.loc[ : pd.to_datetime(last, unit='ms') ]
    result = pd.DataFrame(result)

    # print(result)

    return result
import ccxt
import pandas as pd
from datetime import datetime
import time

def get_ohlcv(start, last, symbol, timeframe):

    start = round(datetime.strptime(start, '%Y-%m-%d %H:%M:%S').timestamp()*1000)
    last = round(datetime.strptime(last, '%Y-%m-%d %H:%M:%S').timestamp()*1000)

    binance = ccxt.binance(config={
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
        limit=1500
        )

        df = pd.DataFrame(data=btc, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
        df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
        df.set_index('datetime', inplace=True)
        start = round(datetime.strptime(str(df.index[-1]), '%Y-%m-%d %H:%M:%S').timestamp()*1000)

        dfs.append(df)

        time.sleep(0.1)

        if pd.to_datetime(last, unit='ms') in df.index:
            break


    result = pd.concat(dfs).sort_index()
    result = result.loc[ : pd.to_datetime(last, unit='ms') ]
    result = pd.DataFrame(result)

    print(result)

    return result
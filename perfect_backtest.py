from perfect_backtest_mod import *

start = "2020-09-01 10:00:00"
last = "2021-09-01 10:00:00"

symbol = "BTC/USDT"

get_ohlcv(start, last, symbol, '30m')
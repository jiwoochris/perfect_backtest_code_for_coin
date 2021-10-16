from perfect_backtest_mod import *

start_list = [
    "2021-06-15 09:00:00", "2021-03-15 09:00:00", "2020-12-15 09:00:00", "2020-09-15 09:00:00",
    "2020-06-15 09:00:00", "2020-03-15 09:00:00","2019-12-15 09:00:00", "2019-09-15 09:00:00"
]
last_list = [
    "2021-09-23 09:00:00", "2021-06-23 09:00:00", "2021-03-23 09:00:00", "2020-12-23 09:00:00",
    "2020-09-23 09:00:00", "2020-06-23 09:00:00", "2020-03-23 09:00:00", "2019-12-23 09:00:00",
]

history_print = False
excel = True
compound = False

symbol = "BTC/USDT"

# leverage = [1, 2, 3, 5, 10, 15, 20]
leverage = [3]

timeframe = ["15m", "30m", "1h", "2h", "4h"]
# timeframe = ["2h"]

rr = [(2,2), (2,3), (3,2), (3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (4,6), (5,3), (5,4), (5,5), (5,6)]

for quarter in range(len(start_list)):
    start = start_list[quarter]
    last = last_list[quarter]
    print("-------------------------------------------------")

    for l in leverage:

        수수료 = 0.0008 * l # 수수료 설정

        for tf in timeframe:
            ohlcv = get_ohlcv(start, last, symbol, tf)

            # 지표 설정

            data_rr = []
            data_rate = []

            for r in rr:
                손익비 = {'익절' : r[0], '손절' : r[1]}

                if excel == False:
                    print("\n", tf, r, " x",l)

                win = 0
                lose = 0

                if compound == True:
                    rate = 1
                else:
                    rate = 0
                
                entry = False
                
                position = "nothing"

                for i in range(200, len(ohlcv)):

                    if entry == False:
                        if : # long position 매매 조건
                            long_entry = ohlcv.iloc[i]['close']
                            date = ohlcv.iloc[i].name
                            entry = True
                            position = "long"

                        elif : # short postion 매매 조건
                            short_entry = ohlcv.iloc[i]['close']
                            date = ohlcv.iloc[i].name
                            entry = True
                            position = "short"

                    elif entry == True:
                        if position == "long":
                            if : # long 손절 기준
                                long_exit = # exit 가격
                                lose += 1

                                if compound == True:
                                    rate *= ( 1 + ( (long_exit / long_entry) - 1 ) * l ) * (1 - 수수료)
                                else:
                                    rate += ( 1 + ( (long_exit / long_entry) - 1 ) * l ) * (1 - 수수료) - 1

                                entry = False
                                exit_date = ohlcv.iloc[i].name
                                if history_print == True:
                                    print("ㅅㅈ", long_exit / long_entry, date, position, exit_date)

                            elif : # long 익절 기준
                                long_exit = # exit 가격
                                win += 1

                                if compound == True:
                                    rate *= ( 1 + ( (long_exit / long_entry) - 1 ) * l ) * (1 - 수수료)
                                else:
                                    rate += ( 1 + ( (long_exit / long_entry) - 1 ) * l ) * (1 - 수수료) - 1

                                entry = False
                                exit_date = ohlcv.iloc[i].name
                                if history_print == True:
                                    print("ㅇㅈ", long_exit / long_entry, date, position, exit_date)

                        elif position == "short":
                            if : # short 손절 기준
                                short_exit = # exit 가격
                                lose += 1

                                if compound == True:
                                    rate *= ( 1 + ( (short_entry / short_exit) - 1 ) * l ) * (1 - 수수료)
                                else:
                                    rate += ( 1 + ( (short_entry / short_exit) - 1 ) * l ) * (1 - 수수료) - 1

                                entry = False
                                exit_date = ohlcv.iloc[i].name
                                if history_print == True:
                                    print("ㅅㅈ", short_entry / short_exit, date, position, exit_date)

                            elif : # short 익절 기준
                                short_exit = # exit 가격
                                win += 1

                                if compound == True:
                                    rate *= ( 1 + ( (short_entry / short_exit) - 1 ) * l ) * (1 - 수수료)
                                else:
                                    rate += ( 1 + ( (short_entry / short_exit) - 1 ) * l ) * (1 - 수수료) - 1

                                entry = False
                                exit_date = ohlcv.iloc[i].name
                                if history_print == True:
                                    print("ㅇㅈ", short_entry / short_exit, date, position, exit_date)

                if excel == False:
                    print("승패 : ", win, lose)
                    if win + lose != 0:
                        print("승률 : ", win / (win+lose) * 100)
                    else:
                        print("승률 : ", 0)
                    print("수익률 : ", rate * 100)

                else:
                    if compound == True:
                        print(rate * 100 - 100)
                    else:
                        print(rate * 100)
                    

                data_rr += [str(r)]
                data_rate += [rate]

            # data_dict = {'손익비' : data_rr, '수익률' : data_rate}
            # plt.plot('손익비', '수익률', data=data_dict, label=tf)
            # plt.legend()
            # plt.show()
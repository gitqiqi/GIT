import requests
import csv
import pandas as pd


def Text (headers,urls,num):
    key = {
        "gameNo": 85,
        "provinceId": 0,
        "pageSize": 30,
        "isVerify": 1,
        "pageNo": num
        # "termLimits": num,
    }
    response = requests.get(url=urls, headers=headers, timeout=1, params=key)
    info = response.json()
    value = info['value']
    lst = pd.DataFrame(value['list'])
    return lst


def downloader_data(df1,num,headers,urls):
    for i in range(2, num):
        lst = Text(headers, urls, i)
        df1 = pd.concat([df1, lst.loc[1:,:]]).fillna(0)
    # print('df1', df1)
    df1.to_csv(r'data/data.csv')
# my_sql.execute_sql(df1)


#lotteryDrawNum 期号
#lotteryDrawResult 中奖号码
#lotteryDrawTime：开奖日期
#lotteryEquipmentCount:本期使用第3套摇奖球
# lotterySaleBeginTime：开始时间
#lotterySaleEndtime:结束时间
#lotteryUnsortDrawresult：本期出球顺序：
# lotteryPaidBeginTime:交易开始时间
# lotteryPaidEndTime：交易结束时间
#poolBalanceAfterdraw：滚入下期奖池
#totalSaleAmount：总售卖金额
#lotteryEquipmentCount ：使用第几套摇奖球
# drawPdfUrl：pdf链接



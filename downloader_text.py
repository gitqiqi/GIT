import requests
import csv
import time

def Text (headers,urls,num):
    key={
        "gameNo": 85,
        "provinceId": 0,
        "isVerify": 1,
        "termLimits": num
    }
    response=requests.get(url=urls,headers=headers,timeout=1, params=key)
    info = response.json()
    value=info['value']
    lst=value['list']
    return lst

if __name__=="__main__":
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}
    urls = "https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry"
    num = 1000

    file = open(r"data.csv", "w", newline='', encoding='utf-8')  # 建立一个文件
    writer = csv.writer(file)  # 以表格的形式来写这个文件

    lst = Text(headers, urls, num)
    writer.writerow(lst[1].keys())
    for i in range(num):
        writer.writerow(lst[i].values())
        if (i%10 == 0):
            time.sleep((0.1))
    file.close()


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



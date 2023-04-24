import pandas as pd

name1 = ['first1_x', 'first2_x', 'first3_x', 'first4_x', 'first5_x', 'last1_x', 'last2_x']
name2 = ['first1_num', 'first2_num', 'first3_num', 'first4_num', 'first5_num', 'last1_num', 'last2_num']
name3 = ['first1_y', 'first2_y', 'first3_y', 'first4_y', 'first5_y', 'last1_y', 'last2_y']

def lottery_draw_result(name1,name3):
    # 数据预处理
    data = pd.read_csv(r"data.csv")

    # {lotteryDrawNum:期号,lotteryDrawResult:中奖号码,lotteryDrawTime：开奖日期,
    # lotteryUnsortDrawresult：本期出球顺序：poolBalanceAfterdraw：滚入下期奖池金额，totalSaleAmount：总售卖金额
    # lotteryEquipmentCount ：使用第几套摇奖球，prizeLevelList：list，drawPdfUrl：pdf链接}

    df1 = data.loc[:,
          ['lotteryDrawNum', 'lotteryDrawResult', 'lotteryDrawTime', 'lotteryUnsortDrawresult', 'poolBalanceAfterdraw',
           'drawFlowFund', 'totalSaleAmount', 'lotteryEquipmentCount', 'prizeLevelList', 'drawPdfUrl']]
    df1['YlotteryDrawResult'] = df1.shift(1, axis=0).lotteryDrawResult
    df1=df1.loc[1:,:]
    for _name1,_name3 in zip(name1,name3):
        i = name1.index(_name1)
        df1[_name1] = df1.lotteryDrawResult.map(lambda x: x.split(' ')[i])
        df1[_name3] = df1.YlotteryDrawResult.map(lambda x: x.split(' ')[i])
    return df1


df1 = lottery_draw_result(name1,name3)


def lottery_first_draw_result(df1, _name1, _name2, num):
    df_init = pd.DataFrame()
    for i in range(1, num + 1):
        List1 = df1[df1[_name1].astype(int) == i]
        List2 = List1.shift(-1, axis=0).lotteryDrawNum.rename(_name2)  # 最后一列重命名为   保存上一次该号出现的期数
        List = pd.concat([List1, List2], axis=1).fillna(0)
        List.iloc[:,-1]=List.lotteryDrawNum-List.iloc[:,-1]
        df_init = pd.concat([df_init, List])
    return df_init


Lists1=df1

for _name1, _name2 in zip(name1, name2):
    Lists2 = lottery_first_draw_result(df1, _name1, _name2, 35)[['lotteryDrawNum', _name2]]
    Lists1 = pd.merge(Lists1, Lists2, left_on='lotteryDrawNum', right_on='lotteryDrawNum', how='left')
Lists1.to_csv('list.csv', index=False, index_label='index')

import pandas as pd
name1 = ['first1', 'first2', 'first3', 'first4', 'first5', 'last1', 'last2']
name2 = ['first1_', 'first2_', 'first3_', 'first4_', 'first5_', 'last1_', 'last2_']
def lottery_draw_result():
    # 数据预处理
    data = pd.read_csv("data.csv")
    # {lotteryDrawNum:期号,lotteryDrawResult:中奖号码,lotteryDrawTime：开奖日期,
    # lotteryUnsortDrawresult：本期出球顺序：poolBalanceAfterdraw：滚入下期奖池金额，totalSaleAmount：总售卖金额
    # lotteryEquipmentCount ：使用第几套摇奖球，prizeLevelList：list，drawPdfUrl：pdf链接}

    df1 = data[['lotteryDrawNum', 'lotteryDrawResult', 'lotteryDrawTime', 'lotteryUnsortDrawresult', 'poolBalanceAfterdraw', 'drawFlowFund', 'totalSaleAmount', 'lotteryEquipmentCount', 'prizeLevelList', 'drawPdfUrl']]
    df1 = data.loc[:, ['lotteryDrawNum', 'lotteryDrawResult', 'lotteryDrawTime', 'lotteryUnsortDrawresult', 'poolBalanceAfterdraw', 'drawFlowFund', 'totalSaleAmount', 'lotteryEquipmentCount', 'prizeLevelList', 'drawPdfUrl']]

    for name in name1:
        i = name1.index(name)
        df1[name] = df1.lotteryDrawResult.map(lambda x:x.split(' ')[i])
    df1.to_csv('df.csv')


# lottery_draw_result()

df2=pd.read_csv('df.csv')
def lottery_first_draw_result(df,name1_, name2_, num):
    df_init = pd.DataFrame()
    for i in range(1,num+1):
        List1 = df2[df2[name1_] == i]
        List2 = List1.shift(-1, axis=0).lotteryDrawNum.rename(name2_)#最后一列重命名为   保存上一次该号出现的期数
        List = pd.concat([List1,List2],axis=1)
        df_init=pd.concat([df_init, List])
    return df_init

Lists1 = df2
for name1_, name2_ in zip (name1, name2):
    Lists2 = lottery_first_draw_result(Lists1,name1_, name2_, 35)[['lotteryDrawNum',name2_]]
    Lists1 = pd.merge(Lists1,Lists2,left_on='lotteryDrawNum',right_on='lotteryDrawNum',how='left')
Lists1.to_csv('list.csv', index=False,index_label='index')


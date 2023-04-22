import pandas as pd

#数据预处理
data=pd.read_csv("data.csv")
data.lotteryDrawNum
#{lotteryDrawNum:期号,lotteryDrawResult:中奖号码,lotteryDrawTime：开奖日期,
#lotteryUnsortDrawresult：本期出球顺序：poolBalanceAfterdraw：滚入下期奖池金额，totalSaleAmount：总售卖金额
#lotteryEquipmentCount ：使用第几套摇奖球，prizeLevelList：list，drawPdfUrl：pdf链接}

df1=[['lotteryDrawNum','lotteryDrawResult','lotteryDrawTime','lotteryUnsortDrawresult','poolBalanceAfterdraw','drawFlowFund','totalSaleAmount','lotteryEquipmentCount','prizeLevelList','drawPdfUrl']]
df1=data.loc[:,['lotteryDrawNum','lotteryDrawResult','lotteryDrawTime','lotteryUnsortDrawresult','poolBalanceAfterdraw','drawFlowFund','totalSaleAmount','lotteryEquipmentCount','prizeLevelList','drawPdfUrl']]
df1['first1']=df1.lotteryDrawResult.map(lambda x:x.split(' ')[0])
df1['first2']=df1.lotteryDrawResult.map(lambda x:x.split(' ')[1])
df1['first3']=df1.lotteryDrawResult.map(lambda x:x.split(' ')[2])
df1['first4']=df1.lotteryDrawResult.map(lambda x:x.split(' ')[3])
df1['first5']=df1.lotteryDrawResult.map(lambda x:x.split(' ')[4])

df1['last1']=df1.lotteryDrawResult.map(lambda x:x.split(' ')[5])
df1['last2']=df1.lotteryDrawResult.map(lambda x:x.split(' ')[6])

df1.to_csv('df.csv')




import pandas as pd
df = pd.read_csv('list.csv')
df1 = df[['lotteryDrawNum', 'first1', 'first2', 'first3', 'first4', 'first5', 'last1', 'last2','first1_num', 'first2_num', 'first3_num', 'first4_num', 'first5_num', 'last1_num', 'last2_num']]


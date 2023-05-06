import downloader_text
import data_preprocess

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}
urls = "https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry"
num = 81
name1 = ['first1_x', 'first2_x', 'first3_x', 'first4_x', 'first5_x', 'last1_x', 'last2_x']
name2 = ['first1_num', 'first2_num', 'first3_num', 'first4_num', 'first5_num', 'last1_num', 'last2_num']
name3 = ['first1_y', 'first2_y', 'first3_y', 'first4_y', 'first5_y', 'last1_y', 'last2_y']

df1 = downloader_text.Text(headers, urls, 1)
downloader_text.downloader_data(df1, num, headers, urls)

df1 = data_preprocess.lottery_draw_result(name1, name3)
df1 = data_preprocess.lotter_data_preprocess(df1)







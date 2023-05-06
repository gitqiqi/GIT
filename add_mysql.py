from sqlalchemy import create_engine
import pandas as pd
def execute_sql(df):
    # create_engine('mysql+pymysql://用户名:密码@主机/库名?charset=utf8')
    engine = create_engine('mysql+pymysql://root:lqq675637@localhost/my_data?charset=utf8')
    pd.io.sql.to_sql(df,'lottery_data', con = engine ,if_exists = 'append',index="False")
    # print('result', result)

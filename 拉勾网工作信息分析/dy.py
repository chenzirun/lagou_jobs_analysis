import pandas as pd
import pymysql

def con_sql(str):
    conn = pymysql.connect(host='localhost', user='root', password='czrlh1234', port=3306, db='lagou_job', charset='utf8mb4')
    cursor = conn.cursor()
    sql = "select * from {}".format(str)
    df = pd.read_sql(sql, conn)
    return df
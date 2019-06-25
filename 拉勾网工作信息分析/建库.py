import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', password='czrlh1234', port=3306)
cursor = db.cursor()
cursor.execute("CREATE DATABASE lagou_job DEFAULT CHARACTER SET utf8mb4")
db.close()
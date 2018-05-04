# encoding: utf-8
# Author: LW

import pymysql

# 打开数据库连接
db = pymysql.connect("10.69.80.70", "indigo", "indigo", "indigoDB")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("select BUSSNO from TB_PROCESSQUEUE where CREATETIME > DATE_SUB(CURDATE(),INTERVAL 0 DAY)")

# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
data = cursor.fetchall()

print("Database version : " , data)

# 关闭数据库连接
db.close()
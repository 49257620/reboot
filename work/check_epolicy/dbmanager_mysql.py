# encoding: utf-8
# Author: LW


import pymysql

# 打开数据库连接






def find_all(sql):
    db = pymysql.connect("10.69.80.70", "indigo", "indigo", "indigoDB")
    cursor = db.cursor()

    cursor.execute(sql)

    data = cursor.fetchall()

    db.close()
    return data

def find_one(sql):
    db = pymysql.connect("10.69.80.70", "indigo", "indigo", "indigoDB")
    cursor = db.cursor()

    cursor.execute(sql)

    data = cursor.fetchone()

    db.close()
    return data

if __name__ == '__main__':
    pass
# encoding: utf-8
# Author: LW

import cx_Oracle as orcl


DB_CONF = 'hicuat/hicuat@sinodb'

def find_all(sql):
    conn = orcl.connect(DB_CONF)
    curs = conn.cursor()
    curs.execute(sql)
    rows = curs.fetchall()
    curs.close()
    conn.close()
    return rows

def find_one(sql):
    conn = orcl.connect(DB_CONF)
    curs = conn.cursor()
    curs.execute(sql)
    row = curs.fetchone()
    curs.close()
    conn.close()
    return row

if __name__ == '__main__':
    pass
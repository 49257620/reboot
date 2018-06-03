#encoding: utf-8

'''
create table accesslog(
    id int primary key auto_increment,
    logtime datetime not null,
    ip varchar(256) not null default '',
    url varchar(1024) not null default '',
    status int not null default 0
) engine=innodb default charset utf8;
'''

from datetime import datetime

import MySQLdb

params = {
    'host' : '47.104.188.243',
    'port' : 3306,
    'db' : 'cmdb_lw',
    'user' : 'root',
    'passwd' : '1qaz@WSX',
    'charset' : 'utf8'
}


SQL = 'INSERT INTO accesslog(logtime, ip, url, status) VALUES(%s, %s, %s, %s);'

if __name__ == '__main__':
    path = 'C:\\文档\\刘伟\\学习文档\\Python\\access.txt'
    with open(path, 'rt', encoding='utf-8') as fhandler:
        conn = MySQLdb.connect(**params)
        cursor = conn.cursor()
        cnt = 0
        for line in fhandler:
            nodes = line.split()
            args = (
                datetime.strptime(nodes[3], '[%d/%b/%Y:%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S'),
                nodes[0],
                nodes[6],
                nodes[8],
            )
            cnt += cursor.execute(SQL, args)
            if cnt % 5000 == 0:
                conn.commit()

        conn.commit()
        cursor.close()
        conn.close()
        print(cnt)
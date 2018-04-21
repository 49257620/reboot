# encoding: utf-8
# Author: LW

"""
D:\app\oracle\product\11.2.0\client_1\bin;C:\Program Files (x86)\Python36-32\Scripts\;C:\Program Files (x86)\Python36-32\;%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;C:\ProgramData\Oracle\Java\javapath;D:\oracle\product\instantclient_11_2;C:\Program Files (x86)\Intel\iCLS Client\;C:\Program Files\Intel\iCLS Client\;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\TortoiseSVN\bin;D:\nodejs\;D:\Git\cmd
D:\app\oracle\product\11.2.0\client_1\bin;C:\Program Files (x86)\Python36-32\Scripts\;C:\Program Files (x86)\Python36-32\;%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;C:\ProgramData\Oracle\Java\javapath;D:\app\oracle\product\11.2.0\client_1\BIN;C:\Program Files (x86)\Intel\iCLS Client\;C:\Program Files\Intel\iCLS Client\;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\TortoiseSVN\bin;D:\nodejs\;D:\Git\cmd

"""

import cx_Oracle as orcl

conn = orcl.connect('hicis/hicis@sinodb')
curs = conn.cursor()
sql = 'SELECT * FROM prpcmain where rownum<10'
rr = curs.execute(sql)

rows = curs.fetchall()
print(rows)
curs.close()
conn.close()

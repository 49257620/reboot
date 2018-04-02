# encoding: utf-8
# Author: LW
"""

[root@localhost ~]# ssh-keygen -t rsa -C "49257620@qq.com"

[root@localhost ~]# cd /root/.ssh/
[root@localhost .ssh]# ls
id_rsa  id_rsa.pub
[root@localhost .ssh]# cat id_rsa.pub

[root@localhost .ssh]# ssh -T git@github.com


[root@localhost projects]# git config --global user.name "49257620"
[root@localhost projects]# git config --global user.email "49257620@qq.com"


第一次使用
git clone git@github.com:51reboot/actual-18-homework.git
cd actual-17-homework
mkdir panda
echo  print 123 >> woniu/zuoye.py
git add .
git commit -m "first commit:joy:"
git push

后面添加代码，只需要下面三行即可
git add .
git commit -m "first commit"
git push


"""
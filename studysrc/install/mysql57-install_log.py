# encoding: utf-8
# Author: LW
"""
sudo yum localinstall mysql57-community-release-el7-11.noarch.rpm

yum repolist enabled | grep "mysql.*-community.*"

sudo yum install mysql-community-server

修改my.cnf
增加：bind-address=0.0.0.0

关闭防火请
systemctl stop firewalld.service 关闭防火墙
systemctl disable firewalld.service 关闭开机启动

sudo service mysqld start

sudo service mysqld status

sudo grep 'temporary password' /var/log/mysqld.log


ALTER USER 'root'@'localhost' IDENTIFIED BY '1qaz@WSX';

show databases;

use mysql;

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '1qaz@WSX' WITH GRANT OPTION;

FLUSH PRIVILEGES ;


sudo service mysqld restart


"""
# encoding: utf-8
# Author: LW
"""
第一步 - 添加Nginx存储库
sudo yum install epel-release

第二步 - 安装Nginx
sudo yum install nginx

第三步 - 启动Nginx
Nginx不会自行启动。要运行Nginx，请输入：
启动
sudo systemctl start nginx
sudo service nginx start

停止
sudo systemctl stop nginx
sudo service nginx stop

重新加载
sudo nginx -s reload


如果您正在运行防火墙，请运行以下命令以允许HTTP和HTTPS通信：
sudo firewall-cmd --permanent --zone=public --add-service=http
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --reload

如果想在系统启动时启用Nginx。请输入以下命令：
sudo systemctl enable nginx

配置文件
cd /etc/nginx/conf.d/


"""

"""
添加用户到sudo list，有两种做法可以做到：
1. 修改sudoers文件

a. 切换到root用户下
b. 添加sudo文件的写权限,命令是:
    chmod u+w /etc/sudoers
c. 编辑sudoers文件
    vi /etc/sudoers
    找到这行 root ALL=(ALL) ALL,在他下面添加xxx ALL=(ALL) ALL (这里的xxx是你的用户名)
d. ps:这里说下你可以sudoers添加下面四行中任意一条
    youuser            ALL=(ALL)                ALL
    %youuser           ALL=(ALL)                ALL
    youuser            ALL=(ALL)                NOPASSWD: ALL
    %youuser           ALL=(ALL)                NOPASSWD: ALL

第一行:允许用户youuser执行sudo命令(需要输入密码).
第二行:允许用户组youuser里面的用户执行sudo命令(需要输入密码).
第三行:允许用户youuser执行sudo命令,并且在执行的时候不输入密码.
第四行:允许用户组youuser里面的用户执行sudo命令,并且在执行的时候不输入密码.

Attention： 在有的环境中，配置为youuser            ALL=(ALL)                ALL
也可以达到sudo无需输入密码的效果，但不能保证所有环境都有效，肯定有效的做法是:
youuser            ALL=(ALL)                NOPASSWD: ALL


2. 增加用户组文件

在etc/sudoers.d目录下增加以用户组为名的文件，例如:TestGroup，在其中配置如下内容：
%TestGroup ALL=(ALL) NOPASSWD: ALL

则属于TestGroup组的用户都被加入到了sudo list


"""
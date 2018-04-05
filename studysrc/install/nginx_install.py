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

停止
sudo systemctl stop nginx


如果您正在运行防火墙，请运行以下命令以允许HTTP和HTTPS通信：
sudo firewall-cmd --permanent --zone=public --add-service=http
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --reload

如果想在系统启动时启用Nginx。请输入以下命令：
sudo systemctl enable nginx


"""
# encoding: utf-8
# Author: LW

"""
配置JDK
在终端，通过：

yum list java*
1
查看阿里云有的java包

可以看到有很多，并且有java1.8.0，所以我们愉快的安装就可以了

通过如下命令安装jdk：

yum install java-1.8.0-openjdk*
1
安装完成之后，我们可以通过

java -version
1
查看java安装是否成功


配置mysql
我当时也不知道为什么脑抽就选择了安装mysql5.7，因为最新版本的很多改动比较大，除了错误网上很多都搜索不到，是通过查看mysql的参考文档解决的。

其实这也挺好的，你走在别人前头的感觉还是挺不错的。

首先，这里并没有通过yum方式安装，因为aliyun的mysql版本比较低，所以可以直接到mysql网站下载：

这里是最新版本下载方式，在服务器终端输入如下命令下载：

wget http://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.17-1.el7.x86_64.rpm-bundle.tar
1
然后将其添加到yum库中进行安装即可。安装方式同上。

以下介绍自己遇到的坑点：

首先，我安装过程中，好像没让我输入过密码，但是安装完成后，我通过mysql -u root或者mysql都无法登陆，所以只能通过强制更改密码方式：
参考这篇文章修改密码。
http://www.centoscn.com/mysql/2014/0603/3081.html
第一个槽点：修改密码指令mysql数据库中没有了password字段，改为了authentication_string字段，所以修改密码需要将命令中的password替换为authentication_string

修改完成后，确实可以登录进入mysql了，但是坑爹的是什么指令都执行不了，提示请用alter user方式更改密码后再执行命令。。。更改密码，发现不能改，提示密码不符合要求，好嘛，查了一下，5.7版本要求大小写字母，数字，特殊符号一个都不能少，改了密码之后终于可以正常使用了！

具体更改密码指令参见参考文档：
http://dev.mysql.com/doc/refman/5.7/en/preface.html

这里我们就可以把之前穿好的sql文件导入到服务器的mysql中了，首先在msyql中建立相同名字的数据库。例如：users

然后使用该数据库执行

source users.sql
1
就可以成功导入了。




配置tomcat
由于tomcat在aliyun的yum库不全，所以我们去官网下载文件

同样使用wget下载，下载后将tar.gz解压到你想要的安装目录，一般是/usr/local/

这样其实就算是安装好了

启动命令（针对刚才的安装路径）：

./usr/local/apache-tomcat-9.0.0.M15/bin/startup.sh
1
之后就可以通过外网访问你的tomcat了

访问方式，ip改为你的主网ip：

60.205.XXX.XXX:8080
1
如果能够成功访问并显示如下页面，就说明ok了

"""
# encoding: utf-8
# Author: LW
"""
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz

mkdir /usr/local/python3

建立一个空文件夹

然后解压压缩包，进入该目录，安装Python3

tar -xvJf  Python-3.6.4.tar.xz
cd Python-3.6.4
./configure --prefix=/usr/local/python3
make && make install

最后创建软链接
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

"""
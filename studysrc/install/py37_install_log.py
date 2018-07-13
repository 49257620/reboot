# encoding: utf-8
# Author: LW
"""
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel 
gdbm-devel db4-devel libpcap-devel xz-devel

3.7版本需要一个新的包libffi-devel，安装此包之后再次进行编译安装即可。
yum install libffi-devel -y

wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0rc1.tar.xz 

mkdir /usr/local/python3

建立一个空文件夹

然后解压压缩包，进入该目录，安装Python3

tar -xvJf  Python-3.7.0rc1.tar.xz
cd Python-3.7.0rc1
./configure --prefix=/usr/local/python3
make && make install

最后创建软链接
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

------------------------------------------------------------------------------
centos 7 安装pip3
3.7版本需要一个新的包libffi-devel，安装此包之后再次进行编译安装即可。

yum install libffi-devel -y

wget https://files.pythonhosted.org/packages/1a/04/d6f1159feaccdfc508517dba1929eb93a2854de729fa68da9d5c6b48fa00/setuptools-39.2.0.zip

unzip setuptools-39.2.0.zip



wget https://files.pythonhosted.org/packages/ae/e8/2340d46ecadb1692a1e455f13f75e596d4eab3d11a57446f08259dee8f02/pip-10.0.1.tar.gz

tar -zxvf pip-10.0.1.tar.gz

cd pip-10.0.1



"""
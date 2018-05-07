# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

"""
pip3 install django
python3 –c “import django; print(django.get_version());”   # 测试版本

环境到导出到文件
pip freeze -> requirements.txt
通过文件进行安装
pip install -r requirements.txt

找到django-admin 位置
find / -name django-admin
建立环境变量软连接
sudo ln -s /usr/local/python3/bin/django-admin /usr/local/bin

"""

"""
创建项目
django-admin startproject cmdb
创建app
python3 manage.py startapp user
启动app
python3 manage,py runserver 0.0.0.0:8888
python3 manage,py runserver
"""

"""
创建项目
django-admin startproject cmdb
创建app
python3 manage.py startapp user

创建2个文件
/root/projects/django_study/cmdb/user  
mkdir -p templates/user 
mkdir -p static/user
在user目录下创建 urls.py文件
touch urls.py

设置项目的/settings.py
ALLOWED_HOSTS = ['*']
INSTALLED_APPS =>  user[app的名字].apps.UserConfig[apps.py里面class xxxConfig]

编写app/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("我的第一个页面")

编辑项目的urls.py（参考下方代码）
urlpatterns 加 
path('user/', include('user.urls'))
增加include 的引用

定义app/urls.py（user）

from user import views

urlpatterns = [
    path('index/', views.index, name='index')
]

启动app
python3 manage.py runserver 0.0.0.0:8888
python3 manage.py runserver  默认8000端口

启动app 并输入到日志 nohup.out 并开始追踪日志
nohup python3 manage.py runserver 0.0.0.0:8888 &tail -f nohup.out
"""
"""
# 在 root 用户下运行这条命令创建一个新用户，yangxg 是用户名
# 因为我叫杨学光，所以我取的用户名是 yangxg
# 选择一个你喜欢的用户名，不一定非得和我的相同
root@localhost:~# useradd -m -s /bin/bash liuwei

# 把新创建的用户加入超级权限组
root@localhost:~# usermod -a -G root liuwei

# 为新用户设置密码
# 注意在输密码的时候不会有字符显示，不要以为键盘坏了，正常输入即可
root@localhost:~# passwd liuwei

# 切换到创建的新用户
root@localhost:~# su - liuwei

# 切换成功，@符号前面已经是新用户名而不是 root 了
yangxg@localhost:~$
"""

"""
进入虚拟环境 venv
创建 venv
python3 -m venv venv

进入虚拟环境
source venv/bin/activate

退出虚拟环境
deactivate

"""

"""
导出requirement 文件
首先进入虚拟环境，然后进入项目目录

pip freeze > requirements.txt

这时项目根目录下会生成了一个 requirements.txt 的文本文件，其内容记录了项目的全部依赖。

"""
"""
进入新的虚拟环境，复制项目后，进入到项目目录，安装项目的全部依赖
pip install -r requirements.txt

启动服务

python manage.py runserver 0.0.0.0:8888
"""

"""
创建 Admin 后台管理员账户

python manage.py createsuperuser

Username (leave blank to use 'zmrenwu@163.com'):  admin
Email address:  admin@example.com
Warning: Password input may be echoed.
Password:  ******
Warning: Password input may be echoed.
Password (again):  ******
Superuser created successfully.

"""

"""
nginx 配置
（你就直接写 cmdb.conf 扔 conf.d 下面就好。）

server {
    charset utf-8;
    listen 80;
    server_name 47.104.188.243;
    access_log /home/liuwei/site/cmdb/cmdb/logs/access.log;
    error_log /home/liuwei/site/cmdb/cmdb/logs/error.log;

	location /static {
        alias /home/liuwei/site/cmdb/cmdb/static; 
    }

    location / {
        proxy_set_header Host $host;
        proxy_pass http://127.0.0.1:8888;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
"""


"""
使用 Gunicorn
在虚拟环境下，安装 Gunicorn：
pip install gunicorn

用 Gunicorn 启动服务器进程：

gunicorn --bind 0.0.0.0:8888 cmdb.wsgi:application

gunicorn -w 2 --bind 0.0.0.0:8888 cmdb.wsgi:application



"""

"""
Commonly Used Arguments
-c CONFIG, --config=CONFIG - Specify a config file in the form $(PATH), file:$(PATH), or python:$(MODULE_NAME).
-b BIND, --bind=BIND - Specify a server socket to bind. Server sockets can be any of $(HOST), $(HOST):$(PORT), or unix:$(PATH). An IP is a valid $(HOST).
-w WORKERS, --workers=WORKERS - The number of worker processes. This number should generally be between 2-4 workers per core in the server. Check the FAQ for ideas on tuning this parameter.
-k WORKERCLASS, --worker-class=WORKERCLASS - The type of worker process to run. You’ll definitely want to read the production page for the implications of this parameter. You can set this to $(NAME) where $(NAME) is one of sync, eventlet, gevent, tornado, gthread, gaiohttp (deprecated). sync is the default. See the worker_class documentation for more information.
-n APP_NAME, --name=APP_NAME - If setproctitle is installed you can adjust the name of Gunicorn process as they appear in the process system table (which affects tools like ps and top).
"""
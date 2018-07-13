"""
输入"uname -a ",可显示电脑以及操作系统的相关信息。
输入"cat /proc/version",说明正在运行的内核版本。
输入"cat /etc/issue", 显示的是发行版本信息
lsb_release -a (适用于所有的linux，包括Redhat、SuSE、Debian等发行版，但是在debian下要安装lsb)
"""
"""
//更新apt-get
apt-get update

//卸载
apt-get remove vim

//重新安装procps -- ps
apt-get --reinstall install procps

//ifconfig 
apt install net-tools       
//ping
apt install iputils-ping 
//vim
apt-get install vim

//curl
apt-get install curl

//查看iptables规则
iptables -t nat -xvL
"""

"""
使用下面的shell命令安装Docker
curl -sSL https://get.docker.com/ | sh

yum install deltarpm
yum install docker-ce

docker -v

service docker restart

使用Docker创建一个nginx的容器:
docker run -d --name=web -p 80:80 nginx:latest

docker ps

docker images

docker exec -i -t web bash

docker inspect web

docker container ls

docker pull django
docker pull redis

"""

"""
docker run -d --name=redis -p 6379 redis
docker run -it --name=app -p 8080:8000 -v /code:/usr/src/app --link=redis:db django bash

$ django-admin startproject django_app
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8000 &

django-admin startapp ping
apt-get update
apt-get install vim-tiny

pip install redis
pip freeze > requirements.txt
"""
from django.shortcuts import render
from django.http import HttpResponse
import redis

rds = redis.StrictRedis('db', 6379)

def ping(request):
    rds.incr('count', 1)
    cnt = rds.get('count')
    cnt = b'0' if cnt is None else cnt
    return HttpResponse(cnt.decode())


''' urls.py
from views import ping

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ping)
]
'''

"""
FROM django:latest

COPY ./django_app /usr/src/app

COPY supervisord.conf /etc/supervisord.conf

COPY gunicorn_conf.py /etc/gunicorn_conf.py

RUN apt-get update && \
    apt-get install -y supervisor && \
    rm -rf /var/lib/apt/lists/*

RUN pip install meinheld && \
    pip install gunicorn && \
    cd /usr/src/app && \
    pip install -r requirements.txt && \
    python manage.py makemigrations && \
    python manage.py migrate

WORKDIR /usr/src/app

CMD supervisord -c /etc/supervisord.conf
"""

"""
docker build -t test/app .
"""
docker run -d --name=app -p 8080:8000  --link=redis:db test/app
docker run -d --name=app -p 8080:8000  --link=sentinel_1:sentinel test/app

docker run -d --name=app1 -p 8081:8000  --link=sentinel_1:sentinel test/app
docker run -d --name=app2 -p 8082:8000  --link=sentinel_1:sentinel test/app
docker run -d --name=app3 -p 8083:8000  --link=sentinel_1:sentinel test/app


$ docker run -d --name=redis_slave_1 -p 6380:6379 --link=redis:master redis redis-server --slaveof master 6379
$ docker run -d --name=redis_slave_2 -p 6381:6379 --link=redis:master redis redis-server --slaveof master 6379

"""
redis
Dockerfile

"""
FROM redis:latest

COPY run-sentinel.sh /run-sentinel.sh

COPY sentinel.conf /etc/sentinel.conf

RUN chmod +x /run-sentinel.sh

ENTRYPOINT ["/run-sentinel.sh"]


"""
sentinel.conf
"""
port 26379

dir /tmp

sentinel monitor master redis-master 6379 2

sentinel down-after-milliseconds master 30000

sentinel parallel-syncs master 1

sentinel failover-timeout master 180000

"""
run-sentinel.sh
"""

#!/bin/bash

exec redis-server /etc/sentinel.conf --sentinel


docker build -t test/redis_sentinel .



$ docker run -d --name=sentinel_1 --link=redis:redis-master test/redis_sentinel 
$ docker run -d --name=sentinel_2 --link=redis:redis-master test/redis_sentinel 
$ docker run -d --name=sentinel_3 --link=redis:redis-master test/redis_sentinel 


简单验证一下当redis主节点挂掉后sentinel怎么处理：
docker logs -f --tail=100 sentinel_1

docker exec -it sentinel_1 redis-cli -p 26379 info Sentinel



"""
docker pull haproxy
"""
"""
Dockerfile
"""
FROM haproxy:latest

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

"""
haproxy.cfg
"""
global
    log 127.0.0.1 local0
    maxconn 4096
    daemon
    nbproc 4

defaults
    log 127.0.0.1 local3
    mode http
    option dontlognull
    option redispatch
    retries 2
    maxconn 2000
    balance roundrobin
    timeout connect 5000ms
    timeout client 5000ms
    timeout server 5000ms

frontend main
    bind *:6301
    default_backend webserver

backend webserver
    server app1 app1:8000 check inter 2000 rise 2 fall 5
    server app2 app2:8000 check inter 2000 rise 2 fall 5
    server app3 app3:8000 check inter 2000 rise 2 fall 5

"""
build
"""
docker build -t test/haproxy .

docker run -d --name=lb -p 80:6301 --link app1:app1 --link app2:app2 --link app3:app3  test/haproxy




curl http://127.0.0.1:80

"""

Usage:  docker COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/root/.docker")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/root/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/root/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/root/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  config      Manage Docker configs
  container   Manage containers
  image       Manage images
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  secret      Manage Docker secrets
  service     Manage services
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.
"""


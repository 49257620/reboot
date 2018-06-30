
"""
RHEL或CentOS用户,需要 配置 EPEL
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

sudo yum install ansible


通过 Pip 安装最新发布版本
sudo pip install ansible
sudo pip3 install ansible


ansible -i ./hosts --connection=local local -a "/bin/echo hello"

ansible -i ./hosts --connection=local local -m ping

ansible -i /etc/ansible/hosts local -m ping -k

ansible -i /etc/ansible/hosts remote -m ping -k


"""

"""
Using a SSH password instead of a key is not possible because Host Key checking is enabled and sshpass does not support this.  Please add this host's fingerprint to your known_hosts file to manage this host.
默认host_key_checking部分是注释的，通过找开该行的注释，同样也可以实现跳过 ssh 首次连接提示验证部分。由于配置文件中直接有该选项
host_key_checking = False  

"""

"""

ssh-keygen

方法一：通过copy 和 file模块来进行。
ansible local -m copy -a "src=/root/.ssh/id_rsa.pub dest=/tmp/authorized_keys" -k 
ansible local -m file -a "path=/root/.ssh state=directory" -k 
ansible local -m shell -a "cat /tmp/authorized_keys >> /root/.ssh/authorized_keys" -k 

方法二：通过authorized_key模块来进行添加
ansible local -m authorized_key -a "user=root key='{{ lookup('file','/root/.ssh/id_rsa.pub') }}'" -k
#lookup('file','/root/.ssh/id_rsa.pub') 是读取/root/.ssh/id_rsa.pub的内容

"""

"""
对于多个主机，密码存在差异，我要一个个执行输入吗？岂不是累死，不累死也烦死了。那该如何是好呢？


在进行以下步骤前，要先把192.168.2.92中存在的PUBkey清空

[root@ldap ~]# ansible para -i /tmp/ansible_inventory.txt -m authorized_key -a "user=root key='{{ lookup('file','/root/.ssh/id_rsa.pub') }}' state=absent"

#清空之后，在执行命令时，就需要加入-k参数，然后输入密码，否则报错

修改ansible配置文件/etc/ansible/ansible.cfg

echo "host_key_checking = False"  >> /etc/ansible/ansible.cfg

#关闭host_key_checking


#新增一台主机192.168.2.94

[root@ldap ~]# cat /tmp/ansible_inventory.txt

[para]
192.168.2.94 ansible_connection=ssh ansible_ssh_user=root ansible_ssh_pass=pass1
192.168.2.92 ansible_connection=ssh ansible_ssh_user=root ansible_ssh_pass=pass2

#ansible_connection=ssh   使用ssh连接 

#ansible_ssh_user=root      root用户名

#ansible_ssh_pass=passx    root用户密码



再次通过authorized_key模块，来分发公钥文件

[root@ldap ~]# ansible para -i /tmp/ansible_inventory.txt -m authorized_key -a "user=root key='{{ lookup('file','/root/.ssh/id_rsa.pub') }}'

"""

"""
查看ansible事实 fact
ansible local -m setup
"""

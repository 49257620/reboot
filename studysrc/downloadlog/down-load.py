# encoding: utf-8
# Author: LW
"""
pyinstaller -F -w down-load.py

"""
import os
import sys

import paramiko
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import downlog

svrs = [('10.69.82.24',22,'root','Hxyw8224app1','/weblogicapp1/weblogic/Oracle/Middleware/user_projects/domains/hicis_domain/bin/nohup.out'),('10.69.82.25',22,'root','Hxyw8225app2','/weblogicapp2/weblogic/Oracle/Middleware/user_projects/domains/hicis_domain/bin/nohup.out')]

def sftp_download(host, port, username, password, local, remote):
    sf = paramiko.Transport((host, port))
    sf.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    try:
        if os.path.isdir(local):  # 判断本地参数是目录还是文件
            for f in sftp.listdir(remote):  # 遍历远程目录
                sftp.get(os.path.join(remote + f), os.path.join(local + f))  # 下载目录中文件
        else:
            sftp.get(remote, local)  # 下载文件
    except Exception as e:
        print('download exception:', e)
    sf.close()

def selectPath():
    directory1 = QFileDialog.getExistingDirectory(Form,
                                                  "选取文件夹",
                                                  "C:/")
    ui.path_edit.setText(directory1+"/nohup.out")

def downloadByConditions():
    local = ui.path_edit.text()
    idx =  ui.server_cob.currentIndex()
    sftp_download(svrs[idx][0], svrs[idx][1], svrs[idx][2], svrs[idx][3], local, svrs[idx][4])  # 下载
    reply = QMessageBox.question(Form, '消息框标题', '下载完成', QMessageBox.Yes, QMessageBox.Yes)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QMainWindow()

    ui = downlog.Ui_Form()

    ui.setupUi(Form)

    ui.path_select.clicked.connect(selectPath);
    ui.download_btn.clicked.connect(downloadByConditions);

    Form.show()

    sys.exit(app.exec_())

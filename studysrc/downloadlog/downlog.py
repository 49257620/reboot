# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downlog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("核心日志下载")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 171, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.server_cob = QtWidgets.QComboBox(Form)
        self.server_cob.setGeometry(QtCore.QRect(40, 70, 151, 21))
        self.server_cob.setObjectName("server_cob")
        self.server_cob.addItem("")
        self.server_cob.addItem("")
        self.path_edit = QtWidgets.QLineEdit(Form)
        self.path_edit.setGeometry(QtCore.QRect(40, 110, 281, 20))
        self.path_edit.setObjectName("path_edit")
        self.path_select = QtWidgets.QPushButton(Form)
        self.path_select.setGeometry(QtCore.QRect(328, 108, 61, 23))
        self.path_select.setObjectName("path_select")
        self.download_btn = QtWidgets.QPushButton(Form)
        self.download_btn.setGeometry(QtCore.QRect(40, 180, 91, 41))
        self.download_btn.setObjectName("download_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "核心日志下载"))
        self.server_cob.setItemText(0, _translate("Form", "24日志"))
        self.server_cob.setItemText(1, _translate("Form", "25日志"))
        self.path_select.setText(_translate("Form", "保存路径"))
        self.download_btn.setText(_translate("Form", "下载"))


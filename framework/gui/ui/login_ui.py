# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/login.ui'
#
# Created: Fri Dec 26 13:26:48 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(600, 280)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/mainicon/res/wp.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(_fromUtf8("background-image: url(:/bg/res/login.png);"))
        self.lbl_info = QtGui.QLabel(Form)
        self.lbl_info.setGeometry(QtCore.QRect(350, 60, 161, 16))
        self.lbl_info.setObjectName(_fromUtf8("lbl_info"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 100, 45, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txt_username = QtGui.QLineEdit(Form)
        self.txt_username.setGeometry(QtCore.QRect(355, 96, 190, 23))
        self.txt_username.setStyleSheet(_fromUtf8(""))
        self.txt_username.setFrame(False)
        self.txt_username.setObjectName(_fromUtf8("txt_username"))
        self.txt_pwd = QtGui.QLineEdit(Form)
        self.txt_pwd.setGeometry(QtCore.QRect(355, 140, 190, 23))
        self.txt_pwd.setFrame(False)
        self.txt_pwd.setObjectName(_fromUtf8("txt_pwd"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(300, 140, 45, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btn_login = QtGui.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(340, 210, 90, 28))
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(436, 210, 90, 28))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_info.setText(_translate("Form", "使用JIRA账号登录", None))
        self.label_2.setText(_translate("Form", "账号：", None))
        self.label_3.setText(_translate("Form", "密码：", None))
        self.btn_login.setText(_translate("Form", "登录", None))
        self.btn_cancel.setText(_translate("Form", "取消", None))

import res_rc

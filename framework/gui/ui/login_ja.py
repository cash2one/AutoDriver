# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ja.ui'
#
# Created: Wed Dec 24 14:30:08 2014
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
        Form.resize(516, 308)
        self.btn_login = QtGui.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(140, 210, 90, 32))
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(250, 210, 90, 32))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lbl_info = QtGui.QLabel(Form)
        self.lbl_info.setGeometry(QtCore.QRect(170, 50, 251, 16))
        self.lbl_info.setObjectName(_fromUtf8("lbl_info"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 140, 72, 15))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txt_username = QtGui.QLineEdit(Form)
        self.txt_username.setGeometry(QtCore.QRect(170, 90, 220, 30))
        self.txt_username.setObjectName(_fromUtf8("txt_username"))
        self.txt_pwd = QtGui.QLineEdit(Form)
        self.txt_pwd.setGeometry(QtCore.QRect(170, 140, 220, 30))
        self.txt_pwd.setObjectName(_fromUtf8("txt_pwd"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_login.setText(_translate("Form", "PushButton", None))
        self.btn_cancel.setText(_translate("Form", "PushButton", None))
        self.lbl_info.setText(_translate("Form", "登录到JIRA", None))
        self.label_2.setText(_translate("Form", "账号：", None))
        self.label_3.setText(_translate("Form", "密码：", None))


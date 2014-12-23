# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_jira.ui'
#
# Created: Tue Dec 23 15:53:47 2014
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
        Form.resize(439, 230)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../woodpecker.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.btnLogin = QtGui.QPushButton(Form)
        self.btnLogin.setGeometry(QtCore.QRect(100, 160, 93, 28))
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.txt_username = QtGui.QLineEdit(Form)
        self.txt_username.setGeometry(QtCore.QRect(140, 40, 201, 31))
        self.txt_username.setObjectName(_fromUtf8("txt_username"))
        self.txt_pwd = QtGui.QLineEdit(Form)
        self.txt_pwd.setGeometry(QtCore.QRect(140, 90, 201, 31))
        self.txt_pwd.setObjectName(_fromUtf8("txt_pwd"))
        self.btnCancel = QtGui.QPushButton(Form)
        self.btnCancel.setGeometry(QtCore.QRect(230, 160, 93, 28))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "登录JIRA", None))
        self.btnLogin.setText(_translate("Form", "登录", None))
        self.btnCancel.setText(_translate("Form", "取消", None))
        self.label.setText(_translate("Form", "用户名", None))
        self.label_2.setText(_translate("Form", "密 码", None))


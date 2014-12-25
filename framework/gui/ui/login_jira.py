# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/login_jira.ui'
#
# Created: Thu Dec 25 14:11:44 2014
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
        Form.resize(499, 254)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/wp/res/wp.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.lbl_info = QtGui.QLabel(Form)
        self.lbl_info.setGeometry(QtCore.QRect(140, 30, 251, 16))
        self.lbl_info.setObjectName(_fromUtf8("lbl_info"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(140, 160, 186, 28))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.btn_login = QtGui.QPushButton(self.splitter)
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.btn_cancel = QtGui.QPushButton(self.splitter)
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.splitter_2 = QtGui.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(80, 70, 216, 21))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_2 = QtGui.QLabel(self.splitter_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txt_username = QtGui.QLineEdit(self.splitter_2)
        self.txt_username.setObjectName(_fromUtf8("txt_username"))
        self.splitter_3 = QtGui.QSplitter(Form)
        self.splitter_3.setGeometry(QtCore.QRect(80, 120, 216, 21))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_3 = QtGui.QLabel(self.splitter_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txt_pwd = QtGui.QLineEdit(self.splitter_3)
        self.txt_pwd.setObjectName(_fromUtf8("txt_pwd"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_info.setText(_translate("Form", "登录到JIRA", None))
        self.btn_login.setText(_translate("Form", "登录", None))
        self.btn_cancel.setText(_translate("Form", "取消", None))
        self.label_2.setText(_translate("Form", "账号：", None))
        self.label_3.setText(_translate("Form", "密码：", None))

import res_rc

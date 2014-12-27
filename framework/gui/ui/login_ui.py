# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/login.ui'
#
# Created: Sat Dec 27 23:07:18 2014
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
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 600, 280))
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.lbl_info = QtGui.QLabel(self.widget)
        self.lbl_info.setGeometry(QtCore.QRect(350, 60, 161, 16))
        self.lbl_info.setObjectName(_fromUtf8("lbl_info"))
        self.btn_login = QtGui.QPushButton(self.widget)
        self.btn_login.setGeometry(QtCore.QRect(355, 210, 78, 28))
        self.btn_login.setAutoFillBackground(True)
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.btn_cancel = QtGui.QPushButton(self.widget)
        self.btn_cancel.setGeometry(QtCore.QRect(450, 210, 80, 30))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(300, 140, 45, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(300, 100, 45, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txt_pwd = QtGui.QLineEdit(self.widget)
        self.txt_pwd.setGeometry(QtCore.QRect(358, 141, 180, 19))
        self.txt_pwd.setFrame(False)
        self.txt_pwd.setObjectName(_fromUtf8("txt_pwd"))
        self.txt_username = QtGui.QLineEdit(self.widget)
        self.txt_username.setGeometry(QtCore.QRect(358, 97, 180, 19))
        self.txt_username.setStyleSheet(_fromUtf8(""))
        self.txt_username.setFrame(False)
        self.txt_username.setObjectName(_fromUtf8("txt_username"))
        self.checkBox = QtGui.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(358, 180, 71, 16))
        self.checkBox.setIconSize(QtCore.QSize(16, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_info.setText(_translate("Form", "使用JIRA账号登录", None))
        self.btn_login.setText(_translate("Form", "登录", None))
        self.btn_cancel.setText(_translate("Form", "取消", None))
        self.label_3.setText(_translate("Form", "密码", None))
        self.label_2.setText(_translate("Form", "账号", None))
        self.checkBox.setText(_translate("Form", "记住密码", None))

import res_rc

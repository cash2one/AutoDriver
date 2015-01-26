# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/monitor.ui'
#
# Created: Fri Jan 09 11:37:16 2015
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(620, 400)
        Dialog.setMaximumSize(QtCore.QSize(620, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/mainicon/res/wp.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txt_host = QtGui.QLineEdit(Dialog)
        self.txt_host.setMinimumSize(QtCore.QSize(0, 25))
        self.txt_host.setObjectName(_fromUtf8("txt_host"))
        self.gridLayout.addWidget(self.txt_host, 0, 1, 1, 1)
        self.btn_start = QtGui.QPushButton(Dialog)
        self.btn_start.setMinimumSize(QtCore.QSize(70, 25))
        self.btn_start.setMaximumSize(QtCore.QSize(70, 25))
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.gridLayout.addWidget(self.btn_start, 0, 5, 1, 1)
        self.btn_end = QtGui.QPushButton(Dialog)
        self.btn_end.setMinimumSize(QtCore.QSize(70, 25))
        self.btn_end.setMaximumSize(QtCore.QSize(70, 25))
        self.btn_end.setObjectName(_fromUtf8("btn_end"))
        self.gridLayout.addWidget(self.btn_end, 0, 6, 1, 1)
        self.txt_port = QtGui.QLineEdit(Dialog)
        self.txt_port.setMinimumSize(QtCore.QSize(0, 25))
        self.txt_port.setMaximumSize(QtCore.QSize(80, 16777215))
        self.txt_port.setObjectName(_fromUtf8("txt_port"))
        self.gridLayout.addWidget(self.txt_port, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.chk_server = QtGui.QCheckBox(Dialog)
        self.chk_server.setObjectName(_fromUtf8("chk_server"))
        self.gridLayout.addWidget(self.chk_server, 0, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 5, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.txt_msg = QtGui.QTextEdit(Dialog)
        self.txt_msg.setObjectName(_fromUtf8("txt_msg"))
        self.verticalLayout.addWidget(self.txt_msg)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "服务器性能监控", None))
        self.label.setText(_translate("Dialog", "服务器地址", None))
        self.btn_start.setText(_translate("Dialog", "开始", None))
        self.btn_end.setText(_translate("Dialog", "结束", None))
        self.label_2.setText(_translate("Dialog", "端口", None))
        self.chk_server.setText(_translate("Dialog", "我是服务器", None))
        self.label_3.setText(_translate("Dialog", "响应信息", None))


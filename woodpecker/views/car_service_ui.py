# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/car_service.ui'
#
# Created: Sat Jan 31 14:45:52 2015
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
        Dialog.resize(950, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/mainicon/res/wp.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lbl_file_path = QtGui.QLabel(Dialog)
        self.lbl_file_path.setObjectName(_fromUtf8("lbl_file_path"))
        self.horizontalLayout_3.addWidget(self.lbl_file_path)
        self.btn_del_file = QtGui.QPushButton(Dialog)
        self.btn_del_file.setObjectName(_fromUtf8("btn_del_file"))
        self.horizontalLayout_3.addWidget(self.btn_del_file)
        self.txt_file = QtGui.QLineEdit(Dialog)
        self.txt_file.setMinimumSize(QtCore.QSize(180, 0))
        self.txt_file.setMaximumSize(QtCore.QSize(180, 16777215))
        self.txt_file.setObjectName(_fromUtf8("txt_file"))
        self.horizontalLayout_3.addWidget(self.txt_file)
        self.btn_select_file = QtGui.QPushButton(Dialog)
        self.btn_select_file.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_select_file.setObjectName(_fromUtf8("btn_select_file"))
        self.horizontalLayout_3.addWidget(self.btn_select_file)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.txt_scr_width = QtGui.QLineEdit(Dialog)
        self.txt_scr_width.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txt_scr_width.setText(_fromUtf8(""))
        self.txt_scr_width.setObjectName(_fromUtf8("txt_scr_width"))
        self.horizontalLayout_3.addWidget(self.txt_scr_width)
        self.btn_reset = QtGui.QPushButton(Dialog)
        self.btn_reset.setMinimumSize(QtCore.QSize(88, 0))
        self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
        self.horizontalLayout_3.addWidget(self.btn_reset)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tree = QtGui.QTreeView(Dialog)
        self.tree.setMinimumSize(QtCore.QSize(260, 0))
        self.tree.setMaximumSize(QtCore.QSize(260, 16777215))
        self.tree.setObjectName(_fromUtf8("tree"))
        self.horizontalLayout.addWidget(self.tree)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.webView = QtWebKit.QWebView(Dialog)
        self.webView.setMinimumSize(QtCore.QSize(450, 0))
        self.webView.setMaximumSize(QtCore.QSize(450, 16777215))
        self.webView.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.horizontalLayout.addWidget(self.webView)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "行车助手", None))
        self.lbl_file_path.setText(_translate("Dialog", "已有车助手文件存在！", None))
        self.btn_del_file.setText(_translate("Dialog", "删除文件", None))
        self.btn_select_file.setText(_translate("Dialog", "选择文件", None))
        self.label_2.setText(_translate("Dialog", "屏幕宽度", None))
        self.btn_reset.setText(_translate("Dialog", "重置屏幕尺寸", None))

from PyQt4 import QtWebKit
import res_rc

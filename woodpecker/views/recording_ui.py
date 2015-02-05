# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/recording.ui'
#
# Created: Thu Feb 05 21:55:50 2015
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
        Form.resize(917, 525)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.img_layout = QtGui.QVBoxLayout()
        self.img_layout.setObjectName(_fromUtf8("img_layout"))
        self.horizontalLayout_3.addLayout(self.img_layout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.txt_ip_addr = QtGui.QLineEdit(Form)
        self.txt_ip_addr.setObjectName(_fromUtf8("txt_ip_addr"))
        self.horizontalLayout_4.addWidget(self.txt_ip_addr)
        self.btn_connect = QtGui.QPushButton(Form)
        self.btn_connect.setObjectName(_fromUtf8("btn_connect"))
        self.horizontalLayout_4.addWidget(self.btn_connect)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_menu = QtGui.QPushButton(Form)
        self.btn_menu.setMinimumSize(QtCore.QSize(80, 0))
        self.btn_menu.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_menu.setObjectName(_fromUtf8("btn_menu"))
        self.horizontalLayout.addWidget(self.btn_menu)
        self.btn_home = QtGui.QPushButton(Form)
        self.btn_home.setMinimumSize(QtCore.QSize(80, 0))
        self.btn_home.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_home.setObjectName(_fromUtf8("btn_home"))
        self.horizontalLayout.addWidget(self.btn_home)
        self.btn_back = QtGui.QPushButton(Form)
        self.btn_back.setMinimumSize(QtCore.QSize(80, 0))
        self.btn_back.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_back.setObjectName(_fromUtf8("btn_back"))
        self.horizontalLayout.addWidget(self.btn_back)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.btn_refresh = QtGui.QPushButton(Form)
        self.btn_refresh.setMinimumSize(QtCore.QSize(80, 0))
        self.btn_refresh.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_refresh.setObjectName(_fromUtf8("btn_refresh"))
        self.horizontalLayout_2.addWidget(self.btn_refresh)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.txt_elements = QtGui.QTextEdit(Form)
        self.txt_elements.setMinimumSize(QtCore.QSize(0, 0))
        self.txt_elements.setMaximumSize(QtCore.QSize(16777215, 180))
        self.txt_elements.setObjectName(_fromUtf8("txt_elements"))
        self.verticalLayout_2.addWidget(self.txt_elements)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_connect.setText(_translate("Form", "连接", None))
        self.btn_menu.setText(_translate("Form", "Menu", None))
        self.btn_home.setText(_translate("Form", "Home", None))
        self.btn_back.setText(_translate("Form", "Back", None))
        self.checkBox.setText(_translate("Form", "脚本录制", None))
        self.pushButton.setText(_translate("Form", "保存脚本", None))
        self.btn_refresh.setText(_translate("Form", "刷新", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/recording.ui'
#
# Created: Thu Feb 05 17:43:28 2015
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
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.img_layout = QtGui.QVBoxLayout()
        self.img_layout.setObjectName(_fromUtf8("img_layout"))
        self.verticalLayout_2.addLayout(self.img_layout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_menu = QtGui.QPushButton(Form)
        self.btn_menu.setObjectName(_fromUtf8("btn_menu"))
        self.horizontalLayout.addWidget(self.btn_menu)
        self.btn_home = QtGui.QPushButton(Form)
        self.btn_home.setObjectName(_fromUtf8("btn_home"))
        self.horizontalLayout.addWidget(self.btn_home)
        self.btn_back = QtGui.QPushButton(Form)
        self.btn_back.setObjectName(_fromUtf8("btn_back"))
        self.horizontalLayout.addWidget(self.btn_back)
        self.btn_refresh = QtGui.QPushButton(Form)
        self.btn_refresh.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_refresh.setObjectName(_fromUtf8("btn_refresh"))
        self.horizontalLayout.addWidget(self.btn_refresh)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.txt_elements = QtGui.QTextEdit(Form)
        self.txt_elements.setMinimumSize(QtCore.QSize(400, 0))
        self.txt_elements.setMaximumSize(QtCore.QSize(400, 16777215))
        self.txt_elements.setObjectName(_fromUtf8("txt_elements"))
        self.verticalLayout.addWidget(self.txt_elements)
        self.txt_info = QtGui.QLineEdit(Form)
        self.txt_info.setObjectName(_fromUtf8("txt_info"))
        self.verticalLayout.addWidget(self.txt_info)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_menu.setText(_translate("Form", "Menu", None))
        self.btn_home.setText(_translate("Form", "Home", None))
        self.btn_back.setText(_translate("Form", "Back", None))
        self.btn_refresh.setText(_translate("Form", "刷新", None))


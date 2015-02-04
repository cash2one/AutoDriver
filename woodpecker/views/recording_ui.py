# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/recording.ui'
#
# Created: Wed Feb 04 19:09:23 2015
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
        Form.resize(857, 525)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.img_layout = QtGui.QVBoxLayout()
        self.img_layout.setObjectName(_fromUtf8("img_layout"))
        self.horizontalLayout.addLayout(self.img_layout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btn_refresh = QtGui.QPushButton(Form)
        self.btn_refresh.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_refresh.setObjectName(_fromUtf8("btn_refresh"))
        self.verticalLayout.addWidget(self.btn_refresh)
        self.txt_elements = QtGui.QTextEdit(Form)
        self.txt_elements.setMinimumSize(QtCore.QSize(400, 0))
        self.txt_elements.setMaximumSize(QtCore.QSize(400, 16777215))
        self.txt_elements.setObjectName(_fromUtf8("txt_elements"))
        self.verticalLayout.addWidget(self.txt_elements)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_refresh.setText(_translate("Form", "刷新", None))


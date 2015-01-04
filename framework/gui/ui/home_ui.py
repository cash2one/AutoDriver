# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/home.ui'
#
# Created: Sun Jan 04 00:02:32 2015
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
        Form.resize(878, 573)
        Form.setAutoFillBackground(False)
        self.tv_task = QtGui.QTableView(Form)
        self.tv_task.setGeometry(QtCore.QRect(10, 80, 511, 91))
        self.tv_task.setObjectName(_fromUtf8("tv_task"))
        self.tv_task.horizontalHeader().setCascadingSectionResizes(True)
        self.lbl_weather = QtGui.QLabel(Form)
        self.lbl_weather.setGeometry(QtCore.QRect(20, 10, 681, 31))
        self.lbl_weather.setObjectName(_fromUtf8("lbl_weather"))
        self.txt_a = QtGui.QTextEdit(Form)
        self.txt_a.setGeometry(QtCore.QRect(10, 200, 681, 221))
        self.txt_a.setObjectName(_fromUtf8("txt_a"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_weather.setText(_translate("Form", "TextLabel", None))

import res_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/home.ui'
#
# Created: Thu Jan 08 00:30:47 2015
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
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_weather = QtGui.QLabel(Form)
        self.lbl_weather.setObjectName(_fromUtf8("lbl_weather"))
        self.verticalLayout.addWidget(self.lbl_weather)
        self.txt_a = QtGui.QTextEdit(Form)
        self.txt_a.setObjectName(_fromUtf8("txt_a"))
        self.verticalLayout.addWidget(self.txt_a)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_weather.setText(_translate("Form", "TextLabel", None))

import res_rc

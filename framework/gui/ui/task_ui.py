# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/task.ui'
#
# Created: Thu Jan 01 23:11:00 2015
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
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tv_task = QtGui.QTableView(Form)
        self.tv_task.setObjectName(_fromUtf8("tv_task"))
        self.tv_task.horizontalHeader().setCascadingSectionResizes(True)
        self.verticalLayout.addWidget(self.tv_task)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "新建任务", None))
        self.label.setText(_translate("Form", "Welcome", None))

import res_rc

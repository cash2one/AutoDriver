# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/task.ui'
#
# Created: Fri Jan 16 15:11:09 2015
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
        self.btn_new_task = QtGui.QPushButton(Form)
        self.btn_new_task.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_new_task.setObjectName(_fromUtf8("btn_new_task"))
        self.horizontalLayout.addWidget(self.btn_new_task)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tv_task = QtGui.QTableView(Form)
        self.tv_task.setObjectName(_fromUtf8("tv_task"))
        self.tv_task.horizontalHeader().setCascadingSectionResizes(True)
        self.verticalLayout.addWidget(self.tv_task)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_new_task.setText(_translate("Form", "新建任务", None))


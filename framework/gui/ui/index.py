# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created: Thu Dec 25 00:23:17 2014
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
        Form.resize(791, 485)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table_task = QtGui.QTableWidget(Form)
        self.table_task.setBaseSize(QtCore.QSize(0, 0))
        self.table_task.setObjectName(_fromUtf8("table_task"))
        self.table_task.setColumnCount(7)
        self.table_task.setRowCount(15)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setVerticalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.table_task)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "新建任务", None))
        self.label.setText(_translate("Form", "Welcome", None))
        item = self.table_task.verticalHeaderItem(0)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(1)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(2)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(3)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(4)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(5)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(6)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(7)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(8)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(9)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(10)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(11)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(12)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(13)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.verticalHeaderItem(14)
        item.setText(_translate("Form", "新建行", None))
        item = self.table_task.horizontalHeaderItem(0)
        item.setText(_translate("Form", "新建列", None))
        item = self.table_task.horizontalHeaderItem(1)
        item.setText(_translate("Form", "新建列", None))
        item = self.table_task.horizontalHeaderItem(2)
        item.setText(_translate("Form", "新建列", None))
        item = self.table_task.horizontalHeaderItem(3)
        item.setText(_translate("Form", "新建列", None))
        item = self.table_task.horizontalHeaderItem(4)
        item.setText(_translate("Form", "新建列", None))
        item = self.table_task.horizontalHeaderItem(5)
        item.setText(_translate("Form", "新建列", None))
        item = self.table_task.horizontalHeaderItem(6)
        item.setText(_translate("Form", "新建列", None))


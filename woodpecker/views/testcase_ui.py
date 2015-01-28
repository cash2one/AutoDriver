# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/testcase.ui'
#
# Created: Wed Jan 28 17:18:01 2015
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
        Form.resize(1244, 603)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cmb_project = QtGui.QComboBox(Form)
        self.cmb_project.setMinimumSize(QtCore.QSize(240, 0))
        self.cmb_project.setMaximumSize(QtCore.QSize(240, 16777215))
        self.cmb_project.setObjectName(_fromUtf8("cmb_project"))
        self.cmb_project.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.cmb_project)
        self.treeView = QtGui.QTreeView(Form)
        self.treeView.setMaximumSize(QtCore.QSize(240, 16777215))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout_3.addWidget(self.treeView)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_excel = QtGui.QPushButton(Form)
        self.btn_excel.setMinimumSize(QtCore.QSize(110, 0))
        self.btn_excel.setMaximumSize(QtCore.QSize(110, 16777215))
        self.btn_excel.setObjectName(_fromUtf8("btn_excel"))
        self.horizontalLayout_2.addWidget(self.btn_excel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tv_cases = QtGui.QTableView(Form)
        self.tv_cases.setObjectName(_fromUtf8("tv_cases"))
        self.verticalLayout.addWidget(self.tv_cases)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.cmb_project.setItemText(0, _translate("Form", "选择项目", None))
        self.btn_excel.setText(_translate("Form", "导入excel", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/jira_main.ui'
#
# Created: Mon Dec 29 15:03:22 2014
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
        Form.resize(1137, 480)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_bug = QtGui.QLabel(Form)
        self.lbl_bug.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lbl_bug.setObjectName(_fromUtf8("lbl_bug"))
        self.horizontalLayout.addWidget(self.lbl_bug)
        self.cmb_project = QtGui.QComboBox(Form)
        self.cmb_project.setMaximumSize(QtCore.QSize(160, 30))
        self.cmb_project.setObjectName(_fromUtf8("cmb_project"))
        self.horizontalLayout.addWidget(self.cmb_project)
        self.cmb_user = QtGui.QComboBox(Form)
        self.cmb_user.setMaximumSize(QtCore.QSize(160, 30))
        self.cmb_user.setObjectName(_fromUtf8("cmb_user"))
        self.cmb_user.addItem(_fromUtf8(""))
        self.cmb_user.addItem(_fromUtf8(""))
        self.cmb_user.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cmb_user)
        self.btn_find = QtGui.QPushButton(Form)
        self.btn_find.setMaximumSize(QtCore.QSize(90, 30))
        self.btn_find.setObjectName(_fromUtf8("btn_find"))
        self.horizontalLayout.addWidget(self.btn_find)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tv_bugs = QtGui.QTableView(Form)
        self.tv_bugs.setObjectName(_fromUtf8("tv_bugs"))
        self.verticalLayout.addWidget(self.tv_bugs)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_bug.setText(_translate("Form", "查询条件", None))
        self.cmb_user.setItemText(0, _translate("Form", "20", None))
        self.cmb_user.setItemText(1, _translate("Form", "30", None))
        self.cmb_user.setItemText(2, _translate("Form", "40", None))
        self.btn_find.setText(_translate("Form", "查询", None))
        self.label.setText(_translate("Form", "TextLabel", None))


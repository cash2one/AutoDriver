# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/interface.ui'
#
# Created: Sat Jan 10 20:48:57 2015
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
        Form.resize(861, 480)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tree_infs = QtGui.QTreeView(Form)
        self.tree_infs.setMaximumSize(QtCore.QSize(220, 16777215))
        self.tree_infs.setObjectName(_fromUtf8("tree_infs"))
        self.horizontalLayout.addWidget(self.tree_infs)
        self.tab_inf = QtGui.QTabWidget(Form)
        self.tab_inf.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tab_inf.setObjectName(_fromUtf8("tab_inf"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_desc = QtGui.QLabel(self.tab_3)
        self.lbl_desc.setObjectName(_fromUtf8("lbl_desc"))
        self.verticalLayout.addWidget(self.lbl_desc)
        self.tv_inf = QtGui.QTableView(self.tab_3)
        self.tv_inf.setFrameShape(QtGui.QFrame.NoFrame)
        self.tv_inf.setObjectName(_fromUtf8("tv_inf"))
        self.verticalLayout.addWidget(self.tv_inf)
        self.txt_result = QtGui.QTextEdit(self.tab_3)
        self.txt_result.setFrameShape(QtGui.QFrame.NoFrame)
        self.txt_result.setObjectName(_fromUtf8("txt_result"))
        self.verticalLayout.addWidget(self.txt_result)
        self.tab_inf.addTab(self.tab_3, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tab_inf)

        self.retranslateUi(Form)
        self.tab_inf.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_desc.setText(_translate("Form", "TextLabel", None))
        self.tab_inf.setTabText(self.tab_inf.indexOf(self.tab_3), _translate("Form", "Tab 1", None))


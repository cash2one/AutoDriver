# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created: Mon Dec 22 15:43:31 2014
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
        Form.resize(600, 400)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(460, 330, 121, 41))
        self.pushButton.setStyleSheet(_fromUtf8("font: 9pt \"微软雅黑\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.labela = QtGui.QLabel(Form)
        self.labela.setGeometry(QtCore.QRect(20, 340, 72, 15))
        self.labela.setStyleSheet(_fromUtf8("font: 9pt \"微软雅黑\";"))
        self.labela.setObjectName(_fromUtf8("labela"))
        self.lv_testcase = QtGui.QListView(Form)
        self.lv_testcase.setGeometry(QtCore.QRect(20, 60, 561, 261))
        self.lv_testcase.setObjectName(_fromUtf8("lv_testcase"))
        self.cmbProject = QtGui.QComboBox(Form)
        self.cmbProject.setGeometry(QtCore.QRect(100, 20, 201, 31))
        self.cmbProject.setStyleSheet(_fromUtf8("font: 9pt \"微软雅黑\";"))
        self.cmbProject.setObjectName(_fromUtf8("cmbProject"))
        self.labela_2 = QtGui.QLabel(Form)
        self.labela_2.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.labela_2.setStyleSheet(_fromUtf8("font: 9pt \"微软雅黑\";"))
        self.labela_2.setObjectName(_fromUtf8("labela_2"))
        self.cmb_subProject = QtGui.QComboBox(Form)
        self.cmb_subProject.setGeometry(QtCore.QRect(320, 20, 201, 31))
        self.cmb_subProject.setStyleSheet(_fromUtf8("font: 9pt \"微软雅黑\";"))
        self.cmb_subProject.setObjectName(_fromUtf8("cmb_subProject"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Autotest", None))
        self.pushButton.setText(_translate("Form", "run", None))
        self.labela.setText(_translate("Form", "已选文件", None))
        self.labela_2.setText(_translate("Form", "选择项目", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/task_ui.ui'
#
# Created: Thu Dec 25 13:23:47 2014
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
        Form.resize(713, 470)
        self.txt_TaskName = QtGui.QLineEdit(Form)
        self.txt_TaskName.setGeometry(QtCore.QRect(130, 20, 531, 25))
        self.txt_TaskName.setObjectName(_fromUtf8("txt_TaskName"))
        self.txt_Creator = QtGui.QLineEdit(Form)
        self.txt_Creator.setGeometry(QtCore.QRect(130, 100, 180, 25))
        self.txt_Creator.setObjectName(_fromUtf8("txt_Creator"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 180, 180, 25))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(130, 270, 541, 111))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(130, 220, 200, 28))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox_2 = QtGui.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 60, 180, 28))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(364, 100, 60, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.btnAutomate = QtGui.QPushButton(Form)
        self.btnAutomate.setGeometry(QtCore.QRect(350, 220, 71, 28))
        self.btnAutomate.setObjectName(_fromUtf8("btnAutomate"))
        self.comboBox_3 = QtGui.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(441, 60, 180, 28))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(390, 60, 45, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(330, 140, 101, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.txt_Creator_2 = QtGui.QLineEdit(Form)
        self.txt_Creator_2.setGeometry(QtCore.QRect(130, 140, 180, 25))
        self.txt_Creator_2.setObjectName(_fromUtf8("txt_Creator_2"))
        self.txt_Creator_3 = QtGui.QLineEdit(Form)
        self.txt_Creator_3.setGeometry(QtCore.QRect(440, 100, 180, 25))
        self.txt_Creator_3.setObjectName(_fromUtf8("txt_Creator_3"))
        self.txt_Creator_4 = QtGui.QLineEdit(Form)
        self.txt_Creator_4.setGeometry(QtCore.QRect(440, 140, 180, 25))
        self.txt_Creator_4.setObjectName(_fromUtf8("txt_Creator_4"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(20, 20, 90, 271))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_7 = QtGui.QLabel(self.splitter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_3 = QtGui.QLabel(self.splitter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_10 = QtGui.QLabel(self.splitter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_4 = QtGui.QLabel(self.splitter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.splitter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_5 = QtGui.QLabel(self.splitter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 400, 101, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_8.setText(_translate("Form", "创建时间", None))
        self.btnAutomate.setText(_translate("Form", "自动化", None))
        self.label_9.setText(_translate("Form", "状态", None))
        self.label_11.setText(_translate("Form", "实际执行时间", None))
        self.label_2.setText(_translate("Form", "任务名称", None))
        self.label_7.setText(_translate("Form", "优先级", None))
        self.label_3.setText(_translate("Form", "创建人", None))
        self.label_10.setText(_translate("Form", "期望执行时间", None))
        self.label_4.setText(_translate("Form", "执行人", None))
        self.label_6.setText(_translate("Form", "任务类型", None))
        self.label_5.setText(_translate("Form", "任务描述", None))
        self.pushButton.setText(_translate("Form", "确定", None))


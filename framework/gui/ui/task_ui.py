# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/task.ui'
#
# Created: Fri Dec 26 17:41:38 2014
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
        Form.resize(700, 520)
        Form.setMaximumSize(QtCore.QSize(700, 520))
        self.txt_TaskName = QtGui.QLineEdit(Form)
        self.txt_TaskName.setGeometry(QtCore.QRect(130, 30, 531, 25))
        self.txt_TaskName.setObjectName(_fromUtf8("txt_TaskName"))
        self.txt_Creator = QtGui.QLineEdit(Form)
        self.txt_Creator.setGeometry(QtCore.QRect(130, 150, 180, 25))
        self.txt_Creator.setObjectName(_fromUtf8("txt_Creator"))
        self.txt_Requester = QtGui.QLineEdit(Form)
        self.txt_Requester.setGeometry(QtCore.QRect(440, 152, 180, 25))
        self.txt_Requester.setObjectName(_fromUtf8("txt_Requester"))
        self.txt_TaskDescription = QtGui.QTextEdit(Form)
        self.txt_TaskDescription.setGeometry(QtCore.QRect(130, 320, 541, 111))
        self.txt_TaskDescription.setObjectName(_fromUtf8("txt_TaskDescription"))
        self.cmb_TaskType = QtGui.QComboBox(Form)
        self.cmb_TaskType.setGeometry(QtCore.QRect(440, 70, 131, 28))
        self.cmb_TaskType.setObjectName(_fromUtf8("cmb_TaskType"))
        self.cmb_TaskType.addItem(_fromUtf8(""))
        self.cmb_TaskType.addItem(_fromUtf8(""))
        self.cmb_TaskType.addItem(_fromUtf8(""))
        self.cmb_TaskType.addItem(_fromUtf8(""))
        self.cmb_TaskType.addItem(_fromUtf8(""))
        self.cmb_TaskType.addItem(_fromUtf8(""))
        self.cmb_TaskType.addItem(_fromUtf8(""))
        self.cmb_TaskPriority = QtGui.QComboBox(Form)
        self.cmb_TaskPriority.setGeometry(QtCore.QRect(130, 110, 180, 28))
        self.cmb_TaskPriority.setObjectName(_fromUtf8("cmb_TaskPriority"))
        self.cmb_TaskPriority.addItem(_fromUtf8(""))
        self.cmb_TaskPriority.addItem(_fromUtf8(""))
        self.cmb_TaskPriority.addItem(_fromUtf8(""))
        self.cmb_TaskPriority.addItem(_fromUtf8(""))
        self.btn_Automate = QtGui.QPushButton(Form)
        self.btn_Automate.setGeometry(QtCore.QRect(590, 70, 65, 28))
        self.btn_Automate.setObjectName(_fromUtf8("btn_Automate"))
        self.cmb_TaskState = QtGui.QComboBox(Form)
        self.cmb_TaskState.setGeometry(QtCore.QRect(441, 110, 180, 28))
        self.cmb_TaskState.setObjectName(_fromUtf8("cmb_TaskState"))
        self.cmb_TaskState.addItem(_fromUtf8(""))
        self.cmb_TaskState.addItem(_fromUtf8(""))
        self.cmb_TaskState.addItem(_fromUtf8(""))
        self.cmb_TaskState.addItem(_fromUtf8(""))
        self.cmb_TaskState.addItem(_fromUtf8(""))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(390, 115, 45, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(370, 261, 101, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.txt_ExpectedStartDateTime = QtGui.QLineEdit(Form)
        self.txt_ExpectedStartDateTime.setGeometry(QtCore.QRect(130, 261, 180, 25))
        self.txt_ExpectedStartDateTime.setObjectName(_fromUtf8("txt_ExpectedStartDateTime"))
        self.txt_CreateDateTime = QtGui.QLineEdit(Form)
        self.txt_CreateDateTime.setGeometry(QtCore.QRect(130, 220, 180, 25))
        self.txt_CreateDateTime.setObjectName(_fromUtf8("txt_CreateDateTime"))
        self.txt_ExpectedEndDateTime = QtGui.QLineEdit(Form)
        self.txt_ExpectedEndDateTime.setGeometry(QtCore.QRect(480, 261, 180, 25))
        self.txt_ExpectedEndDateTime.setObjectName(_fromUtf8("txt_ExpectedEndDateTime"))
        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(404, 220, 60, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.txt_ExecuteEndDate = QtGui.QLineEdit(Form)
        self.txt_ExecuteEndDate.setGeometry(QtCore.QRect(480, 220, 180, 25))
        self.txt_ExecuteEndDate.setObjectName(_fromUtf8("txt_ExecuteEndDate"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 200, 651, 2))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(20, 300, 651, 2))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.txt_TaskNo = QtGui.QLineEdit(Form)
        self.txt_TaskNo.setGeometry(QtCore.QRect(130, 70, 180, 25))
        self.txt_TaskNo.setObjectName(_fromUtf8("txt_TaskNo"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 460, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 460, 93, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(360, 80, 60, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(380, 155, 45, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(20, 20, 90, 321))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_13 = QtGui.QLabel(self.splitter)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_7 = QtGui.QLabel(self.splitter)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_3 = QtGui.QLabel(self.splitter)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_8 = QtGui.QLabel(self.splitter)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_10 = QtGui.QLabel(self.splitter)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_5 = QtGui.QLabel(self.splitter)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "任务", None))
        self.cmb_TaskType.setItemText(0, _translate("Form", "请选择任务类型", None))
        self.cmb_TaskType.setItemText(1, _translate("Form", "自动化", None))
        self.cmb_TaskType.setItemText(2, _translate("Form", "车机测试", None))
        self.cmb_TaskType.setItemText(3, _translate("Form", "App", None))
        self.cmb_TaskType.setItemText(4, _translate("Form", "Web平台", None))
        self.cmb_TaskType.setItemText(5, _translate("Form", "接口", None))
        self.cmb_TaskType.setItemText(6, _translate("Form", "性能测试", None))
        self.cmb_TaskPriority.setItemText(0, _translate("Form", "请选择优先级", None))
        self.cmb_TaskPriority.setItemText(1, _translate("Form", "普通", None))
        self.cmb_TaskPriority.setItemText(2, _translate("Form", "中级", None))
        self.cmb_TaskPriority.setItemText(3, _translate("Form", "高级", None))
        self.btn_Automate.setText(_translate("Form", "自动化", None))
        self.cmb_TaskState.setItemText(0, _translate("Form", "请选择状态", None))
        self.cmb_TaskState.setItemText(1, _translate("Form", "未开始", None))
        self.cmb_TaskState.setItemText(2, _translate("Form", "已开始", None))
        self.cmb_TaskState.setItemText(3, _translate("Form", "已取消", None))
        self.cmb_TaskState.setItemText(4, _translate("Form", "已结束", None))
        self.label_9.setText(_translate("Form", "状态", None))
        self.label_11.setText(_translate("Form", "实际执行时间", None))
        self.label_12.setText(_translate("Form", "结束时间", None))
        self.pushButton.setText(_translate("Form", "确定", None))
        self.pushButton_2.setText(_translate("Form", "取消", None))
        self.label_6.setText(_translate("Form", "任务类型", None))
        self.label_4.setText(_translate("Form", "执行人", None))
        self.label_2.setText(_translate("Form", "任务名称", None))
        self.label_13.setText(_translate("Form", "任务编号", None))
        self.label_7.setText(_translate("Form", "优先级", None))
        self.label_3.setText(_translate("Form", "创建人", None))
        self.label_8.setText(_translate("Form", "创建时间", None))
        self.label_10.setText(_translate("Form", "期望执行时间", None))
        self.label_5.setText(_translate("Form", "任务描述", None))


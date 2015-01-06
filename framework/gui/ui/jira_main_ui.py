# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/jira_main.ui'
#
# Created: Mon Jan 05 16:44:23 2015
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
        self.searchLayout = QtGui.QHBoxLayout()
        self.searchLayout.setContentsMargins(-1, 2, -1, 5)
        self.searchLayout.setObjectName(_fromUtf8("searchLayout"))
        self.lbl_bug = QtGui.QLabel(Form)
        self.lbl_bug.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lbl_bug.setObjectName(_fromUtf8("lbl_bug"))
        self.searchLayout.addWidget(self.lbl_bug)
        self.cmb_project = QtGui.QComboBox(Form)
        self.cmb_project.setMaximumSize(QtCore.QSize(160, 30))
        self.cmb_project.setObjectName(_fromUtf8("cmb_project"))
        self.searchLayout.addWidget(self.cmb_project)
        self.comboBox_2 = QtGui.QComboBox(Form)
        self.comboBox_2.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon16/res/status_open.gif")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.comboBox_2.addItem(icon, _fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon16/res/status_inprogress.gif")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.comboBox_2.addItem(icon1, _fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon16/res/status_reopened.gif")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.comboBox_2.addItem(icon2, _fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon16/res/status_resolved.gif")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.comboBox_2.addItem(icon3, _fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon16/res/status_closed.gif")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.comboBox_2.addItem(icon4, _fromUtf8(""))
        self.searchLayout.addWidget(self.comboBox_2)
        self.comboBox_3 = QtGui.QComboBox(Form)
        self.comboBox_3.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon16/res/priority_blocker.gif")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.comboBox_3.addItem(icon5, _fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon16/res/priority_critical.gif")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.comboBox_3.addItem(icon6, _fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon16/res/priority_major.gif")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.comboBox_3.addItem(icon7, _fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon16/res/priority_minor.gif")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.comboBox_3.addItem(icon8, _fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon16/res/priority_trivial.gif")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.comboBox_3.addItem(icon9, _fromUtf8(""))
        self.searchLayout.addWidget(self.comboBox_3)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.searchLayout.addWidget(self.comboBox)
        self.btn_find = QtGui.QPushButton(Form)
        self.btn_find.setMaximumSize(QtCore.QSize(70, 30))
        self.btn_find.setObjectName(_fromUtf8("btn_find"))
        self.searchLayout.addWidget(self.btn_find)
        self.lbl_results = QtGui.QLabel(Form)
        self.lbl_results.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_results.setObjectName(_fromUtf8("lbl_results"))
        self.searchLayout.addWidget(self.lbl_results)
        self.pageLayout = QtGui.QHBoxLayout()
        self.pageLayout.setObjectName(_fromUtf8("pageLayout"))
        self.btn_prev = QtGui.QPushButton(Form)
        self.btn_prev.setMaximumSize(QtCore.QSize(40, 30))
        self.btn_prev.setObjectName(_fromUtf8("btn_prev"))
        self.pageLayout.addWidget(self.btn_prev)
        self.btn_next = QtGui.QPushButton(Form)
        self.btn_next.setMaximumSize(QtCore.QSize(40, 30))
        self.btn_next.setObjectName(_fromUtf8("btn_next"))
        self.pageLayout.addWidget(self.btn_next)
        self.cmb_pages = QtGui.QComboBox(Form)
        self.cmb_pages.setMaximumSize(QtCore.QSize(100, 30))
        self.cmb_pages.setObjectName(_fromUtf8("cmb_pages"))
        self.cmb_pages.addItem(_fromUtf8(""))
        self.pageLayout.addWidget(self.cmb_pages)
        self.searchLayout.addLayout(self.pageLayout)
        self.verticalLayout.addLayout(self.searchLayout)
        self.tv_bugs = QtGui.QTableView(Form)
        self.tv_bugs.setObjectName(_fromUtf8("tv_bugs"))
        self.verticalLayout.addWidget(self.tv_bugs)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_bug.setText(_translate("Form", "查询条件", None))
        self.comboBox_2.setItemText(0, _translate("Form", "任何状态", None))
        self.comboBox_2.setItemText(1, _translate("Form", "开启", None))
        self.comboBox_2.setItemText(2, _translate("Form", "进行中", None))
        self.comboBox_2.setItemText(3, _translate("Form", "重开", None))
        self.comboBox_2.setItemText(4, _translate("Form", "已解决", None))
        self.comboBox_2.setItemText(5, _translate("Form", "关闭", None))
        self.comboBox_3.setItemText(0, _translate("Form", "任何优先级", None))
        self.comboBox_3.setItemText(1, _translate("Form", "崩溃", None))
        self.comboBox_3.setItemText(2, _translate("Form", "严重", None))
        self.comboBox_3.setItemText(3, _translate("Form", "主要", None))
        self.comboBox_3.setItemText(4, _translate("Form", "次要", None))
        self.comboBox_3.setItemText(5, _translate("Form", "微小", None))
        self.comboBox.setItemText(0, _translate("Form", "任何用户", None))
        self.btn_find.setText(_translate("Form", "查询", None))
        self.lbl_results.setText(_translate("Form", "TextLabel", None))
        self.btn_prev.setText(_translate("Form", "<", None))
        self.btn_next.setText(_translate("Form", ">", None))
        self.cmb_pages.setItemText(0, _translate("Form", "选择页数", None))

import res_rc

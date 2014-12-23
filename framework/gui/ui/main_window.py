# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Tue Dec 23 15:20:52 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(720, 514)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 370, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 651, 331))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 370, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 370, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menuJIRA = QtGui.QMenu(self.menubar)
        self.menuJIRA.setObjectName(_fromUtf8("menuJIRA"))
        self.menu_S = QtGui.QMenu(self.menubar)
        self.menu_S.setObjectName(_fromUtf8("menu_S"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(30, 30))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_JIRA = QtGui.QAction(MainWindow)
        self.action_JIRA.setCheckable(True)
        self.action_JIRA.setObjectName(_fromUtf8("action_JIRA"))
        self.action_upload = QtGui.QAction(MainWindow)
        self.action_upload.setObjectName(_fromUtf8("action_upload"))
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        self.action_4 = QtGui.QAction(MainWindow)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.action_save = QtGui.QAction(MainWindow)
        self.action_save.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/task/res/inbox-table.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save.setIcon(icon)
        self.action_save.setObjectName(_fromUtf8("action_save"))
        self.menu.addAction(self.action_JIRA)
        self.menu.addAction(self.action_upload)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuJIRA.menuAction())
        self.menubar.addAction(self.menu_S.menuAction())
        self.toolBar.addAction(self.action_save)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.menu.setTitle(_translate("MainWindow", "文件(&F)", None))
        self.menuJIRA.setTitle(_translate("MainWindow", "JIRA(&J)", None))
        self.menu_S.setTitle(_translate("MainWindow", "设置(&S)", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.action_JIRA.setText(_translate("MainWindow", "登录到JIRA", None))
        self.action_upload.setText(_translate("MainWindow", "上传测试结果", None))
        self.action_3.setText(_translate("MainWindow", "保存", None))
        self.action_4.setText(_translate("MainWindow", "退出", None))
        self.action_save.setText(_translate("MainWindow", "save", None))
        self.action_save.setToolTip(_translate("MainWindow", "save", None))

import res_rc

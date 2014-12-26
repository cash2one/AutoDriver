# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/main_window.ui'
#
# Created: Fri Dec 26 16:04:48 2014
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
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/mainicon/res/wp.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setStyleSheet(_fromUtf8(""))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_file = QtGui.QMenu(self.menubar)
        self.menu_file.setStyleSheet(_fromUtf8(""))
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        self.menu_tools = QtGui.QMenu(self.menubar)
        self.menu_tools.setObjectName(_fromUtf8("menu_tools"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setAutoFillBackground(True)
        self.toolBar.setIconSize(QtCore.QSize(30, 30))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menu_save = QtGui.QAction(MainWindow)
        self.menu_save.setObjectName(_fromUtf8("menu_save"))
        self.menu_exit = QtGui.QAction(MainWindow)
        self.menu_exit.setObjectName(_fromUtf8("menu_exit"))
        self.menu_login = QtGui.QAction(MainWindow)
        self.menu_login.setCheckable(False)
        self.menu_login.setObjectName(_fromUtf8("menu_login"))
        self.toolbar_home = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbars/res/home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolbar_home.setIcon(icon1)
        self.toolbar_home.setObjectName(_fromUtf8("toolbar_home"))
        self.toolbar_jira = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbars/res/table.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolbar_jira.setIcon(icon2)
        self.toolbar_jira.setObjectName(_fromUtf8("toolbar_jira"))
        self.menu_inf = QtGui.QAction(MainWindow)
        self.menu_inf.setObjectName(_fromUtf8("menu_inf"))
        self.menu_settings = QtGui.QAction(MainWindow)
        self.menu_settings.setObjectName(_fromUtf8("menu_settings"))
        self.menu_file.addAction(self.menu_login)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_save)
        self.menu_file.addAction(self.menu_exit)
        self.menu_tools.addAction(self.menu_inf)
        self.menu_tools.addSeparator()
        self.menu_tools.addAction(self.menu_settings)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())
        self.toolBar.addAction(self.toolbar_home)
        self.toolBar.addAction(self.toolbar_jira)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Autotest", None))
        self.menu_file.setTitle(_translate("MainWindow", "文件(&F)", None))
        self.menu_tools.setTitle(_translate("MainWindow", "工具(&T)", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.menu_save.setText(_translate("MainWindow", "保存", None))
        self.menu_exit.setText(_translate("MainWindow", "退出", None))
        self.menu_login.setText(_translate("MainWindow", "登录到JIRA", None))
        self.toolbar_home.setText(_translate("MainWindow", "Home", None))
        self.toolbar_jira.setText(_translate("MainWindow", "JIRA", None))
        self.menu_inf.setText(_translate("MainWindow", "接口测试", None))
        self.menu_settings.setText(_translate("MainWindow", "设置", None))

import res_rc

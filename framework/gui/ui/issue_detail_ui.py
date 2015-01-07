# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/issue_detail.ui'
#
# Created: Tue Jan 06 17:11:18 2015
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(780, 580)
        Dialog.setMaximumSize(QtCore.QSize(780, 580))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/mainicon/res/wp.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lbl_project_avastar = QtGui.QLabel(Dialog)
        self.lbl_project_avastar.setMinimumSize(QtCore.QSize(48, 48))
        self.lbl_project_avastar.setMaximumSize(QtCore.QSize(48, 48))
        self.lbl_project_avastar.setStyleSheet(_fromUtf8("background-image: url(:/bg/res/projectavatar.png);"))
        self.lbl_project_avastar.setObjectName(_fromUtf8("lbl_project_avastar"))
        self.horizontalLayout_2.addWidget(self.lbl_project_avastar)
        self.lbl_title = QtGui.QLabel(Dialog)
        self.lbl_title.setMinimumSize(QtCore.QSize(0, 48))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_title.setWordWrap(True)
        self.lbl_title.setMargin(0)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.horizontalLayout_2.addWidget(self.lbl_title)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_detail1 = QtGui.QLabel(Dialog)
        self.lbl_detail1.setObjectName(_fromUtf8("lbl_detail1"))
        self.horizontalLayout.addWidget(self.lbl_detail1)
        self.lbl_detail2 = QtGui.QLabel(Dialog)
        self.lbl_detail2.setObjectName(_fromUtf8("lbl_detail2"))
        self.horizontalLayout.addWidget(self.lbl_detail2)
        self.lbl_detail3 = QtGui.QLabel(Dialog)
        self.lbl_detail3.setObjectName(_fromUtf8("lbl_detail3"))
        self.horizontalLayout.addWidget(self.lbl_detail3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.txt_desc = QtGui.QTextEdit(Dialog)
        self.txt_desc.setObjectName(_fromUtf8("txt_desc"))
        self.verticalLayout.addWidget(self.txt_desc)
        self.web_attachment = QtWebKit.QWebView(Dialog)
        self.web_attachment.setMaximumSize(QtCore.QSize(16777215, 100))
        self.web_attachment.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.web_attachment.setObjectName(_fromUtf8("web_attachment"))
        self.verticalLayout.addWidget(self.web_attachment)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lbl_project_avastar.setText(_translate("Dialog", " ", None))
        self.lbl_title.setText(_translate("Dialog", "TextLabel", None))
        self.lbl_detail1.setText(_translate("Dialog", "TextLabel", None))
        self.lbl_detail2.setText(_translate("Dialog", "TextLabel", None))
        self.lbl_detail3.setText(_translate("Dialog", "TextLabel", None))

from PyQt4 import QtWebKit
import res_rc

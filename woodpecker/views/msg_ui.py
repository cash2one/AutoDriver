# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/msg.ui'
#
# Created: Fri Dec 26 14:28:49 2014
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
        Dialog.resize(404, 207)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 130, 211, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lbl_msg = QtGui.QLabel(Dialog)
        self.lbl_msg.setGeometry(QtCore.QRect(180, 60, 72, 15))
        self.lbl_msg.setObjectName(_fromUtf8("lbl_msg"))
        self.graphicsView = QtGui.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(110, 50, 32, 32))
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setStyleSheet(_fromUtf8("border-image: url(:/formicon/res/alert.png);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "确认", None))
        self.lbl_msg.setText(_translate("Dialog", "TextLabel", None))


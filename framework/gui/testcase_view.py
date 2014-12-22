# coding=utf-8
__author__ = 'Administrator'

import sys
from PyQt4 import QtGui, QtCore, uic


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("hello")
        self.resize(300, 200)

        gridlayout = QtGui.QGridLayout()
        self.button = QtGui.QPushButton("CreateDialog")
        gridlayout.addWidget(self.button)
        self.setLayout(gridlayout)

        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.OnButtoN)

    def OnButtoN(self):
        dialog = Dialog()
        r = dialog.exec_()
        if r:
            self.button.setText(dialog.labela.text())


class Dialog(QtGui.QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        uic.loadUi("pyui.ui", self)

        # def table(self):
        # table = QtGui.QTableWidget()
        #     table.setRowCount(5)
        #     table.setColumnCount(5)
        #     led = QtGui.QLineEdit("Sample")
        #     self.layout.addWidget(led, 0, 0)
        #     self.layout.addWidget(table, 1, 0)
        #
        #     table.setItem(1, 0, QtGui.QTableWidgetItem(led.text()))


app = QtGui.QApplication(sys.argv)
window = Window()
window.show()
app.exec_()
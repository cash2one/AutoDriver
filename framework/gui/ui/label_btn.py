# coding=utf-8
__author__ = 'guguohai@outlook.com'

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class LabelButton(QLabel):
    def __init__(self, parent=None):
        super(LabelButton, self).__init__()
        self.isClicked = False


    def mouseReleaseEvent(self, event):
        # print 'Release:',event.type()
        # if not self.isClicked:
        #     if event.button() == Qt.LeftButton:
        #         self.emit(SIGNAL('clicked()'))
        #         self.isClicked = True
        pass

    def mousePressEvent(self, event):
        # print 'Press:',event.type()
        if event.button() == Qt.LeftButton:
            self.emit(SIGNAL('clicked()'))

    def leaveEvent(self, *args, **kwargs):
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs):
        self.emit(SIGNAL('doubleClicked()'))

    def mouseMoveEvent(self, event):
        # if event.MouseMove == event.type():
        # print event.type()
        pass
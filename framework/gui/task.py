# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from framework.gui.models import tree_model
from framework.gui.ui import select_task


class SelectAutomate(QDialog, select_task.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)

        # self.ui = select_task.Ui_Form()
        # self.ui.setupUi(self)
        self.setupUi(self)

        f = QFile(':/default.txt')
        f.open(QIODevice.ReadOnly)
        model = tree_model.TreeModel(f.readAll())
        f.close()
        self.treeView.setModel(model)


    def confirm(self):
        self.reject()  # 关闭窗口



        # class SelectTask(QDialog):
        # def __init__(self, ui):
        # QDialog.__init__(self)
        # self.ui = ui
        # ui.setupUi(self)
        #
        # f = QFile(':/default.txt')
        # f.open(QIODevice.ReadOnly)
        # model = tree_model.TreeModel(f.readAll())
        # f.close()
        # self.ui.treeView.setModel(model)
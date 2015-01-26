# coding=utf-8
__author__ = 'guguohai@outlook.com'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from woodpecker.models import tree_model
from woodpecker.views import autos_ui


class ScriptsDialog(QDialog, autos_ui.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)

        # self.ui = select_task.Ui_Form()
        # self.ui.setupUi(self)
        self.setupUi(self)

        f = QFile(':/default.txt')
        f.open(QIODevice.ReadOnly)

        print f.readAll()
        model = tree_model.TreeModel(f.readAll())
        f.close()
        self.treeView.setModel(model)


    def confirm(self):
        self.reject()  # 关闭窗口
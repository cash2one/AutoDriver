# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
from PyQt4.QtGui import *
from PyQt4 import QtCore
from framework.gui.views import interface_ui
from framework.gui.models import listview_model
from framework.gui.helpers import param_infr


class InterfaceForm(QWidget, interface_ui.Ui_Form):
    def __init__(self):
        super(InterfaceForm, self).__init__()

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))
        self.tab_inf.setFont(QFont("Microsoft YaHei", 9))
        self.lbl_desc.setFont(QFont("Microsoft YaHei", 9))
        self.txt_result.setFont(QFont("Microsoft YaHei", 9))

        tree_model = listview_model.StampTreeModel()#param_infr.inf, self
        self.tree_infs.setModel(tree_model)

        #self.tree_infs.clicked.connect(self.on_treeView_clicked)


    # @QtCore.pyqtSlot(QtCore.QModelIndex)
    # def on_treeView_clicked(self, index):
    #     print 'selected item index found at %s with data: %s' % (index.row(), index.data().toString())


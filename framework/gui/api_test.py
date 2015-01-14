# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
from PyQt4.QtGui import *
from PyQt4 import QtCore
from framework.gui.views import interface_ui
from framework.gui.models import listview_model
from framework.gui.models import tree_model_apis,tree_model
from framework.util import fs

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class InterfaceForm(QWidget, interface_ui.Ui_Form):
    def __init__(self):
        super(InterfaceForm, self).__init__()

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))
        self.tab_inf.setFont(QFont("Microsoft YaHei", 9))
        self.lbl_desc.setFont(QFont("Microsoft YaHei", 9))
        self.txt_result.setFont(QFont("Microsoft YaHei", 9))


        #tree_model = listview_model.StampTreeModel(param_infr.inf)  # param_infr.inf, self
        #self.tree_infs.clicked.connect(self.itemSelected)
        inf = []
        dirs=PATH('../../resource/api/')
        xml_files=os.listdir(dirs)
        for x in xml_files:
            dicts={}
            dicts['name']=''
            dicts['api'] = fs.read_xml(os.path.join(dirs,x))
            inf.append(dicts)
        print inf

        f = QtCore.QFile(':/default.txt')
        f.open(QtCore.QIODevice.ReadOnly)
        model = tree_model_apis.TreeModel(inf) #param_infr.inf
        self.tree_infs.setModel(model)


        @QtCore.pyqtSlot(QtCore.QModelIndex)
        def itemSelected(self, index):
            print 'selected item index found at %s with data: %s' % (index.row(), index.data().toString())


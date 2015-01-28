# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import json
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.util import fs, const, xls
from framework.core import data
from framework.core import box

from woodpecker.views import testcase_ui

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestCaseForm(QWidget, testcase_ui.Ui_Form):
    def __init__(self):
        super(TestCaseForm, self).__init__()

        self.setupUi(self)

        self.btn_excel.clicked.connect(self.get_filename)

        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.openMenu)

        QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
        # QTextCodec.setCodecForCStrings(QTextCodec.codecForName("UTF-8"))
        self.connect(self.treeView, SIGNAL("clicked(QModelIndex)"), self.getCurrentIndex)
        self.connect(self.cmb_project, SIGNAL("activated(QString)"), self.onActivated)

        xlss = os.listdir(PATH('../resource/xls'))
        for item in xlss:
            file_name = os.path.splitext(item)
            if cmp('.xls', file_name[1]) == 0:
                self.cmb_project.addItem(file_name[0])


    def addItems(self, parent, elements):
        for text, children in elements:
            item = QStandardItem(text)
            parent.appendRow(item)
            if children:
                self.addItems(item, children)


    def openMenu(self, position):
        indexes = self.treeView.selectedIndexes()
        if len(indexes) > 0:

            level = 0
            index = indexes[0]
            while index.parent().isValid():
                index = index.parent()
                level += 1

        menu = QMenu()
        menu.addAction(self.tr("新增"))
        menu.addAction(self.tr("删除"))
        # if level == 0:
        # menu.addAction(self.tr("Edit person"))
        # elif level == 1:
        # menu.addAction(self.tr("Edit object/container"))
        # elif level == 2:
        # menu.addAction(self.tr("Edit object"))

        menu.exec_(self.treeView.viewport().mapToGlobal(position))

    def get_filename(self):
        fd = QFileDialog(self)
        file_path = fd.getOpenFileName()

        # xls_path = '../resource/xls/'
        excel = xls.Excel(file_path, const.EXCEL_HEADER, True)

        if excel.openExcel() != None:
            xls_data = data.getExcelData(excel)
            self.read_xls(xls_data)

    def read_xls(self, xls_data):
        catt = []
        for d in xls_data:
            path_str = d['cat'] + os.sep + d['name']
            catt.append(path_str)

        datas = fs.walk_tree_tuple(catt)

        self.model = QStandardItemModel()
        self.addItems(self.model, datas)
        self.treeView.setModel(self.model)

        self.model.setHorizontalHeaderLabels([self.tr("用例列表")])

    def getCurrentIndex(self, index):
        # print index.internalPointer().itemData[0]
        print 'click tree'

    def onActivated(self, txt):
        xls_file = PATH('../resource/xls/%s.xls' % txt)
        #temps = self.my_import('helpers.%s' % txt)
        excel = xls.Excel(xls_file, const.EXCEL_HEADER, True)
        if excel.openExcel() != None:
            xls_data = data.getExcelData(excel)
            self.read_xls(xls_data)

    def my_import(self, name):
        mod = __import__(name)
        components = name.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod
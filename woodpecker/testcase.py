# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.util import fs
from framework.core import data

from woodpecker.views import testcase_ui

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestCaseForm(QWidget, testcase_ui.Ui_Form):
    def __init__(self):
        super(TestCaseForm, self).__init__()

        self.setupUi(self)
        # cat = [u'订单管理\历史订单\查询成功\查询成功1', u'订单管理\历史订单\查询f成功', u'客户管理\客户投诉\回访', u'客户管理\客户投诉\审核', u'订单管理\待处理订单\查询失败',
        # u'客户管理\客户投诉\审核\结果']
        # print cat
        xls_path = '../resource/xls/'
        xlss = data.getExcelsData(PATH(xls_path), True)
        catt = []
        for xls in xlss:
            path_str = xls['cat'] + os.sep + xls['name']
            catt.append(path_str)

        print catt

        datas = fs.walk_tree_tuple(catt)

        self.model = QStandardItemModel()
        self.addItems(self.model, datas)
        self.treeView.setModel(self.model)
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.openMenu)

        QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
        self.model.setHorizontalHeaderLabels([self.tr("用例列表")])

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
        #     menu.addAction(self.tr("Edit person"))
        # elif level == 1:
        #     menu.addAction(self.tr("Edit object/container"))
        # elif level == 2:
        #     menu.addAction(self.tr("Edit object"))

        menu.exec_(self.treeView.viewport().mapToGlobal(position))
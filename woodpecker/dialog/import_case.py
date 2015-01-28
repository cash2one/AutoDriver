# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from woodpecker.views import import_case_ui
from woodpecker.models import autotest_model
from framework.core import data
from framework.core import task as ta
from framework.util import fs,const,xls


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ImportCaseDialog(QDialog, import_case_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 10))
        self.lbl_tips.setFont(QFont("Microsoft YaHei", 10))
        QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
        self.btn_excel.clicked.connect(self.get_filename)


    def get_filename(self):
        fd = QFileDialog(self)
        file_path = fd.getOpenFileName()

        # xls_path = '../resource/xls/'
        excel = xls.Excel(file_path, const.EXCEL_HEADER, True)

        if excel.openExcel() is not None:
            xls_data = data.getExcelData(excel)
            self.read_xls(xls_data, file_path)

    def addItems(self, parent, elements):
        for text, children in elements:
            item = QStandardItem(text)
            parent.appendRow(item)
            if children:
                self.addItems(item, children)

    def read_xls(self, xls_data, xls_name):
        cat_nodes = fs.walk_tree_tuple(xls_data, xls_name)
        if cat_nodes is not None:
            model = QStandardItemModel()
            self.addItems(model, cat_nodes)
            self.tree.setModel(model)

            model.setHorizontalHeaderLabels([self.tr("用例树")])
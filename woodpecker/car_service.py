# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import json
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.util import fs, const, xls
from framework.core import data
from framework.core import box

from woodpecker.views import car_service_ui
from woodpecker.dialog import import_case

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class CarServiceDialog(QDialog, car_service_ui.Ui_Dialog):
    def __init__(self):
        super(CarServiceDialog, self).__init__()

        self.setupUi(self)

        QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
        self.btn_select_file.clicked.connect(self.get_filename)

        self.webView.setMinimumWidth(450 + 15)

        webv_width = self.webView.width()
        self.txt_scr_width.setText(str(webv_width))

    def get_filename(self):
        fd = QFileDialog(self)
        file_path = fd.getOpenFileName()

        self.txt_file.setText(file_path)
        ff = file_path.split(os.sep)[-1]

        nodes = self.parse_json(file_path)['children']
        cat_nodes = []
        for nd in nodes:
            nds = (str(nd['id']), [])

            nd_child = nd['children']
            for child in nd_child:
                nds[1].append((str(child['id']), []))
            cat_nodes.append(nds)

        model = QStandardItemModel()
        self.addItems(model, cat_nodes)
        self.tree.setModel(model)
        self.connect(self.tree.selectionModel(), SIGNAL("selectionChanged(QItemSelection, QItemSelection)"),
                     self.getCurrentIndex)
        # self.connect(self.tree, SIGNAL("clicked(const QModelIndex&)"), self.getCurrentIndex1)
        model.setHorizontalHeaderLabels([self.tr("说明书")])


    def addItems(self, parent, elements):
        for text, children in elements:
            item = QStandardItem(text)
            parent.appendRow(item)
            if children:
                self.addItems(item, children)

    def getCurrentIndex1(self, index):
        # print index.model()
        m = index.model()

        for a in m:
            print a


    @pyqtSlot("QItemSelection, QItemSelection")
    def getCurrentIndex(self, selected, deselected):
        print selected
        print deselected


    def parse_json(self, file_path):
        f = open(file_path, 'r')
        all_the_text = ''
        nodes = None
        try:
            all_the_text = f.read()
        except IOError:
            return None
        finally:
            f.close()

        try:
            nodes = json.loads(all_the_text)
        except KeyError:
            return None

        return nodes

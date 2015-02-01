# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import json
import zipfile
import shutil
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from woodpecker.views import car_service_ui

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class CarServiceDialog(QDialog, car_service_ui.Ui_Dialog):
    def __init__(self):
        super(CarServiceDialog, self).__init__()

        self.setupUi(self)

        QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
        self.btn_select_file.clicked.connect(self.get_filename)
        self.btn_del_file.clicked.connect(self.del_file)

        self.webView.setMinimumWidth(450 + 15)

        webv_width = self.webView.width()
        self.txt_scr_width.setText(str(webv_width))
        self.find_car_file()

    def find_car_file(self):
        f = PATH('../../temporary/k211_91')
        if os.path.exists(f):
            self.lbl_file_path.setText(f)
            self.txt_file.hide()
            self.btn_select_file.hide()
        else:
            self.lbl_file_path.hide()
            self.btn_del_file.hide()

    def del_file(self):
        f = PATH('../../temporary/k211_91')
        if os.path.exists(f):
            shutil.rmtree(f)

        self.lbl_file_path.hide()
        self.btn_del_file.hide()
        self.txt_file.show()
        self.btn_select_file.show()


    def get_filename(self):
        fd = QFileDialog(self)
        file_path = fd.getOpenFileName()

        self.txt_file.setText(file_path)
        # ff = file_path.split(os.sep)[-1]
        dir_json = self.unzip_file(file_path)

        nodes = self.parse_json(dir_json)['children']
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
        # print selected
        # print deselected
        items = selected.indexes()
        for index in items:
            # text = QString("(%1,%2)").arg(index.row()).arg(index.column())
            # model.setData(index, text)
            print index.row(), index.column()

        itts = deselected.indexes()
        for it in itts:
            print it.row(), it.column()

            # indexes = self.tree.selectionModel().selectedIndexes()
            # #QModelIndex index;
            # for index in indexes:
            # text = QString("(%1,%2)").arg(index.row()).arg(index.column())
            # #model.setData(index, text)
            # print text

    def unzip_file(self, zipfilename):
        unziptodir = PATH('../../temporary')
        if not os.path.exists(unziptodir):
            os.mkdir(unziptodir, 0777)

        dir_json = ''

        zfobj = zipfile.ZipFile(str(zipfilename))
        for name in zfobj.namelist():
            name = name.replace('\\', '/')
            if 'dir.json' in name:
                dir_json = name

            if name.endswith('/'):
                os.mkdir(os.path.join(unziptodir, name))
            else:
                ext_filename = os.path.join(unziptodir, name)
                outfile = open(ext_filename, 'wb')
                outfile.write(zfobj.read(name))
                outfile.close()

        self.txt_file.hide()
        self.btn_select_file.hide()
        self.lbl_file_path.setText(PATH('../../temporary/'))
        self.lbl_file_path.show()
        self.btn_del_file.show()
        return PATH('../../temporary/' + dir_json)

    def parse_json(self, file_path):
        print 'parse_json'
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

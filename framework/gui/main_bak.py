# coding=utf-8
__author__ = 'Administrator'

import os
import sys
import re
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from framework.woodpecker.ui import main_form
from framework.woodpecker.models import list_model

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()

        self.ui = main_form.Ui_Form()
        self.ui.setupUi(self)

        self.button = self.ui.pushButton
        self.listview = self.ui.lv_testcase
        self.cmb_project = self.ui.cmbProject
        self.cmb_subproject = self.ui.cmb_subProject
        self.labela = self.ui.labela
        self.show_project()
        # self.connect(self.button, QtCore.SIGNAL('clicked()'), self.OnButton)
        self.cmb_project.activated[str].connect(self.OnActivated)
        self.cmb_subproject.activated[str].connect(self.onSubActivated)


    def show_project(self):
        di = os.listdir(PATH('../../testcase'))
        for d in di:
            self.cmb_project.addItem(d)

    def show_files(self, files):
        re_f = re.compile(".py", re.IGNORECASE)
        f = filter(re_f.search, files)

        model = list_model.MyListModel(f)

        self.listview.setModel(model)
        self.listview.show()


    def OnActivated(self, txt):
        self.cmb_subproject.clear()
        f = os.listdir(PATH('../../testcase/%s' % txt))

        for subf in f:
            if os.path.isdir(PATH('../../testcase/%s/%s' % (txt, subf))):
                self.cmb_subproject.addItem(subf)

        self.show_files(f)

    def onSubActivated(self, txt):
        f = os.listdir(PATH('../../testcase/%s/%s' % (self.cmb_project.currentText(), txt)))
        self.show_files(f)


        # def OnButton(self):
        # f = os.listdir(PATH('../../testcase/AutobookClient/customer'))
        # re_f = re.compile(".py", re.IGNORECASE)
        #     f = filter(re_f.search, f)
        #
        #     model = list_model.MyListModel(f)
        #
        #     self.listview.setModel(model)
        #     self.listview.show()


def show():
    app = QApplication(sys.argv)
    main = MainForm()
    main.show()

    app.exec_()


if __name__ == "__main__":
    show()
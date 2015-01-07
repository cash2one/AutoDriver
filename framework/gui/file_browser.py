# coding=utf-8
__author__ = 'guguohai@outlook.com'

import json
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.gui.ui import file_browser_ui
from framework.gui.base import *
from PyQt4 import QtNetwork

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class FileDialog(QDialog, file_browser_ui.Ui_Dialog):
    def __init__(self, data=None, net_acc=None):
        QDialog.__init__(self)

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))
        self.data = data

        self.show_file(net_acc)

    def show_file(self, acc_method):
        fi = self.data['content'].split('/')[-1]
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )

        p_a = os.path.join(PATH('../../thumbnail/'), fi)
        if not os.path.exists(p_a):
            acc_method(self.data['content'], self.issue_detail_reply)
        else:
            self.load_file()

    # def show_file(self):
    # try:
    # file_ = self.data['thumbnail'].split('/')[-1]
    # png = QPixmap()
    # png.load("../../thumbnail/%s" % file_)
    # self.label.setPixmap(png)
    #     except KeyError:
    #         file_ = self.data['content'].split('/')[-1]
    #         file_path = os.path.join(PATH('../../thumbnail/'), file_)
    #         con = self.read_txt(file_path)
    #         self.label.setText(con)

    def read_txt(self, file_path):
        file_object = open(file_path)
        content = ''
        try:
            content = file_object.read()
        finally:
            file_object.close()

        return content

    def issue_detail_reply(self, reply):
        if reply.error() == reply.NoError:
            # print reply.readAll()
            file_ = self.data['content'].split('/')[-1]
            self._write_file(file_, reply.readAll())

            self.load_file()
        else:
            print reply.error()


    def load_file(self):
        file_ = self.data['content'].split('/')[-1]
        try:
            t = self.data['thumbnail']
            png = QPixmap()
            png.load("../../thumbnail/%s" % file_)
            #self.label.setMaximumWidth(300)
            #self.label.setScaledContents(True)
            if png.width() > 600:
                picSize = QSize(600, 600)
                #//将pixmap缩放成picSize大小然后保存在scaledPixmap中
                #按比例缩放:
                scaledPixmap = png.scaled(picSize, Qt.KeepAspectRatio)
                #不按照比例缩放
                #QPixmap scaledPixmap = png.scaled(picSize)
                self.label.setPixmap(scaledPixmap)
            else:
                self.label.setPixmap(png)

        except KeyError:
            file_path = os.path.join(PATH('../../thumbnail/'), file_)
            con = self.read_txt(file_path)
            self.label.setText(con)

    def _write_file(self, filename, data_reply):
        if os.path.exists(PATH('../../thumbnail/')):
            try:
                output_file = open(os.path.join(PATH('../../thumbnail/'), filename), 'wb')
                output_file.writelines(data_reply)
                output_file.close()
            except IOError:
                print "写文件失败！"

                # try:
                # thum_file = att['thumbnail'].split('/')[-1]
                # label = QLabel()
                # png = QPixmap()
                # png.load("../../thumbnail/%s" % thum_file)
                # label.setPixmap(png)
                # self.attachment_layout.addWidget(label)
                # except KeyError:
                # btn = QPushButton()
                # btn.setText(att['filename'])
                # btn.setMaximumWidth(300)
                # f = att['content'].split('/')[-1]
                #     self.connect(btn, SIGNAL("clicked()"), lambda: self.open_file_browser(f))
                #     # btn.clicked.connect(self.open_web(att['content']))
                #     self.attachment_layout.addWidget(btn)
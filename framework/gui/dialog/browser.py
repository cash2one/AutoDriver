# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

from framework.gui.views import file_browser_ui, label_btn
from framework.core import the


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

TXT = 0
PIC = 1
HTML = 2


class FileDialog(QDialog, file_browser_ui.Ui_Dialog):
    def __init__(self, file_url='', file_type=0, net_acc=None):
        QDialog.__init__(self)

        self.setupUi(self)

        flags = Qt.Dialog
        # flags |= Qt.WindowMinimizeButtonHint
        flags |= Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        # self.setWindowFlags(Qt.Widget)
        self.setSizeGripEnabled(True)

        self.file_url = file_url
        self.file_type = file_type

        self.img_label = None
        self.png = None
        self.origin_png = None

        self.lbl_status = QLabel('Loading...')
        self.lbl_status.setFont(QFont("Microsoft YaHei", 11))
        self.lbl_status.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.v_layout.addWidget(self.lbl_status)

        if file_type != HTML:
            self.file_name = file_url.split('/')[-1]
            self.file_path = os.path.join(PATH(the.jira.folder), self.file_name)
            self.setWindowTitle(u'文件浏览：' + self.file_name)
        else:
            self.file_name = ''
            self.file_path = ''
            self.setWindowTitle(u'测试相关内容浏览')

        self.show_file(net_acc)

    def show_file(self, acc_method):
        # 临时文件夹里没有图片则下载，否则直接读取
        if not os.path.exists(self.file_path):
            acc_method(self.file_url, self.issue_detail_reply)
        else:
            self.load_file()


    def issue_detail_reply(self, reply):
        if reply.error() == reply.NoError:
            if self.file_type == HTML:
                # codec = QTextCodec.codecForName("GBK")
                self.load_file(reply.readAll())

            else:
                self.write_file(reply.readAll())
                self.load_file()
        else:
            print reply.error()

    def resize_image(self, png):
        p_img = png
        if png.width() > self.width():
            picSize = QSize(self.width(), self.width())
            # //将pixmap缩放成picSize大小然后保存在scaledPixmap中
            # 按比例缩放:
            p_img = png.scaled(picSize, Qt.KeepAspectRatio)
            # 不按照比例缩放
            # scaledPixmap = png.scaled(picSize)
            # self.img_label.setPixmap(scaledPixmap)
        # else:
        # self.img_label.setPixmap(png)
        return p_img

    def load_file(self, content=''):
        if self.file_type == PIC:
            self.img_label = label_btn.LabelButton()
            self.img_label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            self.connect(self.img_label, SIGNAL("doubleClicked()"), self.restore_image_event)
            self.origin_png = QPixmap()

            self.origin_png.load(self.file_path)

            # self.label.setScaledContents(True)

            self.png = self.resize_image(self.origin_png)
            self.img_label.setPixmap(self.png)
            self.finish_load()
            self.v_layout.addWidget(self.img_label)
        elif self.file_type == TXT:
            txtEdit = QTextEdit()
            f = open(self.file_path)
            try:
                content = f.read()
                txtEdit.setPlainText(content)
            finally:
                f.close()
            self.finish_load()
            self.v_layout.addWidget(txtEdit)
        elif self.file_type == HTML:
            webview = QWebView()
            self.browser_web(webview, content)
            self.finish_load()
            self.v_layout.addWidget(webview)

    def write_file(self, data_reply):
        folder = PATH(the.jira.folder)
        if not os.path.exists(folder):
            os.mkdir(PATH(folder))

        try:
            output_file = open(self.file_path, 'wb')
            output_file.writelines(data_reply)
            output_file.close()
        except IOError:
            print "写文件失败！"


    def restore_image_event(self):
        if self.png.width() <= self.width():
            # 还原到原来的尺寸
            self.showMaximized()
            self.img_label.setPixmap(self.origin_png)
            self.png = self.origin_png
        else:
            # 缩放到屏幕匹配的尺寸
            picSize = QSize(self.width(), self.width())
            self.png = self.png.scaled(picSize, Qt.KeepAspectRatio)
            self.img_label.setPixmap(self.png)


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
            # self.connect(btn, SIGNAL("clicked()"), lambda: self.open_file_browser(f))
            # # btn.clicked.connect(self.open_web(att['content']))
            # self.attachment_layout.addWidget(btn)

    def finish_load(self):
        self.v_layout.removeWidget(self.lbl_status)
        self.lbl_status.deleteLater()
        self.lbl_status = None


    def browser_web(self, webview, content):
        if '51testing.com' in self.file_url:
            # codec = QTextCodec.codecForName("GBK")
            # webview.setHtml(unicode(codec.toUnicode(content)))
            webview.load(QUrl(self.file_url))
        elif 'zaodula.com' in self.file_url:
            codec = QTextCodec.codecForName("utf-8")
            con = unicode(codec.toUnicode(content))

            start_str = '<!-- Article begin -->'
            end_str = '<!-- Article end -->'
            start_idx = con.find(start_str) + len(start_str)
            end_idx = con.find(end_str)
            get_con = con[start_idx:end_idx]
            webview.setHtml(get_con)
        elif 'testerhome.com' in self.file_url:
            codec = QTextCodec.codecForName("utf-8")
            con = unicode(codec.toUnicode(content))

            start_str = '<div class="body entry-content">'
            end_str = '<div class="excellent">'
            start_idx = con.find(start_str) + len(start_str)
            end_idx = con.find(end_str)
            get_con = con[start_idx:end_idx]
            webview.setHtml(get_con)
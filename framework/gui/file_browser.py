# coding=utf-8
__author__ = 'guguohai@outlook.com'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.gui.ui import file_browser_ui
from framework.gui.base import *
import label_btn

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

jira_folder = PATH(jira.folder)


class FileDialog(QDialog, file_browser_ui.Ui_Dialog):
    def __init__(self, file_url='', isPic=False, net_acc=None):
        QDialog.__init__(self)

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))

        flags = Qt.Dialog
        #flags |= Qt.WindowMinimizeButtonHint
        flags |= Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        #self.setWindowFlags(Qt.Widget)
        self.setSizeGripEnabled (True)

        self.file_url = file_url
        self.file_name = file_url.split('/')[-1]
        self.isPic = isPic

        self.setWindowTitle(u'文件浏览：' + self.file_name)
        self.img_label = None
        self.png = None
        self.origin_png = None

        self.show_file(net_acc)

    def show_file(self, acc_method):
        p_a = os.path.join(jira_folder, self.file_name)
        # 临时文件夹里没有图片则下载，否则直接读取
        if not os.path.exists(p_a):
            acc_method(self.file_url, self.issue_detail_reply)
        else:
            self.load_file(self.file_name)


    def issue_detail_reply(self, reply):
        if reply.error() == reply.NoError:
            self.write_file(self.file_name, reply.readAll())
            self.load_file(self.file_name)
        else:
            print reply.error()

    def restore_image(self, png):
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

    def load_file(self, file_name):
        file_path = os.path.join(jira_folder, file_name)

        if self.isPic:
            self.img_label = label_btn.LabelButton()
            self.img_label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            self.connect(self.img_label, SIGNAL("doubleClicked()"), self.restore_image_event)
            self.origin_png = QPixmap()

            self.origin_png.load(jira.folder + file_name)
            # self.label.setScaledContents(True)

            self.png = self.restore_image(self.origin_png)
            self.img_label.setPixmap(self.png)
            self.v_layout.addWidget(self.img_label)
        else:
            txtEdit = QTextEdit()
            f = open(file_path)
            try:
                content = f.read()
                txtEdit.setPlainText(content)
            finally:
                f.close()
            self.v_layout.addWidget(txtEdit)

    def write_file(self, filename, data_reply):
        if not os.path.exists(jira_folder):
            os.mkdir(jira_folder)

        try:
            output_file = open(os.path.join(jira_folder, filename), 'wb')
            output_file.writelines(data_reply)
            output_file.close()
        except IOError:
            print "写文件失败！"


    def restore_image_event(self):
        if self.png.width() <= self.width():
            self.img_label.setPixmap(self.origin_png)
            self.png = self.origin_png
        else:
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
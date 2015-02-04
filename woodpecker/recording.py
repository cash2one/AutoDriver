# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from woodpecker.views import recording_ui
from framework.adb import element as ele
from framework.adb import utils
from framework.adb import image
from woodpecker.views import label_btn


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class RecordingForm(QWidget, recording_ui.Ui_Form):
    def __init__(self):
        super(RecordingForm, self).__init__()

        self.setupUi(self)
        self.png = None
        self.origin_png = None
        # png = QPixmap()
        # png.load("../../thumbnail/%s" % thum_file)
        # self.label.setPixmap(png)
        self.img_label = None
        self.btn_refresh.clicked.connect(self.screenshot)

    def screenshot(self):
        self.img_label = label_btn.LabelButton()
        self.img_label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        # self.connect(self.img_label, SIGNAL("doubleClicked()"), self.restore_image_event)

        adb = utils.ADB()
        img = image.ImageUtils()
        img.screen_shot()
        print adb.getScreenResolution()

        element = ele.Element()

        png_dir = PATH('../temporary/')

        # 清除原先加载的Label
        for i in reversed(range(0, self.img_layout.count())):
            self.img_layout.itemAt(i).widget().deleteLater()
            self.img_layout.itemAt(i).widget().setParent(None)

        self.origin_png = QPixmap()
        self.origin_png.load(os.path.join(png_dir, 'temp.png'))

        self.png = self.resize_image(self.origin_png)
        self.img_label.setPixmap(self.png)
        self.img_layout.addWidget(self.img_label)

        eles = element.element_tree()
        txt_eles = ''
        for el in eles:
            txt_el = str(el) + '\r\n'
            txt_eles += txt_el

        self.txt_elements.setText(txt_eles)
        self.txt_elements.setMinimumHeight(self.png.height())
        self.txt_elements.setMaximumHeight(self.png.height())

    def resize_image(self, png):
        print png.width(), png.height()
        picSize = QSize(png.width() / 2, png.height() / 2)
        p_img = png.scaled(picSize, Qt.KeepAspectRatio)
        print p_img.width(), p_img.height()
        return p_img

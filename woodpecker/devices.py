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
from framework.adb import keycode
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
        self.btn_menu.clicked.connect(self.action_menu)
        self.btn_home.clicked.connect(self.action_home)
        self.btn_back.clicked.connect(self.action_back)
        self.adb = utils.ADB()
        self.img = image.ImageUtils()
        self.action = utils.Action()
        self.element = ele.Element()

    def screenshot(self):
        self.img_label = label_btn.LabelButton()
        self.img_label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.connect(self.img_label, SIGNAL("my_click"), self.handler_devices)

        self.img.screen_shot()

        png_dir = PATH('../temporary/')

        # 清除原先加载的Label
        for i in reversed(range(0, self.img_layout.count())):
            self.img_layout.itemAt(i).widget().deleteLater()
            self.img_layout.itemAt(i).widget().setParent(None)

        self.origin_png = QPixmap()
        self.origin_png.load(os.path.join(png_dir, 'temp.png'))

        self.png = self.resize_image(self.origin_png)
        self.img_label.setMinimumWidth(self.png.width())
        self.img_label.setMinimumHeight(self.png.height())
        self.img_label.setMaximumWidth(self.png.width())
        self.img_label.setMaximumHeight(self.png.height())
        self.img_layout.addWidget(self.img_label)
        self.img_label.setPixmap(self.png)

        eles = self.element.element_tree()
        txt_eles = ''
        for el in eles:
            txt_el = str(el) + '\r\n'
            txt_eles += txt_el

        self.txt_elements.setText(txt_eles)

    def resize_image(self, png):
        print png.width(), png.height()
        picSize = QSize(png.width() / 2, png.height() / 2)
        p_img = png.scaled(picSize, Qt.KeepAspectRatio)
        return p_img

    def handler_devices(self, event):
        self.action.touchByPos(event.x() * 2, event.y() * 2)
        #self.txt_info.setText(str(event.x() * 2)+','+str(event.y() * 2))
        self.screenshot()

    def action_home(self):
        self.action.sendKeyEvent(keycode.HOME)
        self.screenshot()

    def action_menu(self):
        self.action.sendKeyEvent(keycode.MENU)
        self.screenshot()

    def action_back(self):
        self.action.sendKeyEvent(keycode.BACK)
        self.screenshot()
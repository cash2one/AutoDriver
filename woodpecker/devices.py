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
        self.btn_refresh.clicked.connect(self.screenshot)
        self.btn_connect.clicked.connect(self.connect_device)
        self.btn_menu.clicked.connect(self.action_menu)
        self.btn_home.clicked.connect(self.action_home)
        self.btn_back.clicked.connect(self.action_back)

        self.img_label = label_btn.LabelButton()
        self.img_label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.con_heihgt = self.height() - self.txt_elements.height() - 18
        self.img_label.setMinimumHeight(self.con_heihgt)
        self.img_label.setMaximumHeight(self.con_heihgt)
        self.img_layout.addWidget(self.img_label)


    def connect_device(self):
        ip_addr = self.txt_ip_addr.text()
        self.adb = utils.ADB(str(ip_addr.trimmed()))
        self.img = image.ImageUtils()
        self.action = utils.Action()
        self.element = ele.Element()
        png_width, png_height = self.screenshot()

        screen_width, screen_height = self.adb.getScreenResolution()
        sw = screen_width * 1.0 / png_width
        sh = screen_height * 1.0 / png_height
        self.scale_size = (sw, sh)


    def screenshot(self):
        self.connect(self.img_label, SIGNAL("my_click"), self.handler_devices)

        self.img.screen_shot()

        png_dir = PATH('../temporary/')

        # 清除原先加载的Label
        # for i in reversed(range(0, self.img_layout.count())):
        # self.img_layout.itemAt(i).widget().deleteLater()
        # self.img_layout.itemAt(i).widget().setParent(None)

        self.origin_png = QPixmap()
        self.origin_png.load(os.path.join(png_dir, 'temp.png'))

        self.png = self.resize_image(self.origin_png, self.con_heihgt)
        self.img_label.setPixmap(self.png)
        return self.png.width(), self.png.height()
        # self.img_label.setMinimumWidth(self.png.width())
        # self.img_label.setMinimumHeight(self.png.height())
        # self.img_label.setMaximumWidth(self.png.width())
        # self.img_label.setMaximumHeight(self.png.height())
        # self.img_layout.addWidget(self.img_label)

        # eles = self.element.element_tree()
        # txt_eles = ''
        # for el in eles:
        # txt_el = str(el) + '\r\n'
        # txt_eles += txt_el
        #
        # self.txt_elements.setText(txt_eles)

    def resize_image(self, png, height_):
        picSize = QSize(height_, height_)
        p_img = png.scaled(picSize, Qt.KeepAspectRatio)
        return p_img

    def handler_devices(self, event):
        ss = self.scale_size
        print event.x(), ss[0]
        self.action.touchByPos(event.x() * ss[0], event.y() * ss[1])
        print self.img_label.height(),self.height(),self.txt_elements.height()

    def action_home(self):
        self.action.sendKeyEvent(keycode.HOME)

    def action_menu(self):
        self.action.sendKeyEvent(keycode.MENU)

    def action_back(self):
        self.action.sendKeyEvent(keycode.BACK)

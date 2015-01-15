# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from framework.core import the
from framework.util import const, strs, mysql, fs
from framework.core import ios

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Application(ios.IOS):
    def __init__(self, config):
        super(Application, self).__init__(config)

    def splash(self):
        pass




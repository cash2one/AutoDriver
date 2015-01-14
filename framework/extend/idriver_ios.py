# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from framework.core import the
from framework.util import idriver_const, const, strs, mysql, fs

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Application(WebDriver):
    def __init__(self, config, browser_profile=None, proxy=None, keep_alive=False):
        self.config = fs.parserConfig(PATH('../../resource/app/%s' % config))
        self.settings = self.config['settings']

        desired_caps = {
            'deviceName': self.settings['device_name'],
            'platformName': self.settings['platform_name'],  # 'iOS',
            'app': PATH('../../resource/app/' + self.settings['app']),
        }
        command_executor = 'http://localhost:%s/wd/hub' % self.settings['remote_port']
        super(Application, self).__init__(command_executor, desired_caps, browser_profile, proxy, keep_alive)

    def splash(self):
        pass


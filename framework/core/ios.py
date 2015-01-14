# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from framework.util import idriver_const, strs, mysql, fs

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

TIME_OUT = 100


class IOS(WebDriver):
    def __init__(self, config):
        self.config = fs.parserConfig(PATH('../../resource/app/%s' % config))
        self.settings = self.config['settings']

        desired_caps = {
            'deviceName': self.settings['device_name'],
            'platformName': self.settings['platform_name'],  # 'iOS',
            'app': PATH('../../resource/app/' + self.settings['app']),
        }

        browser_profile = None
        proxy = None
        keep_alive = False
        command_executor = 'http://localhost:%s/wd/hub' % self.settings['remote_port']

        super(IOS, self).__init__(command_executor, desired_caps, browser_profile, proxy, keep_alive)

    def layouts(self):
        try:
            return self.config[self.current_activity]
        except KeyError:
            raise NameError, 'current_activity error'

    def layout(self, id_):
        try:
            return self.layouts()[id_.lower()]
        except KeyError:
            raise NameError, '%s is not exist' % id_

    def find_id(self, id_):
        pass

    def find_ids(self, id_):
        pass

    def find_tag(self, class_name):
        pass

    def find_tags(self, class_name):
        pass

    def find_name(self, name_):
        pass

    def switch_to_home(self):
        '''
        切换到主界面
        '''
        pass

    def splash(self):
        pass

    def login(self, robot_name=''):
        pass

    def wait_loading(self):
        pass

    def wait_find_id(self, id_):
        '''
        等待动态控件的id 出现
        '''
        pass

    def wait_find_id_text(self, id_, txt):
        pass
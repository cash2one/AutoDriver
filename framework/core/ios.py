# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
from appium.webdriver.webdriver import WebDriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
import element

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

TIME_OUT = 100


class IOS(WebDriver):
    def __init__(self, config):
        self.config = config  # fs.parserConfig(PATH('../../resource/app/%s' % config))
        self.settings = self.config['settings']

        desired_caps = {
            'deviceName': self.settings['device_name'],
            'platformName': self.settings['platform_name'],  # 'iOS',
            'platformVersion':self.settings['platform_version'],
            'app': PATH('../../resource/app/' + self.settings['app']),

            # 'bundleId': 'umeng.SocialDemo',
            # 'udid': 'a9fff175c8746c64907612c7329bc33a95ff97e8',
        }

        browser_profile = None
        proxy = None
        keep_alive = False
        command_executor = 'http://localhost:%s/wd/hub' % self.settings['remote_port']

        super(IOS, self).__init__(command_executor, desired_caps, browser_profile, proxy, keep_alive)

    @property
    def NoSuchElementException(self):
        return exceptions.NoSuchElementException()

    def create_web_element(self, element_id):
        return element.WebElement(self, element_id)

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
        p_id = self.package + self.layout(id_)
        return self.find_element(by=By.ID, value=p_id)

    def find_ids(self, id_):
        p_id = self.package + self.layout(id_)
        return self.find_elements(by=By.ID, value=p_id)

    def find_class(self, name):
        name_ = name
        if not 'android.widget.' in name:
            name_ = 'android.widget.' + name
        return self.find_element(by=By.CLASS_NAME, value=name_)

    def find_classes(self, name):
        name_ = name
        if not 'android.widget.' in name:
            name_ = 'android.widget.' + name
        return self.find_elements(by=By.CLASS_NAME, value=name_)

    def find_name(self, name):
        return self.find_element(by=By.NAME, value=name)

    def find_names(self, name):
        return self.find_elements(by=By.NAME, value=name)


    def switch_to_home(self):
        pass

    def splash(self):
        pass

    def login(self, robot_name=''):
        pass

    def wait_switch(self, origin_activity):
        '''
        等待界面切换完成
        '''
        pass

    def wait_loading(self):
        '''
        等待界面上的loading加载完毕
        有的界面切换完成后，还有loading加载
        '''
        pass


    def wait_find_id(self, id_):
        pass

    def wait_find_id_text(self, id_, txt):
        pass

    def clear_text(self, id_):
        pass
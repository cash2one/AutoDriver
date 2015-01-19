# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
from appium.webdriver.webdriver import WebDriver
from selenium.common import exceptions

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

TIME_OUT = 100


class Android(WebDriver):
    def __init__(self, config):
        self.config = config  # fs.parserConfig(PATH('../../resource/app/%s' % config))
        self.settings = self.config['settings']
        self.api = self.config['api']
        self.api_token = ''

        desired_capabilities = {}
        desired_capabilities['platformName'] = self.settings['platform_name']
        desired_capabilities['platformVersion'] = self.settings['platform_version']
        desired_capabilities['deviceName'] = self.settings['device_name']
        desired_capabilities['app'] = PATH('../../resource/app/' + self.settings['app'])
        desired_capabilities['appPackage'] = self.settings['app_package']
        desired_capabilities['app-activity'] = self.settings['app_activity']
        command_executor = 'http://localhost:%s/wd/hub' % self.settings['remote_port']

        browser_profile = None
        proxy = None
        keep_alive = False

        super(Android, self).__init__(command_executor, desired_capabilities, browser_profile, proxy, keep_alive)

        self.package = self.settings['app_package'] + ':id/'
        self.pkg = self.settings['app_package'] + ':id/'

    @property
    def NoSuchElementException(self):
        return exceptions.NoSuchElementException()

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
        id = self.layout(id_)
        return self.find_element_by_id(self.package + id)

    def find_ids(self, id_):
        id = self.layout(id_)
        return self.find_elements_by_id(self.package + id)

    def find_tag(self, class_name):
        return self.find_element_by_class_name('android.widget.' + class_name)

    def find_tags(self, class_name):
        return self.find_elements_by_class_name('android.widget.' + class_name)

    def find_name(self, name_):
        return self.find_element_by_name(name_)

    def switch_to_home(self):
        '''
        切换到主界面
        '''
        main_activity = self.settings['main_activity']

        time.sleep(1)
        if not main_activity in self.current_activity:
            time.sleep(1)
            self.keyevent(4)
            if not main_activity in self.current_activity:
                self.switch_to_home()

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
        time_out = TIME_OUT
        while time_out > 0:
            try:
                return self.find_id(id_)
            except NoSuchElementException:
                pass

            time_out -= 1
            time.sleep(0.5)
        else:
            raise NameError, 'find_element timeout'

    def wait_find_id_text(self, id_, txt):
        time_out = TIME_OUT
        while time_out > 0:
            try:
                if txt in self.find_id(id_).text:
                    return self.find_id(self.package + id_)
            except NoSuchElementException:
                pass

            time_out -= 1
            time.sleep(0.5)
        else:
            raise NameError, 'find_element timeout'
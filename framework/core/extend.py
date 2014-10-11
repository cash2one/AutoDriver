# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
from framework.util import fs
from framework.core import the
from appium import webdriver as am
from selenium.common.exceptions import NoSuchElementException

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

res = '../../resource/'
#configs = fs.readConfigs(PATH(res+'config.ini'),'android')

class Android(object):
    def __init__(self):
        if the.android == None:
            desired_caps = {}
            desired_caps['platformName'] = self.configs('android','platform_name')
            desired_caps['platformVersion'] = self.configs('android','platform_version')
            desired_caps['deviceName'] = self.configs('android','device_name')
            desired_caps['app'] = PATH(res+self.configs('android','app'))
            desired_caps['appPackage'] = self.configs('android','app_package')
            desired_caps['app-activity'] = self.configs('android','app_activity')
            the.android = am.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.driver = the.android
        self.package = self.configs('android','app_package')+':id/'


    def configs(self,selections,option):
        return the.settings[selections][option]

    def find_id(self,id):
        return self.driver.find_element_by_id(self.package+id)

    def find_ids(self,id):
        return self.driver.find_elements_by_id(self.package+id)

    def find_tag(self,clazz):
        return self.driver.find_element_by_class_name('android.widget.'+clazz)

    def find_tags(self,clazz):
        return self.driver.find_elements_by_tag_name('android.widget.'+clazz)

    def aa(self):
        pass

    #self.driver.start_activity()

    def switch_to_home(self):
        main_acitivity = self.configs('android','main_acitivity')

        time.sleep(1)
        if not main_acitivity in self.driver.current_activity:
            time.sleep(1)
            self.driver.keyevent(4)
            if not main_acitivity in self.driver.current_activity:
                self.switch_to_home()

    def getConfigs(self):
        pass

    def getMainActivity(self):
        main_activity = self.configs('android','main_acitivity')

        isExist = False

        while not isExist:
            if main_activity in self.driver.current_activity:
                isExist = True

        time.sleep(1)
        return main_activity

    def current_activity(self):
        return self.driver.current_activity

    def login(self,login_config):
        login = self.configs('android','login_acitivity')
        main = self.configs('android','main_acitivity')
        usr_name = self.configs(login_config,'user_name')
        usr_pwd = self.configs(login_config,'user_pwd')
        et_username = self.configs(login_config,'user_name_edittext')
        et_password = self.configs(login_config,'user_pwd_edittext')
        bt_login = self.configs(login_config,'user_login_button')

        isFinishSplash = False
        while not isFinishSplash:
            if login in self.driver.current_activity:
                isFinishSplash = True
            if main in self.driver.current_activity:
                isFinishSplash = True
        else:
            time.sleep(2)
            #在main界面没有登录控件id
            try:
                self.find_id(et_username).send_keys(usr_name)
                self.find_id(et_password).send_keys(usr_pwd)
                self.find_id(bt_login).click()
            except NoSuchElementException:
                pass

        time.sleep(1)

        self.switch_finish(login)


    def switch_finish(self,current_activity):
        '''
        Activity切换完成
        :return:
        '''

        isChanged = False
        while not isChanged:
            c_activity = self.current_activity()
            if c_activity.find('.')==0 and len(c_activity)>4:#判断当前Activity获取正确
                if current_activity not in c_activity:
                    isChanged = True

        time.sleep(1)


        # isChanged = False
        #
        # isActivity = False
        # origin_activity = ''
        # while not isActivity:
        #     origin_activity = self.driver.current_activity
        #     if origin_activity.find('.')==0 and len(origin_activity)>4:
        #         isActivity = True
        #         origin_activity = self.driver.current_activity
        #
        # while not isChanged:
        #     if origin_activity not in self.driver.current_activity:
        #         print origin_activity,'ffffffff'
        #         print self.driver.current_activity
        #         isChanged = True
        #
        # time.sleep(1)



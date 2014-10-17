# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
from framework.util import mysql
import the
from appium import webdriver as am
from selenium.common.exceptions import NoSuchElementException

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Android(object):
    def __init__(self,app_ini):
        self.configs= the.project_settings[app_ini]
        if the.android == None:
            desired_caps = {}
            desired_caps['platformName'] = self.configs['platform_name']
            desired_caps['platformVersion'] = self.configs['platform_version']
            desired_caps['deviceName'] = self.configs['device_name']
            desired_caps['app'] = PATH('../../resource/'+self.configs['app'])
            desired_caps['appPackage'] = self.configs['app_package']
            desired_caps['app-activity'] = self.configs['app_activity']
            am_port = self.configs['remote_port']
            the.android = am.Remote('http://localhost:%s/wd/hub' % am_port, desired_caps)

        self.driver = the.android
        self.package = self.configs['app_package']+':id/'

    def find_id(self,id):
        return self.driver.find_element_by_id(self.package+id)

    def find_ids(self,id):
        return self.driver.find_elements_by_id(self.package+id)

    def find_tag(self,clazz):
        return self.driver.find_element_by_class_name('android.widget.'+clazz)

    def find_tags(self,clazz):
        return self.driver.find_elements_by_tag_name('android.widget.'+clazz)

    def sql(self,sql,size=0):
        '''
        mysql 查询，size大于1时查询多条记录
        :param sql:
        :param size:
        :return:
        '''
        db_host = self.configs['db_host']
        db_user = self.configs['db_user']
        db_pwd = self.configs['db_pwd']
        dbm = mysql.DBManager(db_host,db_user,db_pwd,self.configs['db_name'])

        r = None

        cu = dbm.get_cursor()
        cu.execute(sql)
        if size == 0:
            r = cu.fetchone()
        elif size >= 1:
            r = cu.fetchall()
        else:
            print u'error'

        cu.close()
        dbm.close_db()
        return r

    def switch_to_home(self):
        main_activity = self.configs['main_activity']

        time.sleep(1)
        if not main_activity in self.driver.current_activity:
            time.sleep(1)
            self.driver.keyevent(4)
            if not main_activity in self.driver.current_activity:
                self.switch_to_home()

    def getConfigs(self):
        pass

    def getMainActivity(self):
        main_activity = self.configs['main_activity']

        isExist = False

        while not isExist:
            if main_activity in self.driver.current_activity:
                isExist = True

        time.sleep(1)
        return main_activity

    def current_activity(self):
        return self.driver.current_activity

    def login(self):
        login = self.configs['login_activity']
        main = self.configs['main_activity']
        usr_name = self.configs['user_name']
        usr_pwd = self.configs['user_pwd']
        et_username = self.configs['user_name_edittext']
        et_password = self.configs['user_pwd_edittext']
        bt_login = self.configs['user_login_button']

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



class IOS():
    def __init__(self,app_ini):
        self.configs= the.project_settings[app_ini]

    def aa(self):
        pass



class Web():
    def __init__(self,app_ini):
        self.configs= the.project_settings[app_ini]

    def aa(self):
        pass
# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
import subprocess
from framework.util import mysql
import the
from appium import webdriver as am
from selenium.common.exceptions import NoSuchElementException

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
1020:去除current_activity() 方法，改用原来的current_activity属性
'''

class Android(object):
    def __init__(self,app_ini):
        self.configs= the.project_settings[app_ini]

        #if the.android == None:
        if the.devices[app_ini] == None:
            am_port=self.configs['remote_port']
            self.start_appium(am_port)

            desired_caps = {}
            desired_caps['platformName'] = self.configs['platform_name']
            desired_caps['platformVersion'] = self.configs['platform_version']
            desired_caps['deviceName'] = self.configs['device_name']
            desired_caps['app'] = PATH('../../resource/'+self.configs['app'])
            desired_caps['appPackage'] = self.configs['app_package']
            desired_caps['app-activity'] = self.configs['app_activity']

            #the.android = am.Remote('http://localhost:%s/wd/hub' % am_port, desired_caps)

            the.devices[app_ini] = am.Remote('http://localhost:%s/wd/hub' % am_port, desired_caps)

        #self.driver = the.android
        self.driver = the.devices[app_ini]
        self.package = self.configs['app_package']+':id/'

    def getConfigs(self,key):
        return self.configs[key]

    def start_appium(self,port):
        #cmds = os.popen('appium --port %s' % port).readlines()
        p = subprocess.Popen('appium --port %s' % port, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        isFinish = False
        while not isFinish:
            for line in p.stdout.readlines():
                if port in line:
                    isFinish = True
                    break
        time.sleep(1)


    def find_id(self,id):
        return self.driver.find_element_by_id(self.package+id)

    def find_ids(self,id):
        return self.driver.find_elements_by_id(self.package+id)

    def find_tag(self,clazz):
        self.driver.switch_to_alert()
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

    def sharep(self):
        self.driver.setAppPreference('key', 'value')
        value = self.driver.getAppPreference('key')

    def switch_to_home(self):
        main_activity = self.configs['main_activity']

        time.sleep(1)
        if not main_activity in self.current_activity:
            time.sleep(1)
            self.driver.keyevent(4)
            if not main_activity in self.current_activity:
                self.switch_to_home()


    def getMainActivity(self):
        main_activity = self.configs['main_activity']

        isExist = False

        while not isExist:
            if main_activity in self.current_activity:
                isExist = True

        time.sleep(1)
        return main_activity

    @property
    def current_activity(self):
        return self.driver.current_activity
    # def current_activity(self):
    #     return self.current_activity

    @property
    def current_context(self):
        return self.driver.current_context

    def switch_to_window(self,window_name):
        self.driver.switch_to_window(window_name)

    def switch_to_alert(self):
        self.driver.switch_to_alert()

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
            print self.current_activity
            if login in self.current_activity:
                isFinishSplash = True
            if main in self.current_activity:
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

    def switch_wait(self,origin_activity):
        '''
        等待界面切换完成
        :param origin_activity:
        :return:
        '''
        isChanged = False
        while not isChanged:
            c_activity = self.current_activity
            print c_activity
            if c_activity.find('.')==0 and len(c_activity)>4:#判断当前Activity获取正确
                if origin_activity not in c_activity:
                    isChanged = True

        time.sleep(1)

    def switch_finish(self,origin_activity):
        '''
        等待界面切换完成
        :param origin_activity:
        :return:
        '''
        isChanged = False
        while not isChanged:
            c_activity = self.current_activity
            if c_activity.find('.')==0 and len(c_activity)>4:#判断当前Activity获取正确
                if origin_activity not in c_activity:
                    isChanged = True

        time.sleep(1)


        # isChanged = False
        #
        # isActivity = False
        # origin_activity = ''
        # while not isActivity:
        #     origin_activity = self.current_activity
        #     if origin_activity.find('.')==0 and len(origin_activity)>4:
        #         isActivity = True
        #         origin_activity = self.current_activity
        #
        # while not isChanged:
        #     if origin_activity not in self.current_activity:
        #         print origin_activity,'ffffffff'
        #         print self.current_activity
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
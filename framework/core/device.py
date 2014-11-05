# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
import subprocess
from framework.util import mysql
import the
import threading
from selenium import webdriver as selen
import xmlrpclib

from appium import webdriver as am
from appium.webdriver import webdriver as wd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

TIME_OUT = 100

'''
1020:去除current_activity() 方法，改用原来的current_activity属性
'''


class Android(wd.WebDriver):
    def __init__(self, configs, browser_profile=None, proxy=None, keep_alive=False):
        self.configs = configs

        desired_capabilities = {}
        desired_capabilities['platformName'] = self.configs['platform_name']
        desired_capabilities['platformVersion'] = self.configs['platform_version']
        desired_capabilities['deviceName'] = self.configs['device_name']
        desired_capabilities['app'] = PATH('../../resource/' + self.configs['app'])
        desired_capabilities['appPackage'] = self.configs['app_package']
        desired_capabilities['app-activity'] = self.configs['app_activity']
        command_executor = 'http://localhost:%s/wd/hub' % self.configs['remote_port']

        super(Android, self).__init__(command_executor, desired_capabilities, browser_profile, proxy, keep_alive)

        self.package = self.configs['app_package'] + ':id/'

    def find_id(self, id_):
        return self.find_element_by_id(self.package + id_)

    def find_ids(self, id_):
        return self.find_elements_by_id(self.package + id_)

    def find_tag(self, class_name):
        return self.find_element_by_class_name('android.widget.' + class_name)

    def find_tags(self, class_name):
        return self.find_elements_by_class_name('android.widget.' + class_name)

    def clear_text(self, id_):
        txt = self.find_element_by_id(self.package + 'tv_phone').get_attribute('text')
        self.keyevent(123)

        for i in range(0, len(txt)):
            self.keyevent(67)


    def send_new_order(self, user_name):
        '''发送消息，设置为下单action为True，并给出用户名为XX女士。由服务器端修改值。下单机器人获取后，切换到个人信息，
        查看是不是XX女士，如果不是就改名，并下个1人的周边订单
        '''
        xmlrpc_s = the.settings['xmlrpc']
        s = xmlrpclib.ServerProxy('http://%s:%s' % (xmlrpc_s['host'], xmlrpc_s['port']))
        try:
            s.set_customer(True, user_name)
        except xmlrpclib.Fault:
            pass


    def sql(self, sql, size=0):
        '''
        mysql数据查询，size大于0时为查询多条数据
        '''
        dbs = self.configs['database'].split('|')
        # url,usr,pwd,db_name,port
        dbm = mysql.DBManager(dbs[0], dbs[1], dbs[2], dbs[3], int(dbs[4]))

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
        '''
        切换到主界面
        '''
        main_activity = self.configs['main_activity']

        time.sleep(1)
        if not main_activity in self.current_activity:
            time.sleep(1)
            self.keyevent(4)
            if not main_activity in self.current_activity:
                self.switch_to_home()

    def wait_loading(self):
        isLoading = False
        while not isLoading:
            try:
                self.find_element_by_id(self.package + 'progressbar_net_wait')
                #print 'wait ....'
            except NoSuchElementException:
                isLoading = True
        time.sleep(1)


    def wait_find_id(self, id_):
        '''
        等待动态控件的id 出现
        '''
        time_out = TIME_OUT
        while time_out > 0:
            try:
                self.find_element_by_id(self.package + id_)
                isExist = True
            except NoSuchElementException:
                isExist = False

            if isExist:
                return self.find_element_by_id(self.package + id_)

            time_out -= 1
            time.sleep(0.5)
        else:
            raise NameError, 'find_element timeout'

    def wait_find_id_text(self, id_, txt):
        time_out = TIME_OUT
        while time_out > 0:
            try:
                if txt in self.find_element_by_id(self.package + id_).text:
                    return self.find_element_by_id(self.package + id_)
                    # break
            except NoSuchElementException:
                pass

            time_out -= 1
            time.sleep(0.5)
        else:
            raise NameError, 'find_element timeout'

    def wait_switch(self, origin_activity):
        time_out = TIME_OUT
        while time_out > 0:
            if self.current_activity.find('.') == 0 and len(self.current_activity) > 4:
                if origin_activity not in self.current_activity:
                    break
            time_out -= 1
            time.sleep(0.5)
        else:
            raise NameError, 'switch timeout'


firefox = 0
chrome = 1


def app(ini_section, browser=0):
    '''

    :param ini_section:
    :param idx:
    :return:
    '''
    if browser == chrome:
        key_ini = ini_section + '.chrome'
    else:
        key_ini = ini_section

    try:
        the.devices[key_ini]
    except KeyError:
        the.devices[key_ini] = None

    configs = the.project_settings[ini_section]

    # 初始化时，都为None
    if the.devices[key_ini] == None:
        if 'android' in key_ini:
            the.devices[key_ini] = Android(configs)
            # android等待splash界面加载完成
            the.devices[key_ini].wait_switch(configs['app_activity'])

            # if 'web' in ini_section:
            # if browser == firefox:
            #         the.devices[key_ini] = firefox.WebDriver()
            #     elif browser == chrome:
            #         the.devices[key_ini] = Chrome1()

    return the.devices[key_ini]


def execute_sql(configs, sql, size):
    '''
    mysql 查询，size大于1时查询多条记录
    :param sql:
    :param size:
    :return:
    '''

    dbs = configs['database'].split('|')
    # url,usr,pwd,db_name,port
    dbm = mysql.DBManager(dbs[0], dbs[1], dbs[2], dbs[3], int(dbs[4]))

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


class Firefox1(selen.Firefox):
    def __init__(self, firefox_profile=None, firefox_binary=None, timeout=30,
                 capabilities=None, proxy=None):
        super(Firefox1, self).__init__(firefox_profile, firefox_binary, timeout,
                                       capabilities, proxy)


    def find_id(self, id_):
        return selen.Firefox.find_element_by_id(self, id_)

    def find_tag(self, class_name):
        return selen.Firefox.find_element_by_tag_name(self, class_name)

    def find_tags(self, class_name):
        return self.find_elements_by_tag_name(class_name)


class Chrome1(selen.Chrome):
    def __init__(self, executable_path="chromedriver", port=0,
                 chrome_options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None):
        super(Chrome1, self).__init__(executable_path, port,
                                      chrome_options, service_args,
                                      desired_capabilities, service_log_path)
        self.opt = 'Chrome'

    def find_id(self, id_):
        return self.find_element_by_id(id_)

    def find_tag(self, class_name):
        return self.find_element_by_class_name(class_name)

    def find_tags(self, class_name):
        return self.find_elements_by_class_name(class_name)


# def Web(configs):
# def __init__(self, app_ini,browser):
#         if 'firefox' in browser:
#             selen.Chrome()
#             selen.Firefox()
#             self.configs = the.project_settings[app_ini]
#
#     def find_id(self, id_):
#         return self.find_element_by_id(id_)
#
#     def find_ids(self, id_):
#         return self.find_elements_by_id(self.package + id_)
#
#     def find_tag(self, class_name):
#         return self.find_element_by_class_name(class_name)
#
#     def find_tags(self, class_name):
#         return self.find_elements_by_class_name(class_name)


class Runium(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port


    def run(self):
        p1 = subprocess.Popen('appium --port %s' % self.port, stdout=subprocess.PIPE, shell=True)
        #ap = p1.stdout.read()
        #p1.stdout.readline()
        isExistPort = False
        infos = 'server args: {"port":%s}' % self.port
        print infos
        while not isExistPort:
            if infos in p1.stdout.readlines():
                isExistPort = True
                print 'ffffffffffffffffffffffff'
                #time.sleep(2)

# class Android(object):
# def __init__(self,app_ini):
# self.configs= the.project_settings[app_ini]
#
#         #if the.android == None:
#         if the.devices[app_ini] == None:
#             am_port=self.configs['remote_port']
#
#             desired_caps = {}
#             desired_caps['platformName'] = self.configs['platform_name']
#             desired_caps['platformVersion'] = self.configs['platform_version']
#             desired_caps['deviceName'] = self.configs['device_name']
#             desired_caps['app'] = PATH('../../resource/'+self.configs['app'])
#             desired_caps['appPackage'] = self.configs['app_package']
#             desired_caps['app-activity'] = self.configs['app_activity']
#
#             #the.android = am.Remote('http://localhost:%s/wd/hub' % am_port, desired_caps)
#
#             the.devices[app_ini] = am.Remote('http://localhost:%s/wd/hub' % am_port, desired_caps)
#
#         #self.driver = the.android
#         self.driver = the.devices[app_ini]
#         self.package = self.configs['app_package']+':id/'
#         #self.appium_status = False
#         print 'android start.....'
#
#
#
#     def getConfigs(self,key):
#         return self.configs[key]
#
#     # def start_appium(self,port):
#     #     #cmds = os.popen('appium --port %s' % port).readlines()
#     #     #p = subprocess.Popen('ipconfig -all', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     #     p=subprocess.Popen('appium --port %s' % port,stdout=subprocess.PIPE,shell=True)
#     #     out_info = 'Appium REST http interface listener started on 0.0.0.0:%s' % port
#     #     error = "error: Couldn't start Appium REST http interface listener"
#     #     isFinish = False
#     #     while not isFinish:
#     #         if out_info in p.stdout.readline():
#     #             isFinish=True
#     #
#     #     time.sleep(1)
#     #     #print p.pid
#     #     # for line in p.stdout.readlines():
#     #     #     print line
#     #     # isFinish = False
#     #     # while not isFinish:
#     #     #     print 'start ...a'
#     #     #     for line in p.stdout.readlines():
#     #     #         print line
#     #     #         if port in line:
#     #     #             isFinish = True
#     #     #             break
#     #     # time.sleep(1)
#
#
#     def find_id(self,id):
#         return self.driver.find_element_by_id(self.package+id)
#
#     def find_ids(self,id):
#         return self.driver.find_elements_by_id(self.package+id)
#
#     def find_tag(self,clazz):
#         #self.driver.switch_to_alert()
#         return self.driver.find_element_by_class_name('android.widget.'+clazz)
#
#     def find_tags(self,clazz):
#         return self.driver.find_elements_by_tag_name('android.widget.'+clazz)
#
#     def sql(self,sql,size=0):
#         '''
#         mysql 查询，size大于1时查询多条记录
#         :param sql:
#         :param size:
#         :return:
#         '''
#         db_host = self.configs['db_host']
#         db_user = self.configs['db_user']
#         db_pwd = self.configs['db_pwd']
#         dbm = mysql.DBManager(db_host,db_user,db_pwd,self.configs['db_name'])
#
#         r = None
#
#         cu = dbm.get_cursor()
#         cu.execute(sql)
#         if size == 0:
#             r = cu.fetchone()
#         elif size >= 1:
#             r = cu.fetchall()
#         else:
#             print u'error'
#
#         cu.close()
#         dbm.close_db()
#         return r
#
#     def sharep(self):
#         self.driver.setAppPreference('key', 'value')
#         value = self.driver.getAppPreference('key')
#
#     def switch_to_home(self):
#         main_activity = self.configs['main_activity']
#
#         time.sleep(1)
#         if not main_activity in self.current_activity:
#             time.sleep(1)
#             self.driver.keyevent(4)
#             if not main_activity in self.current_activity:
#                 self.switch_to_home()
#
#
#     def getMainActivity(self):
#         main_activity = self.configs['main_activity']
#
#         isExist = False
#
#         while not isExist:
#             if main_activity in self.current_activity:
#                 isExist = True
#
#         time.sleep(1)
#         return main_activity
#
#     @property
#     def current_activity(self):
#         return self.driver.current_activity
#     # def current_activity(self):
#     #     return self.current_activity
#
#     @property
#     def current_context(self):
#         return self.driver.current_context
#
#     def switch_to_window(self,window_name):
#         self.driver.switch_to_window(window_name)
#
#     def switch_to_alert(self):
#         self.driver.switch_to_alert()
#
#     def login(self):
#         login = self.configs['login_activity']
#         main = self.configs['main_activity']
#         usr_name = self.configs['user_name']
#         usr_pwd = self.configs['user_pwd']
#         et_username = self.configs['user_name_edittext']
#         et_password = self.configs['user_pwd_edittext']
#         bt_login = self.configs['user_login_button']
#
#
#         isFinishSplash = False
#         while not isFinishSplash:
#             print self.current_activity
#             if login in self.current_activity:
#                 isFinishSplash = True
#             if main in self.current_activity:
#                 isFinishSplash = True
#
#         else:
#             time.sleep(2)
#             #在main界面没有登录控件id
#
#             try:
#                 self.find_id(et_username).send_keys(usr_name)
#                 self.find_id(et_password).send_keys(usr_pwd)
#                 self.find_id(bt_login).click()
#             except NoSuchElementException:
#                 pass
#
#         time.sleep(1)
#
#         self.switch_finish(login)
#
#     def switch_wait(self,origin_activity):
#         '''
#         等待界面切换完成
#         :param origin_activity:
#         :return:
#         '''
#         isChanged = False
#         while not isChanged:
#             c_activity = self.current_activity
#             print c_activity
#             if c_activity.find('.')==0 and len(c_activity)>4:#判断当前Activity获取正确
#                 if origin_activity not in c_activity:
#                     isChanged = True
#
#         time.sleep(1)
#
#     def switch_finish(self,origin_activity):
#         '''
#         等待界面切换完成
#         :param origin_activity:
#         :return:
#         '''
#         isChanged = False
#         while not isChanged:
#             c_activity = self.current_activity
#             if c_activity.find('.')==0 and len(c_activity)>4:#判断当前Activity获取正确
#                 if origin_activity not in c_activity:
#                     isChanged = True
#
#         time.sleep(1)
#
#
#         # isChanged = False
#         #
#         # isActivity = False
#         # origin_activity = ''
#         # while not isActivity:
#         #     origin_activity = self.current_activity
#         #     if origin_activity.find('.')==0 and len(origin_activity)>4:
#         #         isActivity = True
#         #         origin_activity = self.current_activity
#         #
#         # while not isChanged:
#         #     if origin_activity not in self.current_activity:
#         #         print origin_activity,'ffffffff'
#         #         print self.current_activity
#         #         isChanged = True
#         #
#         # time.sleep(1)





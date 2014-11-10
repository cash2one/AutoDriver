# coding=utf-8
__author__ = 'Administrator'

import os
import re
import time
import the
from framework.util import idriver_const
from framework.util import mysql
from appium import webdriver
import xmlrpclib
from selenium.common.exceptions import NoSuchElementException

TIME_OUT = 100
DRIVER = 'idriver.android.driver'
CUSTOMER = 'idriver.android.customer'
#订单加载loading
ORDER_LOAD = 'order_load'
HISTORY_ORDER_FINISH = 'history_order_finish'
HISTORY_ORDER_CANCLE = 'history_order_cancle'
WORK_STATE = 'tb_work_state'
NET_WAIT='progressbar_net_wait'

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def driver():
    _configs = the.app_configs[DRIVER]
    if the.devices[DRIVER] == None:
        the.devices[DRIVER] = Android(_configs)
        the.devices[DRIVER].wait_switch(_configs['app_activity'])

    return the.devices[DRIVER]

def customer():
    _configs = the.app_configs[CUSTOMER]
    if the.devices[CUSTOMER] == None:
        the.devices[CUSTOMER] = Android(_configs)
        the.devices[CUSTOMER].wait_switch(_configs['app_activity'])

    return the.devices[CUSTOMER]



class Android(webdriver.Remote):
    def __init__(self, configs,browser_profile=None, proxy=None, keep_alive=False):
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
        self.pkg = self.configs['app_package'] + ':id/'


    def find_id(self, id_):
        return self.find_element_by_id(self.package + id_)

    def find_ids(self, id_):
        return self.find_elements_by_id(self.package + id_)

    def find_tag(self, class_name):
        return self.find_element_by_class_name('android.widget.' + class_name)

    def find_tags(self, class_name):
        return self.find_elements_by_class_name('android.widget.' + class_name)

    def find_name(self, name_):
        return self.find_element_by_name(name_)


    def wait_loading(self):
        '''
        如果有loading，等待加载完成
        '''
        isLoading = False
        while not isLoading:
            try:
                self.find_element_by_id(self.package + NET_WAIT)
                # print 'wait ....'
            except NoSuchElementException:
                isLoading = True

    def change_status(self, isWorking):
        try:
            status = the.devices['driver_status']
        except KeyError:
            the.devices['driver_status'] = False

        if the.devices['driver_status'] != isWorking:
            self.find_element_by_id(self.package + WORK_STATE).click()
            the.devices['driver_status'] = isWorking
            self.wait_loading()

    def login(self,robot_name=''):
        if '.driver' in self.configs['app_package']:
            login_driver(self)
        elif '.customer' in self.configs['app_package']:
            login_customer(self,robot_name)

    def swipe_up(self,id_):
        #{'y': 274, 'x': 0}
        #{'width': 720, 'height': 894}
        loc = self.find_element_by_id(self.package + id_).location
        sz = self.find_element_by_id(self.package + id_).size

        start_y = loc['y']+5
        end_y = start_y-5 + sz['height']-5

        self.swipe(5,end_y,5,start_y,500)
        time.sleep(1)


    def swipe_click(self,list_id,item_id,target_id,target_txt,page_size=0):
        '''
        列表滑动，找到匹配的内容后，click
        '''
        while True:
            itemss = self.find_elements_by_id(self.package + item_id)
            for item in itemss:
                if target_txt in item.find_element_by_id(target_id).text:
                    item.click()
                    break
            self.swipe_up(list_id)
            self.wait_find_id(ORDER_LOAD)

    def swipe_load_item(self, list_id, item_id,sub_item_id=(), page_size=1):
        '''
        列表滑动，装载ListView item,[{'id':'id_text'}]
        '''
        datas = []
        while page_size > 0:
            items = self.find_elements_by_id(self.package + item_id)

            for item in items:
                if len(sub_item_id) > 0:
                    sub_dict = {}
                    for sub in sub_item_id:
                        try:
                            sub_txt = item.find_element_by_id(self.package + sub).text
                            sub_dict[sub] = sub_txt
                        except NoSuchElementException:
                            pass
                    if len(sub_dict)>0:
                        datas.append(sub_dict)

            self.swipe_up(list_id)
            #self.wait_find_id(ORDER_LOAD)
            page_size -= 1

        return datas


    def countdown(self):
        '''
        订单倒计时
        :return:
        '''
        while True:
            tv_wait = self.find_element_by_id(self.package + 'tv_wait').text
            if int(tv_wait) <= 0:
                break
            time.sleep(1)

    def location(self,current_location):
        '''
        通过百度地图api获取经纬度
        :param current_location:用户端一键下单内获取所在位置
        :return:
        '''
        import urllib2, json

        ak = '3QaWoBGE8jWtBdIfl56yn582'
        uri = 'http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=%s&callback=showLocation' % (current_location, ak)
        req = urllib2.Request(uri)
        response = urllib2.urlopen(req)
        the_page = response.read()
        a = the_page.split('(')[1].replace(')', '')

        loc = ()
        try:
            j = json.loads(a)
            lat = j['result']['location']['lat']
            lng = j['result']['location']['lng']
            loc += (lng, lat)
        except ValueError:
            pass
        except KeyError:
            pass

        return loc

    def request_order(self, user_name):
        '''发送消息，设置为下单action为True，并给出用户名为XX女士。由服务器端修改值。下单机器人获取后，切换到个人信息，
        查看是不是XX女士，如果不是就改名，并下个1人的周边订单
        '''
        xmlrpc_s = the.settings['xmlrpc']
        s = xmlrpclib.ServerProxy('http://%s:%s' % (xmlrpc_s['host'], xmlrpc_s['port']))
        try:
            s.set_customer(True, user_name)
        except xmlrpclib.Fault:
            pass

    def enum(self,key,val):
        return idriver_const.idriver_enum[key]['key_' + str(val)]

    @property
    def no(self):
        return self.configs['user_name']#['idriver.android.ium']

    def phone(self):
        return self.configs['contact_phone']#['idriver.android.customer']

    def clear_text(self, id_):
        txt = self.find_element_by_id(self.package + id_).get_attribute('text')
        self.keyevent(123)

        for i in range(0, len(txt)):
            self.keyevent(67)

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

        self.wait_loading()



def add_devices(key, val):
    try:
        status = the.devices[key]
    except KeyError:
        the.devices[key] = val

    return the.devices[key]


def register_user(self_driver, user_name):
    '''
    用户端个人信息注册
    :param self_driver:
    :param user_name:
    :return:
    '''
    pkg = self_driver.package

    main_activity = self_driver.configs['main_activity']
    contact_phone = self_driver.configs['contact_phone']
    # user_name = self_driver.configs['user_name']
    code = self_driver.configs['code']

    self_driver.find_element_by_id(pkg + 'btn_personalcenter').click()
    self_driver.wait_switch(main_activity)

    self_driver.find_elements_by_id(pkg + 'personal_name')[0].click()

    self_driver.wait_switch('.PersonActivity')

    self_driver.find_element_by_id(pkg + 'phonenumber').send_keys(contact_phone)

    read_status = self_driver.find_element_by_id(pkg + 'login_agree').get_attribute('checked')
    if 'true' not in read_status:
        self_driver.find_element_by_id(pkg + 'login_agree').click()

    self_driver.find_element_by_id(pkg + 'next_step').click()
    time.sleep(1)
    self_driver.find_element_by_id(pkg + 'verification_code').send_keys(code)
    self_driver.find_element_by_id(pkg + 'code_submit').click()

    #验证码完成后，会返回到PersonActivity
    self_driver.wait_switch('.MyInfoActivity')

    #方便调试先注释
    # #点击我的信息
    # self_driver.find_ids('personal_name')[0].click()
    # self_driver.wait_switch('.PersonActivity')
    #
    #
    # #txt = self_driver.find_element_by_id(pkg+'personal_user_name').get_attribute('text')
    # #self_driver.clear(txt)
    # self_driver.clear_text('personal_user_name')
    #
    # self_driver.find_element_by_id(pkg+'personal_user_name').send_keys(user_name)
    #
    # #选择性别
    # if 'true' not in self_driver.find_element_by_id(pkg+'personal_man').get_attribute('checked'):
    #     self_driver.find_id('personal_man').click()
    # #点击完成按钮
    # self_driver.find_id('personal_finish').click()
    #
    # self_driver.wait_switch('.MyInfoActivity')
    #方便调试先注释

    #点击附近司机，返回到地图界面
    self_driver.find_element_by_id(pkg + 'button_title_back').click()
    self_driver.wait_switch('.PersonActivity')


def login_customer(self_driver, robot_name=''):
    main = self_driver.configs['main_activity']
    guide_activity = self_driver.configs['guide_activity']
    user_name = self_driver.configs['user_name']

    isFinishSplash = False
    while not isFinishSplash:
        # print self_driver.current_activity
        if guide_activity in self_driver.current_activity:
            isFinishSplash = True
        if main in self_driver.current_activity:
            break
    else:
        time.sleep(2)
        # 在main界面没有登录控件id
        try:
            self_driver.find_element_by_id(self_driver.pkg + 'start_btn').click()
        except NoSuchElementException:
            pass

    time.sleep(1)
    self_driver.wait_switch(guide_activity)

    # 向全局the新增用户端登录状态
    login_status = add_devices('customer_login', False)

    if not login_status:
        register_user(self_driver, user_name)

    #订单机器人发起，发起自定义的用户名，需要修改用户名
    if robot_name != '' and robot_name not in user_name:
        self_driver.switch_to_home()
        register_user(self_driver, robot_name)


def login_driver(self_driver):
    login = self_driver.configs['login_activity']
    main = self_driver.configs['main_activity']
    usr_name = self_driver.configs['user_name']
    usr_pwd = self_driver.configs['user_pwd']

    isFinishSplash = False
    while not isFinishSplash:
        # print self_driver.current_activity
        if login in self_driver.current_activity:
            isFinishSplash = True
        if main in self_driver.current_activity:
            break
            #isFinishSplash = True

    else:
        time.sleep(2)
        # 在main界面没有登录控件id
        try:
            self_driver.find_element_by_id(self_driver.package+'et_username').send_keys(usr_name)
            self_driver.find_element_by_id(self_driver.package+'et_password').send_keys(usr_pwd)
            self_driver.find_element_by_id(self_driver.package+'bt_login').click()
        except NoSuchElementException:
            pass

    time.sleep(1)

    self_driver.wait_switch(login)

# def get_driver_no():
#     return the.project_settings['idriver.android.driver']['user_name']
#
#
# def get_contact_phone():
#     return the.project_settings['idriver.android.customer']['contact_phone']


# def request_order(bol):
#     '''
#     司机端用来通知用户端 发送订单的请求
#     :param host:
#     :param bol:
#     :return:
#     '''
#     host = xmlrpc_host() + ':' + xmlrpc_port()
#     pattern = re.compile("((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
#     match = pattern.match(host)
#     if match:
#         s = xmlrpclib.ServerProxy('http://' + host)
#         try:
#             s.set_customer_action(bol)
#         except xmlrpclib.Fault:
#             pass


# def isHostAddr(value):
#     pattern = re.compile("((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
#     match = pattern.match(value)
#     if match:
#         return True  # match.group()
#     else:
#         return False

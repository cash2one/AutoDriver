# coding=utf-8
__author__ = 'Administrator'

import re
import time
from framework.core import the,device
from framework.util import idriver_const
from framework.util import mysql
import xmlrpclib
from selenium.common.exceptions import NoSuchElementException

TIME_OUT = 100

class Application():
    def __init__(self,apps):
        self.apps = apps
        self.ium = device.container('idriver.android.%s' % apps)

        self.configs = self.ium.configs
        self.package = self.ium.package

        #初始化时先等待splash
        self.wait_switch(self.configs['app_activity'])

    def wait_loading(self):
        '''
        如果有loading，等待加载完成
        '''
        isLoading = False
        while not isLoading:
            try:
                self.ium.find_element_by_id(self.package + 'progressbar_net_wait')
                # print 'wait ....'
            except NoSuchElementException:
                isLoading = True

    def change_status(self, isWorking):
        try:
            status = the.devices['driver_status']
        except KeyError:
            the.devices['driver_status'] = False

        if the.devices['driver_status'] != isWorking:
            self.ium.find_element_by_id(self.package + 'tb_work_state').click()
            the.devices['driver_status'] = isWorking
            self.wait_loading()

    def login(self,robot_name=''):
        if 'driver' in self.apps:
            login_driver(self)
        elif 'customer' in self.apps:
            login_customer(self,robot_name)

    def order_countdown(self):
        while True:
            tv_wait = self.ium.find_element_by_id(self.package + 'tv_wait').text
            if int(tv_wait) <= 0:
                break
            time.sleep(1)

    def get_position(self,current_location):
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

    def enum(self,key,val):
        return idriver_const.idriver_enum[key]['key_' + str(val)]

    def driver_no(self):
        return self.configs['user_name']#['idriver.android.ium']

    def phone(self):
        return self.configs['contact_phone']#['idriver.android.customer']

    def clear_text(self, id_):
        txt = self.ium.find_element_by_id(self.package + id_).get_attribute('text')
        self.ium.keyevent(123)

        for i in range(0, len(txt)):
            self.ium.keyevent(67)

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
        if not main_activity in self.ium.current_activity:
            time.sleep(1)
            self.ium.keyevent(4)
            if not main_activity in self.ium.current_activity:
                self.switch_to_home()

    def wait_find_id(self, id_):
        '''
        等待动态控件的id 出现
        '''
        time_out = TIME_OUT
        while time_out > 0:
            try:
                self.ium.find_element_by_id(self.package + id_)
                isExist = True
            except NoSuchElementException:
                isExist = False

            if isExist:
                return self.ium.find_element_by_id(self.package + id_)

            time_out -= 1
            time.sleep(0.5)
        else:
            raise NameError, 'find_element timeout'

    def wait_find_id_text(self, id_, txt):
        time_out = TIME_OUT
        while time_out > 0:
            try:
                if txt in self.ium.find_element_by_id(self.package + id_).text:
                    return self.ium.find_element_by_id(self.package + id_)
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
            if self.ium.current_activity.find('.') == 0 and len(self.ium.current_activity) > 4:
                if origin_activity not in self.ium.current_activity:
                    break
            time_out -= 1
            time.sleep(0.5)
        else:
            raise NameError, 'switch timeout'

        self.wait_loading()


def changeWork(self_driver, isWorking):
    try:
        status = the.devices['driver_status']
    except KeyError:
        the.devices['driver_status'] = False

    if the.devices['driver_status'] != isWorking:
        self_driver.find_id('tb_work_state').click()
        the.devices['driver_status'] = isWorking
        self_driver.wait_loading()
        # if the.idriver_dict['status'] != isWorking:
        # self_driver.find_id('tb_work_state').click()
        #     the.idriver_dict['status'] = isWorking



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

    self_driver.find_id('btn_personalcenter').click()
    self_driver.wait_switch(main_activity)

    self_driver.find_ids('personal_name')[0].click()

    self_driver.wait_switch('.PersonActivity')

    self_driver.find_id('phonenumber').send_keys(contact_phone)

    read_status = self_driver.find_element_by_id(pkg + 'login_agree').get_attribute('checked')
    if 'true' not in read_status:
        self_driver.find_id('login_agree').click()

    self_driver.find_id('next_step').click()
    time.sleep(1)
    self_driver.find_id('verification_code').send_keys(code)
    self_driver.find_id('code_submit').click()

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
    self_driver.find_id('button_title_back').click()
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
            self_driver.find_id('start_btn').click()
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
        if login in self_driver.ium.current_activity:
            isFinishSplash = True
        if main in self_driver.ium.current_activity:
            break
            #isFinishSplash = True

    else:
        time.sleep(2)
        # 在main界面没有登录控件id
        try:
            self_driver.ium.find_element_by_id(self_driver.package+'et_username').send_keys(usr_name)
            self_driver.ium.find_element_by_id(self_driver.package+'et_password').send_keys(usr_pwd)
            self_driver.ium.find_element_by_id(self_driver.package+'bt_login').click()
        except NoSuchElementException:
            pass

    time.sleep(1)

    self_driver.wait_switch(login)



def license_type(val):
    return idriver_const.idriver_enum['license_types']['key_' + str(val)]

def province(val):
    return idriver_const.idriver_enum['provinces']['key_' + str(val)]

def sex(val):
    return idriver_const.idriver_enum['sex']['key_' + str(val)]

def get_driver_no():
    return the.project_settings['idriver.android.ium']['user_name']


def get_contact_phone():
    return the.project_settings['idriver.android.customer']['contact_phone']


def request_order(bol):
    '''
    司机端用来通知用户端 发送订单的请求
    :param host:
    :param bol:
    :return:
    '''
    host = xmlrpc_host() + ':' + xmlrpc_port()
    pattern = re.compile("((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
    match = pattern.match(host)
    if match:
        s = xmlrpclib.ServerProxy('http://' + host)
        try:
            s.set_customer_action(bol)
        except xmlrpclib.Fault:
            pass


def isHostAddr(value):
    pattern = re.compile("((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
    match = pattern.match(value)
    if match:
        return True  # match.group()
    else:
        return False


def xmlrpc_port():
    return the.settings['xmlrpc']['port']


def xmlrpc_host():
    return the.settings['xmlrpc']['host']


class OrderServer():
    '''
    订单机器人服务器端
    '''

    def __init__(self):
        self.ium_info = {'driver_no': '14009', 'action': False}
        self.customer_info = {'user_name': '', 'action': False}

    def get_driver(self, key):
        try:
            return self.ium_info[key]
        except KeyError:
            pass

    def get_customer(self, key):
        try:
            return self.customer_info[key]
        except KeyError:
            pass

    def set_driver(self, bol, no):
        try:
            self.customer_info['action'] = bol
            self.customer_info['driver_no'] = no
        except KeyError:
            pass

    def set_customer(self, bol, user_name):
        '''
        设置用户端是否下单，并修改用户名为指定名
        :param bol:
        :param user_name:
        :return:
        '''
        try:
            self.customer_info['action'] = bol
            self.customer_info['user_name'] = user_name
        except KeyError:
            pass

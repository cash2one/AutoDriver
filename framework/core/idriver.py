# coding=utf-8
__author__ = 'Administrator'

import re
import time
from framework.core import the
import xmlrpclib
from selenium.common.exceptions import NoSuchElementException

def changeWork(self_driver,isWorking):
    try:
        status = the.devices['driver_status']
    except KeyError:
        the.devices['driver_status'] = False

    if the.devices['driver_status'] != isWorking:
        self_driver.find_id('tb_work_state').click()
        the.devices['driver_status'] = isWorking
    # if the.idriver_dict['status'] != isWorking:
    #     self_driver.find_id('tb_work_state').click()
    #     the.idriver_dict['status'] = isWorking

def add_devices(key,val):
    try:
        status = the.devices[key]
    except KeyError:
        the.devices[key] = val

    return the.devices[key]


def register_user(self_driver,user_name):
    '''
    用户端个人信息注册
    :param self_driver:
    :param user_name:
    :return:
    '''
    pkg = self_driver.package

    main_activity = self_driver.configs['main_activity']
    contact_phone = self_driver.configs['contact_phone']
    #user_name = self_driver.configs['user_name']
    code = self_driver.configs['code']

    self_driver.find_id('btn_personalcenter').click()
    self_driver.wait_switch(main_activity)

    self_driver.find_ids('personal_name')[0].click()

    self_driver.wait_switch('.PersonActivity')

    self_driver.find_id('phonenumber').send_keys(contact_phone)

    read_status = self_driver.find_element_by_id(pkg+'login_agree').get_attribute('checked')
    if 'true' not in read_status:
        self_driver.find_id('login_agree').click()

    self_driver.find_id('next_step').click()
    time.sleep(1)
    self_driver.find_id('verification_code').send_keys(code)
    self_driver.find_id('code_submit').click()

    #验证码完成后，会返回到PersonActivity
    self_driver.wait_switch('.MyInfoActivity')

    #点击我的信息
    self_driver.find_ids('personal_name')[0].click()
    self_driver.wait_switch('.PersonActivity')


    #txt = self_driver.find_element_by_id(pkg+'personal_user_name').get_attribute('text')
    #self_driver.clear(txt)
    self_driver.clear_text('personal_user_name')

    self_driver.find_element_by_id(pkg+'personal_user_name').send_keys(user_name)

    #选择性别
    if 'true' not in self_driver.find_element_by_id(pkg+'personal_man').get_attribute('checked'):
        self_driver.find_id('personal_man').click()
    #点击完成按钮
    self_driver.find_id('personal_finish').click()

    self_driver.wait_switch('.MyInfoActivity')

    #点击附近司机，返回到地图界面
    self_driver.find_id('button_title_back').click()
    self_driver.wait_switch('.PersonActivity')


def login_customer(self_driver,robot_name=''):
    main = self_driver.configs['main_activity']
    guide_activity = self_driver.configs['guide_activity']
    user_name = self_driver.configs['user_name']

    isFinishSplash = False
    while not isFinishSplash:
        #print self_driver.current_activity
        if guide_activity in self_driver.current_activity:
            isFinishSplash = True
        if main in self_driver.current_activity:
            break
    else:
        time.sleep(2)
        #在main界面没有登录控件id
        try:
            self_driver.find_id('start_btn').click()
        except NoSuchElementException:
            pass

    time.sleep(1)
    self_driver.wait_switch(guide_activity)

    #向全局the新增用户端登录状态
    login_status = add_devices('customer_login',False)

    if not login_status:
        register_user(self_driver,user_name)

    #订单机器人发起，发起自定义的用户名，需要修改用户名
    if robot_name!='' and robot_name not in user_name:
        self_driver.switch_to_home()
        register_user(self_driver,robot_name)


def login_driver(self_driver):
    login = self_driver.configs['login_activity']
    main = self_driver.configs['main_activity']
    usr_name = self_driver.configs['user_name']
    usr_pwd = self_driver.configs['user_pwd']

    isFinishSplash = False
    while not isFinishSplash:
        #print self_driver.current_activity
        if login in self_driver.current_activity:
            isFinishSplash = True
        if main in self_driver.current_activity:
            break
            #isFinishSplash = True

    else:
        time.sleep(2)
        #在main界面没有登录控件id
        try:
            self_driver.find_id('et_username').send_keys(usr_name)
            self_driver.find_id('et_password').send_keys(usr_pwd)
            self_driver.find_id('bt_login').click()
        except NoSuchElementException:
            pass

    time.sleep(1)

    self_driver.wait_switch(login)

def get_position(current_location):
    import urllib2,json
    ak = '3QaWoBGE8jWtBdIfl56yn582'
    req = urllib2.Request('http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=%s&callback=showLocation' %(current_location,ak))
    response = urllib2.urlopen(req)
    the_page = response.read()
    a = the_page.split('(')[1].replace(')','')

    # pattern = re.compile('\s*\[\s*\{(.*?)\]/')
    # match = pattern.match(the_page)
    # if match:
    #     print match.group()
    loc = ()
    try:
        j = json.loads(a)
        lat = j['result']['location']['lat']
        lng = j['result']['location']['lng']
        loc += (lng,lat)
    except ValueError:
        pass
    except KeyError:
        pass

    return loc


def license_type(val):
    license_types = {
        'lt_1':u'A1','lt_2':u'A2','lt_3':u'A3','lt_4':u'B1',
        'lt_5':u'B2','lt_6':u'C1','lt_7':u'C2','lt_8':u'C3',
        'lt_9':u'C4','lt_10':u'D','lt_11':u'E','lt_12':u'F',
        'lt_13':u'OT'
        # 'lt_1':u'大型客车','lt_2':u'牵引车','lt_3':u'城市公交车','lt_4':u'中型客车',
        # 'lt_5':u'大型货车','lt_6':u'小型汽车','lt_7':u'小型自动挡汽车','lt_8':u'低速载货汽车',
        # 'lt_9':u'三轮汽车','lt_10':u'普通三轮摩托车','lt_11':u'普通二轮摩托车','lt_12':u'轻便摩托车',
        # 'lt_13':u'其他'
    }
    return license_types['lt_'+str(val)]

def province(val):
    provinces = {
        'p_0':u'全国','p_1':u'北京','p_2':u'天津','p_3':u'上海','p_4':u'重庆',
        'p_5':u'河北','p_6':u'山西','p_7':u'辽宁','p_8':u'吉林','p_9':u'黑龙江',
        'p_10':u'江苏','p_11':u'浙江','p_12':u'安徽','p_13':u'福建','p_14':u'江西',
        'p_15':u'山东','p_16':u'河南','p_17':u'湖北','p_18':u'湖南','p_19':u'广东',
        'p_20':u'海南','p_21':u'四川','p_22':u'贵州','p_23':u'云南','p_24':u'陕西',
        'p_25':u'甘肃','p_26':u'青海','p_27':u'台湾','p_28':u'西藏','p_29':u'广西',
        'p_30':u'内蒙古','p_31':u'宁夏','p_32':u'新疆','p_33':u'香港','p_34':u'澳门'
    }
    return provinces['p_'+str(val)]

def get_driver_no():
    return the.project_settings['idriver.android.driver']['user_name']

def get_contact_phone():
    return the.project_settings['idriver.android.customer']['contact_phone']

def request_order(bol):
    '''
    司机端用来通知用户端 发送订单的请求
    :param host:
    :param bol:
    :return:
    '''
    host = xmlrpc_host()+':'+xmlrpc_port()
    pattern = re.compile("((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
    match = pattern.match(host)
    if match:
        s = xmlrpclib.ServerProxy('http://'+host)
        try:
            s.set_customer_action(bol)
        except xmlrpclib.Fault:
            pass


def isHostAddr(value):
    pattern = re.compile("((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
    match = pattern.match(value)
    if match:
        return True #match.group()
    else:
        return False


def xmlrpc_port():
    return the.settings['xmlrpc']['port']

def xmlrpc_host():
    return the.settings['xmlrpc']['host']

def start_customer(apps):
    app_activity = apps.configs['app_activity']
    guide_activity = apps.configs['guide_activity']

    #splash已经在初始化时加载完成
    apps.find_id('start_btn').click()
    apps.wait_switch(guide_activity)



    #RegisterActivity


class OrderServer():
    '''
    订单机器人服务器端
    '''
    def __init__(self):
        self.driver_info = {'driver_no':'14009','action':False}
        self.customer_info = {'user_name':'','action':False}

    def get_driver(self,key):
        try:
            return self.driver_info[key]
        except KeyError:
            pass

    def get_customer(self,key):
        try:
            return self.customer_info[key]
        except KeyError:
            pass

    def set_driver(self,bol,no):
        try:
            self.customer_info['action'] = bol
            self.customer_info['driver_no'] = no
        except KeyError:
            pass

    def set_customer(self,bol,user_name):
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

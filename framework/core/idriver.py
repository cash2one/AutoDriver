# coding=utf-8
__author__ = 'Administrator'

import re
import time
from framework.core import the
import xmlrpclib

def changeWork(isWorking):
    myself = the.android
    if the.idriver_dict['status'] != isWorking:
        myself.find_element_by_id('cn.com.pathbook.idriver.driver:id/tb_work_state').click()
        the.idriver_dict['status'] = isWorking


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
    return the.project_settings['android.idriver.driver']['user_name']

def get_contact_phone():
    return the.project_settings['android.idriver.customer']['contact_phone']

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
    app_activity = apps.getConfigs('app_activity')
    guide_activity = apps.getConfigs('guide_activity')

    apps.switch_wait(app_activity)
    apps.find_id('start_btn').click()
    apps.switch_wait(guide_activity)

    #RegisterActivity


class OrderServer():
    '''
    订单机器人服务器端
    '''
    def __init__(self):
        self.driver_info = {'driver_no':'14009','action':False}
        self.customer_info = {'user_name':'','action':False,'req':False}

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

    def set_driver_action(self,bol):
        try:
            self.driver_info['action'] = bol
        except KeyError:
            pass

    def set_customer_action(self,bol):
        try:
            self.customer_info['action'] = bol
        except KeyError:
            pass

    def reply(self,bol):
        pass
        # host,port = get_host()
        # s = xmlrpclib.ServerProxy('http://%s:%s' % (host,port))
        # s.set_value('req',True)
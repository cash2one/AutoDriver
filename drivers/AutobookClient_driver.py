# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
import subprocess
import json
import urllib2

from selenium.common.exceptions import NoSuchElementException

import socket
from framework.core import box
from framework.util import strs, mysql
from framework.core import android

TIME_OUT = 100
ORDER_LOAD = 'order_load'
WORK_STATE = 'tb_work_state'
NET_WAIT = 'progressbar_net_wait'
APP_CUSTOMER = 'service/customerService'
APP_DRIVER = 'service/driverService'
APP_COMMON = 'service/commonService'

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Application(android.Android):
    def __init__(self, config):
        super(Application, self).__init__(config)

    def to_datetime(self, str_time):
        return strs.to_datetime(str_time)

    def to_long(self, str_number):
        return strs.to_long(str_number)

    def wait_loading(self):
        '''
        如果有loading，等待加载完成
        '''
        isLoading = False
        while not isLoading:
            try:
                self.find_id(NET_WAIT)
                # print 'wait ....'
            except NoSuchElementException:
                isLoading = True

    def change_status(self, isWorking):
        try:
            status = self.settings['driver_status']
        except KeyError:
            self.settings['driver_status'] = False

        if self.settings['driver_status'] != isWorking:
            self.find_id(WORK_STATE).click()
            self.settings['driver_status'] = isWorking
            self.wait_loading()

    def login(self, robot_name=''):
        login = self.settings['login_activity']
        usr_name = self.settings['user_name']
        usr_pwd = self.settings['user_pwd']

        self.find_id('et_username').send_keys(usr_name)
        self.find_id('et_password').send_keys(usr_pwd)
        self.find_id('bt_login').click()

        self.wait_switch(login)

    def swipe_up(self, id_):
        # {'y': 274, 'x': 0}
        # {'width': 720, 'height': 894}
        loc = self.find_id(id_).location
        sz = self.find_id(id_).size

        start_y = loc['y'] + 5
        end_y = start_y - 5 + sz['height'] - 5

        self.swipe(5, end_y, 5, start_y, 500)
        time.sleep(1)

        # listview 数据载入
        isLoading = False
        while not isLoading:
            try:
                self.find_id(ORDER_LOAD)
            except NoSuchElementException:
                isLoading = True

    def swipee(self, id_):
        ids = self.find_id(id_)
        first_y = ids[0].location['y']
        item_height = ids[0].size['height']

        end_y = first_y + item_height * (len(ids) - 1)
        print len(ids) - 1

        self.swipe(5, end_y, 5, first_y, 500)
        time.sleep(1)
        # listview 数据载入
        isLoading = False
        while not isLoading:
            try:
                self.find_id(ORDER_LOAD)
            except NoSuchElementException:
                isLoading = True


    def swipe_click(self, list_id, item_id, target_id, target_txt, execute_id=''):
        '''
        列表滑动，找到匹配的内容后，click
        '''
        self.find_id(item_id)
        time_out = TIME_OUT + 50
        while time_out > 0:
            items = self.find_id(item_id)
            for item in items:
                if target_txt in item.find_id(target_id).text:
                    if execute_id != '':
                        item.find_id(execute_id).click()
                    else:
                        item.click()
                    break
            self.swipe_up(list_id)
            time_out -= 1
            time.sleep(0.5)

        else:
            raise NameError, 'find_element timeout'

    def swipe_load_item(self, list_id, item_id, sub_items, page_size=1):
        '''
        列表滑动，装载ListView item,[{'id':'id_text'}]
        '''
        datas = ()
        while page_size > 0:
            items = self.find_id(item_id)

            for item in items:
                # if len(sub_item_id) > 0:
                sub_tup = ()

                for sub in sub_items:
                    sub_txt = ''
                    try:
                        sub_txt = item.find_id(sub).text
                        sub_tup += (sub_txt,)
                    except NoSuchElementException:
                        print 'find id fail', sub_txt
                        sub_tup = ()

                if len(sub_tup) > 0 and sub_tup not in datas:
                    datas += (sub_tup,)

            self.swipe_up(list_id)

            page_size -= 1

        return datas


    def countdown(self):
        '''
        订单倒计时
        :return:
        '''
        while True:
            tv_wait = ''
            try:
                tv_wait = self.find_id('tv_wait').text
            except NoSuchElementException:
                break

            if int(tv_wait) <= 0:
                break
            time.sleep(1)

    def location(self, current_location):
        '''
        通过百度地图api获取经纬度
        :param current_location:当前所在的详细中文地址
        :return:lng经度 lat纬度
        '''
        import urllib2, json

        cl = current_location.encode('utf-8')

        ak = '3QaWoBGE8jWtBdIfl56yn582'
        uri = 'http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=%s' % (
            cl, ak)
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

    # def request_order(self, user_name):
    # '''发送消息，设置为下单action为True，并给出用户名为XX女士。由服务器端修改值。下单机器人获取后，切换到个人信息，
    # 查看是不是XX女士，如果不是就改名，并下个1人的周边订单
    # '''
    # xmlrpc_s = the.settings['xmlrpc']
    # s = xmlrpclib.ServerProxy('http://%s:%s' % (xmlrpc_s['host'], xmlrpc_s['port']))
    # try:
    #         s.set_customer(True, user_name)
    #     except xmlrpclib.Fault:
    #         pass

    def exec_api(self, api, arg_dict):
        '''
        执行app子平台的接口
        :param api:例：/service/customerService/createOrderByDrive
        :param arg_dict:字典格式的参数，例{'tokenNo':'','driverNo':''}
        :return:
        '''
        LOGIN_NUM = 0

        status_code = self.api['status_code'].strip().split(',')

        args = arg_dict
        for arg in args:
            if 'tokenNo' in arg:
                args[arg] = self.api_token

        uri = strs.combine_url(self.api['host'], api, args)

        request = urllib2.Request(uri)
        request.add_header('User-Agent', 'Mozilla/5.0')
        request.add_header('Content-type', 'text/html;charset=UTF-8')
        try:
            response = urllib2.urlopen(request, timeout=15)
            read_result = response.read()
            try:
                res = json.loads(read_result)
                #返回值res不包含在错误码中
                if not res['res'] in status_code:
                    #self.save_token(res)  #保存token
                    return res
                else:
                    #令牌号超时失效等返回, 递归调用,调用次数不允许超过3次
                    if LOGIN_NUM <= 3:
                        self.get_token(api, arg_dict)
                        LOGIN_NUM += 1
                        #exec_api(api, arg_dict)
                    else:
                        return None

            except ValueError, e:
                #json解析错误
                #raise NameError, e.message
                return None
        except urllib2.HTTPError, e:
            #http错误
            #raise NameError, e.code
            return None


    def get_token(self, api, arg_dict):
        '''
        调用接口后，返回res为'-2030', '-2031'，则重新登录后，继续调用接口
        :param api:登录接口
        :return:无
        '''
        login_api = self.api['login']
        params = {}

        if APP_CUSTOMER in login_api:
            phone = self.location(self.api['phone'])
            code = self.location(self.api['code'])
            versionNo = self.location(self.api['version_no'])
            params = {'phone': phone, 'code': code, 'versionNo': versionNo}

        if APP_DRIVER in login_api:
            loc = self.location(self.api['location'])
            imsi = self.location(self.api['imsi'])
            versionNo = self.location(self.api['version_no'])
            driverNo = self.location(self.api['driver_no'])
            password = self.location(self.api['password'])
            pmid = self.location(self.api['pmid'])
            params = {'imsi': imsi, 'versionNo': versionNo, 'driverNo': driverNo, 'password': password, 'pmId': pmid,
                      'loginMode': 1, 'lng': loc[0], 'lat': loc[1]}
            self.exec_api(login_api, params)

        if APP_COMMON in login_api:
            pass

        res = self.exec_api(login_api, params)
        if res != None:
            try:
                self.api_token = res['msg']['tokenNo']
                #重新调用接口
                self.exec_api(api, arg_dict)
            except KeyError:
                pass

    def auto_order(self, cmd):
        """
        与其他端通信，发送或者接收订单
        :param cmd:
        :return:
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 7556))

        time.sleep(2)
        sock.send('request_order:%s' % cmd)
        recv_str = sock.recv(1024)
        sock.close()
        return recv_str

    def enum(self, key, val):
        idriver_enum = {
            'province': {
                'key_0': u'全国', 'key_1': u'北京', 'key_2': u'天津', 'key_3': u'上海', 'key_4': u'重庆',
                'key_5': u'河北', 'key_6': u'山西', 'key_7': u'辽宁', 'key_8': u'吉林', 'key_9': u'黑龙江',
                'key_10': u'江苏', 'key_11': u'浙江', 'key_12': u'安徽', 'key_13': u'福建', 'key_14': u'江西',
                'key_15': u'山东', 'key_16': u'河南', 'key_17': u'湖北', 'key_18': u'湖南', 'key_19': u'广东',
                'key_20': u'海南', 'key_21': u'四川', 'key_22': u'贵州', 'key_23': u'云南', 'key_24': u'陕西',
                'key_25': u'甘肃', 'key_26': u'青海', 'key_27': u'台湾', 'key_28': u'西藏', 'key_29': u'广西',
                'key_30': u'内蒙古', 'key_31': u'宁夏', 'key_32': u'新疆', 'key_33': u'香港', 'key_34': u'澳门'
            },
            'sex': {
                'key_0': u'先生', 'key_1': u'女士'
            },
            'license_type': {
                'key_1': u'A1', 'key_2': u'A2', 'key_3': u'A3', 'key_4': u'B1',
                'key_5': u'B2', 'key_6': u'C1', 'key_7': u'C2', 'key_8': u'C3',
                'key_9': u'C4', 'key_10': u'D', 'key_11': u'E', 'key_12': u'F',
                'key_13': u'OT'
            }
        }
        return idriver_enum[key]['key_' + str(val)]

    @property
    def no(self):
        return self.settings['user_name']  # ['idriver.android.ium']

    def phone(self):
        return self.settings['contact_phone']  # ['idriver.android.customer']

    def clear_text(self, id_):
        txt = self.find_id(id_).get_attribute('text')
        self.keyevent(123)

        for i in range(0, len(txt)):
            self.keyevent(67)

    def sql(self, sql, db_no=0, size=0):
        '''
        mysql数据查询，size大于0时为查询多条数据
        '''
        db_array = self.settings['database'].split('|')[db_no]
        dbs = db_array.split(',')

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
        main_activity = self.settings['main_activity']

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
                self.find_id(id_)
                isExist = True
            except NoSuchElementException:
                isExist = False

            if isExist:
                return self.find_id(id_)

            time_out -= 1
            time.sleep(0.5)
        else:
            raise NameError, 'find_element timeout'

    def wait_find_id_text(self, id_, txt):
        time_out = TIME_OUT
        while time_out > 0:
            try:
                if txt in self.find_id(id_).text:
                    return self.find_id(id_)
                    # break
            except NoSuchElementException:
                pass

            time_out -= 1
            time.sleep(0.5)
        else:
            raise NameError, 'find_element timeout'

    def splash(self):
        splash_activity = self.settings['app_activity']  #.SplashActivity
        time_out = TIME_OUT
        while time_out > 0:
            if self.current_activity.find('.') == 0 and len(self.current_activity) > 4:
                if splash_activity not in self.current_activity:
                    break
            time_out -= 1
            time.sleep(0.5)
        else:
            raise NameError, 'switch timeout'
        # time_out = TIME_OUT
        # try:
        #     splash_activity = self.settings['app_activity']
        #     while time_out > 0:
        #         if self.current_activity.find('.') == 0 and len(self.current_activity) > 4:
        #             if splash_activity not in self.current_activity:
        #                 break
        #         time_out -= 1
        #         time.sleep(0.5)
        #     else:
        #         raise NameError, 'switch timeout'
        #
        #     self.wait_loading()
        #
        # except KeyError:
        #     pass  #raise NameError, 'app_activity is not exist'


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
        status = box.devices[key]
    except KeyError:
        box.devices[key] = val

    return box.devices[key]


def register_user(self_driver, user_name):
    '''
    用户端个人信息注册
    :param self_driver:
    :param user_name:
    :return:
    '''
    pkg = self_driver.package

    main_activity = self_driver.settings['main_activity']
    contact_phone = self_driver.settings['contact_phone']
    # user_name = self_driver.configs['user_name']
    code = self_driver.settings['code']

    self_driver.find_id(pkg + 'btn_personalcenter').click()
    self_driver.wait_switch(main_activity)

    self_driver.find_id(pkg + 'personal_name')[0].click()

    self_driver.wait_switch('.PersonActivity')

    self_driver.find_id(pkg + 'phonenumber').send_keys(contact_phone)

    read_status = self_driver.find_id(pkg + 'login_agree').get_attribute('checked')
    if 'true' not in read_status:
        self_driver.find_id(pkg + 'login_agree').click()

    self_driver.find_id(pkg + 'next_step').click()
    time.sleep(1)
    self_driver.find_id(pkg + 'verification_code').send_keys(code)
    self_driver.find_id(pkg + 'code_submit').click()

    # 验证码完成后，会返回到PersonActivity
    self_driver.wait_switch('.MyInfoActivity')

    # 方便调试先注释
    # #点击我的信息
    # self_driver.find_ids('personal_name')[0].click()
    # self_driver.wait_switch('.PersonActivity')
    #
    #
    # #txt = self_driver.find_id(pkg+'personal_user_name').get_attribute('text')
    # #self_driver.clear(txt)
    # self_driver.clear_text('personal_user_name')
    #
    # self_driver.find_id(pkg+'personal_user_name').send_keys(user_name)
    #
    # #选择性别
    # if 'true' not in self_driver.find_id(pkg+'personal_man').get_attribute('checked'):
    # self_driver.find_id('personal_man').click()
    # #点击完成按钮
    # self_driver.find_id('personal_finish').click()
    #
    # self_driver.wait_switch('.MyInfoActivity')
    # 方便调试先注释

    # 点击附近司机，返回到地图界面
    self_driver.find_id(pkg + 'button_title_back').click()
    self_driver.wait_switch('.PersonActivity')


def login_customer(self_driver, robot_name=''):
    main = self_driver.settings['main_activity']
    guide_activity = self_driver.settings['guide_activity']
    user_name = self_driver.settings['user_name']

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
            self_driver.find_id(self_driver.pkg + 'start_btn').click()
        except NoSuchElementException:
            pass

    time.sleep(1)
    self_driver.wait_switch(guide_activity)

    # 向全局the新增用户端登录状态
    login_status = add_devices('customer_login', False)

    if not login_status:
        register_user(self_driver, user_name)

    # 订单机器人发起，发起自定义的用户名，需要修改用户名
    if robot_name != '' and robot_name not in user_name:
        self_driver.switch_to_home()
        register_user(self_driver, robot_name)


def login_driver(self_driver):
    login = self_driver.settings['login_activity']
    main = self_driver.settings['main_activity']
    usr_name = self_driver.settings['user_name']
    usr_pwd = self_driver.settings['user_pwd']

    isFinishSplash = False
    while not isFinishSplash:
        # print self_driver.current_activity
        if login in self_driver.current_activity:
            isFinishSplash = True
        if main in self_driver.current_activity:
            break
            # isFinishSplash = True

    else:
        time.sleep(2)
        # 在main界面没有登录控件id
        try:
            self_driver.find_id(self_driver.package + 'et_username').send_keys(usr_name)
            self_driver.find_id(self_driver.package + 'et_password').send_keys(usr_pwd)
            self_driver.find_id(self_driver.package + 'bt_login').click()
        except:
            pass

    time.sleep(1)

    self_driver.wait_switch(login)


socket_sign = '1'
socket_addr = 'localhost'


def customer_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((socket_addr, 7556))
    sock.listen(5)
    while True:
        connection, address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            if 'request_order:' in buf:
                ss = buf.split('request_order:')[1]
                # if buf == socket_sign:
                # connection.send('welcome to python server!')
                # 执行一个下订单的脚本
                # subprocess.Popen('appium --port %s' % 4723, stdout=subprocess.PIPE, shell=True)
                # cmd = PATH('../src/autobook/android/customer/%s' % py_file)
                p = subprocess.Popen("python %s" % ss, stdout=subprocess.PIPE, shell=True)
                connection.send(p.stdout.read())
        except socket.timeout:
            print 'time out'
        connection.close()


def order_client(cmd):
    """
    与其他端通信，发送或者接收订单
    :param cmd:
    :return:
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 7556))

    time.sleep(2)
    sock.send('request_order:%s' % cmd)
    recv_str = sock.recv(1024)
    sock.close()
    return recv_str


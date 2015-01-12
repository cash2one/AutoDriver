# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn23'

import os
import time
import subprocess
import urllib
import json
import urllib2

from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

import socket
from framework.core import the
from framework.util import idriver_const, const, strs, mysql, fs


TIME_OUT = 100
DRIVER = 'idriver.android.driver'
DRIVER_ROBOT = 'idriver.android.driver_robot'
CUSTOMER = 'idriver.android.customer'
CUSTOMER_ROBOT = 'idriver.android.customer_robot'
# 订单加载loading
ORDER_LOAD = 'order_load'
HISTORY_ORDER_FINISH = 'history_order_finish'
HISTORY_ORDER_CANCLE = 'history_order_cancle'
WORK_STATE = 'tb_work_state'
NET_WAIT = 'progressbar_net_wait'

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# 调用示例self.driver = idriver_android.app(__file__)
def app(current_file):
    # 获取项目路径，转换成app.init 的sections
    # init_size = len(os.path.dirname(__file__))
    init_size = len(PATH('../../testcase')) + 1
    tar_path = os.path.dirname(current_file)
    sections = tar_path[init_size:len(tar_path)].replace(os.sep, '.')

    st = sections.lower()  # .replace('autobook','idriver')
    cfg = the.taskConfig[st]
    if cfg[const.PRODUCT] == None:
        the.taskConfig[st][const.PRODUCT] = Android(cfg[const.TASK_CONFIG])
        the.taskConfig[st][const.PRODUCT].splash()
    return the.taskConfig[st][const.PRODUCT]


# def driver():
# _configs = the.app_configs[DRIVER]
# if the.devices[DRIVER] == None:
# the.devices[DRIVER] = Android(_configs)
# the.devices[DRIVER].wait_switch(_configs['app_activity'])
# return the.devices[DRIVER]
#
#
# def customer():
#     _configs = the.app_configs[CUSTOMER]
#     if the.devices[CUSTOMER] == None:
#         the.devices[CUSTOMER] = Android(_configs)
#         the.devices[CUSTOMER].wait_switch(_configs['app_activity'])
#     return the.devices[CUSTOMER]
#
#
# def driver_robot():
#     _configs = the.app_configs[DRIVER_ROBOT]
#     if the.devices[DRIVER_ROBOT] == None:
#         the.devices[DRIVER_ROBOT] = Android(_configs)
#         the.devices[DRIVER_ROBOT].wait_switch(_configs['app_activity'])
#     return the.devices[DRIVER_ROBOT]
#
#
# def customer_robot():
#     _configs = the.app_configs[CUSTOMER_ROBOT]
#     if the.devices[CUSTOMER_ROBOT] == None:
#         the.devices[CUSTOMER_ROBOT] = Android(_configs)
#         the.devices[CUSTOMER_ROBOT].wait_switch(_configs['app_activity'])
#     return the.devices[CUSTOMER_ROBOT]


class Android(WebDriver):
    def __init__(self, config, browser_profile=None, proxy=None, keep_alive=False):
        cfs = config.strip().split('|')
        self.config = fs.parserConfig(PATH('../../resource/app/%s' % cfs[0]))
        self.settings = self.config['settings']
        #self.app_layouts = fs.parserConfig(PATH('../../resource/app/%s' % self.config['layout']))
        self.api_host = self.settings['api_host']

        desired_capabilities = {}
        desired_capabilities['platformName'] = self.settings['platform_name']
        desired_capabilities['platformVersion'] = self.settings['platform_version']
        desired_capabilities['deviceName'] = self.settings['device_name']
        desired_capabilities['app'] = PATH('../../resource/app/' + self.settings['app'])
        desired_capabilities['appPackage'] = self.settings['app_package']
        desired_capabilities['app-activity'] = self.settings['app_activity']
        command_executor = 'http://localhost:%s/wd/hub' % self.settings['remote_port']

        super(Android, self).__init__(command_executor, desired_capabilities, browser_profile, proxy, keep_alive)

        self.package = self.settings['app_package'] + ':id/'
        self.pkg = self.settings['app_package'] + ':id/'


    def layouts(self):
        #layout_ids = None
        try:
            #layout_ids = self.app_layouts[self.current_activity]
            return self.config[self.current_activity]
        except KeyError:
            raise NameError, 'current_activity error'

    def layout(self, id_):
        try:
            return self.layouts()[id_.lower()]
        except KeyError:
            raise NameError, 'option not exist'

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
            status = self.settings['driver_status']
        except KeyError:
            self.settings['driver_status'] = False

        if self.settings['driver_status'] != isWorking:
            self.find_element_by_id(self.package + WORK_STATE).click()
            self.settings['driver_status'] = isWorking
            self.wait_loading()

    def login(self, robot_name=''):
        if '.driver' in self.settings['app_package']:
            login_driver(self)
        elif '.customer' in self.settings['app_package']:
            login_customer(self, robot_name)

    def swipe_up(self, id_):
        # {'y': 274, 'x': 0}
        #{'width': 720, 'height': 894}
        loc = self.find_element_by_id(self.package + id_).location
        sz = self.find_element_by_id(self.package + id_).size

        start_y = loc['y'] + 5
        end_y = start_y - 5 + sz['height'] - 5

        self.swipe(5, end_y, 5, start_y, 500)
        time.sleep(1)

        #listview 数据载入
        isLoading = False
        while not isLoading:
            try:
                self.find_element_by_id(self.package + ORDER_LOAD)
            except NoSuchElementException:
                isLoading = True

    def swipee(self, id_):
        ids = self.find_elements_by_id(self.package + id_)
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
                self.find_element_by_id(self.package + ORDER_LOAD)
            except NoSuchElementException:
                isLoading = True


    def swipe_click(self, list_id, item_id, target_id, target_txt, execute_id=''):
        '''
        列表滑动，找到匹配的内容后，click
        '''
        self.find_element_by_id(self.package + item_id)
        time_out = TIME_OUT + 50
        while time_out > 0:
            items = self.find_elements_by_id(self.package + item_id)
            for item in items:
                if target_txt in item.find_element_by_id(target_id).text:
                    if execute_id != '':
                        item.find_element_by_id(execute_id).click()
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
            items = self.find_elements_by_id(self.package + item_id)

            for item in items:
                # if len(sub_item_id) > 0:
                sub_tup = ()

                for sub in sub_items:
                    sub_txt = ''
                    try:
                        sub_txt = item.find_element_by_id(self.package + sub).text
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
                tv_wait = self.find_element_by_id(self.package + 'tv_wait').text
            except NoSuchElementException:
                break

            if int(tv_wait) <= 0:
                break
            time.sleep(1)

    def location(self, current_location):
        '''
        通过百度地图api获取经纬度
        :param current_location:用户端一键下单内获取所在位置
        :return:
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
    #     '''发送消息，设置为下单action为True，并给出用户名为XX女士。由服务器端修改值。下单机器人获取后，切换到个人信息，
    #     查看是不是XX女士，如果不是就改名，并下个1人的周边订单
    #     '''
    #     xmlrpc_s = the.settings['xmlrpc']
    #     s = xmlrpclib.ServerProxy('http://%s:%s' % (xmlrpc_s['host'], xmlrpc_s['port']))
    #     try:
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
        uri = strs.combine_url(self.api_host, api, arg_dict)

        request = urllib2.Request(uri)
        request.add_header('User-Agent', 'Mozilla/5.0')
        request.add_header('Content-type', 'text/html;charset=UTF-8')
        try:
            response = urllib2.urlopen(request, timeout=15)
            res = response.read()
            try:
                return json.loads(res)
            except ValueError, e:
                raise NameError, e.message
        except urllib2.HTTPError, e:
            raise NameError, e.code


    # def post(url, data):
    #     req = urllib2.Request(url)
    #     data = urllib.urlencode(data)
    #     #enable cookie
    #     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    #     response = opener.open(req, data)
    #     return response.read()


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
        return idriver_const.idriver_enum[key]['key_' + strs(val)]

    @property
    def no(self):
        return self.settings['user_name']  # ['idriver.android.ium']

    def phone(self):
        return self.settings['contact_phone']  # ['idriver.android.customer']

    def clear_text(self, id_):
        txt = self.find_element_by_id(self.package + id_).get_attribute('text')
        self.keyevent(123)

        for i in range(0, len(txt)):
            self.keyevent(67)

    def sql(self, sql, db_no=0, size=0):
        '''
        mysql数据查询，size大于0时为查询多条数据
        '''
        # db_conf = 'database'
        # if len(db_config.strip()) > 0:
        # db_conf += ('_'+db_config)

        # url,usr,pwd,db_name,port
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

    def splash(self):
        splash_activity = self.settings['app_activity']
        time_out = TIME_OUT
        while time_out > 0:
            if self.current_activity.find('.') == 0 and len(self.current_activity) > 4:
                if splash_activity not in self.current_activity:
                    break
            time_out -= 1
            time.sleep(0.5)
        else:
            raise NameError, 'switch timeout'

        self.wait_loading()

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

    main_activity = self_driver.settings['main_activity']
    contact_phone = self_driver.settings['contact_phone']
    # user_name = self_driver.configs['user_name']
    code = self_driver.settings['code']

    self_driver.find_element_by_id(pkg + 'btn_personal_center').click()
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

    # 验证码完成后，会返回到PersonActivity
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
            self_driver.find_element_by_id(self_driver.pkg + 'start_btn').click()
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
            self_driver.find_element_by_id(self_driver.package + 'et_username').send_keys(usr_name)
            self_driver.find_element_by_id(self_driver.package + 'et_password').send_keys(usr_pwd)
            self_driver.find_element_by_id(self_driver.package + 'bt_login').click()
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
                #if buf == socket_sign:
                #connection.send('welcome to python server!')
                #执行一个下订单的脚本
                #subprocess.Popen('appium --port %s' % 4723, stdout=subprocess.PIPE, shell=True)
                #cmd = PATH('../src/autobook/android/customer/%s' % py_file)
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


# def get_driver_no():
# return the.project_settings['idriver.android.driver']['user_name']
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

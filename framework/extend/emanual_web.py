# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import time

from selenium import webdriver as selen
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common import exceptions

from framework.core import the
from framework.util import const, fs


TIME_OUT = 100
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def firefox(file_):
    # 获取项目路径，转换成app.init 的sections
    init_size = len(os.path.dirname(__file__))
    tar_path = os.path.dirname(file_)
    sections = tar_path[init_size:len(tar_path)].replace(os.sep, '.')

    st = sections.replace('autobook', 'idriver')
    cfg = the.taskConfig[st]
    if cfg[const.PRODUCT] == None:
        #the.products[st][constant.PRODUCT] = Firefox(info)
        the.taskConfig[st][const.PRODUCT] = Firefox(cfg[const.TASK_CONFIG])
        the.taskConfig[st][const.PRODUCT].splash()
    return the.taskConfig[st][const.PRODUCT]


class Firefox(WebDriver):
    def __init__(self, config, timeout=30):
        self.config = fs.parserConfig(PATH('../../resource/app/%s' % config))

        self.settings = self.config['settings']
        self.timeout = timeout
        #self.app_layouts = fs.parserConfig(PATH('../../resource/app/%s' % self.configs['layout']))
        #self.cfg=fs.readConfigs()


        # fp = FirefoxProfile()
        # fp.set_preference("browser.download.folderList",2)
        # fp.set_preference("browser.download.manager.showWhenStarting",False)
        # fp.set_preference("browser.download.dir", os.getcwd())
        # fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        # fp.set_preference("network.cookie.prefsMigrated",True)
        # fp.set_preference("network.cookie.lifetime.days",90)
        # fp.set_preference("network.cookie.lifetimePolicy",0)
        # fp.set_preference("network.cookie.cookieBehavior",0)
        # fp.set_preference("network.cookie.thirdparty.sessionOnly",False)

        # caps=DesiredCapabilities()
        firefox_profile = None
        firefox_binary = None
        capabilities = None
        proxy = None
        super(Firefox, self).__init__(firefox_profile, firefox_binary, timeout,
                                      capabilities, proxy)
    def _get_sections_url(self):
        server_url = self.settings['url']
        return self.current_url.replace(server_url,'')

    def layouts(self):
        # 截取current_url作为ini的selections
        try:
            url = self._get_sections_url()
            return self.config[url]
        except KeyError:
            raise NameError, 'current_url error'

    def layout(self, id_):
        try:
            print self.layouts()
            return self.layouts()[id_.lower()]
        except KeyError:
            raise NameError, 'option not exist'


    def find_id(self, id_):
        id = self.layout(id_)
        return self.find_element_by_id(id)

    def find_ids(self, id_):
        id = self.layout(id_)
        return self.find_elements_by_id(id)

    def find_tag(self, class_name):
        return self.find_element_by_class_name(class_name)

    def find_tags(self, class_name):
        return self.find_elements_by_class_name(class_name)

    def find_name(self, name_):
        return self.find_element_by_name(name_)

    def _index_url(self, value=''):
        index_url = ''
        try:
            index_url = self.settings['index_url']
        except KeyError:
            self.settings['index_url'] = value

        return self.settings['index_url']

    def find_ajax_id(self, id_):
        '''
        系统已有默认等待30秒，这里多加了20秒，防止ajax加载缓慢
        :param id_:
        :return:
        '''
        time_out = self.timeout + 20
        while time_out > 0:
            try:
                return self.find_element_by_id(id_)

            except exceptions.NoSuchElementException:
                pass
            time_out -= 1
            time.sleep(1)

        else:
            raise NameError, 'find_element timeout'

    def splash(self):
        pass

    def switch_to_home(self):
        url = self.settings['index_url']
        time.sleep(2)
        self.get(url)

    def login(self, role=''):
        ini_url = self.settings['url']

        # login_ids = self.config['login_elements'].split(',')
        # usrname_id = login_ids[0]
        # pwd_id = login_ids[1]
        usrname = ''
        pwd = ''
        if len(role.strip()) == 0:
            usrname = self.settings['username']
            pwd = self.settings['password']
        else:
            try:
                role_str = self.settings[role].split(',')
                usrname = role_str[0]
                pwd = role_str[1]
            except KeyError:
                raise NameError, 'account is not exist'

        if cmp('about:blank', self.current_url) == 0:
            self.get(ini_url)

            time.sleep(1)
            temp_url = self.current_url

            self.implicitly_wait(30)

            sections_url = self._get_sections_url()
            cf=self.config[sections_url]

            self.find_element_by_id(cf['username']).send_keys(usrname)
            self.find_element_by_id(cf['password']).send_keys(pwd)

            # 等待输入验证码
            while True:
                #print temp_url,self.current_url
                if cmp(temp_url, self.current_url) == -1:
                    break
                time.sleep(0.5)

            self._index_url(self.current_url)


class Chrome(selen.Chrome):
    def __init__(self, firefox_profile=None, firefox_binary=None, timeout=30,
                 capabilities=None, proxy=None):
        super(Chrome, self).__init__(firefox_profile, firefox_binary, timeout,
                                     capabilities, proxy)
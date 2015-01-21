# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
from selenium.webdriver.common.by import By
import element

TIME_OUT = 100
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Firefox(WebDriver):
    def __init__(self, config, timeout=30):
        self.config = config

        self.settings = self.config['settings']
        self.timeout = timeout

        firefox_profile = None
        firefox_binary = None
        capabilities = None
        proxy = None
        super(Firefox, self).__init__(firefox_profile, firefox_binary, timeout,
                                      capabilities, proxy)


    @property
    def NoSuchElementException(self):
        return exceptions.NoSuchElementException

    def action_chains(self):
        return ActionChains(self)

    def keys(self):
        return Keys()

    def _get_sections_url(self):
        server_url = self.settings['url']
        return self.current_url.replace(server_url, '')

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

    def create_web_element(self, element_id):
        return element.WebElement(self, element_id)

    # def find_id(self, id_):
    # #id = self.layout(id_)
    #     #return self.find_element_by_id(id)
    #     return self.find_element(by=By.ID, value=id_)

    def find_id(self, id):
        #id_ = self.layout(id)
        return self.find_element(by=By.ID, value=id)

    def find_ids(self, id_):
        return self.find_elements(by=By.ID, value=id_)

    def find_tag(self, name):
        return self.find_element(by=By.TAG_NAME, value=name)

    def find_tags(self, name):
        return self.find_elements(by=By.TAG_NAME, value=name)

    def find_class(self, name):
        return self.find_element(by=By.CLASS_NAME, value=name)

    def find_classes(self, name):
        return self.find_elements(by=By.CLASS_NAME, value=name)

    def find_name(self, name):
        return self.find_element(by=By.NAME, value=name)

    def find_names(self, name):
        return self.find_elements(by=By.NAME, value=name)

    def find_link(self, link_text):
        return self.find_element(by=By.LINK_TEXT, value=link_text)

    def find_links(self, link_text):
        return self.find_elements(by=By.LINK_TEXT, value=link_text)

    def find_css(self, css_selector):
        return self.find_element(by=By.CSS_SELECTOR, value=css_selector)

    def find_csses(self, css_selector):
        return self.find_elements(by=By.CSS_SELECTOR, value=css_selector)

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
            cf = self.config[sections_url]

            self.find_element_by_id(cf['username']).send_keys(usrname)
            self.find_element_by_id(cf['password']).send_keys(pwd)

            # 等待输入验证码
            while True:
                # print temp_url,self.current_url
                if cmp(temp_url, self.current_url) == -1:
                    break
                time.sleep(0.5)

            self._index_url(self.current_url)


class Chrome(WebDriver):
    def __init__(self, config, timeout=30):
        self.config = config

        self.settings = self.config['settings']
        self.timeout = timeout

        firefox_profile = None
        firefox_binary = None
        capabilities = None
        proxy = None
        super(Chrome, self).__init__(firefox_profile, firefox_binary, timeout,
                                     capabilities, proxy)

# coding=utf-8
__author__ = 'Administrator'

import os
import re
import time
import the
from framework.util import constant
from selenium import webdriver as selen
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common import exceptions

TIME_OUT = 100

def firefox(file_):
    #获取项目路径，转换成app.init 的sections
    init_size = len(os.path.dirname(__file__))
    tar_path = os.path.dirname(file_)
    sections = tar_path[init_size:len(tar_path)].replace(os.sep,'.')

    st = sections.replace('autobook','idriver')
    info = the.products[st]
    if info[constant.PRODUCT] == None:
        the.products[st][constant.PRODUCT] = Firefox(info)
        the.products[st][constant.PRODUCT].wait_switch(info['app_activity'])
    return the.products[st][constant.PRODUCT]



class Firefox(WebDriver):
    def __init__(self,configs,timeout=30):
        self.configs = configs
        self.timeout=timeout

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

        #caps=DesiredCapabilities()
        firefox_profile=None
        firefox_binary=None
        capabilities=None
        proxy=None
        super(Firefox, self).__init__(firefox_profile, firefox_binary, timeout,
                                      capabilities, proxy)
    def index_url(self,value=''):
        index_url=''
        try:
            index_url = self.configs['index_url']
        except KeyError:
            self.configs['index_url'] = value

        return self.configs['index_url']

    def wait_find_id(self, id_):
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


    def switch_to_home(self):
        url=self.configs['index_url']
        time.sleep(2)
        self.get(url)

    def login(self):
        ini_url = self.configs['url']
        login_ids = self.configs['login_elements'].split(',')
        usrname_id = login_ids[0]
        pwd_id = login_ids[1]
        usrname = self.configs['username']
        pwd = self.configs['password']

        if cmp('about:blank',self.current_url)==0:
            self.get(ini_url)
            self.implicitly_wait(30)

            self.find_element_by_id(usrname_id).send_keys(usrname)
            self.find_element_by_id(pwd_id).send_keys(pwd)

            # self.find_element_by_id(pwd_id).send_keys(code)
            # self.find_element_by_id('login').click()

            #等待输入验证码
            while True:
                if cmp(ini_url,self.current_url)==-1:
                    break
                time.sleep(0.5)

            self.index_url(self.current_url)



class Chrome(selen.Chrome):
    def __init__(self, firefox_profile=None, firefox_binary=None, timeout=30,
                 capabilities=None, proxy=None):
        super(Chrome, self).__init__(firefox_profile, firefox_binary, timeout,
                                     capabilities, proxy)
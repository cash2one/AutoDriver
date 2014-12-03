# coding=utf-8
__author__ = 'Administrator'

import os
import re
import time
import the
from framework.util import constant
from selenium import webdriver as selen

TIME_OUT = 100

def firefox(sections):
    info = the.products[sections]
    p = info[constant.PRODUCT]
    if p == None:
        p = Firefox(info)
    return p



class Firefox(selen.Firefox):
    def __init__(self,configs, firefox_profile=None, firefox_binary=None, timeout=30,
                 capabilities=None, proxy=None):
        self.configs = configs
        super(Firefox, self).__init__(firefox_profile, firefox_binary, timeout,
                                      capabilities, proxy)


    def login(self):
        url=self.configs['url']
        usrname_id = self.configs['login_name_id']
        pwd_id = self.configs['login_pwd_id']
        usrname = self.configs['username']
        pwd = self.configs['password']

        self.get(url)
        self.implicitly_wait(30)

        if url in self.current_url:
            self.find_element_by_id(usrname_id).send_keys(usrname)
            self.find_element_by_id(pwd_id).send_keys(pwd)

            while True:
                if url not in self.current_url:
                    break

    # def switch_to_home(self):
    #     try:
    #         status = the.devices['driver_status']
    #     except KeyError:
    #         the.devices['driver_status'] = False
    #
    #     if the.devices['driver_status'] != isWorking:
    #         self.find_element_by_id(self.package + WORK_STATE).click()
    #         the.devices['driver_status'] = isWorking
    #         self.wait_loading()



class Chrome(selen.Chrome):
    def __init__(self, firefox_profile=None, firefox_binary=None, timeout=30,
                 capabilities=None, proxy=None):
        super(Chrome, self).__init__(firefox_profile, firefox_binary, timeout,
                                     capabilities, proxy)
# coding=utf-8
__author__ = 'Administrator'

import os
import re
import time
import the
from selenium import webdriver as selen

CS = 'idriver.web.cs'
HR = 'idriver.web.hr'
FA = 'idriver.web.fa'
OP = 'idriver.web.op'

aa=[]

def start_browser(browser='',configs=None):
    if browser=='':
        the.devices[CS] = Firefox(configs)
    elif browser == 'chrome':
        pass

def cs(browser=''):
    _configs = the.project_settings[CS]
    if the.devices[CS] == None:
        start_browser(browser)
        #the.devices[CS].wait_switch(_configs['app_activity'])

    return the.devices[CS]


class Firefox(selen.Firefox):
    def __init__(self, firefox_profile=None, firefox_binary=None, timeout=30,
                 capabilities=None, proxy=None):
        super(Firefox, self).__init__(firefox_profile, firefox_binary, timeout,
                                      capabilities, proxy)


class Chrome(selen.Chrome):
    def __init__(self, firefox_profile=None, firefox_binary=None, timeout=30,
                 capabilities=None, proxy=None):
        super(Chrome, self).__init__(firefox_profile, firefox_binary, timeout,
                                     capabilities, proxy)
# coding=utf-8
__author__ = 'Administrator'

import os,time
from appium import webdriver as am
from selenium import webdriver as sm
from framework.util import fs

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

res = '../../resource/'

def android():
    configs = fs.readConfigs(PATH(res+'config.ini'),'android')

    desired_caps = {}
    desired_caps['platformName'] = configs['platform_name']
    desired_caps['platformVersion'] = configs['platform_version']
    desired_caps['deviceName'] = configs['device_name']
    desired_caps['app'] = PATH(res+configs['app'])
    desired_caps['appPackage'] = configs['app_package']
    desired_caps['app-activity'] = configs['app_activity']

    return am.Remote('http://localhost:4723/wd/hub', desired_caps)

def web():
    firefox = sm.Firefox()
    firefox.maximize_window()
    return firefox

#切换到首页
def switchToHome(sf,main):
    time.sleep(1)
    if not main in sf.driver.current_activity:
        time.sleep(1)
        sf.driver.keyevent(4)
        if not main in sf.driver.current_activity:
            switchToHome(sf,main)


__author__ = 'Administrator'

import os
from appium import webdriver


def android(app_path):
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': PATH(app_path),
            'platformName': 'Android',
            'platformVersion': '4.2',
            'deviceName': 'Android Emulator'
        })
    return driver

def iOS(app_path):
    app = os.path.join(os.path.dirname(__file__),
                       '../../apps/UICatalog/build/Release-iphonesimulator',
                       app_path)
    app = os.path.abspath(app)
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': app,
            'platformName': 'iOS',
            'platformVersion': '7.1',
            'deviceName': 'iPhone Simulator'
        })
    return driver
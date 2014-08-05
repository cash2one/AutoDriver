__author__ = 'Administrator'

from appium import webdriver


def android(apk_path):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.2'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['app'] = apk_path
    desired_caps['appPackage'] = 'cn.com.pathbook.mychevy'
    desired_caps['app-activity'] = '.SplashActivity'

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
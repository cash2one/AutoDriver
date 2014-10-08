# coding=utf-8
__author__ = 'Administrator'

import os
import time
import threading
from appium import webdriver as am
from selenium import webdriver as sm
from framework.util import fs
from framework.core import the,HTMLTestRunner


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

res = '../../resource/'

def android():
    if the.android == None:
        configs = fs.readConfigs(PATH(res+'config.ini'),'android')

        desired_caps = {}
        desired_caps['platformName'] = configs['platform_name']
        desired_caps['platformVersion'] = configs['platform_version']
        desired_caps['deviceName'] = configs['device_name']
        desired_caps['app'] = PATH(res+configs['app'])
        desired_caps['appPackage'] = configs['app_package']
        desired_caps['app-activity'] = configs['app_activity']

        #return am.Remote('http://localhost:4723/wd/hub', desired_caps)
        the.android = am.Remote('http://localhost:4723/wd/hub', desired_caps)
    return the.android

def web():
    if the.web == None:
        firefox = sm.Firefox()
        firefox.maximize_window()
        the.web = firefox
    return the.web

def ios():
    pass


#切换到首页
def switchToHome(mainActivity):
    self_driver = android()
    time.sleep(1)
    if not mainActivity in self_driver.current_activity:
        time.sleep(1)
        self_driver.keyevent(4)
        if not mainActivity in self_driver.current_activity:
            switchToHome(mainActivity)


def isCurrentActivity(activity):
    self_driver = android()
    if self_driver.current_activity == activity:
        return True
    else:
        return False


class RunTest(threading.Thread):
    def __init__(self,task):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.startSuccess = False
        self.task = task

    def stream(self):
        t= time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        resultDir = PATH('../../report%s.html') % t
        fp = open(resultDir, 'wb')
        return fp

    def run(self):
        while not self.thread_stop:
            if self.task.getDevice().current_activity=='.CarAssistMainActivity':
                self.startSuccess = True

            if self.startSuccess and not self.task.getState() and self.task.getTestNum() > 0:
                runner = HTMLTestRunner.HTMLTestRunner(
                    stream=self.stream(),
                    task=self.task,
                    title=u'测试报告',
                    description=u'用例执行情况'
                )

                self.task.start()
                runner.run(self.task.getTestSuite())

            elif self.task.getTestNum() <= 0:
                self.stop()

            time.sleep(2)

    def stop(self):
        self.thread_stop = True


class WaitActivity(threading.Thread):

    def __init__(self,self_case,activity_name,target=None,args=()):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.target = target
        self.args = args
        self.activity_name = activity_name
        self.self_case = self_case

    def run(self):
        while not self.thread_stop:
            if self.activity_name in self.self_case.current_activity:
                apply(self.target,self.args)

                self.stop()

    def stop(self):
        self.thread_stop = True
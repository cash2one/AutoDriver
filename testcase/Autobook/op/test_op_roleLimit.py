# coding=utf-8
__author__ = 'zhangchun@pathbook.com.cn'

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from framework.core import idriver_web
import os

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def selectType(self,type,id,limit):
        opts=self.driver.find_id('role_platformType').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==type:  #获取对象属性
                opt.click()
        text=self.driver.find_id(id).find_element_by_id('lv1MenuName').text
        self.assertTrue(text==limit)
        #切换角色，查看权限框中的权限是否显示相应权限


    def test_roleName1(self):
        above=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a')
        ActionChains(self.driver).move_to_element(above).perform()
        #鼠标悬停在系统管理上
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/ul/li[1]/a').click()
        self.driver.find_id('create').click()#进入角色添加页面

        self.selectType(u'运维','lv1Menu51',u'系统监控')
        #类型为运维
        self.selectType(u'财务','lv1Menu41',u'充值付款')
        #类型为人事
        self.selectType(u'人事','lv1Menu31',u'司机管理')
        #类型为财务
        self.selectType(u'接口','lv1Menu61',u'账号服务')
        #类型为人事



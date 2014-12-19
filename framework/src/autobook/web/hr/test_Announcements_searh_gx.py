__author__ = 'gaoxu@pathbook.com.cn'
# coding=utf-8

import time
import unittest
from framework.core import idriver_web


class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        #登录平台
        self.driver.login()

    def tearDown(self):
         #返回首页
        # self.driver.switch_to_home()
        time.sleep(5)
         #关闭浏览器
        # self.driver.close()

    def test_Announcements(self):
       #跳转至公告管理界面
        self.driver.get("http://192.168.3.31/hr/hr/notice/listNotice.html")
        self.driver.find_element_by_id('noticeInfo').clear()
        self.driver.find_id('noticeInfo').send_keys(u'公告')
        time.sleep(5)
        self.driver.find_id('query').click()
        #点击排序
        self.driver.find_id('jqgh_list_title').click()
        time.sleep(2)
        self.driver.find_id('jqgh_list_creator_realName').click()
        time.sleep(2)
        self.driver.find_id('jqgh_list_createTime').click()
        time.sleep(2)







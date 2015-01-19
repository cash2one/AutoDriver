# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
import unittest
from framework.core import testcase


class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver =testcase.app(__file__)
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
        self.driver.find_element_by_id('noticeInfo').send_keys(u'公告')
        time.sleep(5)
        self.driver.find_element_by_id('query').click()


    def test_Announcements_error(self,Announcements_value):
        #跳转至公告管理界面
        self.driver.get("http://192.168.3.31/hr/hr/notice/listNotice.html")
        self.driver.find_element_by_id('noticeInfo').clear()
        self.driver.find_element_by_id('noticeInfo').send_keys(Announcements_value)
        time.sleep(5)
        self.driver.find_element_by_id('query').click()

 #调用initInputValue，并输入不存在的参数
    def test_vulue_error(self):
        self.test_Announcements_error(u'aaabbbbbbbbbcccccddddddddeeeeeeeee')
        tx=self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[3]/div/div[2]').text
        print tx
        self.assertTrue(u'没有符合条件的数据...' in tx)

     #调用initInputValue，为空
    def test_value_null3(self):
        self.test_Announcements_error('')

       #调用initInputValue，为空
    def test_value_correct(self):
        self.test_Announcements_error(u'公告')

    def test_Announcements_sort(self):
        #跳转至公告管理界面
        self.driver.get("http://192.168.3.31/hr/hr/notice/listNotice.html")
        #点击标题排序
        self.driver.find_element_by_id('jqgh_list_title').click()
        time.sleep(2)
        #点击发布人排序
        self.driver.find_element_by_id('jqgh_list_creator_realName').click()
        time.sleep(2)
        #点击发布时间排序
        self.driver.find_element_by_id('jqgh_list_createTime').click()
        time.sleep(2)







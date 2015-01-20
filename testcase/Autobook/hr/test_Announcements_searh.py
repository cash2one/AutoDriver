# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    def test_Announcements(self):
       #跳转至公告管理界面
        self.driver.get("http://192.168.3.31/hr/hr/notice/listNotice.html")
        self.driver.find_element_by_id('noticeInfo').clear()
        self.driver.find_element_by_id('noticeInfo').send_keys(u'公告')
        time.sleep(5)
        que=self.driver.find_element_by_id('query').click()
        self.assertTrue(que.is_selected())


    def test_Announcements_error(self,Announcements_value):
        #跳转至公告管理界面
        self.driver.get("http://192.168.3.31/hr/hr/notice/listNotice.html")
        self.driver.find_element_by_id('noticeInfo').clear()
        self.driver.find_element_by_id('noticeInfo').send_keys(Announcements_value)
        time.sleep(5)
        que=self.driver.find_element_by_id('query').click()
        self.assertTrue(que.is_selected())

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
        tit=self.driver.find_element_by_id('query').click()
        self.assertTrue(tit.is_selected())
        time.sleep(2)
        #点击发布人排序
        re=self.driver.find_element_by_id('jqgh_list_creator_realName').click()
        self.assertTrue(re.is_selected())
        time.sleep(2)
        #点击发布时间排序
        ti=self.driver.find_element_by_id('jqgh_list_createTime').click()
        self.assertTrue(ti.is_selected())
        time.sleep(2)







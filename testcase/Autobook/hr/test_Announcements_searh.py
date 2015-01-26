# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        #浏览器最大化
        self.driver.maximize_window()
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()
        # 关闭浏览器
        # self.driver.close()

    def test_Announcements(self):
       #跳转至公告管理界面
        self.driver.find_element_by_link_text(u'公告管理').click()
        self.driver.find_element_by_id('noticeInfo').clear()
        self.driver.find_element_by_id('noticeInfo').send_keys(u'公告')
        nottx=self.driver.find_element_by_id('noticeInfo').get_attribute('value')
        print nottx
        self.assertTrue(u'公告' in nottx)
        time.sleep(2)
        self.driver.find_element_by_id('query').click()


    #输入不存在的参数
    def test_vulue_error(self):
        #跳转至公告管理界面
        self.driver.find_element_by_link_text(u'公告管理').click()
        self.driver.find_element_by_id('noticeInfo').send_keys(u'123456poiuytrewq')
        nottx=self.driver.find_element_by_id('noticeInfo').get_attribute('value')
        print nottx
        self.assertTrue(u'123456poiuytrewq' in nottx)
        self.driver.find_element_by_id('query').click()
        tx=self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[3]/div/div[2]').text
        print tx
        self.assertTrue(u'没有符合条件的数据...' in tx)

     #内容为空
    def test_value_null3(self):
        #跳转至公告管理界面
        self.driver.find_element_by_link_text(u'公告管理').click()
        self.driver.find_element_by_id('noticeInfo').clear()
        self.driver.find_element_by_id('noticeInfo').send_keys('')
        nottx=self.driver.find_element_by_id('noticeInfo').get_attribute('value')
        print nottx
        self.assertTrue(u'' in nottx)
        self.driver.find_element_by_id('query').click()

    def test_Announcements_sort(self):
       #跳转至公告管理界面
        self.driver.find_element_by_link_text(u'公告管理').click()
        #点击标题排序
        self.driver.find_element_by_id('jqgh_list_title').click()
        self.driver.find_element_by_id('query').click()
        time.sleep(2)
        #点击发布人排序
        self.driver.find_element_by_id('jqgh_list_creator_realName').click()
        time.sleep(2)
        #点击发布时间排序
        self.driver.find_element_by_id('jqgh_list_createTime').click()
        time.sleep(2)







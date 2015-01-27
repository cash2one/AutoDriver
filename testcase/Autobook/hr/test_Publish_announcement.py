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
        # self.driver.switch_to_home()
        # 关闭浏览器
        self.driver.close()

     #发布公告
    def test_announcement(self):
       gltx=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').text
       print gltx
       self.assertTrue(u'司机管理' in gltx,u'与对比值不一致')
       self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
       addtx=self.driver.find_element_by_id('release').text
       self.assertTrue(u'发布公告' in addtx,u'与对比值不一致')
       self.driver.find_element_by_id('release').click()
       nutx=self.driver.find_element_by_id('number').text
       print nutx
       subtx=self.driver.find_element_by_id('noticeSubmit').text
       self.assertTrue(u'发布' in subtx,u'与对比值不一致')
       self.driver.find_element_by_id('noticeSubmit').click()


    def test_announcement_driver(self):
       # 司机总人数
       nutx=self.driver.find_element_by_id('number').text
       print nutx
       # 查看司机
       self.driver.find_element_by_link_text(u'查看司机').click()
       self.driver.switch_to_alert()
       self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/span[1]/a').click()

    def test_announcement_null(self):
       # 公告内容为空
       self.driver.find_element_by_id('noticeSubmit').click()
       tittx=self.driver.find_element_by_id('title_tip').text
       self.assertTrue(u'标题不能为空.' in tittx,u'标题与对比值不一致')
       contx=self.driver.find_element_by_id('content_tip').text
       self.assertTrue(u'内容不能为空.' in contx,u'内容与对比值不一致')

    def test_announcement_null1(self):
       # 公告内容为空
       self.driver.find_element_by_id('noticeSubmit').click()
       tittx=self.driver.find_element_by_id('title_tip').text
       self.assertTrue(u'标题不能为空.' in tittx,u'标题与对比值不一致')
       contx=self.driver.find_element_by_id('content_tip').text
       self.assertTrue(u'内容不能为空.' in contx,u'内容与对比值不一致')


    def test_announcement_correct(self):
       # 公告内容正确
       self.driver.find_element_by_id('noticeSubmit').click()
       tittx=self.driver.find_element_by_id('title_tip').text
       self.assertTrue(u'标题不能为空.' in tittx,u'标题与对比值不一致')




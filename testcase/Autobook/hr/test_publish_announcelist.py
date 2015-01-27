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

    def test_setting_reset(self):
       gltx=self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').text
       print gltx
       self.assertTrue(u'司机管理' in gltx,u'与对比值不一致')
       self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
       addtx=self.driver.find_element_by_id('release').text
       self.assertTrue(u'发布公告' in addtx,u'与对比值不一致')
       self.driver.find_element_by_id('release').click()
       nutx=self.driver.find_element_by_id('number').text
       print nutx
       self.driver.find_element_by_link_text(u'查看司机').click()
       self.driver.switch_to_alert()
       righttx=self.driver.find_element_by_id('pager2_right').text
       # 截取列表总条数值
       str=righttx[-4:-2]
       print str
       # 判断总条数是否一致
       if nutx==str:
           print '正确'
       else:
           print '错误'

       pagetx=self.driver.find_element_by_id('sp_1_pager2').text
       print pagetx
       self.driver.find_element_by_id('ui-icon ui-icon-seek-next').click()
       listtx=self.driver.find_element_by_id('gview_list2').text
       print listtx
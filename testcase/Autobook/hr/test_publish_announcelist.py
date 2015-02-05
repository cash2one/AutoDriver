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
    def test_driver_reset(self):
       '''
        对比总条数是否一致，一致输出"正确",否则输出"错误"
       :return:
       '''
       self.driver.find_element_by_link_text(u'司机管理').click()
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
       time.sleep(2)
       #关闭司机列表
       self.driver.find_element_by_xpath('//*[@id="xubox_layer1"]/div[1]/span[1]/a').click()

    def test_sort(self):
       '''
        对比总条数是否一致，一致输出"正确",否则输出"错误"
       :return:
       '''
       self.driver.find_element_by_link_text(u'司机管理').click()
       addtx=self.driver.find_element_by_id('release').text
       self.assertTrue(u'发布公告' in addtx,u'与对比值不一致')
       self.driver.find_element_by_id('release').click()
       nutx=self.driver.find_element_by_id('number').text
       print nutx
       self.driver.find_element_by_link_text(u'查看司机').click()
       self.driver.switch_to_alert()
       #点击姓名排序
       self.driver.find_element_by_id('jqgh_list2_name').click()
       #点击工号排序
       self.driver.find_element_by_id('jqgh_list2_no').click()
       #点击电话排序
       self.driver.find_element_by_id('jqgh_list2_phone').click()
       #点击状态排序
       self.driver.find_element_by_id('list2_state').click()





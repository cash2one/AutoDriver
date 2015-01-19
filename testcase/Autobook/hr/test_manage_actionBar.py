# coding=utf-8
__author__ = 'gaoxu@pathbook.com.cn'


import time
import unittest
from framework.core import testcase


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver =testcase.app(__file__)
        # 浏览器最大化
        self.driver.maximize_window()
        #登录平台
        self.driver.login()

    def tearDown(self):
        # 返回首页
        # self.driver.switch_to_home()
        time.sleep(5)
        #关闭浏览器
        # self.driver.close()

    def test_state(self):
        # 司机管理
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
        #司机状态
        opts = self.driver.find_element_by_id('state').find_elements_by_tag_name('option')
        time.sleep(1)
        #查询全部状态信息
        for opt in opts:
            if opt.get_attribute('text') == u'全部状态':
                opt.click()
        self.driver.find_element_by_id('query').click()
    def test_stste_normal(self):
        self.test_state()
        #所有行
        trs = self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        #循环最后一行，最后一列
        for i in range(1,len(trs)-1):
            tds=trs[i].find_elements_by_tag_name('td')
            td_last=tds[len(tds)-1]
            #判断状态
            if trs[i].find_elements_by_tag_name('td')[8].text==u'正常':
               #判断最后一列中是否有查询的名称链接，没有则报错
               self.assertTrue(td_last.find_elements_by_link_text(u'修改'))
               self.assertTrue(td_last.find_elements_by_link_text(u'禁用'))
               self.assertFalse(td_last.find_elements_by_link_text(u'培训'))
               self.assertTrue(td_last.find_elements_by_link_text(u'离职'))
               self.assertTrue(td_last.find_elements_by_link_text(u'详情'))
               self.assertTrue(td_last.find_elements_by_link_text(u'缩略图'))

            elif trs[i].find_elements_by_tag_name('td')[8].text==u'待付款':
               #判断最后一列中是否有查询的名称链接，没有则报错
               self.assertTrue(td_last.find_elements_by_link_text(u'修改'))
               self.assertFalse(td_last.find_elements_by_link_text(u'禁用'))
               self.assertFalse(td_last.find_elements_by_link_text(u'培训'))
               self.assertFalse(td_last.find_elements_by_link_text(u'离职'))
               self.assertTrue(td_last.find_elements_by_link_text(u'详情'))
               self.assertTrue(td_last.find_elements_by_link_text(u'缩略图'))

            elif trs[i].find_elements_by_tag_name('td')[8].text==u'待培训':
               #判断最后一列中是否有查询的名称链接，没有则报错
               self.assertTrue(td_last.find_elements_by_link_text(u'修改'))
               self.assertFalse(td_last.find_elements_by_link_text(u'禁用'))
               self.assertTrue(td_last.find_elements_by_link_text(u'培训'))
               self.assertFalse(td_last.find_elements_by_link_text(u'离职'))
               self.assertTrue(td_last.find_elements_by_link_text(u'详情'))
               self.assertTrue(td_last.find_elements_by_link_text(u'缩略图'))

            elif trs[i].find_elements_by_tag_name('td')[8].text==u'禁用':
               #判断最后一列中是否有查询的名称链接，没有则报错
               self.assertFalse(td_last.find_elements_by_link_text(u'修改'))
               self.assertTrue(td_last.find_elements_by_link_text(u'启用'))
               self.assertFalse(td_last.find_elements_by_link_text(u'培训'))
               self.assertFalse(td_last.find_elements_by_link_text(u'离职'))
               self.assertTrue(td_last.find_elements_by_link_text(u'详情'))
               self.assertFalse(td_last.find_elements_by_link_text(u'缩略图'))

            elif trs[i].find_elements_by_tag_name('td')[8].text==u'待退款':
               #判断最后一列中是否有查询的名称链接，没有则报错
               self.assertFalse(td_last.find_elements_by_link_text(u'修改'))
               self.assertFalse(td_last.find_elements_by_link_text(u'启用'))
               self.assertFalse(td_last.find_elements_by_link_text(u'培训'))
               self.assertFalse(td_last.find_elements_by_link_text(u'离职'))
               self.assertTrue(td_last.find_elements_by_link_text(u'详情'))
               self.assertFalse(td_last.find_elements_by_link_text(u'缩略图'))
            else:
                #判断最后一列中是否有查询的名称链接，没有则报错
               self.assertFalse(td_last.find_elements_by_link_text(u'修改'))
               self.assertFalse(td_last.find_elements_by_link_text(u'启用'))
               self.assertFalse(td_last.find_elements_by_link_text(u'培训'))
               self.assertFalse(td_last.find_elements_by_link_text(u'离职'))
               self.assertTrue(td_last.find_elements_by_link_text(u'详情'))
               self.assertFalse(td_last.find_elements_by_link_text(u'缩略图'))
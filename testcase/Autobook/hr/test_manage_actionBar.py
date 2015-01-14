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

    def test_stateQuery(self):
        #司机管理
        self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()
        #司机状态
        opts=self.driver.find_element_by_id('state').find_elements_by_tag_name('option')
        time.sleep(1)
        for opt in opts:
            if opt.get_attribute('text')==u'正常':
                opt.click()
        self.driver.find_element_by_id('query').click()
        tds=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')
         #查找最后一列
        td_last=tds[len(tds)-1]
        #判断最后一列中是否有查询的名称链接，没有则报错
        self.assertTrue(td_last.find_elements_by_link_text(u'修改'))
        self.assertTrue(td_last.find_elements_by_link_text(u'禁用'))
        self.assertTrue(td_last.find_elements_by_link_text(u'离职'))
        self.assertTrue(td_last.find_elements_by_link_text(u'详情'))
        self.assertTrue(td_last.find_elements_by_link_text(u'缩略图'))

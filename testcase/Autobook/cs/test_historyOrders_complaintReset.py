# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'
import time
from drivers import *
ORDER=u'15012610598594'

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_complaintReset(self):
        '''
        重置投诉内容
        :return:
        '''
        time.sleep(2)
        self.driver.find_ajax_id('main_menu')
        #鼠标悬浮在订单管理上
        above=self.driver.find_link('订单管理')
        self.driver.action_chains().move_to_element(above).perform()
        time.sleep(1)
        self.driver.find_link('历史订单').click()
        time.sleep(1)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/listOrderHistory.html' in self.driver.current_url,u'不是历史订单页面')
        finally:
            pass
        self.driver.find_id('orderNo').send_keys(ORDER)
        #点击查询按钮
        self.driver.find_id('query').click()
        time.sleep(1)
        trs=self.driver.find_id('list').find_tags('tr')
        tds=trs[1].find_tags('td')
        if ORDER in tds[1].text:
            try:
                tds[9].find_id('complaint').click()
                time.sleep(1)
            except self.driver.NoSuchElementException:
                pass

        try:
            #判断跳转的页面是否是客户投诉页面
            self.assertTrue('http://192.168.3.31/cs/cs/orderInform/addOrderInform.html' in self.driver.current_url,u'不是客户投诉页面')
        finally:
            pass
        self.driver.find_id('informVo_content').send_keys(u'投诉司机驾车绕路，开车不稳')
        #点击重置按钮
        #self.driver.find_class('a_button a_reset').click()
        self.driver.find_link('重置').click()
        time.sleep(1)
        contents_complaint=self.driver.find_id('informVo_content').text
        self.assertEqual(contents_complaint,'',u'投诉内容没有被清空')

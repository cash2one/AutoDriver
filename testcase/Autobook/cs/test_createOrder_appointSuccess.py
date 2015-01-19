# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
import unittest
from framework.core import testcase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions

class TestCase(unittest.TestCase):
    '''
    指定司机下单成功（订单数为默认1）
    '''

    def setUp(self):
        self.driver = testcase.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

     #点击创建订单跳转到创建订单界面
    def test_appoint_orderSuccess(self):
        self.driver.find_ajax_id('main_menu')
        self.driver.find_element_by_id('main_menu').click()
        # print menu
        #
        # for i in range(0,len(menu)-1):
        #     if menu[i]==u'订单管理':
        self.driver.find_element_by_link_text('订单管理').click()
        time.sleep(3)
        self.driver.find_element_by_link_text('创建订单').click()
        time.sleep(5)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url)
        finally:
            pass
        #time.sleep(3)

        #填写信息
        self.driver.find_element_by_id('customerCall').send_keys('wss')
        self.driver.find_element_by_id('phone').send_keys('13500000000')
        self.driver.find_element_by_id('map_search_btn').click()
        #输入客户位置
        self.driver.find_element_by_id('keyword').send_keys(u'万源路')
        self.driver.find_element_by_id('search_btn').click()
        #选择客户位置
        #self.driver.find_ajax_id('result')
        self.driver.find_element_by_xpath('//*[@id="divid1"]/table/tbody/tr/td[1]/img').click()
        #self.driver.find_element_by_id('divid1').find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[0].click()
        time.sleep(3)

        # 选择周边下单
        opts=self.driver.find_element_by_id('orderType').find_elements_by_tag_name('option')
        for opt in opts:
            if opt.get_attribute('text')==u'指定下单':
                opt.click()
        time.sleep(2)
        #点击选择司机
        self.driver.find_element_by_id('select_driver_btn').click()
        nearbyrivers = []
        try:
            nearbyrivers=self.driver.find_elements_by_class_name('driver_detail_on_list')
        except exceptions.NoSuchElementException:
            pass
        self.assertTrue(len(nearbyrivers) > 0, u'附近没有司机')
        driver_exist = False
        for d in nearbyrivers:
          name=self.driver.find_element_by_class_name('driver_detail_on_list').find_element_by_class_name('driver_name').text
          if u'小米' in name:
           driver_exist = True
           d.click()
        self.driver.find_element_by_id('sure_btn').click()

        #创建订单按钮
        self.driver.find_element_by_id('create_order_btn').click()
        time.sleep(3)
        #弹出订单窗口
        self.driver.switch_to_alert()
        text=self.driver.find_element_by_class_name('xubox_dialog').text
        print text
        #点击弹出订单窗口中确定按钮，跳转到进行中订单
        self.driver.find_element_by_link_text('确定').click()
        time.sleep(5)
        #获取进行中订单的订单号
        trs=self.driver.find_element_by_id('list').find_elements_by_tag_name('tr')
        for i in range(1,len(trs)-1):
            tds=trs[i].find_elements_by_tag_name('td')[1]
            print tds.text
            self.assertTrue(tds.text in text,'msg')



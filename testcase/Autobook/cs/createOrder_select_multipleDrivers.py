# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    指定司机下单(取消已选择的司机、在选择司机页面点击返回)
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_cancel_driver(self):
        '''
        跳转到创建订单页面，选择司机文本框中显示所选择的多个司机
        :return:
        '''
        self.driver.find_ajax_id('main_menu')
        # self.driver.find_id('main_menu').click()
        #鼠标悬浮在订单管理上
        above=self.driver.find_link('订单管理')
        self.driver.action_chains().move_to_element(above).perform()
        time.sleep(1)
        self.driver.find_link('创建订单').click()
        time.sleep(1)
        try:
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url,u'跳转的不是创建订单页面')
        finally:
            pass
        #time.sleep(3)

        #填写信息
        self.driver.find_id('customerCall').send_keys('wss')
        self.driver.find_id('phone').send_keys('13500000000')
        self.driver.find_id('map_search_btn').click()
        #输入客户位置
        self.driver.find_id('keyword').send_keys(u'万源路')
        self.driver.find_id('search_btn').click()
        #选择客户位置
        #self.driver.find_ajax_id('result')
        self.driver.find_element_by_xpath('//*[@id="divid1"]/table/tbody/tr/td[1]/img').click()
        time.sleep(3)
        #点击选择司机按钮
        self.driver.find_id('select_driver_btn').click()
        self.driver.find_ajax_id('near_driver_list')
        #判断列表中是否有司机
        nearbyrivers = []
        try:
              nearbyrivers=self.driver.find_classes('driver_detail_on_list')
        except self.driver.NoSuchElementException:
            pass
        self.assertTrue(len(nearbyrivers) > 0, u'附近没有司机')
        #选择列表中所有的司机
        ul=self.driver.find_id('near_driver_list').find_tag('ul')
        for d in range(0,5):
            li=ul.find_tags('li')
            els=li[d]
            name=els.find_class('driver_name').text
            print name
            els.click()

        time.sleep(3)
        #点击确定按钮，跳转到创建订单页面
        self.driver.find_id('sure_btn').click()
        # js = '$(\'input[id=driverName]\').removeAttr(\'readonly\')'
        # self.driver.execute_script(js)
        # self.driver.find_id('driverName').clear()
        # self.driver.find_id('driverName').send_keys(li)
        # time.sleep(3)
        id=self.driver.find_id('driverName')
        text=id.get_attribute("value")
        print text
        self.assertTrue(name in text,u'选择的司机和文本框中司机相等')


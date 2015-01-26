# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'
import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    指定司机下单(判断是否选择的是该司机)
    '''
    DRIVER=u'小米'

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()

      #在选择司机页面，已选司机后面显示该司机
    def test_select_driver(self):
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
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url,u'跳转的页面不是创建订单页面')
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
        time.sleep(3)
        #点击选择司机按钮
        self.driver.find_element_by_id('select_driver_btn').click()
        self.driver.find_ajax_id('near_driver_list')
        #判断列表中是否有司机
        nearbyrivers = []
        try:
              nearbyrivers=self.driver.find_elements_by_class_name('driver_detail_on_list')
        except self.driver.NoSuchElementException:
            pass
        self.assertTrue(len(nearbyrivers) > 0, u'附近没有司机')
        ul=self.driver.find_element_by_id('near_driver_list').find_element_by_tag_name('ul')
        li=ul.find_elements_by_tag_name('li')
        for d in range(0,len(li)):
            els=li[d]
            name=els.find_element_by_class_name('driver_name').text
            print name
            if u'小米' in name:
                els.click()
                break
            else:
                print(u'没找到司机小米')
        time.sleep(3)
        text=self.driver.find_element_by_class_name('selectd_name').text
        print text
        self.assertTrue(u'小米' in text,u'选择的司机不是小米')


    #在选择司机页面判断选择的司机是否匹配
    def test_driver(self):
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
            self.assertTrue('http://192.168.3.31/cs/cs/order/createOrder.html' in self.driver.current_url,u'跳转的页面不是创建订单页面')
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
        time.sleep(3)
        #点击选择司机按钮
        self.driver.find_element_by_id('select_driver_btn').click()
        self.driver.find_ajax_id('near_driver_list')
        #判断列表中是否有司机
        nearbyrivers = []
        try:
              nearbyrivers=self.driver.find_elements_by_class_name('driver_detail_on_list')
        except self.driver.NoSuchElementException:
            pass
        self.assertTrue(len(nearbyrivers) > 0, u'附近没有司机')
        ul=self.driver.find_element_by_id('near_driver_list').find_element_by_tag_name('ul')
        li=ul.find_elements_by_tag_name('li')
        for d in range(0,len(li)):
            els=li[d]
            name=els.find_element_by_class_name('driver_name').text
            # print name
            if u'小米' in name:
                els.click()
                break
            else:
                print(u'没找到司机小米')
        time.sleep(3)
        #点击确定按钮
        self.driver.find_element_by_id('sure_btn').click()
        time.sleep(3)
        #获取创建订单页面选择司机文本框中的司机
        text=self.driver.find_element_by_id('driverName').get_attribute("value")
        # print text
        self.assertEqual(text,u'小米',u'选择的司机和文本框中显示的司机相等')

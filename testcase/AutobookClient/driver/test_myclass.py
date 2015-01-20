# coding=utf-8
__author__ = 'Administrator'

import time
from drivers import *


class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()
        pass

    def test_my_info(self):
        #idriver.changeWork(self.driver,True)

        # name_id = self.driver.wait_id_text('tv_customer_name',u'xu女士')
        #
        # print 'pass.....'
        # print self.pkg
        # self.driver.find_id('rb_benifit').click()
        # he_td = self.driver.wait_find_id('he_td')


        # #自动下单
        # order_owner = u'AutoZh'
        # self.driver.send_new_order(order_owner)
        # tv_customer_name = self.driver.wait_find_id_text('tv_customer_name',order_owner)
        #
        # print tv_customer_name.text
        activity = self.driver.current_activity
        self.driver.change_status(True)
        #print self.driver.app_strings
        self.driver.find_id('tv_history_order').click()

        self.driver.wait_switch(activity)

        #items = self.driver.swipe_load_item('lv_completed','history_order_finish',('order_number_text','order_amount_text'),3)
        # for i in range(0,10):
        #     self.driver.swipee('history_order_finish'

        #print items


        #txt = self.driver.find_element_by_id(self.driver.pkg+'rl_title').find_element_by_id(self.driver.pkg+'tv_title_text').text
        #print txt




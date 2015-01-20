# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()
    #充值付款界面，打印凭证，打印次数自动加1
    def test_print_trade(self):
        time.sleep(1)

        #取出打印之前的打印次数
        table = self.driver.find_element_by_id('list')
        trs = table.find_elements_by_tag_name('tr')
        printNum = trs[1].find_elements_by_tag_name('td')[9]
        printNum_text = printNum.get_attribute('title')
        trs[1].find_element_by_id('print_trade').click()#点击第一行的打印凭证
        time.sleep(1)
        self.driver.find_element_by_id('print_submit').click()#点击打印
        time.sleep(1)
        self.driver.find_element_by_id('print_close').click()#点击关闭

        #取出打印之后的打印次数
        table2 = self.driver.find_element_by_id('list')
        trs2 = table2.find_elements_by_tag_name('tr')
        printNum2 = trs2[1].find_elements_by_tag_name('td')[9]
        printNum_text_new = printNum2.get_attribute('title')
        print printNum_text,printNum_text_new
        #比较打印前后的次数打印后自动加1，先将次数转换成int型。
        if int(printNum_text_new) == int(printNum_text) + 1:
            print 'Ture'
        else:
            print 'False'

        time.sleep(2)

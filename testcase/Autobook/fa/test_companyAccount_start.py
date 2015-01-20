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

    #公司账户列表操作-启用、设为默认、禁用
    def test_list_operation_start(self):
        time.sleep(0.5)
        self.driver.find_element_by_link_text('账户管理').click()
        time.sleep(1)
        self.driver.find_element_by_link_text('公司账户').click()
        time.sleep(2)
        table = self.driver.find_element_by_id('list')
        trs = table.find_elements_by_tag_name('tr')

        station = trs[1].find_elements_by_tag_name('td')[6]
        station_text = station.get_attribute('title')#取出当前该账户的状态
        print station_text

        self.assertTrue(u'已禁用' in station_text,'msg')

        #点击启用
        trs[1].find_element_by_id('start').click()
        time.sleep(1)
        table1 = self.driver.find_element_by_id('xubox_layer1')
        text1 = table1.find_element_by_class_name('xubox_text').text
        print text1
        self.assertTrue(u'确定启用该账户?' in text1,'msg')

        table1.find_element_by_class_name('xubox_yes').click()
        time.sleep(2)
        table2 = self.driver.find_element_by_id('list')
        trs2 = table2.find_elements_by_tag_name('tr')
        station1 = trs2[1].find_elements_by_tag_name('td')[6]
        station_text1 = station1.get_attribute('title')#取出当前该账户的状态
        print station_text1
        self.assertTrue(u'正常' in station_text1,'msg')


        #点击设为默认
        trs2[1].find_element_by_id('setDefault').click()

        table7 = self.driver.find_element_by_class_name('xubox_main')
        text7 = table7.find_element_by_class_name('xubox_text').text
        print text7

        self.assertTrue(u'确定将该账户设为默认账户吗?' in text7,'msg')
        table7.find_element_by_class_name('xubox_yes').click()
        time.sleep(2)
        #查看是否默认中的字体
        table3 = self.driver.find_element_by_id('list')
        trs3 = table3.find_elements_by_tag_name('tr')
        station3 = trs3[1].find_elements_by_tag_name('td')[5]
        station_text3 = station3.get_attribute('title')#取出当前该账户的状态
        print station_text3
        self.assertTrue(u'是' in station_text3,'msg')
        #点击另一个相同账户类型的账户将其设置为默认账户
        table4 = self.driver.find_element_by_id('list')
        trs4 = table3.find_elements_by_tag_name('tr')
        trs4[17].find_element_by_id('setDefault').click()
        table4 = self.driver.find_element_by_class_name('xubox_main')
        table4.find_element_by_class_name('xubox_yes').click()
        time.sleep(4)

        #点击禁用
        table8 = self.driver.find_element_by_id('list')
        trs8 = table3.find_elements_by_tag_name('tr')
        trs8[1].find_element_by_id('stop').click()
        table5 = self.driver.find_element_by_class_name('xubox_main')
        text5 = table5.find_element_by_class_name('xubox_text').text
        print text5
        self.assertTrue(u'确定禁用该账户?' in text5,'msg')

        table5.find_element_by_class_name('xubox_yes').click()
        time.sleep(2)
        table6 = self.driver.find_element_by_id('list')
        trs6 = table6.find_elements_by_tag_name('tr')
        station6 = trs6[1].find_elements_by_tag_name('td')[6]
        station_text6 = station6.get_attribute('title')#取出当前该账户的状态
        print station_text6
        self.assertTrue(u'已禁用' in station_text6,'msg')

        time.sleep(2)

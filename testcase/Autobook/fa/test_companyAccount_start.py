# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'
import time
import unittest
from framework.core import idriver_web

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = idriver_web.firefox(__file__)
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
        table1 = self.driver.find_element_by_id('xubox_layer1')
        table1.find_elments_by_class_name('xubox_botton2').click()
        time.sleep(2)
        table2 = self.driver.find_element_by_id('list')
        trs2 = table2.find_elements_by_tag_name('tr')
        station1 = trs2[1].find_elements_by_tag_name('td')[6]
        station_text1 = station1.get_attribute('title')#取出当前该账户的状态
        print station_text1
        self.assertTrue(u'正常' in station_text1,'msg')



        #点击设为默认
        trs2[1].find_element_by_id('setDefault').click()

        table2 = self.driver.find_element_by_id('xubox_layer16')
        table2.find_elments_by_class_name('xubox_yes').click()
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
        table4 = self.driver.find_element_by_id('xubox_layer16')
        table4.find_elments_by_class_name('xubox_yes').click()
        time.sleep(2)

        #点击禁用
        trs4[1].find_element_by_id('stop').click()
        table5 = self.driver.find_element_by_id('xubox_layer10')
        table5.find_elments_by_class_name('xubox_yes').click()
        time.sleep(2)
        table6 = self.driver.find_element_by_id('list')
        trs6 = table6.find_elements_by_tag_name('tr')
        station6 = trs6[1].find_elements_by_tag_name('td')[6]
        station_text6 = station6.get_attribute('title')#取出当前该账户的状态
        print station_text6
        self.assertTrue(u'已禁用' in station_text6,'msg')





        time.sleep(2)



        time.sleep(2)

if __name__ =='__main__':
    unittest.main()

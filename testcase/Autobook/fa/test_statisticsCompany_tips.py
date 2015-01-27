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

    #公司出入账,未选择账户类型和报表类型提示语对比
    def test_statisticsCompany_Tips(self):
        time.sleep(2)
        self.driver.find_element_by_link_text('统计报表').click()
        time.sleep(0.5)
        self.driver.find_element_by_link_text('公司出入账').click()
        time.sleep(2)

        #未选中账户类型提示语对比
        self.driver.find_element_by_id('statistics').click()
        time.sleep(1)
        account_type_text = self.driver.find_element_by_id('account_type_tip').text
        self.assertTrue(u'请选择账户类型' in account_type_text,u'没有找到指定字符串')

        #未选中报表类型提示语对比
        self.driver.find_element_by_id('account_type').find_elements_by_tag_name('option')[2].click()
        self.driver.find_element_by_id('statistics').click()
        time.sleep(1)
        statement_type_text = self.driver.find_element_by_id('statement_type_tip').text
        self.assertTrue(u'请选择报表类型' in statement_type_text,u'没有找到指定字符串')


        self.driver.find_element_by_id('statement_type').find_elements_by_tag_name('option')[1].click()
        time.sleep(1)

        js = '$(\'input[id=startTime]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('startTime').clear()
        self.driver.find_element_by_id('startTime').send_keys('2015-01-06')
        #选择开始时间
        js = '$(\'input[id=endTime]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('endTime').clear()
        self.driver.find_element_by_id('endTime').send_keys('2015-01-01')
        self.driver.find_element_by_id('statistics').click()
        #选择结束时间
        time.sleep(3)
        text = self.driver.switch_to_alert().text
        self.assertEqual(text,u'开始日期不能大于截止日期，请重新选择日期！',u'没有找到指定字符串')
        self.driver.switch_to_alert().accept()
        print(text)









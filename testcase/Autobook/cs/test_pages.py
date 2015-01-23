# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    （首页）跳转页面
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()


    def tearDown(self):
         #返回首页
        self.driver.switch_to_home()


    def test_pages(self):
        '''
        页面（跳转）
        :return:
        '''
        #点击下一页
        self.driver.find_id('next_pager').click()
        time.sleep(2)
        two=self.driver.find_class('ui-pg-input').get_attribute("value")
        self.assertEqual(two,2,u'从第一页跳转到第二页失败')

        #点击上一页
        self.driver.find_id('prev_pager').click()
        time.sleep(2)
        one=self.driver.find_class('ui-pg-input').get_attribute("value")
        self.assertEqual(one,1,u'从第二页跳转到第一页失败')

        #点击尾页(最后一页)
        sp_1_pager=self.driver.find_id('sp_1_pager').get_attribute("value")
        self.driver.find_id('last_pager').click()
        time.sleep(2)
        last_pager=self.driver.find_class('ui-pg-input').get_attribute("value")
        self.assertEqual(last_pager,sp_1_pager,u'总页面数和最后一页不一致')

        #点击首页（第一页）
        self.driver.find_id('first_pager').click()
        first_pager=self.driver.find_class('ui-pg-input').get_attribute("value")
        self.assertEqual(first_pager,1,u'显示的不是第一页面')
        time.sleep(2)

        #输入页面跳转至指定的页数
        pg_class=self.driver.find_class('ui-pg-input')
        pg_class.clear()
        input=pg_class.send_keys('20').get_attribute("value")
        pg_class.send_keys(self.driver.keys().ENTER)#按回车键
        self.assertEqual(input,20,u'跳转的不是20页')
        time.sleep(2)

        #跳转页面大于总页面，系统跳转至最后一页面
        pg_class=self.driver.find_class('ui-pg-input')
        pg_class.clear()
        input=pg_class.send_keys('102354')
        pg_class.send_keys(self.driver.keys().ENTER)#按回车键
        self.assertEqual(input,20,u'跳转的不是20页')
        time.sleep(2)

        #跳转页面输入小数，系统保留正整数
        pg_class=self.driver.find_class('ui-pg-input')
        pg_class.clear()
        inp=pg_class.send_keys('5.6')
        pg_class.send_keys(self.driver.keys().ENTER)#按回车键
        self.assertTrue(u'5'in inp ,u'跳转的不是20页')
        time.sleep(2)

        #选择每页10行
        self.driver.find_class('ui-pg-selbox').find_tags('option')[0].click()
        time.sleep(1)
        num=self.driver.find_class('ui-pg-selbox').get_attribute("value")
        self.assertEqual(num,10,u'当前页面显示的不是10行')

        #选择每页20行
        self.driver.find_class('ui-pg-selbox').find_tags('option')[1].click()
        time.sleep(1)
        num1=self.driver.find_class('ui-pg-selbox').get_attribute("value")
        self.assertEqual(num1,10,u'当前页面显示的不是10行')

        #选择每页40行
        self.driver.find_class('ui-pg-selbox').find_tags('option')[2].click()
        time.sleep(1)
        num2=self.driver.find_class('ui-pg-selbox').get_attribute("value")
        self.assertEqual(num2,10,u'当前页面显示的不是10行')



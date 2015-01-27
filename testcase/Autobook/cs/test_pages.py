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
        time.sleep(3)
        self.driver.find_ajax_id('next_pager')
        self.driver.find_element_by_id('next_pager').click()
        time.sleep(3)
        two=self.driver.find_class('ui-pg-input').get_attribute("value")
        print two
        self.assertEqual(two,u'2',u'从第一页跳转到第二页失败')

        #点击上一页
        self.driver.find_id('prev_pager').click()
        time.sleep(2)
        one=self.driver.find_class('ui-pg-input').get_attribute("value")
        self.assertEqual(one,u'1',u'从第二页跳转到第一页失败')

        #点击尾页(最后一页)
        num=self.driver.find_id('sp_1_pager').text
        #去掉中间的逗号
        num_pages=filter(str.isdigit, str(num))
        self.driver.find_id('last_pager').click()
        time.sleep(2)
        last_pager=self.driver.find_class('ui-pg-input').get_attribute("value")
        self.assertEqual(last_pager,num_pages,u'总页面数和最后一页不一致')

        #点击首页（第一页）
        self.driver.find_id('first_pager').click()
        time.sleep(1)
        first_pager=self.driver.find_class('ui-pg-input').get_attribute("value")
        self.assertEqual(first_pager,u'1',u'显示的不是第一页面')
        time.sleep(2)


        #输入页面跳转至指定的页数
        pg_class=self.driver.find_class('ui-pg-input')
        pg_class.clear()
        pg_class.send_keys('20')
        pg_class.send_keys(self.driver.keys().ENTER)#按回车键
        time.sleep(1)
        input=pg_class.get_attribute("value")
        self.assertEqual(input,u'20',u'跳转的不是20页')
        time.sleep(2)

        #跳转页面大于总页面，系统跳转至最后一页面
        pg_class=self.driver.find_class('ui-pg-input')
        pg_class.clear()
        pg_class.send_keys('102354')
        pg_class.send_keys(self.driver.keys().ENTER)#按回车键
        time.sleep(1)
        put=pg_class.get_attribute("value")
        self.assertEqual(put,num_pages,u'跳转的不是最后一页')
        time.sleep(2)

        #跳转页面输入小数，系统保留正整数
        pg_class.clear()
        pg_class.send_keys('5.6')
        pg_class.send_keys(self.driver.keys().ENTER)#按回车键
        time.sleep(1)
        inp=pg_class.get_attribute("value")
        self.assertTrue(u'5'in inp ,u'跳转的不是5页')
        time.sleep(2)

        #跳转输入非法字符，系统跳转至第一页
        pg_class.clear()
        pg_class.send_keys('dfj')
        pg_class.send_keys(self.driver.keys().ENTER)#按回车键
        time.sleep(1)
        one_1=pg_class.get_attribute("value")
        self.assertEqual(one_1,u'1',u'跳转的不是第一页')
        time.sleep(2)


        #选择每页10行
        self.driver.find_class('ui-pg-selbox').find_tags('option')[0].click()
        time.sleep(1)
        num=self.driver.find_class('ui-pg-selbox').get_attribute("value")
        print num
        self.assertEqual(num,u'10',u'当前页面显示的不是10行')

        #选择每页20行
        self.driver.find_class('ui-pg-selbox').find_tags('option')[1].click()
        time.sleep(1)
        num1=self.driver.find_class('ui-pg-selbox').get_attribute("value")
        self.assertEqual(num1,u'20',u'当前页面显示的不是20行')

        #选择每页40行
        self.driver.find_class('ui-pg-selbox').find_tags('option')[2].click()
        time.sleep(1)
        num2=self.driver.find_class('ui-pg-selbox').get_attribute("value")
        self.assertEqual(num2,u'40',u'当前页面显示的不是40行')



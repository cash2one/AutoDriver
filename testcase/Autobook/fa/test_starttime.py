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


    def test_starttime(self):
        '''
        充值付款交易明细开始日期
        :return:
        '''
        time.sleep(1)

        js = '$(\'input[id=startTime]\').removeAttr(\'readonly\')'
        self.driver.execute_script(js)#只读编辑框可以编辑
        self.driver.find_element_by_id('startTime').clear()
        self.driver.find_element_by_id('startTime').send_keys('2015-01-27')

        self.driver.find_element_by_id('query').click()
        time.sleep(1)
        #定位当前列表
        table = self.driver.find_element_by_id('list')
        trs = table.find_elements_by_tag_name('tr')
        for i in range(1,len(trs)):
            tds = trs[i].find_elements_by_tag_name('td')[5]
            creatTime_text = tds.get_attribute('title')[0:10]#截取前10位
            print creatTime_text
            self.assertTrue(creatTime_text >= u'2015-01-27','msg')









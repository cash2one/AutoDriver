
# coding=utf-8
__author__ = 'lvfangying@pathbook.com.cn'

#hr_循环验证用户名错误登录测试

import time
from drivers import *

class TestCase(unit.TestCase):

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()


    def test_old_address(self):
        self.driver.find_element_by_id('btn_add').click()
        driverVo_address_tx=self.driver.find_element_by_id('detailVo_oldAddress_tip').text
        self.assertTrue(u'户口地址不能为空.'in driverVo_address_tx)


    def test_address_ture(self):
        self.driver.find_element_by_id('detailVo_oldAddress').send_keys(u'湖南省邵阳县黄亭市镇茶铺村3组9号')
        # 输入正确的户口地址



    def test_new_address(self):
        self.driver.find_element_by_id('detailVo_newAddress').clear()
        self.driver.find_element_by_id('btn_add').click()
        driverVo_address_tx=self.driver.find_element_by_id('detailVo_newAddress_tip').text
        self.assertTrue(u'现住址不能为空.'in driverVo_address_tx)



    def test_address_long(self):
        self.driver.find_element_by_id('detailVo_newAddress').send_keys(u'上海市闵行区七宝镇沪清平公路')
        # 输入正确的现住址










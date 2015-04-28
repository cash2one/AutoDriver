# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    用户未登录，1,查看条款 2,不勾选条款。
    '''
    def setUp(self):
        self.driver = self.app(__file__)
        #self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_clause(self):
       #点击进入使用
       # self.driver.find_id('start_btn').click()
       self.driver.wait_loading()
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()

       #点击我的信息
       self.driver.find_ids('person_item')[0].click()
       #在填写手机号界面点击条款
       self.driver.find_id('login_clause').click()


       text=self.driver.find_id('tv_title_text').text
       print text
       self.assertTrue(u'代驾协议' in text,'msg')


       # 点击返回注册按钮
       self.driver.find_id('button_title_back').click()
       #判断条款是否选中，若选中取消选中
       if 'true' in self.driver.find_id('login_agree').get_attribute('checked'):
           self.driver.find_id('login_agree').click()

        #不勾选同意条款，直接点击下一步
       self.driver.find_id('next_step').click()
       #弹框验证
       self.driver.switch_to_alert()
       text=self.driver.find_id('tv_msg').text
       print text
       self.assertTrue(u'请选择同意条款' in text,'msg')

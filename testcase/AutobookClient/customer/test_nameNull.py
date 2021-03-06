# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'

import time
from drivers import *

class TestCase(unit.TestCase):
    '''
    用户登录，用户名为空
    '''

    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        # 返回首页
        self.driver.switch_to_home()

    def test_changePhone(self):
        '''
        changePhone
        :return:
        '''
        self.driver.wait_loading()
        # 点击用户中心
        self.driver.find_id('btn_personal_center').click()
        #我的信息
        self.driver.find_ids('person_item')[0].click()
        #删除姓名
        self.driver.clear_text('personal_user_name')

        time.sleep(3)
        #点击完成（修改成功）
        self.driver.find_id('personal_finish').click()

        #判断是否有弹出框
        self.driver.switch_to_alert()
        text = self.driver.find_id('tv_msg').text
        print text
        self.assertTrue(u'姓名不能为空' in text, 'msg')

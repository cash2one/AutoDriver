# coding=utf-8

__author__ = 'wangshanshan@pathbook.com.cn'


import time
from drivers import *

class TestCase(unit.TestCase):
    def setUp(self):
        self.driver = self.app(__file__)
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def test_changePhone(self):
       '''
       用户登录，修改紧急联系电话
       :return:
       '''

       self.driver.wait_loading()
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #我的信息
       self.driver.find_ids('person_item')[0].click()
      #修改紧急联系电话
       self.driver.find_id('personal_urgent_numbers').click()
       self.driver.clear_text('personal_urgent_numbers')
       self.driver.find_id('personal_urgent_numbers').send_keys('13636468713')
       # self.driver.find_id('personal_user_name').click()
       # self.driver.keyevent(67)
       time.sleep(3)
       #点击完成（修改成功）
       self.driver.find_id('personal_finish').click()



    def test_urgency_phone(self):
       '''
       紧急联系电话输入少于11位,输入10位
       :return:
       '''
       self.driver.wait_loading()
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #我的信息
       self.driver.find_ids('person_item')[0].click()
      #修改紧急联系电话
       self.driver.find_id('personal_urgent_numbers').click()
       self.driver.clear_text('personal_urgent_numbers')
       self.driver.find_id('personal_urgent_numbers').send_keys('1363646871')
       # self.driver.find_id('personal_user_name').click()
       # self.driver.keyevent(67)
       time.sleep(3)
       #点击完成（修改成功）
       self.driver.find_id('personal_finish').click()

       #判断是否有弹出框
       self.driver.switch_to_alert()
       text=self.driver.find_id('tv_msg').text
       print text
       self.assertTrue(u'紧急联系电话格式不正确' in text,'msg')


    def test_urgency_phone1(self):
       '''
       紧急联系电话输入大于11位，系统限制输入
       :return:
       '''
       self.driver.wait_loading()
       #点击用户中心
       self.driver.find_id('btn_personal_center').click()
       #我的信息
       self.driver.find_ids('person_item')[0].click()
       #修改紧急联系电话
       self.driver.find_id('personal_urgent_numbers').click()
       self.driver.clear_text('personal_urgent_numbers')
       self.driver.find_id('personal_urgent_numbers').send_keys('1363646871832')
       # self.driver.find_id('personal_user_name').click()
       # self.driver.keyevent(67)
       time.sleep(3)
       #点击完成（修改成功）
       # self.driver.find_id('personal_finish').click()


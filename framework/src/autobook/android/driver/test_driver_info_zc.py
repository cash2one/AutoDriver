# coding=utf-8
__author__ = 'zhangchun'

import time
import unittest
from framework.core import device,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = device.app('idriver.android.driver')
        idriver.login_driver(self.driver)
        self.driver_no = idriver.get_driver_no()
        #获取登录司机的工号

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def find_driver_info(self,tv_id):
        tv_txt = self.driver.find_id(tv_id).text
        #获取个人信息页面的司机信息
        return tv_txt.split(':')[1].strip()
        #获取的格式为"XX：  XXX",只取后面的名字，split(':')[1]取冒号后的字符串，strip（）过滤左端空格

    def test_my_info(self):
        idriver.changeWork(self.driver,True)

        current_activity = self.driver.current_activity
        self.driver.find_id('iv_head').click()
        self.driver.wait_switch(current_activity)

        current_activity = self.driver.current_activity
        self.driver.find_id('personal_list_text').click()
        self.driver.wait_switch(current_activity)

        db_result = self.driver.sql('select name,province,license_type,driving_age,driving_count from t_driver where no=%s' % self.driver_no)
        #将数据库中查询出的数据存入元组

        driver_tup = (db_result[0],idriver.province(db_result[1]),idriver.license_type(db_result[2]),unicode(db_result[3]),unicode(db_result[4]))
        #籍贯和驾照是枚举型，要获取值后存入新元组,代驾次数和驾龄为long型需转换成Unicode

        text_name=self.find_driver_info('text_name')
        text_hometown=self.find_driver_info('text_hometown')
        text_driver_license=self.find_driver_info('text_driver_license')
        text_driving_experience=self.find_driver_info('text_driving_experience')[:-1]
        text_service_times=self.find_driver_info('text_service_times')[:-1]
        textview_tup = (text_name,text_hometown,text_driver_license,text_driving_experience,text_service_times)


        self.assertTrue(textview_tup == driver_tup,'msg')
        #查看司机的信息与数据库中查询出的是否一致

        self.assertEqual('.MyInfoActivity',self.driver.current_activity)
        #跳转到个人信息页面，












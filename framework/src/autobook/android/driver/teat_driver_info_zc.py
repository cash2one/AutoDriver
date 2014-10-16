# coding=utf-8
__author__ = 'zhangchun'

import time
import unittest
from framework.core import extend,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = extend.Android('android.idriver.driver')
        self.driver.login()

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def my_info(self,):
        idriver.changeWork(True)

        current_activity = self.driver.current_activity()
        self.driver.find_id('iv_head').click()
        self.driver.switch_finish(current_activity)

        self.driver.find_id('personal_list_text').click()
        self.driver.switch_finish(current_activity)
        self.assertTrue('.MyInfoActivity',self.driver.current_activity)
        #跳转到个人信息页面

    def test_my_name(self):
        self.my_info()
        els=self.driver.sql('select name from t_driver where no=140018')
        name=self.driver.find_id('text_name').text
        self.assertTrue(els,name)
        #查看司机的姓名

    def test_my_country(self):
        self.my_info()
        t=self.driver.sql('select province from t_driver where no=140018')[0]
        els=idriver.province(t)
        d_age=self.driver.find_id('text_hometown').text
        self.assertTrue(els,d_age[-2:])
        print els #查看司机籍贯

    def test_my_license(self):
        self.my_info()
        t=self.driver.sql('select license_type from t_driver where no=140018')[0]
        els=idriver.license_type(t)
        l_type=self.driver.find_id('text_driver_license').text
        self.assertTrue(els,l_type[-2:])
        print els#查看司机驾照

    def test_my_drivingAge(self):
        self.my_info()
        els=self.driver.sql('select driving_age from t_driver where no =140018')
        d_age=self.driver.find_id('text_driving_experience').text
        self.assertTrue(els,d_age[-1])#查看司机驾龄

    def test_my_count(self):
        self.my_info()
        els=self.driver.sql('select driving_count from t_driver where no =140018')
        d_count=self.driver.find_id('text_service_times').text
        self.assertTrue(els,d_count[-2])#查看司机代驾次数











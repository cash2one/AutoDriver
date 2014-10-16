# coding=utf-8
__author__ = 'zhangchun'

import time
import unittest
from framework.core import extend,idriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = extend.Android('android.idriver.driver')
        self.driver.login()
        self.driver_no = idriver.get_driver_no()
        #获取登录司机的工号

    def tearDown(self):
        #返回首页
        self.driver.switch_to_home()

    def my_info(self):
        idriver.changeWork(True)

        current_activity = self.driver.current_activity()
        self.driver.find_id('iv_head').click()
        self.driver.switch_finish(current_activity)

        self.driver.find_id('personal_list_text').click()
        self.driver.switch_finish(current_activity)
        # self.assertEqual('.MyInfoActivity',self.driver.current_activity())
        # self.assertTrue('' in self.driver.current_activity(),'err')
        #跳转到个人信息页面

    def test_my_name(self):
        self.my_info()
        els=self.driver.sql('select name from t_driver where no=%s' % self.driver_no)
        name=self.driver.find_id('text_name').text
        name1=name.split(':')[1].strip()
        #获取的格式为"姓名：  XXX",只取后面的名字，split(':')[1]取冒号后的字符串，strip（）过滤左端空格

        self.assertEqual(els[0],name1)
        # self.assertEqual('.MyInfoActivity',self.driver.current_activity())
        #查看司机的姓名

    # def test_my_country(self):
    #     self.my_info()
    #     t=self.driver.sql('select province from t_driver where no=%s'% self.driver_no)[0]
    #     els=idriver.province(t)
    #     d_age=self.driver.find_id('text_hometown').text
    #     self.assertEqual(els,d_age[-2:])
    #     print els #查看司机籍贯
    #
    # def test_my_license(self):
    #     self.my_info()
    #     t=self.driver.sql('select license_type from t_driver where no=%s'% self.driver_no)[0]
    #     els=idriver.license_type(t)
    #     l_type=self.driver.find_id('text_driver_license').text
    #     self.assertEqual(els,l_type[-2:])
    #     print els#查看司机驾照
    #
    # def test_my_drivingAge(self):
    #     self.my_info()
    #     els=self.driver.sql('select driving_age from t_driver where no =%s'% self.driver_no)
    #     d_age=self.driver.find_id('text_driving_experience').text
    #     self.assertEqual(els,d_age[-1])#查看司机驾龄
    #
    # def test_my_count(self):
    #     self.my_info()
    #     els=self.driver.sql('select driving_count from t_driver where no =%s'% self.driver_no)
    #     d_count=self.driver.find_id('text_service_times').text
    #     self.assertEqual(els,d_count[-2])#查看司机代驾次数











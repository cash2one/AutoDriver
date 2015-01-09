# coding=utf-8
__author__ = 'xuguanghua@pathbook.com.cn'
#附近司机列表界面，滑动列表，及点击附近司机界面的“用户中心”按钮
import time
import unittest
from framework.core import idriver_android



class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = idriver_android.app(__file__)
        self.driver.login()

    def tearDown(self):
        self.driver.switch_to_home()

    #附近司机列表界面，滑动列表
    def test_List(self):

        #点击附近司机界面的“列表”
        self.driver.find_id('rb_map_list').click()
        self.driver.wait_loading()


        #向上滑动2屏
        order = self.driver.swipe_load_item('xlistview','nearbyriver','licensetype',page_size=2)

    #点击附近司机界面的“用户中心”按钮
    def test_centerbutton(self):

        #点击附近司机界面的“用户中心”按钮
        self.driver.find_id('btn_personal_center').click()

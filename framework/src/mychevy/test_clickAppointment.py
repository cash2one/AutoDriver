__author__ = 'zhangchun'
# coding=utf-8
import unittest
from time import sleep
from framework.core import the,device


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = the.android()

    def tearDown(self):
        #返回首页
        device.switchToHome(self,self.mainActivity)


    def test_case(self):
        #每个测试用例，都需要把首页加入到变量mainActivity
        self.mainActivity = self.driver.current_activity
        els=self.driver.find_elements_by_class_name('android.widget.ImageView')
        els[3].click()
        sleep(2)
        self.driver.switch_to_alert()
        txts=self.driver.find_elements_by_class_name('android.widget.EditText')
        txts[0].clear()
        txts[0].send_keys('hdfuo')
        txts[1].clear()
        txts[1].send_keys('13800000002')
        sleep(1)
        self.driver.find_element_by_name(u'确定').click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_name(u'确定').click()
        sleep(2)
        self.driver.find_elements_by_class_name('android.widget.Button')[0].click()

        self.driver.switch_to_alert()
        print self.driver.current_activity
        self.assertEqual('.OrderActivity',self.driver.current_activity)

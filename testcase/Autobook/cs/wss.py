# coding=utf-8
__author__ = 'wangshanshan@pathbook.com.cn'
#-*-coding=utf-8
from selenium import webdriver
import unittest

class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []

    def test_loginpass(self):
        driver = self.driver
        driver.get(self.base_url)
        nowhandle=driver.current_window_handle#在这里得到当前窗口句柄
        driver.find_id('kw').send_keys('selenium')
        driver.find_id('su').click()
        driver.find_element_by_xpath("//a[@title='selenium 安装']").click()
        aalhandles=driver.window_handles#获取所有窗口句柄
        for handle in aalhandles:#在所有窗口中查找弹出窗口
            if handle!=nowhandle:
                driver.switch_to_window(handle)#这两步是在弹出窗口中进行的操作，证明我们确实进入了
                driver.find_link("新闻").click()
        driver.switch_to_window(nowhandle)#返回到主窗口页面
        driver.find_id("kw").clear()#下面三步是返回到主窗口中进行的操作，证明我们确实返回了
        driver.find_id("kw").send_keys("python")
        driver.find_id("su").click()

    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

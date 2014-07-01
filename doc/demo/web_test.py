# coding=utf-8
__author__ = 'guohai@live.com'

import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']


def main():
    ff = webdriver.Firefox()
    ff.implicitly_wait(10) #设置网页打开超时时间
    ff.get("http://www.baidu.com")
    assert u'百度' in ff.title
    ff.execute_script("alert(123)")
    time.sleep(10)

    #截屏
    ff.save_screenshot('screenshot11.png')

    #find 输入框
    elem = ff.find_element_by_id('kw1')
    elem.send_keys("qq" + Keys.RETURN)
    #time.sleep(5)

    try:
        ff.find_element_by_xpath("//a[contains(@href,'http://baike.baidu.com/view/1535.htm?fr=aladdin')]")
    except NoSuchElementException:
        assert 0, "can't find baike"
    ff.close()


if __name__ == "__main__":
    main()
# coding=utf-8

__author__ = 'Administrator'

from selenium import webdriver as seleniumWeb
from appium import webdriver as appi

ANDROID='android'
IOS='ios'
WEB='web'

class Location(seleniumWeb.Remote):

    def __init__(self,driver):
        #self.driverType = driver_type
        super(Location, self).__init__(driver)
        self.driver=driver

    def findIdd(self):
        pass

    def findId(self,id):
        if 'firefox' in str(self.driver):
            return self.driver.find_element_by_id(id)
        elif 'ios' in str(self.driver):
            return self.driver.find_element_by_accessibility_id(id)
        elif 'android' in str(self.driver):
            return self.driver.find_element_by_android_uiautomator(id)

    def findName(self,name):
        return self.driver.find_element_by_name(name)

    def findClassName(self,name):
        return self.driver.find_element_by_class_name(name)

    def findTagName(self,name):
        return self.driver.find_element_by_tag_name(name)

    def findLinkText(self,text):
        return self.driver.find_element_by_link_text(text)

    def findPLinkText(self,text):
        return self.driver.find_element_by_partial_link_text(text)

    def findXpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

    def findCss(self,css):
        return self.driver.find_element_by_css_selector(css)

    def findIds(self,id):
        return self.driver.find_elements_by_id(id)

    def findNames(self,name):
        return self.driver.find_elements_by_name(name)

    def findClassNames(self,name):
        return self.driver.find_elements_by_class_name(name)

    def findTagNames(self,name):
        return self.driver.find_elements_by_tag_name(name)

    def findLinkTexts(self,text):
        return self.driver.find_elements_by_link_text(text)

    def findPLinkTexts(self,text):
        return self.driver.find_elements_by_partial_link_text(text)

    def findXpaths(self,xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def findCsss(self,css):
        return self.driver.find_elements_by_css_selector(css)

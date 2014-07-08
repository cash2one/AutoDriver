# coding=utf-8

__author__ = 'Administrator'

#from selenium import webdriver

# def driverType(type_str):
#     values = {
#            'web': findId,
#            'android': findName,
#            'ios': findClassName,
#          }
#     values.get('a')()

def findId(driver,id):
    if 'web' in str(driver):
        return driver.find_element_by_id(id)
    elif 'ios' in str(driver):
        return driver.find_element_by_ios_uiautomation(id)
    elif 'android' in str(driver):
        return driver.find_element_by_android_uiautomator(id)

def findName(driver,name):
    return driver.find_element_by_name(name)

def findClassName(driver,name):
    return driver.find_element_by_class_name(name)

def findTagName(driver,name):
    return driver.find_element_by_tag_name(name)

def findLinkText(driver,text):
    return driver.find_element_by_link_text(text)

def findPLinkText(driver,text):
    return driver.find_element_by_partial_link_text(text)

def findXpath(driver,xpath):
    return driver.find_element_by_xpath(xpath)

def findCss(driver,css):
    return driver.find_element_by_css_selector(css)

def findIds(driver,id):
    return driver.find_elements_by_id(id)

def findNames(driver,name):
    return driver.find_elements_by_name(name)

def findClassNames(driver,name):
    return driver.find_elements_by_class_name(name)

def findTagNames(driver,name):
    return driver.find_elements_by_tag_name(name)

def findLinkTexts(driver,text):
    return driver.find_elements_by_link_text(text)

def findPLinkTexts(driver,text):
    return driver.find_elements_by_partial_link_text(text)

def findXpaths(driver,xpath):
    return driver.find_elements_by_xpath(xpath)

def findCsss(driver,css):
    return driver.find_elements_by_css_selector(css)

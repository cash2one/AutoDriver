# coding=utf-8
__author__ = 'Administrator'

import os
import sys
import unittest
import ConfigParser

def loadSuite():
    casePath = sys.path[0] + os.sep + 'testcase'
    #findCase(casePath)

    discover = unittest.defaultTestLoader.discover(casePath)
    suite = unittest.TestSuite()
    for test_suit in discover:
        for test_case in test_suit:
            suite.addTests(test_case)
    return suite

#读取task配置文件
def readConfig(path_str):
    conf = ConfigParser.ConfigParser()
    conf.read(os.path.join(path_str, 'task.cfg'))

    sections = conf.sections()
    dictSuite = {}
    for s in sections:
        dictCase={}
        options = conf.options(s)
        for opt in options:#取出sections内的所有options
            str_val = conf.get(s, opt)
            dictCase[opt]=int(str_val)
        dictSuite[s]=dictCase
    return dictSuite

#读取所有loop不为0的TestCase
def findTestCasePath(dict):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    cf = base_dir + os.sep + 'testcase'
    for key in dict:
        for k in dict[key]:
            if dict[key][k]<>0:
                print cf+os.sep+key + os.sep +k + '.py'

def sendMsg():
    pass

def finish():
    sendMsg()
    pass

def myService():
    pass


if __name__ == "__main__":
    print findTestCasePath(readConfig(''))
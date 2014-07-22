__author__ = 'Administrator'
# coding=utf-8

import os
import re
import sys
import unittest
from util import xls
from util import fs


#获取序列中的script 集合
def getScripts(xlss):
    scripts=[]
    for js in xlss:
        scripts.append(js['script'])
    return scripts

def loadSuite(xlss):
    suite = unittest.TestSuite()
    c=fs.PATH('../testcase/')

    scripts=getScripts(xlss)

    disc = unittest.defaultTestLoader.discover(c,'test*.py',None)

    for test_suit in disc:
        for test_case in test_suit:
            # if 'autobook_' in str(test_case):
            #     print '--aaa'
            if getCaseName(str(test_case)) in scripts:
                suite.addTests(test_case)
    return suite

def getCaseName(con):
    re_symbol = re.compile(r'(?<=\[\<).*?(?=\.TestCase)')#接口正则
    match=re_symbol.search(con)
    if match:
        return match.group()

# def regressionTest():
#     path = fs.PATH('../testcase/')
#     files = os.listdir(path)
#     #print files
#     test = re.compile("^test.*?.py$", re.IGNORECASE)
#     files = filter(test.search, files)
#
#
#     filenameToModuleName = lambda f: os.path.splitext(f)[0]
#
#     moduleNames = map(filenameToModuleName, files)
#
#     sys = __import__('sys', fromlist = ['testcase'])
#
#     modules = map(__import__, moduleNames)
#     load = unittest.defaultTestLoader.loadTestsFromModule
#     return unittest.TestSuite(map(load, modules))

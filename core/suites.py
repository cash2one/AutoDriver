__author__ = 'Administrator'
# coding=utf-8

import os
import re
import sys
import unittest
from util import xls
from util import fs

def readConfXls():
    path = fs.PATH('../config')
    f = os.listdir(path)
    re_f=re.compile(".xls$", re.IGNORECASE)
    files = filter(re_f.search, f)
    list=[]

    for x in files:
        filename = fs.PATH('../config/'+os.path.basename(x))
        xlss=xls.Excel(filename)
        j= xlss.readTestCaseByConf()
        for s in j:
            list.append(os.path.splitext(x)[0]+'.'+s['script'])
    return list

def discoverPath():
    #casePath = sys.path[0] + os.sep + 'testcase'
    #findCase(casePath)
    discover = unittest.defaultTestLoader.discover('')
    suite = unittest.TestSuite()
    for test_suit in discover:
        for test_case in test_suit:
            suite.addTests(test_case)
    return suite

def loadSuite():
    suite = unittest.TestSuite()
    c=fs.PATH('../testcase/')
    scripts=readConfXls()

    #for root, dis, files in os.walk(c):

    disc = unittest.defaultTestLoader.discover(c,'test*.py',None)

    #与excel 脚本对比
    # files = filter(re_f.search, files)
    # for f in files:
    #     if os.path.basename(f) in readConfXls():
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

if __name__ == "__main__":
    #print loadSuite()
    print loadSuite()
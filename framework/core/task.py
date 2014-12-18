# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os,sys,re
import unittest
from framework.util import constant

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append('testcase')

class Task():

    __state = False
    __testDatas=[]
    __polling = False
    task_id = 0

    def __init__(self,state,test_Datas):
        self.__state = state
        self.__testDatas = test_Datas

    def getState(self):
        return self.__state

    # def getLoopScripts(self):
    #     scripts=[]
    #     for ts in self.__testDatas:
    #         if ts['loop'] > 0:
    #             t=ts['script'].replace('.','_')
    #             scripts.append('test_'+t)
    #     return scripts
    def recombineFileName(self,xs):
        new_cat = xs['cat'].replace('_' + constant.FLOW_NAME,'')
        if xs['script'] == '':
            new_script = str(xs['no'])
        else:
            new_script = xs['script']
        return 'test_%s_%s' % (new_cat,new_script)


    def getTestData(self):
        datas = []
        for ts in self.__testDatas:
            if ts['loop'] > 0:
                datas.append(ts)
        return datas

    def getTestSuite(self):
        #重新获取loop不为0的脚本
        #loop_scripts=self.getLoopScripts()

        path = PATH('../../testcase/')

        test = re.compile("^test.*?.py$", re.IGNORECASE)
        files = filter(test.search, os.listdir(path))

        filenameToModuleName = lambda f: os.path.splitext(f)[0]
        moduleNames = map(filenameToModuleName, files)

        run_testcase = []
        #通过载入的testcase 对读取的xlss进行筛选
        for ts in self.__testDatas:
            #t = 'test_'+ts['script'].replace('.','_')
            t = self.recombineFileName(ts)
            loop = ts['loop']
            if t in moduleNames and loop > 0:
                run_testcase.append(ts)
        self.__testDatas = run_testcase
        #print self.__testDatas

        #print loop_scripts

        #筛选不在scirpts[]中的脚本
        new_lists=[]
        for f in moduleNames:
            if f in run_testcase:
                new_lists.append(f)

        #sys.path.append('testcase')
        modules = map(__import__, moduleNames)
        load = unittest.defaultTestLoader.loadTestsFromModule
        return unittest.TestSuite(map(load, modules))

    def isFinish(self):
        pass

    def isRunning(self):
        pass


    def start(self):
        #print self.getTestSuite()
        self.__state = True

    def finish(self):
        self.__state = False

        #所有测试用例的count-1
        for td in self.__testDatas:
            if td['loop'] > 0:
                 td['loop'] -= 1

    # def getCustomerToken(self):
    #     self.__customer_token=''
    #
    # def setCustomerToken(self,):
    #     __customer_token = ''



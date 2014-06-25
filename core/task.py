__author__ = 'xiuhong'

import sys
import os
import unittest

class Task():

    def __init__(self,dict_case):
        self.dictCase=dict_case
        self.casePath = sys.path[0] + os.sep + 'testcase'

    def updateDict(self):
        self.dictCase={}

    def getDictCase(self):
        return self.dictCase

    def loadSuite(self):
        #self = sys.path[0] + os.sep + 'testcase'
        #findCase(casePath)
        #self.getDictCase()

        for k,v in self.getDictCase().iteritems():
            print "dict[%s]=" % k,v



        discover = unittest.defaultTestLoader.discover(self.casePath)
        suite = unittest.TestSuite()
        for test_suit in discover:
            for test_case in test_suit:
                suite.addTests(test_case)
        return suite



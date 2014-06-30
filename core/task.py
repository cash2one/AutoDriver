__author__ = 'xiuhong'

import sys
import os
import unittest

class Task():

    def __init__(self,dict_case):
        self.dictCase=dict_case
        self.casePath = sys.path[0] + os.sep + 'testcase'

    def updateDict(self):
        self.dictCase = {}

    def getDictCase(self):
        return self.dictCase



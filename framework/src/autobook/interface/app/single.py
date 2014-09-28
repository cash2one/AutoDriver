# coding=utf-8
__author__ = 'Administrator'

import unittest
from framework.modules import interface

class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_interface(self):
        desc = u'{{description}}'
        exp = u'{{expectation}}'
        interface.assertResult(self,desc,exp)
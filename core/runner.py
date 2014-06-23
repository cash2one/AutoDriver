__author__ = 'Administrator'

import unittest

class Runner(unittest.TextTestRunner):

    def run(self, test):
        unittest.TextTestRunner.__init__(self)
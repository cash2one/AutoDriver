__author__ = 'xiuhong'


import unittest
from test import test_support

class MyTestCase(unittest.TestCase):
    def setUp(self):
        #some setup code
        pass

    def clear(self):
        #some cleanup code
        pass

    def action(self, arg1, arg2):
        pass

    @staticmethod
    def getTestFunc(arg1, arg2):
        def func(self):
            self.actions(arg1, arg2)
            return func

def __generateTestCases():
     arglists = [('arg11', 'arg12'), ('arg21', 'arg22'), ('arg31', 'arg32')]
     for args in arglists:
         setattr(MyTestCase, 'test_func_%s_%s'%(args[0], args[1]), MyTestCase.getTestFunc(*args))
__generateTestCases()


if __name__ =='__main__':
    test_support.run_unittest(MyTestCase)
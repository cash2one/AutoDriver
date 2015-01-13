# coding=utf-8
__author__ = 'gaoxu'
import unittest

class TestCase(unittest.TestCase):
    def test_case1(self):
        for i in range(1,10):
            for j in range(1,10):
                k=i*j
                print k


    def test(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print(" %d*%d=%d" % (j,i,i*j)),
                print '\n'

    def test2(self):
        for i in range(1, 10):
            print " ".join(["%d*%d=%d" % (j, i, i*j) for j in range(1, i+1)])


    def test_3(self):
        for i in range(1,10):
            for j in range(1, i+1):
                 k=i*j
                 print k,
                 if k%2==0:
                    print ".",
                 else:
                   print ",",
            print ""















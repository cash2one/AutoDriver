__author__ = 'Administrator'
# coding=utf-8

import os
import sys
import ConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def filePath(file_path,isParentPath):
    if file_path is not None and file_path != '':
        if(isParentPath):
            spl=os.path.split(file_path)[0]
            return spl.split(os.sep)
        else:
            return os.path.dirname(file_path)
    else:
        print('is empty or equal None!')


#遍历文件夹，获取所有文件夹内和子文件夹的所有文件路径
def findCase(folder):
    for root, dis, files in os.walk(folder):
        for file in files:
            print root + os.sep + file


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
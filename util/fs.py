__author__ = 'Administrator'
# coding=utf-8
"""
各种文件操作方法 集合
"""


import os
import sys
import re
import ConfigParser

base_dir = os.path.dirname(os.path.dirname(__file__))

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

    list_file=[]
    find_file=re.compile("^test.*?.py$", re.IGNORECASE)

    for root, dis, files in os.walk(folder):
        for file in files:
            #print os.path.dirname(file)
            if find_file.search(file):
                list_file.append(file)
    return list_file


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

#读取task配置文件
def readConfigs(path_str,selections):
    conf = ConfigParser.ConfigParser()
    conf.read(path_str)

    sections = conf.sections()

    dictCase={}
    options = conf.options(selections)
    for opt in options:#取出sections内的所有options
        str_val = conf.get(selections, opt)
        dictCase[opt]=str_val.decode('utf-8')

    return dictCase


#读取所有loop不为0的TestCase
def findTestCasePath(dict):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    cf = base_dir + os.sep + 'testcase'
    for key in dict:
        for k in dict[key]:
            if dict[key][k]<>0:
                print cf+os.sep+key + os.sep +k + '.py'

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def scanKeyword(str):
    p=PATH('../config/settings.cfg')
    kw= readConfigs(p,'excel_keyword')

    if str==kw['begin']:
        return 1
    elif str==kw['end']:
        return 0
    else:
        return -1

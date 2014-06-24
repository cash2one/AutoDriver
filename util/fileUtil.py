__author__ = 'Administrator'
# coding=utf-8

import os
import sys
import ConfigParser

def filePath(file_path,isParentPath):
    if file_path is not None and file_path != '':
        if(isParentPath):
            spl=os.path.split(file_path)[0]
            return spl.split(os.sep)
        else:
            return os.path.dirname(file_path)
    else:
        print('is empty or equal None!')

#读取config到字典
def readConfig():
    dict={}
    conf = ConfigParser.ConfigParser()
    conf.read(sys.path[0] + os.sep+'task.cfg')
    #sections = conf.sections()
    options = conf.options('task')
    for opt in options:
        str_val = conf.get('task', opt)
        dict[opt]=str_val
    return dict

#遍历文件夹，获取所有文件夹内和子文件夹的所有文件路径
def findCase(folder):
    for root, dis, files in os.walk(folder):
        for file in files:
            print root + os.sep + file


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


__author__ = 'Administrator'

import os
import sys
import ConfigParser

def getPath(folder_name):
    pass
    # p=os.path.dirname(os.path.abspath(__file__))
    #
    # if folder_name:
    #
    # return os.path.dirname(p)+os.sep+folder_name


def currentPath():
    return os.path.dirname(__file__)


def readConfig():
    dict={}
    conf = ConfigParser.ConfigParser()
    conf.read(sys.path[0] + os.sep+'config.cfg')
    #sections = conf.sections()
    options = conf.options('task')
    for opt in options:
        str_val = conf.get('task', opt)
        dict[opt]=str_val
    return dict


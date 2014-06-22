__author__ = 'xiuhong'

import sqlite3


class DbHelper():

    def __init__(self,mPath):
        self.mPath=mPath

    def getConn(self):
        return sqlite3.connect(self.mPath)

    def create_table_test():
        pass

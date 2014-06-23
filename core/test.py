__author__ = 'Administrator'

import os
import db

def dbPath(db_path):
    p=os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(p)+os.sep+'settings'+os.sep+db_path

def main():
    db.get_conn(dbPath('autotest.db'))

if __name__ =='__main__':
    main()
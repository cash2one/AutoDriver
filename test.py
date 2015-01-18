__author__ = 'Administrator'

import sys

def add_path():
    import webbrowser
    webbrowser.open('http://www.baidu.com')

if __name__ == "__main__":
    add_path()
    add_path()
    print sys.path
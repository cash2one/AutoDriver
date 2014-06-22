# coding=utf-8
__author__ = 'guohai@live.com'

import urllib2


# 读取网页HTML,写入到文件
def getWebContent(file_path, url):
    f = open(file_path, 'w')
    html = urllib2.urlopen(url).read()
    f.write(html)
    f.close()

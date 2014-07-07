# coding=utf-8
__author__ = 'guohai@live.com'

import urllib2
import httplib2


# # 读取网页HTML,写入到文件
# def getWebContent(file_path, url):
#     f = open(file_path, 'w')
#     html = urllib2.urlopen(url).read()
#     f.write(html)
#     f.close()


def getHttp(url):
    h=httplib2.Http(".cache",timeout=10)
    return h.request(url, "GET",headers={'cache-control':'no-cache',"Accept": "application/json"})
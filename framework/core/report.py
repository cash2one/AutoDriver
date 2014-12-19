# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import re
import views
import shutil
from framework.util import sqlite

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Report():

    def __init__(self,db_path,page):
        self.page = page
        self.dbm = sqlite.DBManager(db_path)
        self.root = PATH('../../report/')
        self.assets = PATH('./assets/')
        self.folders = ('styles','images','scripts')

        pattern = re.compile(r'(?<=result).*?(?=.db)')
        match=pattern.search(db_path)
        if match:
            self.date_time = match.group()
        else:
            self.date_time = ''

    def close(self):
        self.dbm.close_db()

    def start(self):
        self.copyAssets(self.assets)
        file_name = 'autobook_interface'
        #data = 'select * from TestCase where cat=file_name'

        data = self.dbm.fetchall('select TestCase_Id,ExecuteResult,ResultDesc,ExecuteDT from Result')
        if data!=None:
            self.pages(file_name,data,True)
        self.close()

    def copyAssets(self,path):
        for s in self.folders:
            src = os.path.join(self.assets,s)
            tar = os.path.join(self.root,s)
            if not os.path.isdir(tar):
                shutil.copytree(src,tar)

    def pages(self,file_name,data,isList):
        if isList:
            datas = self.pagination(file_name,data)
            for ds in datas:
                fi = open(os.path.join(self.root,ds+'.html'),'w')
                html = views.result(datas[ds],datas.keys())
                fi.write(html)
                fi.close()
        else:
            #未完成
            fi = open(os.path.join(self.root,file_name+'.html'),'w')
            html = views.result(data,'')
            fi.write(html)
            fi.close()

    #数据分页
    def pagination(self,file_name,data):
        k = 0
        n = 0 #页码
        data_dict = {}
        for i in range(self.page,len(data),self.page):
            _data = []
            for d in range(k,i):
                _data.append(data[d])
            k = i

            n+=1
            f_name = '%s%s' % (file_name,n)

            data_dict[f_name] = _data

        #剩余的数据
        left_data = []
        if len(data)-k >0:
            for k in range(k,len(data)):
                left_data.append(data[k])
        data_dict[file_name+str(n+1)] = left_data

        return data_dict


# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
import re
import json
import datetime

from framework.core import models, box
from framework.core import box
from framework.util import xls,const,sqlite


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

settings = PATH('../../config.ini')
product_json = PATH('../config/product.json')

#server_url = the.settings['interface']['url']


#读取制定xls文件的数据
def getExcelData(excel):
    #excel = xls.Excel(path,constant.EXCEL_HEADER,skip_cat)
    xls = excel.openExcel()
    sheets = xls.sheets()
    titles = sheets[0].row_values(0)#excel表头

    list = []

    for i in range(0,len(sheets)):#sheet:#遍历所有Sheet
        temp = {}
        isBegin = False
        for n in range(1, sheets[i].nrows):#遍历所有行
            new_titles,new_rows = excel.filterRows(titles,sheets[i].row_values(n))
            app = excel.getCellsValue(new_rows,new_titles,i)

            #判断是否存在流程类用例
            if '_begin' in app['cat']:
                app['cat'] = app['cat'].replace('begin','flow')
                isBegin = True
            elif '_end' in app['cat']:
                isBegin = False

            if isBegin:
                #判断是否首次添加temp，如果是，则把第一条记录插入到temp
                if len(temp) <= 0:
                    #begin开始行，作为字典
                    temp = app
                if app['desc']!='':
                    temp['desc'] += app['desc'] + const.SEP
                if app['exp']!='':
                    temp['exp'] += app['exp'] + const.SEP
                if temp['script'] == '':
                    temp['script'] = app['script']
            else:
                #结束时，判断temp是否被添加
                if len(temp) > 0:
                    #在这里判断已经组装完成的流程字典，屏蔽loop=0
                    if temp['loop'] > 0:
                        list.append(temp)
                    temp={}
                else:
                    if app['loop'] > 0:
                        list.append(app)
    return list



#读取制定目录内的所有xls文档
def getExcelsData(xls_dir,skip_cat):
    # f = os.listdir(xls_dir)
    # re_f=re.compile(".xls$", re.IGNORECASE)
    # files = filter(re_f.search, f)

    products = box.settings['product']

    list=[]

    for p in products:
        xls_path = os.path.join(xls_dir, p+'.xls')
        try:
            val = products[p].strip()#.split(',')[1]
            if int(val) == 1:
                excel = xls.Excel(xls_path,const.EXCEL_HEADER,skip_cat)
                if excel.openExcel() != None:
                    list.extend(getExcelData(excel))
                # else:
                #     break
        except IndexError:
            print u'ini文件缺少索引值'
        except ValueError:
            print u'ini文件数值类型错误'

    # for x in files:
    #     f = os.path.basename(x)
    #     f_name = os.path.splitext(f)[0]
    #     dir = xls_dir + os.sep + f
    #     #如果ini文件里指定了 xls的读取状态值0、1,则根据状态值筛选xls，没指定则默认读取
    #     if f_name in products.keys():
    #         try:
    #             val = products[f_name].strip()#.split(',')[1]
    #             if int(val) == 1:
    #                 excel = xls.Excel(dir,constant.EXCEL_HEADER,skip_cat)
    #                 list.extend(getExcelData(excel))
    #         except IndexError:
    #             print u'ini文件缺少索引值'
    #         except ValueError:
    #             print u'ini文件数值类型错误'
    #     else:
    #         list.extend(getExcelData(dir,excel))

    return list


def sortTestCase(xls_path):
    excel = xls.Excel(xls_path,const.EXCEL_HEADER,False)
    data = excel.openExcel()
    sheets = data.sheets()
    titles = sheets[0].row_values(0)#excel表头
    time_val = datetime.datetime.now()

    xls_file = os.path.basename(xls_path).replace('.xls','')

    #f_name = os.path.splitext(xls_path)[0]

    testcases = []
    modules = []
    temp_modules = []

    for i in range(0,len(sheets)):#sheet:#遍历所有Sheet
        isBegin = False
        flow = []
        tup_flow = ()

        for n in range(1, sheets[i].nrows):#遍历所有行
            new_titles,new_rows = excel.filterRows(titles,sheets[i].row_values(n))
            app = excel.getCellsAllValue(new_rows,new_titles,i)
            tup = (
                xls_file,
                app['no'],
                # app['cat'],
                # app['script'],
                # app['loop'],
                time_val
            )

            module_names = app['cat'].split('\\')
            module_name = module_names[-1]

            if 'begin' in app['cat']:
                isBegin = True
            elif 'end' in app['cat']:
                isBegin = False


            if not 'begin' in app['cat'] and not 'end' in app['cat']:

                if app['cat']!='':
                    temp_modules.append(app['cat'])

                if isBegin:
                    if len(tup_flow) <= 0:
                        tup_flow = tup
                    flow.append((module_name,))#,app['desc'],app['exp']))#,time_val))
                else:
                    print app['no'],'-----'
                    if len(flow) > 0:
                        print app['no']
                        temp_tup = (tup_flow[0],tup_flow[1],flow,tup_flow[2],)
                        testcases.append(temp_tup)

                        flow = [(module_name,)]#,app['desc'],app['exp'])]#,time_val))
                        temp_tup = (tup[0],tup[1],flow,tup[2],)
                        testcases.append(temp_tup)

                        flow=[]
                        tup_flow = ()
                    else:
                        flow = [(module_name,)]#,app['desc'],app['exp'])]#,time_val))
                        new_t1 = (tup[0],tup[1],flow,tup[2],)
                        testcases.append(new_t1)
                        flow=[]

    filter_modules = set(temp_modules)
    for cat in filter_modules:
        module_names = cat.split('\\')

        module_name = module_names[-1]
        d = (xls_file,module_name,'',1,1,cat,0,'tree_id_path',time_val,time_val,1)
        modules.append(d)

    return modules,testcases



def getDatabasePath(db_dir):
    '''
    如果the.db_path为空，则读取最新的数据库
    :return:数据库路径
    '''
    if box.db_path == '':
        db_files_name = []
        files = os.listdir(db_dir)
        for file in files:
            # pattern = re.compile(r'(?<=report).*?(?=.db)')
            # match=pattern.search(os.path.basename(file))
            # if match:
            #     db_files_name.append(match.group())
            pattern = re.compile(r'^report.*?.db$')
            match = pattern.match(os.path.basename(file))
            if match:
                db_files_name.append(match.group())
        if len(db_files_name) > 0:
            db_path = os.path.join(db_dir,max(db_files_name))
        else:
            db_path = ''
    else:
        db_path = os.path.join(db_dir, box.db_path)
    return db_path


def getProducts(product_path):
    '''
    从config/product.json中读取产品信息
    :param product_path:
    :return:
    '''
    file_product = open(product_path)
    try:
         txt_product = file_product.read()
         product_json = json.loads(txt_product)
    finally:
         file_product.close()

    products = []
    product_types = []

    for p in product_json:
        product_name = p['product_name']
        product_desc = p['product_desc']
        product_platform = p['product_platform']
        isEnable = p['isEnable']
        tup = (product_name,product_desc)

        #字典排序
        temp = sorted(product_platform.iteritems(),key=lambda asd:asd[0],reverse=False)

        for pf in temp:
            if len(pf[1]) >0:
                for pff in pf[1]:
                    #print pff,'---',pf[0],'---',product_name
                    product_types.append((product_name,pff,pf[0],1))
                osExist = True
            else:
                osExist = False
            tup+=(osExist,)

        tup+=(isEnable,)
        products.append(tup)
    return products,product_types



#读取制定xls文件的数据
def getExcelAllData(excel):
    data = excel.openExcel()
    sheet = data.sheets()

    titles = sheet[0].row_values(0)#excel表头
    list = []

    for i in range(0,len(sheet)):#sheet:#遍历所有Sheet
        for n in range(1, sheet[i].nrows):#遍历所有行
            new_titles,new_rows = excel.filterRows(titles,sheet[i].row_values(n))
            app = excel.getCellsValue(new_rows,new_titles,i)
            list.append(app)
    return list

def getDataFromXlss(xls_path):
    '''
    从xls文件中读取数据
    :param xls_path:
    :return:模块,所有的用例
    '''
    time_val = datetime.datetime.now()
    products = box.settings['product']
    data_module = []
    all_testcase = []
    for p in  products:
        dir = os.path.join(xls_path,p+'.xls')

        #excel = xls.Excel(dir,constant.EXCEL_HEADER,True)
        m,t = sortTestCase(dir)
        data_module.extend(m)
        all_testcase.extend(t)
        # list1 = getExcelAllData(excel)
        #
        # cats = []
        # for c in list1:
        #     if not 'begin' in c['cat'] and not 'end' in c['cat'] and c['cat']!='':
        #         cats.append(c['cat'])
        #
        #     xls_row = (p,c['no'],c['cat'],c['desc'],c['exp'],c['script'],c['loop'])
        #     all_testcase.append(xls_row)
        #
        # filter_cats = set(cats)
        # for cat in filter_cats:
        #     module_names = cat.split('\\')
        #     module_name = module_names[-1]
        #     d = (p,module_name,'',1,1,cat,0,'tree_id_path',time_val,time_val,1)
        #     data_module.append(d)

    return data_module,all_testcase


class generateData():

    def __init__(self,xls_path,db_path):
        self.xls_path = xls_path
        self.dbm = sqlite.DBManager(db_path)

        self.cursor = self.dbm.get_cursor()
        self.conn = self.dbm.conn

        self.initTable(self.dbm)
        #self.initData()

    def initTable(self,_dbm):
        #初始化，建表
        sql_list = models.sql(models.Tables())

        for sql in sql_list:
            self.cursor.execute(sql)
            self.conn.commit()
        self.cursor.close()

    def initData(self):
        products,types = getProducts(product_json)

        modules_info = []
        new_types = []
        all_testcases = []


        #插入产品和产品类型数据
        for p in products:
            p_id = self.init_product(p)

            for t in types:
                #pt_id = self.init_productType(p,t,p_id)
                #t+=(pt_id,)
                if len(new_types)!=len(types):
                    new_types.append(t)


        for nt in new_types:
            product_type_name = nt[0]+'_'+nt[2]+'_'+nt[1]

            dir = os.path.join(self.xls_path,product_type_name+'.xls')

            if os.path.exists(dir):
                modules,testcases = sortTestCase(dir)

                for m in modules:
                    m_id = self.init_module(m,product_type_name,nt[-1])
                    modules_info.append((m_id,m[1]))

                for t in testcases:
                    tc_id = self.init_testcase(t)
                    for td in t[2]:
                        print len(t[2])
                        for mm in modules_info:
                            if td[0] == mm[1]:
                                self.init_testcaseDetail(td,tc_id,mm[0])
                                break


    def init_product(self,data):
        sql = "INSERT INTO Product values (NULL,?,?,?,?)"
        return self.dbm.insert_value(sql,data)

    # def init_productType(self,product,product_type,pid):
    #     sql_t = "INSERT INTO ProductType values (NULL,?,?,?,?)"
    #
    #     if product[0] == product_type[0]:
    #         #去除第一个作为匹配product的name，加入product的id，重新生成一个元组
    #         tu = ()
    #         for i in range(1,len(product_type)):
    #             tu+=(product_type[i],)
    #         tu+=(pid,)
    #
    #         return self.dbm.insert_value(sql_t,tu)
    #     else:
    #         return 0

    def init_module(self,module,p_type_name,pt_id):
        sql = "INSERT INTO Module values (NULL,?,?,?,?,?,?,?,?,?,?,?)"
        if pt_id == 0:
            return

        moduleTup = ()
        ms = module[0].split('_') #interface最后一位可能带创建者名

        p_name = '_'.join(ms[0:3])

        if p_name == p_type_name:
            for n in range(1,len(module)):
                moduleTup += (module[n],)
            moduleTup+=(pt_id,)
        if len(moduleTup) > 0:
            return self.dbm.insert_value(sql,moduleTup)
        else:
            return 0

    def init_testcase(self,testcase):
        sql = "INSERT INTO TestCase values (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)"

        #non_flow = (module_name,app['desc'],app['exp'])
        #tup = (xls_file,app['no'],app['cat'],[non_flow],app['script'],app['loop'])

        t = ('testcase_name',testcase[-1],'usename','priority',001,'desc',testcase[3],1,1,'tag','abs',testcase[-1],testcase[-1])
        return self.dbm.insert_value(sql,t)

    def init_testcaseDetail(self,detail,tc_id,m_id):
        sql = "INSERT INTO TestCaseDetail values (NULL,?,?,?,?,?)"
        data = (detail[1],detail[2],1,tc_id,m_id)
        return self.dbm.insert_value(sql,data)

    def close(self):
        self.dbm.close_db()




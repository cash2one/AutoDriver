# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import re
import shutil
from framework.util import sqlite

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


HTML_HEADER = r'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>测试报告%(report_time)s</title>
<meta name="description" content="">
<link type="text/css" href="./styles/layout.css" rel="stylesheet" media="all" />
<link type="text/css" href="./styles/default.css" rel="stylesheet" media="all" id="skin" />

<script type="text/javascript" src="./scripts/jquery-1.9.0.js"></script>
<script type="text/javascript" src="./scripts/jquery.mousewheel.js"></script>
<script type="text/javascript" src="./scripts/jquery.jscrollpane.min.js"></script>

<script type="text/javascript" src="./scripts/result.js"></script>
<script type="text/javascript">
$(function(){
     swichStyle("skin","switchSkin","styles/");

	 $(window).resize(function() {
		$('#dataArea').jScrollPane({showArrows: true});
		$('#leftBar').jScrollPane({showArrows: true});
	});
});

</script>
</head>
<body>
<div class="header">
	<div class="logo-menu">
		 <h1>测试报告%(report_time)s-durationTime</h1>
		 <ul class="menu">
		 	<li><a href="#" onclick="showbox(this,'#switchSkin',event)" class="settings"></a></li>
			<li><a href="#" onclick="showbox(this,'#uploadFiles',event)" class="upload"></a></li>
		 </ul>
		 <div id="switchSkin" class="menubox">
			 <h3>Skin</h3>
			 <ul>
				<li id="default">&nbsp;</li>
				<li id="darkgreen">&nbsp;</li>
				<li id="olivine">&nbsp;</li>
				<li id="blue">&nbsp;</li>
				<li id="darkblue">&nbsp;</li>
				<li id="modena">&nbsp;</li>
				<li id="lightblue">&nbsp;</li>
				<li id="purple">&nbsp;</li>
				<li id="pink">&nbsp;</li>
				<li id="crimson">&nbsp;</li>
				<li id="red">&nbsp;</li>
				<li id="brown">&nbsp;</li>
				<li id="orange">&nbsp;</li>
				<li id="yellow">&nbsp;</li>
				<li id="black">&nbsp;</li>
				<li id="gray">&nbsp;</li>
			 </ul>
			 <h3>Feedback</h3>
			 <h3>Clear Cookie</h3>
		 </div>
		 <div id="uploadFiles" class="menubox">
			<h3>Upload Files</h3>
			<ul>
			    <!--li><iframe src='http://www.url.com' border='0' width='200' height='150'></iframe</li-->
				<li>Select TestResult Folder<input type="file" size="58" /></li>
				<li>Select Images Folder<input type="file" size="58" /></li>
				<li class="btn">
					<input type="button" value="Cancel" />
					<input type="button" value="Upload" />
				</li>
			</ul>
		 </div>
	</div>
	<div class="nav">
		<div class="changeDate">
			<!--input type="text" value="Result List" id="SelectDate" onchange="refreshXML(this)" /><a href="#" onclick="showbox(this,'.calendarBox',event)">&nbsp;</a-->
			<input type="text" value="Result List" id="SelectDate" /><!-- onchange="refreshXML(this)" />
			<a class="date" href="#" onclick="showbox(this,'#dateList',event)">&nbsp;</a>
			<div id="dateList">
				<h3>2013年3月份:</h3>
				<ul>
					<li>1</li>
					<li>2</li>
					<li>3</li>
				</ul>
				<h3>2013年4月份:</h3>
				<ul>
					<li>1</li>
					<li>2</li>
					<li>3</li>
				</ul>
			</div-->
		</div>
		<div class="" id="ResultCount">
			<ul>
			<li>&nbsp;&nbsp;<input type='radio' checked="checked" name='showTable' id="Totle" onclick='SortByRootCause()' />
				<label for="Totle">Totle Case：</label><span class="TotleCaseCount"></span>
			</li>
			<li><input type='radio' name='showTable' id="Pass" onclick='SortByRootCause()' />
				<label for="Pass">Pass：</label><span class="PassCount">%(PassCount)s</span>
			</li>
			<li><input type='radio' name='showTable' id="Failure" onclick='SortByRootCause()' />
				<label for="Failure">Failure：</label><span class="FailureCount">%(FailureCount)s</span>
			</li>
			<li><input type='radio' name='showTable' id="Failure" onclick='SortByRootCause()' />
				<label for="Failure">Error：</label><span class="FailureCount">%(ErrorCount)s</span>
			</li>
            <li class="pages"><ul style="padding:0;margin:0;">%(li)s</ul></li>
			</ul>
	</div>
	</div>
</div>
<div id="leftBar" class="bg01">
     <ul id="resultList">
        <!--li><a href='#' onclick='clk(this)'>autobook_interface</a></li-->
        <li><a href='#'>autobook_interface</a></li>
        <li><a href='#'>autobook_android_customer</a></li>
        <li><a href='#'>autobook_android_driver</a></li>
     </ul>
</div>

<div id="dataArea">
	<div class="dataList">%(result_data)s</div>
</div>

</body>
</html>
'''


HTML_TABLE_RESULTS=r'''
<h3>project_Name</h3>
<table cellpadding='5' cellspacing='0' border='0' width='98%%'>
<tr>
    <th>Testcase</th>
    <th>Count</th>
    <th>Pass</th>
    <th>Fail</th>
    <th>Error</th>
    <th width='150px'>UpdateTime</th>
    <th>Detail</th>
</tr>
%(tbody)s
</table>
'''

class Report():

    def __init__(self,db_path,page_size=25):
        self.page = page_size
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
                html = self.result(datas[ds],datas.keys())
                fi.write(html)
                fi.close()
        else:
            #未完成
            fi = open(os.path.join(self.root,file_name+'.html'),'w')
            html = self.result(data,'')
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


    def result(self,data,link_names):
        trs = ''
        li_str = ''
        pass_count = 0
        fail_count = 0
        error_count = 0

        for r in data:
            td = ''
            td_status = ''
            for i in range(0,len(r)):
                td += '<td>%s</td>\n' % str(r[i])

            tr = '<tr class="%s">\n%s</tr>\n' % (td_status,td)
            trs += tr

        data_list = HTML_TABLE_RESULTS % dict(tbody = trs)

        link_names_sort = sorted(link_names)
        for n in range(0,len(link_names_sort)):
            li_str += '<li><a href="%s.html">%s</a></li>' % (link_names_sort[n],n+1)

        result_str = 'pass:%s, fail:%s, error:%s' %(pass_count,fail_count,error_count)

        html_dict = dict(
            report_time = '2014',
            result_num = result_str,
            li = li_str,
            PassCount = 0,
            FailureCount = 0,
            ErrorCount = 0,
            result_data = data_list,
        )

        html = HTML_HEADER
        return html % html_dict
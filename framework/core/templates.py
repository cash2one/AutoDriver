# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

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

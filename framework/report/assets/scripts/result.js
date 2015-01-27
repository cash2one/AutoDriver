function SortByRootCause() {
	var testType = $("#ResultCount li").find("input:checked").attr("id");
	var tb = $("#dataArea .dataList table");
	if (testType == "Totle") {
		tb.find("tr td").show();
	} else if (testType == "Pass") {
		tb.find("tr td").show();
		tb.find("tr.fail td").hide();
	} else {
		tb.find("tr td").show();
		tb.find("tr:not('.fail') td").hide();
	}
}

function GetNameByPython(py, str) {
	var ds, c, arr = [];
	var s = str.split(",");
	for (var j = 0; j < s.length; j++) {
		ds = py.split("common." + s[j] + "(");
		for (var k = 1; k < ds.length; k++) {
			c = ds[k].split(")")[0].match(/[\'"](.*?)[\'"]/)[1];
			var cr=c.replace("/.","_");
			arr.push(cr);
		}
	}

	//去除数组中重复
	var newArr = [];
	for (var i = 0, len = arr.length; i < len; i++) {
		! RegExp(arr[i], "g").test(newArr.join(",")) && (newArr.push(arr[i]));
	}
	return newArr;
}

function showPic(obj, testcase, cycle, loop,date) {
	var fileName = "TestCase/" + testcase + "/" + testcase + ".txt"
	// $.ajax({
		// url : fileName,
		// type : 'GET',
		// timeout : 3000,
		// error : function(data) {
			// alert(fileName);
			// alert("error");
		// },
		// success : function(data) {
			// var imgArr = GetNameByPython(data, "checkImage,checkSubImage,checkOriginalImage,assertCurrentActivity");
	$.ajax({
		url : fileName,
		dataType : 'text',
		type : 'GET',
		timeout : 2000,
		error : function(text) {
			alert("error");
		},
		success : function(text) {
			
			var imgArr = GetNameByPython(text, "checkImage,checkSubImage,checkOriginalImage,assertCurrentActivity");

			var path, imgFail, imgPass, imgs = "";
			for (var k = 0; k < imgArr.length; k++) {
				var lastFileName;
				if(imgArr[k].indexOf("com.")!=-1 && imgArr[k].indexOf("_")!=-1){
					lastFileName="_AcitivityFail_"+date+".png";
				}
				else{
					lastFileName="_Fail_"+date+".png";
				}
				
				imgPass = imgArr[k] + ".png";
				imgFail = imgArr[k] + "_" + cycle + "_Loop" + loop + lastFileName//BTSearch_Cycle1_Loop1_Fail.png
				//<img width='100' src='./TestCase/" + testcase + "/img/" + imgPass + "' onclick='zoomImg(this)' />
				path = "<img width='100' src='./TestCase/" + testcase + "/img/" + imgFail + "' onclick='zoomImg(this)' /><img width='100' src='./TestCase/" + testcase + "/img/" + imgPass + "' onclick='zoomImg(this)' style='display:none' />";
				imgs += path;
			}

			var zoom = 0.5;
			var boxw = $(document).width() * zoom;
			var boxh = $(document).height() * (zoom + 0.1);
			var boxl = ($(document).width() - boxw - 10) / 2;
			//padding 10;
			var imgwrap = boxh - 30;
			var boxStr = "<div class='box' style='width:" + boxw + "px;height:" + boxh + "px;left:" + boxl + "px;'><h3><span>" + testcase + "</span>";
			boxStr += "<a href='#' onclick='closebox()'></a></h3>";
			boxStr += "<div class='imgwrap' style='height:" + imgwrap + "px;'>" + imgs + "</div></div>";
			boxStr += "<div class='mask' style='z-index:1'></div>";

			$("body").append(boxStr);
			//判断图片加载失败，也就是去除不存在的截图
			$("body").find(".box .imgwrap img").error(function() {
				$(this).remove();
			});

			var startTop = ($(document).height() - boxh) / 3;
			var endTop = ($(document).height() - boxh) / 2.3;

			$("body").find(".box").css({
				"z-index" : "10",
				top : startTop
			}).show().animate({
				top : endTop
			}, 500);

			var doc = $(document)//this.getDoc();
			var currentBox = doc.find(".box");
			dragBox(currentBox, doc);

		}
	});

}


/**
 * 图片头数据加载就绪事件 - 更快获取图片尺寸
 * @version	2011.05.27
 * @author	TangBin
 * @see		http://www.planeart.cn/?p=1121
 * @param	{String}	图片路径
 * @param	{Function}	尺寸就绪
 * @param	{Function}	加载完毕 (可选)
 * @param	{Function}	加载错误 (可选)
 * @example imgReady('http://www.google.com.hk/intl/zh-CN/images/logo_cn.png', function () {
		alert('size ready: width=' + this.width + '; height=' + this.height);
	});
 */
var imgReady = (function () {
	var list = [], intervalId = null,

	// 用来执行队列
	tick = function () {
		var i = 0;
		for (; i < list.length; i++) {
			list[i].end ? list.splice(i--, 1) : list[i]();
		};
		!list.length && stop();
	},

	// 停止所有定时器队列
	stop = function () {
		clearInterval(intervalId);
		intervalId = null;
	};

	return function (url, ready, load, error) {
		var onready, width, height, newWidth, newHeight,
			img = new Image();
		
		img.src = url;

		// 如果图片被缓存，则直接返回缓存数据
		if (img.complete) {
			ready.call(img);
			load && load.call(img);
			return;
		};
		
		width = img.width;
		height = img.height;
		
		// 加载错误后的事件
		img.onerror = function () {
			error && error.call(img);
			onready.end = true;
			img = img.onload = img.onerror = null;
		};
		
		// 图片尺寸就绪
		onready = function () {
			newWidth = img.width;
			newHeight = img.height;
			if (newWidth !== width || newHeight !== height ||
				// 如果图片已经在其他地方加载可使用面积检测
				newWidth * newHeight > 1024
			) {
				ready.call(img);
				onready.end = true;
			};
		};
		onready();
		
		// 完全加载完毕的事件
		img.onload = function () {
			// onload在定时器时间差范围内可能比onready快
			// 这里进行检查并保证onready优先执行
			!onready.end && onready();
		
			load && load.call(img);
			
			// IE gif动画会循环执行onload，置空onload即可
			img = img.onload = img.onerror = null;
		};

		// 加入队列中定期执行
		if (!onready.end) {
			list.push(onready);
			// 无论何时只允许出现一个定时器，减少浏览器性能损耗
			if (intervalId === null) intervalId = setInterval(tick, 40);
		};
	};
})();


function zoomImg(tar) {
	var tw=$(tar).width();
	var th=$(tar).height();
	var dh = $(document).height(), dw = $(document).width();
	

	var l = $(tar).offset().left;
	var t = $(tar).offset().top;

	// var nl = (dw - currentW) / 2;
	// var nt = (dh - currentH) / 2;
	var box = $("body").find(".box");
	
	$(".box").append("<div class='mask' id='imgmask' style='width:" + box.width() + "px;height:" + box.height() + "px;left:5px;top:5px;' />");
	//if($("body").find("img").attr("src"));
	// var newimg = $(tar).clone().removeAttr("onclick").addClass("zoomimg").css({
		// left : l,
		// top : t,
		// opacity : 0.2,
		// "z-index" : 10000
	// });
	// newimg.bind("click", function() {
		// $(this).remove();
		// $("body").find("#imgmask").remove();
	// });
	var failSrc=$(tar).attr("src");
	var passSrc=$(tar).attr("src").split("_Cycle")[0]+".png";
	
	var fw,fh,pw,ph;
	
	imgReady(passSrc, function () {
	    pw=this.width;
	    ph=this.height;
		if(ph>dh){
			ph = parseInt(dh - dh * 0.05);
			pw=parseInt(pw*(ph/this.height));
		}
		var t=parseInt((dh-ph)/2);
		var pl=parseInt((dw-pw)/2-pw/2-5);
		
		$("body").append("<img src='"+passSrc+"' id='passImg' style='width:"+pw+"px;height:"+ph+"px;left:"+pl+"px;top:"+t+"px' />");
	});
	
	imgReady(failSrc, function () {
	    fw=this.width;
	    fh=this.height;
		if(fh>dh){
			fh = dh - dh * 0.05;
			fw=fw*(fh/this.height);
		}
		var t=parseInt((dh-fh)/2);
		var fl=parseInt((dw-fw)/2);
		$("body").find(".box img").each(function(){
			if($(this).attr("src")==passSrc){
				fl=parseInt((dw-fw)/2+fw/2);
				console.log("yes");
				return fl;
			}
		});
		
		$("body").append("<img src='"+failSrc+"' id='failImg' style='width:"+fw+"px;height:"+fh+"px;left:"+fl+"px;top:"+t+"px' />");
	});


	$("body").find("#passImg").error(function() {
		$(this).remove();
		if($("body").find("#failImg").length>0){
			var fl=parseInt(($(document).width-$("body").find("#failImg").width())/2);
			$("body").find("#failImg").css("left",fl);
		}
	});

	$("body").find("#failImg").bind("click", function() {
		$("body").find("#failImg").remove();
		if($("body").find("#passImg").length>0){
			$("body").find("#passImg").remove();
		}
		$("body").find("#imgmask").remove();
	});
	if($("body").find("#passImg").length>0){
		$("body").find("#passImg").bind("click", function() {
			$("body").find("#failImg").remove();
			$("body").find("#passImg").remove();
			$("body").find("#imgmask").remove();
		});
	}
}

function closebox() {
	$(".box").remove();
	$(".mask").remove();
}

//function GetResult(xmlFile) {
//	$.ajax({
//		url : xmlFile,
//		dataType : 'xml',
//		type : 'GET',
//		timeout : 2000,
//		error : function(xml) {
//			alert("error");
//		},
//		success : function(xml) {
//			var xf = xmlFile.split("TestResult/")[1].split(".xml")[0];
//			var datePostfix=xf.replace("Result_","");
//
//			$("#resultList li").each(function() {
//				if ($(this).find("a").text() == xf) {
//					$(this).addClass("selected");
//				}
//			});
//
//			var saveRoot = "";
//			var FailureCount = 0;
//			var num = 0;
//			$(xml).find("TestResult").children().not("Used_Time").each(function(i) {
//				var rootName = $(this)[0].tagName;
//				var tables = "<h3>" + rootName + "</h3><table cellpadding='0' cellspacing='0' border='0'>";
//				tables += "<tr><th width='35%'>Case</th><th width='10%'>Loop</th><th width='15%'>Result</th><th width='170'>Root Cause</th><th width='220'>Time</th></tr>";
//
//				$(this).children().each(function(i) {
//					num += $(this).length;
//					var tname = $(this)[0].tagName;
//					var loop = $(this).children("Result").attr("loop");
//					var reason = $(this).children("Result").attr("reason");
//					var result = $(this).children("Result").attr("result");
//					var time = $(this).children("Result").attr("time");
//
//					if (result == "FAIL") {
//						FailureCount++;
//						tables += "<tr class='fail'><td>" + tname + "</td><td>" + loop + "</td><td>" + result + "</td><td align='center'><a href='#' onclick=showPic(this,'" + tname + "','" + rootName + "','" + loop + "','" + datePostfix + "')>" + reason + "</a></td><td align='center'>" + time + "</td></tr>";
//					} else {
//						tables += "<tr><td>" + tname + "</td><td>" + loop + "</td><td>" + result + "</td><td align='center'>" + reason + "</td><td align='center'>" + time + "</td></tr>";
//					}
//				});
//				tables += "</table>";
//				saveRoot += tables;
//			});
//			$("#dataArea .dataList").html(saveRoot);
//			SortByRootCause();
//			var durationTime = $(xml).find("Used_Time").attr("duration_time");
//			var ds = durationTime.split(":");
//			var sec = Number(ds[0]) * 3600 + Number(ds[1]) * 60 + Number(ds[2]);
//			var mtbf = (sec / FailureCount) / 3600;
//
//			$("#ResultCount .TotleCaseCount").text(num);
//			$("#ResultCount .PassCount").text(num - FailureCount);
//			$("#ResultCount .FailureCount").text(FailureCount);
//			$("#ResultCount .MTBF").text(mtbf.toFixed(3) + "(h)");
//			$("#ResultCount .UsedTime").text(durationTime);
//
//			$('#dataArea').jScrollPane({
//				showArrows : true
//			});
//
//		}
//	});
//}

function getAllDate(ds) {
	var start, end;
	var dateArray = [];
	if (ds.indexOf(" - ") != -1) {
		start = ds.split(" - ")[0];
		end = ds.split(" - ")[1];
	} else {
		dateArray.push(ds);
		return dateArray;
	}
	var startDate = new Date(start.replace(/-/g, "/"));
	var endDate = new Date(end.replace(/-/g, "/"));

	var times = endDate.getTime() - startDate.getTime();
	var days = parseInt(times / (1000 * 60 * 60 * 24)) + 1;

	for (var i = 0; i < days; i++) {
		var d = new Date(start);
		d.setDate(d.getDate() + i);
		dateArray.push(d.getFullYear() + "-" + (parseInt(d.getMonth()) + 1) + "-" + d.getDate());
	}
	return dateArray;
}

function DelSame(arr) {
	var newArr = [];
	for (var i = 0, len = arr.length; i < len; i++) {
		! RegExp(arr[i], "g").test(newArr.join(",")) && (newArr.push(arr[i]));
	}
	return newArr;
}

function clk(obj) {
	var fileName = $(obj).text();
	GetResult("TestResult/" + fileName + ".xml");
	$(obj).parent().parent().find("li").removeClass();
	//$(obj).parent().addClass("selected");
}

function GetList(xmlFile) {
	$.ajax({
		url : xmlFile,
		dataType : 'xml',
		type : 'GET',
		timeout : 2000,
		error : function(xml) {
			alert("error");
		},
		success : function(xml) {

			var resultList = "";
			//var dArray=getAllDate(strDate);
			var listData = [], dateAry = [];
			$(xml).find("Result").children().each(function(i) {
				var val = $(this).attr("value");
				var value = val.split(".xml")[0];
				var date = val.substr(7, 10);

				listData.push(val);
				dateAry.push(date);

			});

			//$("#resultList").find("li").bind({click:function(){clk(this,listData)}});

			var newdateAry = DelSame(dateAry.sort());
			var res = [];
			for (var i = 0; i < newdateAry.length; ) {
				var count = 0, ss = "";
				for (var j = i; j < newdateAry.length; j++) {
					if (newdateAry[i].substr(0, 7) == newdateAry[j].substr(0, 7)) {
						ss += newdateAry[j].substr(8, 2) + ",";
						count++;
					}
				}
				res.push([newdateAry[i].substr(0, 7), ss]);
				ss = "";
				i += count;
			}

			var dropDate = "";
			for (var i = 0; i < res.length; i++) {
				var d = res[i][1].replace(/,/g, "</a></li><li><a href='#'>");
				var y = res[i][0].replace(/-/g, "<br>");
				var list = "";
				if (i % 2 == 0) {
					list = "<div class='evenDate'><h3>" + y + "</h3><ul><li><a href='#'>" + d + "</a></li></ul></div>";
				} else {
					list = "<div class='oddDate'><h3>" + y + "</h3><ul><li><a href='#'>" + d + "</a></li></ul></div>";
				}
				//var dr=list.replace("<li onclick='filterDate(this,"+listData+")'></li>","");
				dropDate += list.replace("<li><a href='#'></a></li>", "");
			}

			$("#dateList").html(dropDate);
			$("#dateList").find("li").bind({
				click : function() {
					filterData(this, listData)
				}
			});

			//显示最早日期的列表
			GetResult("TestResult/" + listData.sort()[0]);
			for (var i = 0; i < listData.length; i++) {//显示最早日期的详细
				var date = listData.sort()[0].substr(7, 10);
				$("#SelectDate").val(date);
				if (listData[i].indexOf(date) != -1) {
					resultList += "<li><a href='#' onclick='clk(this)'>" + listData[i].split(".xml")[0] + "</a></li>";
				}
			}
			$("#resultList").html(resultList);

			$('#leftBar').jScrollPane({
				showArrows : true
			});
			$('#dataArea').jScrollPane({
				showArrows : true
			});
			
		}
	});

}

function filterData(obj, arry) {
	var ym = parseInt($(obj).parent().prev().text()) + "";
	var date = ym.substr(0, 4) + "-" + ym.substr(4, 2) + "-" + $(obj).text();

	var lis = "";
	$("#SelectDate").val(date);
	for (var i = 0; i < arry.length; i++) {
		if (arry[i].indexOf(date) != -1) {
			lis += "<li><a href='#' onclick='clk(this)'>" + arry[i].split(".xml")[0] + "</a></li>";
		}
	}
	
	var rl=$("#resultList").find("li").text().substring(7).split("Result_");
	
	var rlArry=[],newrl=[];
	for(var a=0;a<rl.length;a++){
		//var nrl=rl[a].substr(0, 10);
		rlArry.push(rl[a].substr(0, 10));
	}
	newrl=DelSame(rlArry);
	for(var n=0;n<DelSame(rlArry).length;n++){
		if(DelSame(rlArry)[n]!=date){
			$("#resultList").html(lis);
			$(obj).find("a").addClass("selected");
		}
	}
	

	$('#leftBar').jScrollPane({
		showArrows : true
	});
}


function SortByDate() {
	$("#resultList li").each(function() {
		var dates = $(this).find("a").text().substring(0, 17);
		var dnext = $(this).next().find("a").text().substring(0, 17);

	});
}

function stopEvent(e) {

	if (!e)
		var e = window.event;

	//e.cancelBubble is supported by IE -
	// this will kill the bubbling process.
	e.cancelBubble = true;
	e.returnValue = false;

	//e.stopPropagation works only in Firefox.
	if (e.stopPropagation)
		e.stopPropagation();
	if (e.preventDefault)
		e.preventDefault();

	return false;
}

function showbox(o, tar, e) {

	if ($(tar).is(':hidden')) {
		$(tar).show();
		$(o).parent().addClass("selected");
	} else {
		$(tar).hide();
		$(o).parent().removeClass("selected");
	}

	$(document).one("click", function() {//对document绑定一个影藏Div方法
		$(tar).hide();
		$(o).parent().removeClass("selected");
	});
	//e.stopPropagation();//点击Button阻止事件冒泡到document
	stopEvent(e);

	$(tar).click(function(e) {
		e.stopPropagation();
		//在Div区域内的点击事件阻止冒泡到document
		stopEvent(e);
	});

}

/**
 * swichStyle
 */
function swichStyle(styleId, swichId, stylePath) {
	var c = readCookie("style");
	if (c !== null) {
		$("#" + styleId).attr("href", c);
	}

	$("#" + swichId).find("li").click(function() {
		var styleName = $(this).attr("id") + ".css";
		var newCss = stylePath + styleName;
		$("#" + styleId).attr("href", newCss);
		createCookie("style", newCss, 365);
	});
}

function getDoc() {
	var parent = window;
	while (parent.self.frameElement != null) {
		parent = parent.parent;
	}
	return $xd(parent.document);
}

function dragBox(tar, doc) {
	var dx, dy;
	var tarNum = tar.eq(tar.length - 1);
	var titlebar = tarNum.find("h3").css("cursor", "move");

	titlebar.mousedown(function(e) {
		dx = e.pageX - parseInt(tarNum.css("left"));
		dy = e.pageY - parseInt(tarNum.css("top"));
		doc.mousemove(move);
		doc.mouseup(up);
		return false;
	});
	function move(e) {
		var bleft = e.pageX - dx;
		var btop = e.pageY - dy;
		if (bleft < 0) {
			bleft = 0;
		} else if (bleft > doc.width() - tarNum.width()) {
			bleft = doc.width() - tarNum.width();
		}
		if (btop < 0) {
			btop = 0;
		} else if (btop > doc.height() - tarNum.height()) {
			btop = doc.height() - tarNum.height();
		}
		tarNum.css({
			left : bleft,
			top : btop
		});
	}

	function out(e) {
		setTimeout(function() {
			moveout && up(e)
		}, 100);
	}

	function up(e) {
		doc.unbind("mousemove", move);
		doc.unbind("mouseup", up);
	}

}



/**
 *cookie function http://www.quirksmode.org/js/cookies.html
 */
function createCookie(name, value, days) {
	if (days) {
		var date = new Date();
		date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
		var expires = "; expires=" + date.toGMTString();
	} else
		expires = "";
	document.cookie = name + "=" + value + expires + "; path=/";
}

function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for (var i = 0; i < ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0) == ' ')
		c = c.substring(1, c.length);
		if (c.indexOf(nameEQ) === 0)
			return c.substring(nameEQ.length, c.length);
	}
	return null;
}

function eraseCookie(name) {
	createCookie(name, "", -1);
}

/*jquery cookie*/
function jcookie(key, value, options) {
	// key and at least value given, set cookie...
	if (arguments.length > 1 && String(value) !== "[object Object]") {
		options = jQuery.extend({}, options);

		if (value === null || value === undefined) {
			options.expires = -1;
		}

		if ( typeof options.expires === 'number') {
			var days = options.expires, t = options.expires = new Date();
			t.setDate(t.getDate() + days);
		}
		value = String(value);

		return (document.cookie = [encodeURIComponent(key), '=', options.raw ? value : encodeURIComponent(value), options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
		options.path ? '; path=' + options.path : '', options.domain ? '; domain=' + options.domain : '', options.secure ? '; secure' : ''].join(''));
	}

	// key and possibly options given, get cookie...
	options = value || {};
	var result, decode = options.raw ? function(s) {
		return s;
	} : decodeURIComponent;
	return ( result = new RegExp('(?:^|; )' + encodeURIComponent(key) + '=([^;]*)').exec(document.cookie)) ? decode(result[1]) : null;
};
# coding=utf-8
import requests,re
from bs4 import BeautifulSoup
import lxml
sec = ''
zztj='''<script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_1274386182'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s22.cnzz.com/z_stat.php%3Fid%3D1274386182%26show%3Dpic1' type='text/javascript'%3E%3C/script%3E"));</script>'''
req_url_2 = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>《连续剧风再起时2018》剧情介绍,风再起时2018演员表,国产剧_百万资源网</title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="国产剧风再起时2018,风再起时2018剧情介绍,风再起时2018演员表,百万资源网" name="keywords"/>
</head>
<body>
<link href="/template/diaosizy/css/home.css" rel="stylesheet" type="text/css"/>
<script src="/js/jquery.js"></script>
<script>var SitePath='/',SiteAid='16',SiteTid='12',SiteId='19593';</script>
<script src="/template/diaosizy/js/home.js"></script>
<script type="text/javascript">
<!--
var timeout= 500;
var closetimer= 0;
var ddmenuitem= 0;
function mopen(id)
{	
	mcancelclosetime();
	if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';
	ddmenuitem = document.getElementById(id);
	ddmenuitem.style.visibility = 'visible';
}
function mclose()
{
	if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';
}
function mclosetime()
{
	closetimer = window.setTimeout(mclose, timeout);
}
function mcancelclosetime()
{
	if(closetimer)
	{
		window.clearTimeout(closetimer);
		closetimer = null;
	}
}
document.onclick = mclose; 
// -->
</script>
<script language="JavaScript"> 
eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('p R(4){3 a=t.s(4);3 n=a.q;3 f="";x(3 i=0;i<n;i++){6(a[i].c){f+=a[i].Q;f+="\\r\\n"}}F(f);E("地址全部复制成功！")}p F(9){6(8.l){8.l.P();8.l.A("O",9)}w 6(S.T.W("N")!=-1){8.U=9}w 6(8.z){X{z.M.I.K("J")}L(e){E("被浏览器拒绝！\\n请在浏览器地址栏输入\'H:V\'并回车\\n然后将\'11.1b.1a\'设置为\'1d\'")}3 d=5.j[\'@o.k/u/Y;1\'].h(5.b.C);6(!d)g;3 7=5.j[\'@o.k/u/19;1\'].h(5.b.1c);6(!7)g;7.1e(\'B/G\');3 4=y v();3 1f=y v();3 4=5.j["@o.k/17-18;1"].h(5.b.10);3 m=9;4.Z=m;7.12("B/G",4,m.q*2);3 D=5.b.C;6(!d)g 14;d.A(7,15,D.16)}}p 13(4,c){3 a=t.s(4);3 n=a.q;x(3 i=0;i<n;i++){a[i].c=c}}',62,78,'|||var|str|Components|if|trans|window|txt||interfaces|checked|clip||ed2kcopy|return|createInstance||classes|org|clipboardData|copytext||mozilla|function|length||getElementsByName|document|widget|Object|else|for|new|netscape|setData|text|nsIClipboard|clipid|alert|copyToClipboard|unicode|about|PrivilegeManager|UniversalXPConnect|enablePrivilege|catch|security|Opera|Text|clearData|value|copy|navigator|userAgent|location|config|indexOf|try|clipboard|data|nsISupportsString|signed|setTransferData|checkAll|false|null|kGlobalClipboard|supports|string|transferable|codebase_principal_support|applets|nsITransferable|true|addDataFlavor|len'.split('|'),0,{}))
</script>
<link href="/admin123/tpl/images/123.css" rel="stylesheet" type="text/css"/>
<table bgcolor="#ff0000" border="0" cellpadding="0" cellspacing="0" style="font-size: 12px" width="100%"><tr><td>
<p align="center"><span style="line-height:25px; color:#FFFF00"> <b>因本站持续被竞争对手CC攻击！开启防御后原采集地址暂时无法使用<br/>请入群获取新的采集地址 QQ群号 589981019<br/>郑重承诺：资源永久免费,资源不含任何联盟富媒体弹窗广告,<br/>只有三次走马灯水印广告(承诺绝不影响用户体验！</b><br/>
百万资源分享群：<a href="//shang.qq.com/wpa/qunwpa?idkey=a603f27a03be43df2f5c6a9f7064a8fb83d1abf72a0fa8db1bf5c98ccd447fc3" target="_blank"><img alt="百万资源" border="0" src="//pub.idqqimg.com/wpa/images/group.png" title="百万资源"/></a><br/>
</span></p></td>
　
</tr></table>
<div id="topBar">
<div class="wtop fn-clear">
<div class="home-sign fn-left">
<a class="gonggao_ico" title="公告">
<script language="javaScript">
                now = new Date(),
                hour = now.getHours()
                document.write("<blink>")
                if(hour < 5){document.write("百万资源提醒您：夜已深,请注意休息哦！")}
                else if (hour < 9){document.write("早上好,欢迎光临百万资源!")}
                else if (hour < 12){document.write("上午好,欢迎光临百万资源!")}
                else if (hour < 14){document.write("中午好,欢迎光临百万资源!")}
                else if (hour < 18){document.write("下午好,欢迎光临百万资源!")}
                else if (hour < 23){document.write("晚上好,欢迎光临百万资源!")}
                </script></a>
</div>
<div class="a-link fn-right">
<p>
<a href="/mac.rar" style="width: 100px;" target="_blank"><font color="red">苹果CMS采集插件</font></a><em>|</em>
<a href="/haiyang.rar" style="width: 100px;" target="_blank"><font color="#FF00FF">海洋CMS采集插件</font></a><em>|</em>
<a href="/feifei.rar" style="width: 100px;" target="_blank"><font color="#0000FF">飞飞CMS采集插件</font></a><em>|</em>
<a href="/chitu.rar" style="width: 100px;" target="_blank"><font color="#8B008B">赤兔CMS采集插件</font></a><em>|</em>
<a href="/max.rar" style="width: 100px;" target="_blank"><font color="#00008B">马克思CMS采集插件</font></a>
</p>
</div>
</div>
</div>
﻿<div class="xing_top">
<ul>
<li class="xing_top_left"><img alt="1111" src="/template/diaosizy/images/logo.gif"/></li>
<li class="xing_top_center">
<div class="search">
<div class="search-inner">
<form action="/index.php?m=vod-search" method="post">
<input autocomplete="off" class="search-text" id="wd" name="wd" onblur="if(this.value==''){ this.value='100万部影片任你搜索';this.style.color='#cfcdcd';}" onfocus="if(this.value=='100万部影片任你搜索'){this.value='';this.style.color='';}" type="text" value="100万部影片任你搜索" x-webkit-speech=""/>
<input name="submit" type="hidden" value="search"/>
<input class="search-btn" type="submit" value="搜索"/>
</form>
</div>
</div>
</li>
<li class="xing_top_right">
<div class="topright">
<ul><li>今日更新：<strong>48</strong></li></ul>
<ul><li>百万资源网影片共有：<strong>14069</strong></li></ul>
<ul><li><a href="javascript:window.external.addFavorite('http://www.baiwanzy.com','百万资源网');">收藏本站</a> | <a accesskey="1" class="ge" href="#" id="topmenu1" onclick="var strHref=window.location.href;this.style.behavior='url(#default#homepage)';this.setHomePage('http://www.baiwanzy.com');">设为首页</a> | <a href="/zh.rar"><font color="#FF0000">整合插件</font></a> </li>
</ul>
</div>
</li>
</ul>
<div style="clear:both"></div>
</div>
<div class="sddm">
<ul id="sddm">
<li><a href="/">首页</a></li>
<li><a href="/index.php?m=gbook-show.html">留言求片</a></li>
<li><a href="/?m=vod-type-id-1.html" onmouseout="mclosetime()" onmouseover="mopen('m1')">电影</a>
<div id="m1" onmouseout="mclosetime()" onmouseover="mcancelclosetime()">
<a href="/?m=vod-type-id-5.html">动作片</a><a href="/?m=vod-type-id-6.html">喜剧片</a><a href="/?m=vod-type-id-7.html">爱情片</a><a href="/?m=vod-type-id-8.html">科幻片</a><a href="/?m=vod-type-id-9.html">恐怖片</a><a href="/?m=vod-type-id-10.html">剧情片</a><a href="/?m=vod-type-id-11.html">战争片</a><a href="/?m=vod-type-id-16.html">伦理片</a>
</div>
</li>
<li><a href="/?m=vod-type-id-2.html" onmouseout="mclosetime()" onmouseover="mopen('m2')">连续剧</a>
<div id="m2" onmouseout="mclosetime()" onmouseover="mcancelclosetime()">
<a href="/?m=vod-type-id-12.html">国产剧</a><a href="/?m=vod-type-id-13.html">港剧</a><a href="/?m=vod-type-id-14.html">日剧</a><a href="/?m=vod-type-id-15.html">欧美剧</a><a href="/?m=vod-type-id-17.html">韩剧</a><a href="/?m=vod-type-id-19.html">台剧</a><a href="/?m=vod-type-id-20.html">泰剧</a>
</div>
</li>
<li><a href="/?m=vod-type-id-3.html" onmouseout="mclosetime()" onmouseover="mopen('m3')">综艺</a>
<div id="m3" onmouseout="mclosetime()" onmouseover="mcancelclosetime()">
</div>
</li>
<li><a href="/?m=vod-type-id-4.html" onmouseout="mclosetime()" onmouseover="mopen('m4')">动漫</a>
<div id="m4" onmouseout="mclosetime()" onmouseover="mcancelclosetime()">
</div>
</li>
<li><a href="/?m=vod-type-id-21.html" onmouseout="mclosetime()" onmouseover="mopen('m5')">写真视频</a>
<div id="m5" onmouseout="mclosetime()" onmouseover="mcancelclosetime()">
<a href="/?m=vod-type-id-22.html">美女写真</a><a href="/?m=vod-type-id-23.html">美女视频</a><a href="/?m=vod-type-id-24.html">街拍系列</a><a href="/?m=vod-type-id-25.html">高跟赤足视频</a>
</div>
</li>
<li><a href="/?m=vod-type-id-26.html" onmouseout="mclosetime()" onmouseover="mopen('m6')">VIP视频秀</a>
<div id="m6" onmouseout="mclosetime()" onmouseover="mcancelclosetime()">
</div>
</li>
<li>
<a href="/?m=art-type-id-1.html">插件下载</a>
</li>
</ul>
<div style="clear:both"></div>
</div>
<div class="container">
<div class="nvc">
<dl>
<dt>
<span>当前位置</span>
<i class="arrow"><b class="a_outer"></b><b class="a_inner"></b></i>
</dt>
<dd><a href="/">首页</a>  »  <a href="/?m=vod-type-id-12.html">国产剧</a>  »  <a href="/?m=vod-detail-id-19593.html">风再起时2018</a></dd>
</dl>
</div>
</div>
<div class="warp">
<div class="ibox">
<div class="vod">
<div class="vodBox">
<div class="vodImg">
<img alt="风再起时2018" class="lazy" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2537203670.jpg"/>
<b class="b1"></b>
<b class="b2"></b>
</div>
<div class="vodInfo">
<div class="vodh">
<h2><!--片名开始-->风再起时2018<!--片名结束--></h2>
<span><!--备注开始-->连载16集<!--备注结束--></span>
<label>0.0</label>
</div>
<div class="vodinfobox">
<ul>
<li>别名：<span><!--别名开始--><!--别名结束--></span></li>
<li>导演：<span><!--导演开始-->付宁<!--导演结束--></span></li>
<li>主演：<span><!--主演开始-->陆毅,袁泉,朱雨辰,王维维<!--主演结束--></span></li>
<li>类型：<span><!--类型开始-->国产剧<!--类型结束--> </span></li>
<li>地区：<span><!--地区开始-->大陆<!--地区结束--></span></li>
<li>语言：<span><!--语言开始-->国语<!--语言结束--></span></li>
<li>上映：<span><!--上映开始-->2018<!--上映结束--></span></li>
<li>更新：<span>2018-11-13 22:12:54</span></li>
<li class="cont">
<div class="jjText">
<span class="cl"></span>
<!-- <span class="more" txt="一九七八年十二月，中共十一届三中全会召开，决定把党和国家的工作重点转移到经济建设上来，作出了改革开放的重大决策，实现了新中国成立以来党和国家历史的伟大转折，开创了社会主义事业发展的新时期。一九八四年，“百万大裁军”战略宣布后，方邦彦、何有邻、康宁三人几乎同一时间从部队转业，分别进入外贸国企永江纺织厂、省计委以及乡集体服装厂，开始了各自的改革之路。彼时，改革风起云涌。在经历八六年“第一次价格闯关”失">一九七八年十二月，中共十一届三中全会召开，决定把党和国家的工作重点转移到经济建设上来，作出了改革开放的重大决策，实现了新中国成立以来党和国家历史的伟大转折，开创了社会主义事业发展的新时期。一九八四年，“百万大裁军”战略宣布后，方邦彦、何有邻、康宁三人几乎同一时间从部队转业，分别进入外贸国企永江纺织厂、省计委以及乡集体服装厂，开始了各自的改革之路。彼时，改革风起云涌。在经历八六年“第一次价格闯关”失败后，方邦彦也遭遇了纺织厂改制困境并被迫离开。随着改革的春风再起以及“九二南巡讲话”的发表，方邦彦又看到了新的希望。他与有志青年林云借风创业，走在了互联网大军的第一列。在国家理顺了价格体系并且“第二次价格闯关”成功后，方邦彦不忘初心，毅然回到纺织厂，带领大家积极参与国际竞争，使濒临倒闭的外贸国企扭亏为盈。进入新世纪后，中国重新开启“入世谈判”，方邦彦抓住机遇，在国家政策的支持下完成了自己当年纺织厂的改制梦想，突破重重关卡，实现了国企的现代化企业制度的转型成功上市迈进世界五百强，并且一鼓作气完成海外并购。与此同时，他的老对手也是大舅哥的战友何有邻也渐渐地在改革的浪潮中从墨守成规，拘泥于体制开始解放思想，积极帮助企业改制，并且将全能型政府职能转变为服务型职能；而他的老部下康宁在搞活集体企业的同时却在利益驱动之下将企业据为己有，并利用收购纺织厂生产线来进行走私犯罪，甚至不惜嫁祸昔日部队领导方邦彦，最终锒铛入狱。出狱后，康宁流落中东，并被黑道追杀，最后被自己恨之入骨的方邦彦救回，羞愧难当，在方邦彦与何有邻的帮助下重新开始新的生活。“一带一路”的战略发布后，三个已近耳顺之年的兄弟，举杯展望，风再起时，再度扬帆远航。</span>  -->
<span class="cr"></span>
</div></li>
<li class="tags"><span><a href="/index.php?m=vod-search-tag-%E6%88%90%E7%AB%8B" target="_blank">成立</a> <a href="/index.php?m=vod-search-tag-%E5%BA%B7%E5%AE%81" target="_blank">康宁</a> <a href="/index.php?m=vod-search-tag-%E7%AC%AC%E4%B8%80%E6%AC%A1%E4%BB%B7%E6%A0%BC%E9%97%AF%E5%85%B3" target="_blank">第一次价格闯关</a> </span></li>
</ul>
</div>
</div>
<div class="vodAd"><script src="/template/diaosizy/aaaa/detail300X320.js" type="text/javascript"></script></div>
</div>
</div>
</div> <!-- 心情开始 -->
<div class="ibox playBox">
<div class="vodplayinfo">
<div data-use="emoji" id="cyEmoji" role="cylabs"></div>
<script charset="utf-8" src="http://changyan.itc.cn/js/??lib/jquery.js,changyan.labs.js?appid=cyrNFNgxz" type="text/javascript"></script>
</div>
</div><!-- 心情结束 -->
<!-- 开始 -->
<div class="ibox playBox">
<div class="playBar liketitle">
<strong>剧情介绍：</strong>
</div>
<div class="vodplayinfo"><!--介绍开始-->一九七八年十二月，中共十一届三中全会召开，决定把党和国家的工作重点转移到经济建设上来，作出了改革开放的重大决策，实现了新中国成立以来党和国家历史的伟大转折，开创了社会主义事业发展的新时期。一九八四年，“百万大裁军”战略宣布后，方邦彦、何有邻、康宁三人几乎同一时间从部队转业，分别进入外贸国企永江纺织厂、省计委以及乡集体服装厂，开始了各自的改革之路。彼时，改革风起云涌。在经历八六年“第一次价格闯关”失败后，方邦彦也遭遇了纺织厂改制困境并被迫离开。随着改革的春风再起以及“九二南巡讲话”的发表，方邦彦又看到了新的希望。他与有志青年林云借风创业，走在了互联网大军的第一列。在国家理顺了价格体系并且“第二次价格闯关”成功后，方邦彦不忘初心，毅然回到纺织厂，带领大家积极参与国际竞争，使濒临倒闭的外贸国企扭亏为盈。进入新世纪后，中国重新开启“入世谈判”，方邦彦抓住机遇，在国家政策的支持下完成了自己当年纺织厂的改制梦想，突破重重关卡，实现了国企的现代化企业制度的转型成功上市迈进世界五百强，并且一鼓作气完成海外并购。与此同时，他的老对手也是大舅哥的战友何有邻也渐渐地在改革的浪潮中从墨守成规，拘泥于体制开始解放思想，积极帮助企业改制，并且将全能型政府职能转变为服务型职能；而他的老部下康宁在搞活集体企业的同时却在利益驱动之下将企业据为己有，并利用收购纺织厂生产线来进行走私犯罪，甚至不惜嫁祸昔日部队领导方邦彦，最终锒铛入狱。出狱后，康宁流落中东，并被黑道追杀，最后被自己恨之入骨的方邦彦救回，羞愧难当，在方邦彦与何有邻的帮助下重新开始新的生活。“一带一路”的战略发布后，三个已近耳顺之年的兄弟，举杯展望，风再起时，再度扬帆远航。<!--介绍结束--></div>
</div>
<!--结束-->
<div class="ibox playBox">
<div class="playBar liketitle">
<strong>复制下列地址至浏览器地址栏即可观看正版影片，本站不提供在线正版播放。<font color="red">备注：如有地址错误，请点击→ <a href="javascript:void(0)" onclick='MAC.Error("vod","19593","风再起时2018");return false;' target="_self">我要报错</a> 向我们报错！我们将在第一时间处理！谢谢！</font></strong>
</div>
<div class="vodplayinfo">
<div style="padding-left:10px;word-break: break-all; word-wrap:break-word;">
<h3>来源：bwyun</h3>
<ul>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/KDCwbepl4JVTyZHo"/>第01集$https://t.bwzybf.com/share/KDCwbepl4JVTyZHo</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/nUpDA3ZryxEKsfwx"/>第02集$https://t.bwzybf.com/share/nUpDA3ZryxEKsfwx</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/mch0L5j2EICjb0Qx"/>第03集$https://t.bwzybf.com/share/mch0L5j2EICjb0Qx</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/1TCiGz7qiRlRQLqI"/>第04集$https://t.bwzybf.com/share/1TCiGz7qiRlRQLqI</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/tJ9rNGdYluOgjxdK"/>第05集$https://t.bwzybf.com/share/tJ9rNGdYluOgjxdK</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/aBE7uqViqzscsIG5"/>第06集$https://t.bwzybf.com/share/aBE7uqViqzscsIG5</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/EKxm7pRmK6VEVZtU"/>第07集$https://t.bwzybf.com/share/EKxm7pRmK6VEVZtU</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/bPQlnSY6QlCKdKi7"/>第08集$https://t.bwzybf.com/share/bPQlnSY6QlCKdKi7</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/bZL56tb4CDEJ6ben"/>第09集$https://t.bwzybf.com/share/bZL56tb4CDEJ6ben</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/Dml8W5lQ5n6Ejnyi"/>第10集$https://t.bwzybf.com/share/Dml8W5lQ5n6Ejnyi</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/7v96ygHxhAFusqjl"/>第11集$https://t.bwzybf.com/share/7v96ygHxhAFusqjl</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/pZybi45rgdVmlBDr"/>第12集$https://t.bwzybf.com/share/pZybi45rgdVmlBDr</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/gduCU1wsrHgoxw6P"/>第13集$https://t.bwzybf.com/share/gduCU1wsrHgoxw6P</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/Sl16RpumnJqLxeb5"/>第14集$https://t.bwzybf.com/share/Sl16RpumnJqLxeb5</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/1fVSqXPDFUJYfyYy"/>第15集$https://t.bwzybf.com/share/1fVSqXPDFUJYfyYy</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/share/2AkLsVaof3EN3raZ"/>第16集$https://t.bwzybf.com/share/2AkLsVaof3EN3raZ</li>
</ul>
<input checked="" name="checkbox" onclick="checkAll('copy_sel',this.checked)" type="checkbox" value="checkbox"/>全选 
      <input name="Submit" onclick="copy('copy_sel')" type="button" value="直接复制链接"/>  
      <h3>来源：bwm3u8</h3>
<ul>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/05/KDCwbepl4JVTyZHo/playlist.m3u8"/>第01集$https://t.bwzybf.com/2018/11/05/KDCwbepl4JVTyZHo/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/05/nUpDA3ZryxEKsfwx/playlist.m3u8"/>第02集$https://t.bwzybf.com/2018/11/05/nUpDA3ZryxEKsfwx/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/06/mch0L5j2EICjb0Qx/playlist.m3u8"/>第03集$https://t.bwzybf.com/2018/11/06/mch0L5j2EICjb0Qx/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/06/1TCiGz7qiRlRQLqI/playlist.m3u8"/>第04集$https://t.bwzybf.com/2018/11/06/1TCiGz7qiRlRQLqI/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/07/tJ9rNGdYluOgjxdK/playlist.m3u8"/>第05集$https://t.bwzybf.com/2018/11/07/tJ9rNGdYluOgjxdK/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/07/aBE7uqViqzscsIG5/playlist.m3u8"/>第06集$https://t.bwzybf.com/2018/11/07/aBE7uqViqzscsIG5/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/08/EKxm7pRmK6VEVZtU/playlist.m3u8"/>第07集$https://t.bwzybf.com/2018/11/08/EKxm7pRmK6VEVZtU/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/08/bPQlnSY6QlCKdKi7/playlist.m3u8"/>第08集$https://t.bwzybf.com/2018/11/08/bPQlnSY6QlCKdKi7/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/09/bZL56tb4CDEJ6ben/playlist.m3u8"/>第09集$https://t.bwzybf.com/2018/11/09/bZL56tb4CDEJ6ben/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/10/Dml8W5lQ5n6Ejnyi/playlist.m3u8"/>第10集$https://t.bwzybf.com/2018/11/10/Dml8W5lQ5n6Ejnyi/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/11/7v96ygHxhAFusqjl/playlist.m3u8"/>第11集$https://t.bwzybf.com/2018/11/11/7v96ygHxhAFusqjl/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/11/pZybi45rgdVmlBDr/playlist.m3u8"/>第12集$https://t.bwzybf.com/2018/11/11/pZybi45rgdVmlBDr/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/12/gduCU1wsrHgoxw6P/playlist.m3u8"/>第13集$https://t.bwzybf.com/2018/11/12/gduCU1wsrHgoxw6P/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/13/Sl16RpumnJqLxeb5/playlist.m3u8"/>第14集$https://t.bwzybf.com/2018/11/13/Sl16RpumnJqLxeb5/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/13/1fVSqXPDFUJYfyYy/playlist.m3u8"/>第15集$https://t.bwzybf.com/2018/11/13/1fVSqXPDFUJYfyYy/playlist.m3u8</li>
<li><input checked="" name="copy_sel" type="checkbox" value="https://t.bwzybf.com/2018/11/13/2AkLsVaof3EN3raZ/playlist.m3u8"/>第16集$https://t.bwzybf.com/2018/11/13/2AkLsVaof3EN3raZ/playlist.m3u8</li>
</ul>
<input checked="" name="checkbox" onclick="checkAll('copy_sel',this.checked)" type="checkbox" value="checkbox"/>全选 
      <input name="Submit" onclick="copy('copy_sel')" type="button" value="直接复制链接"/>   

	<!--播放来源开始>bwyun$$$bwm3u8$$$<播放来源结束-->
<!--播放类型开始>bwyun$$$bwm3u8$$$<播放类型结束-->
<!--播放地址开始>第01集$https://t.bwzybf.com/share/KDCwbepl4JVTyZHo<br>第02集$https://t.bwzybf.com/share/nUpDA3ZryxEKsfwx<br>第03集$https://t.bwzybf.com/share/mch0L5j2EICjb0Qx<br>第04集$https://t.bwzybf.com/share/1TCiGz7qiRlRQLqI<br>第05集$https://t.bwzybf.com/share/tJ9rNGdYluOgjxdK<br>第06集$https://t.bwzybf.com/share/aBE7uqViqzscsIG5<br>第07集$https://t.bwzybf.com/share/EKxm7pRmK6VEVZtU<br>第08集$https://t.bwzybf.com/share/bPQlnSY6QlCKdKi7<br>第09集$https://t.bwzybf.com/share/bZL56tb4CDEJ6ben<br>第10集$https://t.bwzybf.com/share/Dml8W5lQ5n6Ejnyi<br>第11集$https://t.bwzybf.com/share/7v96ygHxhAFusqjl<br>第12集$https://t.bwzybf.com/share/pZybi45rgdVmlBDr<br>第13集$https://t.bwzybf.com/share/gduCU1wsrHgoxw6P<br>第14集$https://t.bwzybf.com/share/Sl16RpumnJqLxeb5<br>第15集$https://t.bwzybf.com/share/1fVSqXPDFUJYfyYy<br>第16集$https://t.bwzybf.com/share/2AkLsVaof3EN3raZ<br>$$$第01集$https://t.bwzybf.com/2018/11/05/KDCwbepl4JVTyZHo/playlist.m3u8<br>第02集$https://t.bwzybf.com/2018/11/05/nUpDA3ZryxEKsfwx/playlist.m3u8<br>第03集$https://t.bwzybf.com/2018/11/06/mch0L5j2EICjb0Qx/playlist.m3u8<br>第04集$https://t.bwzybf.com/2018/11/06/1TCiGz7qiRlRQLqI/playlist.m3u8<br>第05集$https://t.bwzybf.com/2018/11/07/tJ9rNGdYluOgjxdK/playlist.m3u8<br>第06集$https://t.bwzybf.com/2018/11/07/aBE7uqViqzscsIG5/playlist.m3u8<br>第07集$https://t.bwzybf.com/2018/11/08/EKxm7pRmK6VEVZtU/playlist.m3u8<br>第08集$https://t.bwzybf.com/2018/11/08/bPQlnSY6QlCKdKi7/playlist.m3u8<br>第09集$https://t.bwzybf.com/2018/11/09/bZL56tb4CDEJ6ben/playlist.m3u8<br>第10集$https://t.bwzybf.com/2018/11/10/Dml8W5lQ5n6Ejnyi/playlist.m3u8<br>第11集$https://t.bwzybf.com/2018/11/11/7v96ygHxhAFusqjl/playlist.m3u8<br>第12集$https://t.bwzybf.com/2018/11/11/pZybi45rgdVmlBDr/playlist.m3u8<br>第13集$https://t.bwzybf.com/2018/11/12/gduCU1wsrHgoxw6P/playlist.m3u8<br>第14集$https://t.bwzybf.com/2018/11/13/Sl16RpumnJqLxeb5/playlist.m3u8<br>第15集$https://t.bwzybf.com/2018/11/13/1fVSqXPDFUJYfyYy/playlist.m3u8<br>第16集$https://t.bwzybf.com/2018/11/13/2AkLsVaof3EN3raZ/playlist.m3u8<br>$$$<播放地址结束-->
<!--海洋CMS地址开始>bwyun$$第01集$https://t.bwzybf.com/share/KDCwbepl4JVTyZHo$bwyun<br>第02集$https://t.bwzybf.com/share/nUpDA3ZryxEKsfwx$bwyun<br>第03集$https://t.bwzybf.com/share/mch0L5j2EICjb0Qx$bwyun<br>第04集$https://t.bwzybf.com/share/1TCiGz7qiRlRQLqI$bwyun<br>第05集$https://t.bwzybf.com/share/tJ9rNGdYluOgjxdK$bwyun<br>第06集$https://t.bwzybf.com/share/aBE7uqViqzscsIG5$bwyun<br>第07集$https://t.bwzybf.com/share/EKxm7pRmK6VEVZtU$bwyun<br>第08集$https://t.bwzybf.com/share/bPQlnSY6QlCKdKi7$bwyun<br>第09集$https://t.bwzybf.com/share/bZL56tb4CDEJ6ben$bwyun<br>第10集$https://t.bwzybf.com/share/Dml8W5lQ5n6Ejnyi$bwyun<br>第11集$https://t.bwzybf.com/share/7v96ygHxhAFusqjl$bwyun<br>第12集$https://t.bwzybf.com/share/pZybi45rgdVmlBDr$bwyun<br>第13集$https://t.bwzybf.com/share/gduCU1wsrHgoxw6P$bwyun<br>第14集$https://t.bwzybf.com/share/Sl16RpumnJqLxeb5$bwyun<br>第15集$https://t.bwzybf.com/share/1fVSqXPDFUJYfyYy$bwyun<br>第16集$https://t.bwzybf.com/share/2AkLsVaof3EN3raZ$bwyun<br>$$$bwm3u8$$第01集$https://t.bwzybf.com/2018/11/05/KDCwbepl4JVTyZHo/playlist.m3u8$bwm3u8<br>第02集$https://t.bwzybf.com/2018/11/05/nUpDA3ZryxEKsfwx/playlist.m3u8$bwm3u8<br>第03集$https://t.bwzybf.com/2018/11/06/mch0L5j2EICjb0Qx/playlist.m3u8$bwm3u8<br>第04集$https://t.bwzybf.com/2018/11/06/1TCiGz7qiRlRQLqI/playlist.m3u8$bwm3u8<br>第05集$https://t.bwzybf.com/2018/11/07/tJ9rNGdYluOgjxdK/playlist.m3u8$bwm3u8<br>第06集$https://t.bwzybf.com/2018/11/07/aBE7uqViqzscsIG5/playlist.m3u8$bwm3u8<br>第07集$https://t.bwzybf.com/2018/11/08/EKxm7pRmK6VEVZtU/playlist.m3u8$bwm3u8<br>第08集$https://t.bwzybf.com/2018/11/08/bPQlnSY6QlCKdKi7/playlist.m3u8$bwm3u8<br>第09集$https://t.bwzybf.com/2018/11/09/bZL56tb4CDEJ6ben/playlist.m3u8$bwm3u8<br>第10集$https://t.bwzybf.com/2018/11/10/Dml8W5lQ5n6Ejnyi/playlist.m3u8$bwm3u8<br>第11集$https://t.bwzybf.com/2018/11/11/7v96ygHxhAFusqjl/playlist.m3u8$bwm3u8<br>第12集$https://t.bwzybf.com/2018/11/11/pZybi45rgdVmlBDr/playlist.m3u8$bwm3u8<br>第13集$https://t.bwzybf.com/2018/11/12/gduCU1wsrHgoxw6P/playlist.m3u8$bwm3u8<br>第14集$https://t.bwzybf.com/2018/11/13/Sl16RpumnJqLxeb5/playlist.m3u8$bwm3u8<br>第15集$https://t.bwzybf.com/2018/11/13/1fVSqXPDFUJYfyYy/playlist.m3u8$bwm3u8<br>第16集$https://t.bwzybf.com/2018/11/13/2AkLsVaof3EN3raZ/playlist.m3u8$bwm3u8<br>$$$<海洋CMS地址结束-->
</div>
</div>
</div>
<div class="ibox playBox">
<div class="playBar liketitle">
<strong>下载地址</strong>
</div>
<div class="vodplayinfo">
<div style="padding-left:10px;word-break: break-all; word-wrap:break-word;">
</div>
</div>
</div>
<!--下载来源开始><下载来源结束-->
<!--下载类型开始><下载类型结束-->
<!--下载地址开始><下载地址结束-->
<!--海洋CMS下载地址开始><海洋CMS下载地址结束-->
<div style="clear:both"></div>
</div>
<!-- 底部截取标签-->
<div class="foot">
<ul class="footb">
<li>本网站所有内容均收集于互联网主流视频网站，不提供在线正版播放。</li>
<li>Copyright ©2017  All Rights Reserved <a href="http://www.baiwanzy.com" target="_blank">www.baiwanzy.com</a> · <a href="/index.php?m=map-baidu.html" target="_blank">百度地图</a> · <a href="/index.php?m=map-google.html" target="_blank">google地图</a> · <a href="/index.php?m=map-rss.html" target="_blank">rss订阅</a></li>
</ul>
</div>
<script language="JavaScript" src="https://s22.cnzz.com/z_stat.php?id=1264558970&amp;web_id=1264558970"></script>
</body>
</html>

Process finished with exit code 0
'''

#ser_url = 'http://www.baiwanzy.com/?m=vod-detail-id-19593.html'
#head = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

#ser = requests.get(ser_url,headers = head).content.decode('utf-8')
soup = BeautifulSoup(req_url_2,'lxml')
#res = soup.find_all('div',style="padding-left:10px;word-break: break-all; word-wrap:break-word;")
res = soup.find('h2').get_text()

print(res)






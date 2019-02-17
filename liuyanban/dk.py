import requests
from bs4 import BeautifulSoup
import lxml
text = '''



<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>
	查询结果
</title><link type="text/css" href="css/style.css" rel="stylesheet" rev="stylesheet" media="all" />

    <script type="text/javascript" src="js/jquery-1.10.1.min.js"></script>

    <script type="text/javascript">
        $(document).ready(function(){  
            $(".stripe .wktr").mouseover(function(){    
                $(this).addClass("over");}).mouseout(function(){    
                    $(this).removeClass("over");})  
            $(".stripe .wktr:even").addClass("alt");    
        });   
    </script>

</head>
<body>
    <form method="post" action="result.aspx?sno=164160318&amp;tid=55" id="form1">
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwULLTE0OTk1MTAxNDYPZBYCAgMPZBYEAgEPFgIeC18hSXRlbUNvdW50AgEWAmYPZBYCZg8VBwwxNjQxNjAzMTggICA45a2Z6KGO6KGOICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAU6K6h566X5py6KOaAgCkxNjMoKikBNgE2AjE1IjxzcGFuIGNsYXNzPSdyZWQnPuS4jeWPiuagvDwvc3Bhbj5kAgMPFgIfAAIEFghmD2QWBGYPFQMBOAEzATNkAgEPFgIfAAIDFgZmD2QWAmYPFQUTMjAxOC8xMC8yMyAxNzo0MzowMhMyMDE4LzEwLzIzIDE4OjUyOjAwAjY5BTAwMDA3CjQxMDk2NTYzNjVkAgEPZBYCZg8VBRMyMDE4LzEwLzI2IDE2OjEyOjQ2EzIwMTgvMTAvMjYgMTY6NDY6NDcCMzQFMDAwMDUKNDEwOTY1NjM2NWQCAg9kFgJmDxUFEzIwMTgvMTAvMjQgMTg6Mjk6MzUTMjAxOC8xMC8yNCAxODo1OTo0NwIzMAUwMDAwNwo0MTA5NjU2MzY1ZAIBD2QWBGYPFQMBOQExATFkAgEPFgIfAAIBFgJmD2QWAmYPFQUTMjAxOC8xMC8zMCAxNzo0NTowOBMyMDE4LzEwLzMwIDE4OjUzOjUyAjY5BTAwMDA5CjQxMDk2NTYzNjVkAgIPZBYEZg8VAwIxMAExATFkAgEPFgIfAAIBFgJmD2QWAmYPFQUSMjAxOC8xMS84IDE3OjM3OjI5EjIwMTgvMTEvOCAxODoxNzowOQI0MAUwMDAwNQo0MTA5NjU2MzY1ZAIDD2QWBGYPFQMCMTEBMQExZAIBDxYCHwACARYCZg9kFgJmDxUFEzIwMTgvMTEvMTMgMTc6NTE6NDUTMjAxOC8xMS8xMyAxODozMzowNAI0MQUwMDAwNwo0MTA5NjU2MzY1ZGRURQNGFHdKCsvWnWHXvgGB6HaP21A253ASrt5A1jrzLQ==" />
</div>

        <div class="div_container">
            <div class="table_title">
                概况</div>
            <table class="table">
                <thead>
                    <tr>
                        <td style="width: 100px;">
                            学号
                        </td>
                        <td style="width: 100px;">
                            姓名
                        </td>
                        <td style="width: 100px;">
                            班级
                        </td>
                        <td style="width: 100px;">
                            活动次数
                        </td>
                        <td style="width: 100px;">
                            有效次数
                        </td>
                        <td style="width: 100px;">
                            通过次数
                        </td>
                        <td style="width: 100px;">
                            成绩
                        </td>
                    </tr>
                </thead>
                
                        <tr>
                            <td>
                                164160318   
                            </td>
                            <td>
                                孙衎衎                                               
                            </td>
                            <td>
                                计算机(怀)163(*)
                            </td>
                            <td>
                                6
                            </td>
                            <td>
                                6
                            </td>
                            <td>
                                15
                            </td>
                            <td>
                                <span class='red'>不及格</span>
                            </td>
                        </tr>
                    
            </table>
        </div>
        <div class="div_container">
            <div class="table_title">
                活动记录</div>
            <table class="table stripe">
                <thead>
                    <tr>
                        <td rowspan="2" style="width: 100px;">
                            周次
                        </td>
                        <td rowspan="2" style="width: 100px;">
                            活动次数
                        </td>
                        <td rowspan="2" style="width: 100px;">
                            有效次数
                        </td>
                        <td colspan="5">
                            活动明细
                        </td>
                    </tr>
                    <tr>
                        <td style="width: 150px;">
                            进场时间
                        </td>
                        <td style="width: 150px;">
                            出场时间
                        </td>
                        <td style="width: 150px;">
                            活动时长（分钟）
                        </td>
                        <td style="width: 150px;">
                            Pos机号
                        </td>
                        <td style="width: 150px;">
                            卡号
                        </td>
                    </tr>
                </thead>
                
                        <tr class="wktr">
                            <td style="width: 50px;">
                                8
                            </td>
                            <td style="width: 50px;">
                                3
                            </td>
                            <td style="width: 50px;">
                                3
                            </td>
                            <td colspan="5">
                                <table>
                                    
                                            <tr>
                                                <td style="width: 150px;">
                                                    2018/10/23 17:43:02
                                                </td>
                                                <td style="width: 150px;">
                                                    2018/10/23 18:52:00
                                                </td>
                                                <td style="width: 150px;">
                                                    69
                                                </td>
                                                <td style="width: 150px;">
                                                    00007
                                                </td>
                                                <td style="width: 150px;">
                                                    4109656365
                                                </td>
                                            </tr>
                                        
                                            <tr>
                                                <td style="width: 150px;">
                                                    2018/10/26 16:12:46
                                                </td>
                                                <td style="width: 150px;">
                                                    2018/10/26 16:46:47
                                                </td>
                                                <td style="width: 150px;">
                                                    34
                                                </td>
                                                <td style="width: 150px;">
                                                    00005
                                                </td>
                                                <td style="width: 150px;">
                                                    4109656365
                                                </td>
                                            </tr>
                                        
                                            <tr>
                                                <td style="width: 150px;">
                                                    2018/10/24 18:29:35
                                                </td>
                                                <td style="width: 150px;">
                                                    2018/10/24 18:59:47
                                                </td>
                                                <td style="width: 150px;">
                                                    30
                                                </td>
                                                <td style="width: 150px;">
                                                    00007
                                                </td>
                                                <td style="width: 150px;">
                                                    4109656365
                                                </td>
                                            </tr>
                                        
                                </table>
                            </td>
                    
                        <tr class="wktr">
                            <td style="width: 50px;">
                                9
                            </td>
                            <td style="width: 50px;">
                                1
                            </td>
                            <td style="width: 50px;">
                                1
                            </td>
                            <td colspan="5">
                                <table>
                                    
                                            <tr>
                                                <td style="width: 150px;">
                                                    2018/10/30 17:45:08
                                                </td>
                                                <td style="width: 150px;">
                                                    2018/10/30 18:53:52
                                                </td>
                                                <td style="width: 150px;">
                                                    69
                                                </td>
                                                <td style="width: 150px;">
                                                    00009
                                                </td>
                                                <td style="width: 150px;">
                                                    4109656365
                                                </td>
                                            </tr>
                                        
                                </table>
                            </td>
                    
                        <tr class="wktr">
                            <td style="width: 50px;">
                                10
                            </td>
                            <td style="width: 50px;">
                                1
                            </td>
                            <td style="width: 50px;">
                                1
                            </td>
                            <td colspan="5">
                                <table>
                                    
                                            <tr>
                                                <td style="width: 150px;">
                                                    2018/11/8 17:37:29
                                                </td>
                                                <td style="width: 150px;">
                                                    2018/11/8 18:17:09
                                                </td>
                                                <td style="width: 150px;">
                                                    40
                                                </td>
                                                <td style="width: 150px;">
                                                    00005
                                                </td>
                                                <td style="width: 150px;">
                                                    4109656365
                                                </td>
                                            </tr>
                                        
                                </table>
                            </td>
                    
                        <tr class="wktr">
                            <td style="width: 50px;">
                                11
                            </td>
                            <td style="width: 50px;">
                                1
                            </td>
                            <td style="width: 50px;">
                                1
                            </td>
                            <td colspan="5">
                                <table>
                                    
                                            <tr>
                                                <td style="width: 150px;">
                                                    2018/11/13 17:51:45
                                                </td>
                                                <td style="width: 150px;">
                                                    2018/11/13 18:33:04
                                                </td>
                                                <td style="width: 150px;">
                                                    41
                                                </td>
                                                <td style="width: 150px;">
                                                    00007
                                                </td>
                                                <td style="width: 150px;">
                                                    4109656365
                                                </td>
                                            </tr>
                                        
                                </table>
                            </td>
                    
            </table>
        </div>
    </form>
</body>
</html>

'''
#url = 'http://1.51.45.102:9500/'
#header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#res = requests.get(url,headers = header).content.decode('utf-8')
soup = BeautifulSoup(text,'lxml')
res = soup.find_all('td')
print(res[13].get_text().strip())

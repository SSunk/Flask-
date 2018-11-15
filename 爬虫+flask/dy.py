from flask import Flask,render_template,request
from bs4 import BeautifulSoup
import requests,re
app = Flask(__name__)
#zztj = '''<script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_1274386182'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s22.cnzz.com/z_stat.php%3Fid%3D1274386182%26show%3Dpic1' type='text/javascript'%3E%3C/script%3E"));</script>'''

ser_url = 'http://www.baiwanzy.com/index.php?m=vod-search'
pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    else:
        temp = []
        name = request.form.get('name')
        data = {
            'wd': name,
            'submit': 'search'
        }
        ser = requests.post(ser_url, data=data, headers=head).content.decode('utf-8')
        soup = BeautifulSoup(ser, 'lxml')
        resau = soup.find_all('span', class_='xing_vb4')
        for each in resau:
            tt = requests.get('http://www.baiwanzy.com' + each.a['href'], headers=head).content.decode('utf-8')
            soup = BeautifulSoup(tt, 'lxml')
            re_pm = soup.find('h2').get_text()
            res = soup.find_all('li')
            re_mb = []
            for each in res:
                if 'https:' in each.get_text():
                    re_mb.append(each.get_text().strip())
            for i in re_mb:
                hre = re.findall(pattern,i)
                context = {
                    'name':re_pm,
                    'link':i,
                    'hre':hre[0]
                }
                temp.append(context)
        return render_template('mov.html',link = temp)





if __name__ == '__main__':
    app.run(debug=True)

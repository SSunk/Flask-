from flask import Flask,render_template,request,redirect,url_for
from model import User
from exts import db
import config
import requests
from bs4 import BeautifulSoup
import lxml



app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


@app.route('/')
def index():
    context = {
        'questions': User.query.order_by('-create_time').all()
    }
    return render_template('index.html', **context)

@app.route('/liuyan/',methods=['GET','POST'])
def liuyan():
    if request.method=='GET':
        return render_template('liuyan.html')
    else:
        name = request.form.get('name')
        content = request.form.get('context')
        leixing = '留言'
        ly_all =User(name=name,context=content,leixing=leixing)
        db.session.add(ly_all)
        db.session.commit()
        return redirect(url_for('index'))



@app.route('/biaobai/',methods=['GET','POST'])
def biaobai():
    if request.method=='GET':
        return render_template('biaobai.html')
    else:
        name = request.form.get('name')
        content = request.form.get('context')
        leixing = '表白'
        ly_all =User(name=name,context=content,leixing=leixing)
        db.session.add(ly_all)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/swzl/',methods=['GET','POST'])
def swzl():
    if request.method=='GET':
        return render_template('swzl.html')
    else:
        name = request.form.get('name')
        content = request.form.get('context')
        leixing = '失物招领'
        ly_all =User(name=name,context=content,leixing=leixing)
        db.session.add(ly_all)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/dkcx/',methods=['GET','POST'])
def dkcx():
    if request.method=='GET':
        return render_template('dkcx.html')
    else:
        sno = request.form.get('xuehao')
        url ='http://1.51.45.102:9500/result.aspx?sno=' +str(sno)+ '&tid=55'
        res = requests.get(url, headers=header).content.decode('utf-8')
        soup = BeautifulSoup(res, 'lxml')
        res = soup.find_all('td')
        context = {
            'sno':res[7].get_text().strip(),
            'name':res[8].get_text().strip(),
            'class':res[9].get_text().strip(),
            'hdcs':res[10].get_text().strip(),
            'yxcs':res[11].get_text().strip(),
            'tgcs':res[12].get_text().strip(),
            'cj':res[13].get_text().strip()



        }
        return render_template('res.html',info = context)




@app.route('/detail/<id>/',methods=['GET','POST'])
def detail(id):
    if request.method=='GET':
        question_model = User.query.filter(User.id==id).first()
        return render_template('detail.html',ques = question_model)




if __name__ == '__main__':
    app.run()

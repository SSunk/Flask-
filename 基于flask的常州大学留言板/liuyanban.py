from flask import Flask,render_template,request,redirect,url_for
from model import User
from exts import db
import config


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


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



if __name__ == '__main__':
    app.run()

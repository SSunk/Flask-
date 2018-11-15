from flask import Flask,render_template,request,url_for,redirect,session
from models import User,Question
from exts import db
import config
from functools import wraps
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


def login_require(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper



@app.route('/')
def index():
    context = {
        'questions':Question.query.order_by('-create_time').all()
    }
    return render_template('index.html',**context)

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        name = request.form.get('name')
        password = request.form.get('password')
        user = User.query.filter(User.name==name,User.password==password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '密码输入错了( •̀ ω •́ )'
@app.context_processor
def my_context():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id==user_id).first()
        if user:
            return {'user':user}
    return { }

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/register/',methods=['GET','POST'])
def  register():
    if request.method=='GET':
        return render_template('res.html')
    else:
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter(User.name==name).first()
        if user:
            return '这个昵称已经被别人起啦！'
        else:
            if password1==password2:
                user=User(name=name,password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))
            else:
                return '输入的密码不一致哦'

@app.route('/question/',methods=['GET','POST'])
@login_require
def question():
    if request.method=='GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title,content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id==user_id).first()
        question.author=user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))





if __name__ == '__main__':
    app.run()

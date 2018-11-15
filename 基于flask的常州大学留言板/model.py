from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),nullable=False)
    leixing = db.Column(db.String(10),nullable=False )
    context = db.Column(db.String(128),nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)



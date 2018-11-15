import os

DEBUG = True
SECRET_KEY = os.urandom(24)
HOSTNAME='134.175.53.90'
PORT='3306'
USERNAME="root"
PASSWORD="123456"
DATABASE='skk'
DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URL
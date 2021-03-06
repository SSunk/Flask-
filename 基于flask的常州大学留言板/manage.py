from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from liuyanban import app
from exts import db
from model import User
manage = Manager(app)
migrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)


if __name__=='__main__':
    manage.run()
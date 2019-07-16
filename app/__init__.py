import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = '3502cc525b3a33ac9b0d4c8664fdfb3c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

_db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_USE_TLS'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'dsb007151@gmail.com'
app.config['MAIL_PASSWORD'] = 'mahadev24041'
mail = Mail(app)


from app import routes

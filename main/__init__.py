import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
import datetime


app = Flask(__name__)
app.config['SECRET_KEY']='43645dfsgfddfgsfgsf'
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DATABASE_URL")


db =SQLAlchemy(app)

bcrypt =Bcrypt(app)
from main import routes

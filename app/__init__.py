from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "supers3cre+br@in"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://gawayne:postgres@localhost/project1"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lhzxwlzmcdjbtc:31cfcc8f1f2b0ca28eaebb71b0e6b1835f67335f9298b6580b6c8406f409c2ee@ec2-23-21-198-69.compute-1.amazonaws.com:5432/dda70olebu408d"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
UPLOAD_FOLDER = './app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
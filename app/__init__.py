from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the app
# instance_relative_config tells the app that configuration files are relative to the instance folder
app = Flask(__name__, instance_relative_config=True)

# configurate the app
# config a database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
# disable the flask modification tracking feature to avoid error messages
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a SQLAlchemy database handler
db = SQLAlchemy(app)

# initiate other scripts
from app import routes, models

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'ed96823c766c274dc3bd19e0'
bcrypt = Bcrypt(app)

db = SQLAlchemy(app)

from markets import routes

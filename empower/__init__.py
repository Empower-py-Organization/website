# Import Flask for flask app object
from flask import Flask


# Import config
from config import Config


# Import Flask modules
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


# Create flask app object
app = Flask(__name__)
app.config.from_object(Config)


# Create Database object from brcrypt object
#db = SQLAlchemy(app)
#bcrypt = Bcrypt(app)


# Create Login manager
#login_manager = LoginManager(app)
#login_manager.login_view = 'login'
#login_manager.login_message_category = 'warning'


# importing all the models and initializing them
#from empower.models import *
#db.create_all()

# Import all views
import empower.views

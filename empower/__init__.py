# Import Flask for flask app object
from flask import Flask

# Import config
from config import Config


# Create flask app object
app = Flask(__name__)
app.config.from_object(Config)


# Import all views
import empower.views

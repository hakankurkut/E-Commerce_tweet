from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLALchemy


# create instance of app variable
app = Flask(__name__)

# all other variable instances need to come after the app instance
bootstrap = Bootstrap(app)
app.config.from_object(Config)

# app variables for database usage
db = SQLALchemy(app)
migrate = Migrate(app, db)

# once app variable is creating
from app import routes

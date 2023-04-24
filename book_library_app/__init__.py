#  __init__ informs that this folder is a package, we will be able to import objects from this folder

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)   # read setting for app from object

db = SQLAlchemy(app)
migrate = Migrate(app, db)




from book_library_app import authors   # app has to be created before this import
from book_library_app import models
from book_library_app import db_manage_commands
from book_library_app import errors

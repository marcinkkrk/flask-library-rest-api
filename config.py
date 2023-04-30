import os
from dotenv import load_dotenv
from pathlib import Path

base_dir = Path(__file__).resolve().parent # path to folder book_library_app
                       #resolve - full path

env_file = base_dir / '.env'   # path to file .env
load_dotenv(env_file)          # load setting from this file (environment variable)


class Config:   # keep setting of our application
    #DEBUG = True   # Automatic restart after a change in the application
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Ensure data security
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Requires extra memory
    PER_PAGE = 5

#print(Config.SECRET_KEY)   # check if key is correct

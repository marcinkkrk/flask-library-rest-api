import json
from pathlib import Path
from datetime import datetime

from book_library_app import app, db
from book_library_app.models import Author
from sqlalchemy import text

@app.cli.group()
def db_manage():
    """Database management commands"""
    pass


@db_manage.command()
def add_data():
    """Add samlple data to database"""
    try:
        autors_path = Path(__file__).parent / 'samples' / 'authors.json'
        with open(autors_path) as file:
            data_json = json.load(file)
        for item in data_json:
            item['birth_date'] = datetime.strptime(item['birth_date'], '%d-%m-%Y').date()
            author = Author(**item)
            db.session.add(author)
        db.session.commit()
        print('Data has beed sucessfully added to database')
    except Exception as exc:
        print("Unexpected error: {}".format(exc))


@db_manage.command()
def remove_data():
    """Remove data from the database"""
    try:
        db.session.execute(text('TRUNCATE TABLE authors'))
        db.session.commit()
        print('Data has been successfully removed from database')
    except Exception as exc:
        print("Unexpected error: {}".format(exc))
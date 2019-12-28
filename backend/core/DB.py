from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy_utils import database_exists, create_database, drop_database

app = Flask(__name__)

DB_URL = "postgresql://postgres:kid@db/enrolle"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db=SQLAlchemy(app)



class commn(db.Model):
    enrollment_id = db.Column(db.String(255), primary_key=True)
    nanodegree_key = db.Column(db.String(255))
    enrolled_at = db.Column(db.DateTime())
    udacity_user_key = db.Column(db.String(255))
    status = db.Column(db.String(255))

    def __init__(self, ID,nanoKey,enrolAt,UK,state):
        self.enrollment_id=ID
        self.nanodegree_key=nanoKey 
        self.enrolled_at=enrolAt 
        self.udacity_user_key=UK 
        self.status=state 
    

def resetdb():
    """Destroys and creates the database + tables."""

    if database_exists(DB_URL):
        print('Deleting database.')
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        print('Creating database.')
        create_database(DB_URL)

    print('Creating tables.')
    db.create_all()
    print('Shiny!')


def setdb():
    """creates the database + tables."""

    if not database_exists(DB_URL):
        print('Creating database.')
        create_database(DB_URL)

    print('Creating tables.')
    db.create_all()
    print('Shiny!')

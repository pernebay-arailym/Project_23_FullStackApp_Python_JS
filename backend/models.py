#Find database models
from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primery_key=True)
    #this is a key that we use to index, must be unique for every single entry of the database
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
#Find database models
from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primery_key=True)
    #this is a key that we use to index, must be unique for every single entry of the database
    
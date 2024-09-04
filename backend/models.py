#Find database models
from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #this is a key that we use to index, must be unique for every single entry of the database
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self): #JSON takes all of the fields we have in contact and converts it to Python dictionary and we can pass from out API
        return {
            "id": self.id,
            "firstName": self.last_name, #camel case used for JSON, word & Capital lett.word
            "lastName": self.last_name,
            "email": self.email,
        }

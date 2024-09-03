from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#Our server can't be hit from a different URL. Also need to connect frontend with backend

app = Flask(__name__) #Next, wrap out app into CORS
CORS(app)

#Initialize database things
#Specifying the location of the local SQL where we store our machine
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"


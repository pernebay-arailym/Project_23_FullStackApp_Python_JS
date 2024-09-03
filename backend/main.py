#create   #CRUD = create, read/get, update, delete
#- first_name
#- last_name
#- email
#Request
#type: POST (create smth new, for ex: create_contact)
#type: PATCH (update request)
#type: DELETE   (we send the request from frontend to backend)
#json: {
#
#}
#Response
#status: 200 = success, 404 = not found, 403 = forbidden, 400 = bad request
#json;{
#    to respond to get a contact
#}  API return response 

from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all() #gives a list of all contacts


if __name__ == "__main__":
    with app.app_context():
        db.create_all() #speed up the db


    app.run(debug=True)



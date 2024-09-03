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
    json_contacts = list(map(lambda x: x.to_json(), contacts)) #map takes all elements from the list 
    return jsonify({"contacts": json_contacts}), 200 #contacts in python dict will be associated with json, we convert into JSON using jsonify fucntion

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a forst name, last name and email"}), 
            400,
        )
    
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created!"}), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all() #speed up the db


    app.run(debug=True)



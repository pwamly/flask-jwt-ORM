from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Branch
from flask_session import Session
from flask import jsonify
from datetime import datetime
import uuid
from werkzeug.security import generate_password_hash

userid = uuid.uuid4()  # to bdo ........... to be return to the setter and getter


def create(data, db):

 phone = data['phone']
 email = data['email']
 client_id = data['client_id']
 created = datetime.utcnow()


 # check if contact exists
 contact = Contact.query.filter_by(id=id).first()

 if not user:
  try:

      client = Client.query.filter_by(id=client_id).first()

      contact = Contact(phone=name, email=email, tinNumber=tinNumber, created=created, client_id=client.id)

      db.session.add(contact)
      db.session.commit()

      return 'Contact created'

  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to create contact'}), 403
      pass
 return jsonify({'message': 'Contact already exist!'}), 407

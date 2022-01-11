from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Users
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash



def registerUser(data, db):
 userid = uuid.uuid4()  # todo ........... to be return to the setter and getter
 firstname = data['firstname']
 lastname = data['lastname']
 email = data['email']
 branch = data['branch']
 role = data['role']
 phone = data['phone']
 password = data['password']
 
 
 
#  check if user exists
 user = Users.query.filter_by(email=email).first()
 if not user:
  try:
      pas = generate_password_hash(password)
      user = Users(fname=firstname, lname=lastname, branch=branch, email=email, userid=userid,
                   role=role, phone=phone, password=pas, isadmin=False)
      db.session.add(user)
      db.session.commit()
      return jsonify({'message': 'User added'}), 200

  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to register'}), 403
      pass
 return jsonify({'message': 'User already exist!'}), 409
 
 
from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Users
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash

userid = uuid.uuid4()  # todo ........... to be return to the setter and getter


def updateUser(data,userId, db):
    
 firstname = data['firstname']
 lastname = data['lastname']
 email = data['email']
 branch = data['branch']
 role = data['role']
 phone = data['phone']
 password = data['password']
 
 
 
#  check if user exists
 user = Users.query.filter_by(userid=userId).first()
 if user:
  try:
      if password:
         hash = generate_password_hash(password) 
         user.password = hash
      
      if firstname:
          user.fname=firstname
          print('ccccccccccc',firstname)
          
      if lastname:
          user.lname=lastname
          print('ccccccccccc',lastname)
          
      if branch:
          user.branch=branch
          print('ccccccccccc',branch)
          
      if role:
          user.role=role
          print('cccccccccccccccc',role)
          
      if phone:
          user.phone=phone
          print('ccccccccccc',phone)
          
      if email:
          user.email=email
          print('ccccccccccccc,email')
        
      user.isadmin=False
      db.session.add(user)
      db.session.commit()
      return jsonify({'message': 'User added'}), 200

  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to register'}), 403
      pass
 return jsonify({'message': 'User already exist!'}), 409
 
 
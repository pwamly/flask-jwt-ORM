from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Users
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash

userid = uuid.uuid4()  # todo ........... to be return to the setter and getter


def updateUser(data,userId, db):
    
 branchId = data['branchId']
 branchname = data['branchname']
 region = data['region']
 district = data['district']
 robranchaddressle = data['branchaddress']
 
#  check if user exists
 user = Users.query.filter_by(branchId=branchId).first()
 if user:
  try:
      if branchname:
         user.branchname = branchname
      
      if region:
          user.region=region
          
      if district:
          user.district=district
          
      if robranchaddressle:
          user.robranchaddressle=robranchaddressle
          
      user.isadmin=False
      db.session.add(user)
      db.session.commit()
      return jsonify({'message': 'Branch updated'}), 200

  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to update branch'}), 403
      pass
 return jsonify({'message': 'Branch not found!'}), 409
 
 
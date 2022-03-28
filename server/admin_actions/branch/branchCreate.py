from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Branch,Destination
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash

userid = uuid.uuid4()  # to bdo ........... to be return to the setter and getter


def create(data, db):
 branchId=data['branchId']
 branchname=data['branchname']
 region=data['region']
#  district=data['district']
 branchaddress=data['branchaddress']
 
 # check if user exists
 user = Branch.query.filter_by(branchname=branchname).first()
 destnid=Destination.query.filter_by(destinationid=region).first().id
 if not user:
  try:
      user = Branch(branchId=branchId, branchname=branchname, region=destnid, branchaddress=branchaddress)
      db.session.add(user)
      db.session.commit()
      print('Branch created')
      return 'Branch created'

  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to create branch'}), 403
      pass
 return jsonify({'message': 'User already exist!'}), 407
 
 
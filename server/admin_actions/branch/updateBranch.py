from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Branch,Destination
from datetime import datetime, timedelta
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash

userid = uuid.uuid4()  # todo ........... to be return to the setter and getter


def updateBranch(data, branchId, db):
 branchId = data['branchId']
 branchname = data['branchname']
 region = data['region']
 branchaddress = data['branchaddress']
 updated = datetime.now()

 
#  check if user exists
 branch = Branch.query.filter_by(branchId=branchId).first()
 destnid=Destination.query.filter_by(destinationid=region).first().id
 if branch:
  try:
      if branchname:
         branch.branchname = branchname
      
      if region:
          branch.region = destnid
          
      if branchaddress:
          branch.branchaddress = branchaddress
          
      if updated:
          branch.updated = updated
          
      branch.isadmin = False
      db.session.add(branch)
      db.session.commit()
      return jsonify({'message': 'Branch updated'}), 200

  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to update branch'}), 403
      pass
 return jsonify({'message': 'Branch not found!'}), 409
 
 
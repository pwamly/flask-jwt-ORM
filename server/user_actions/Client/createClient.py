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

 name = data['name']
 address = data['address']
 tinNumber = data['tinNumber']
 contactPerson = data['contactPerson']
 logo = data['logo']
 physicalLocation = data['physicalLocation']
 status = data['status']
 created = datetime.utcnow()
 region_id = data['region_id']


 # check if client exists
 client = Client.query.filter_by(name=name).first()
 if not client:
  try:
      region = Region.query.filter_by(region_id=regionId).first()

      if region is not None:
          client = Client(name=name, address=address, tinNumber=tinNumber, contactPerson=contactPerson, logo=logo, status=status, region_id=region.id, physicalLocation=physicalLocation, created=created)

          db.session.add(client)
          db.session.commit()

          return 'Client created'

  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to create client'}), 403
      pass
 return jsonify({'message': 'Client already exist!'}), 407

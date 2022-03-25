from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Transporter
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash


# to bdo ........... to be return to the setter and getter

def regTransporter(data, db):
 transporterid = uuid.uuid4()
 name = data['name']
 email = data['email']
 phone = data['phone']
 address = data['address']
 route = data['route']
 vehicledetails = data['vehicledetails']
 tin =data['tin']
 vrn=data['vrn']

 # check if user exists
 transporter = Transporter.query.filter_by(email=email).first()
 if not transporter:
  try:
      trans = Transporter(transporterid=transporterid,
                          name=name,
                          phone=phone,
                          email=email,
                          address=address, vehicledetails=vehicledetails,tin=tin,vrn=vrn,
                          route=route)
      db.session.add(trans)
      db.session.commit()
      print('Transporter registered')
      return 'Transporter registered'

  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to register transporter'}), 403
      pass
 return jsonify({'message': 'transporter already exist!'}), 407

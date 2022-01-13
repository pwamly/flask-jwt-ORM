from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Vehicle
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash

  # to bdo ........... to be return to the setter and getter

def regvehicle(data, db):
 vehid = uuid.uuid4()   
 name=data['name']
 plateno=data['plateno']
 model=data['model']
 loadcapacity=data['loadcapacity']
 status = data['status']
 routestatus = data['routestatus']
 
 # check if user exists
 vehicle = Vehicle.query.filter_by(plateno=plateno).first()
 if not vehicle:
  try:
      vehicle = Vehicle( vehicleid=vehid,
      name=name,
      plateno=plateno,
      model=model,
      loadcapacity=loadcapacity,
      status = status,
      routestatus = routestatus)
      db.session.add(vehicle)
      db.session.commit()
      print('Vehicle registered')
      return 'Vehicle registered'

  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to register vehicle'}), 403
      pass
 return jsonify({'message': 'vehicle already exist!'}), 407
 
 
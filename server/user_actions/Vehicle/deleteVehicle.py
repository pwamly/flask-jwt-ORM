from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Vehicle
from flask_session import Session
from flask import jsonify



def deleteVehicle(id, db):   
 try:
   
    effected_rows = db.session.query(Vehicle).filter(Vehicle.vehicleid == id).delete()
    if effected_rows == 0:
        print('Vehicle  not found')
        return {}
    else:
      db.session.commit()
      return jsonify({'message': 'vehicle deleted'}), 200
 except Exception as e:
      print('iiiiiiiiiii',e)
      return jsonify({'message': 'Failed to delete vehicle'}), 403
      pass
 
from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Regions
from flask_session import Session
from flask import jsonify


def deleteRegion(id, db):
 try:

    effected_rows = db.session.query(Regions).filter(
        Regions.regionId == id).delete()
    if effected_rows == 0:
        print('Region not found')
        return {}
    else:
      db.session.commit()
      return jsonify({'message': 'Region deleted'}), 200
 except Exception as e:
     print('s', e)
     return jsonify({'message': 'Failed to delete Region'}), 403
     pass

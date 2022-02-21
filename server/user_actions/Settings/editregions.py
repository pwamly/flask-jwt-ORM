from jwt import exceptions
from server.models import Regions
from flask_session import Session
from flask import jsonify
import uuid

userid = uuid.uuid4()  # todo ........... to be return to the setter and getter


def updateRegion(data, regionid, db):

 regiondata = data['region']

#  check if user exists
 region = Regions.query.filter_by(regionId=regionid).first()
 if region:
  try:
      if regiondata:
         region.region = regiondata
         db.session.add(region)
         db.session.commit()
         return jsonify({'message': 'Region updated'}), 200
  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to update region'}), 403
      pass
 return jsonify({'message': 'Region not found!'}), 409

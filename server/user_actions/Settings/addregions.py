from flask_sqlalchemy import model
from datetime import datetime
from jwt import exceptions
from server.models import Regions
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash


def registerRegion(data, db):
 regionId = uuid.uuid4()  # todo ........... to be return to the setter and getter
 region_ = data['region']


#  check if user exists
 region = Regions.query.filter_by(region=region_).first()

 if not region:

  try:
      regions = Regions(region=region_, regionId=regionId)
      regions.created = datetime.utcnow()
      db.session.add(regions)
      db.session.commit()
      return jsonify({'message': 'region  added'}), 200

  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to register'}), 403
      pass
 return jsonify({'message': 'A region already exist!'}), 409

from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Bundle
from flask_session import Session
from flask import jsonify
import uuid


def register(data, db):
 bundleid = uuid.uuid4()  # to bdo ........... to be return to the setter and getter
 bundlename = data['bundlename']  # example Dar-Mwanza-1-11-2020

 # check if user exists
 bundle = Bundle.query.filter_by(bundeleid=bundleid).first()
 if not bundle:
  try:
      bundle = Bundle(bundeleid=bundleid)
      db.session.add(bundle)
      db.session.commit()
      print('registered')
      return 'registered'

  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to create a bundle'}), 403
      pass
 return jsonify({'message': 'Bundle already exist!'}), 407

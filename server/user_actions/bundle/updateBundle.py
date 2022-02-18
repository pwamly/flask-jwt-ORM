import uuid
from flask import jsonify, g
from flask_session import Session
from server.models import Bundle, Order, Branch
from jwt import exceptions
from flask_sqlalchemy import model
from server.models import Bundle
from flask import jsonify


def updateBundle(data, bundleid, db):
 oderstobebundled = data['ordertobebundled']
 bundleid = data['bundleid']

 # check if user exists
 bundle = Bundle.query.filter_by(bundleid=bundleid).first()
 if bundle:
  try:
      for order in oderstobebundled:
          updatedorder = Order.query.filter_by(
              orderid=order['orderid']).first()
          updatedorder.bundleId = bundleid
          updatedorder.isbundled = True
          db.session.add(updatedorder)
          db.session.commit()
      return 'updated'

  except Exception as e:
      return jsonify({'message': 'Failed to update a bundle'}), 403
      pass
 return jsonify({'message': 'Bundle already exist!'}), 407

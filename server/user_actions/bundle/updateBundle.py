import uuid
from flask import jsonify, g
from flask_session import Session
from server.models import Bundle, Order, Branch
from jwt import exceptions
from flask_sqlalchemy import model
from server.models import Bundle
from flask import jsonify


def updateUser(data, bundleid, db):

 bundlename = data['bundlenam']


#  check if user exists
 bundle = Bundle.query.filter_by(bundleid=bundleid).first()
 if bundle:
  try:
      if bundlename:
          bundle.bundlenam = bundlename
          print('ccccccccccc', bundlename)

      bundle.isadmin = False
      db.session.add(bundle)
      db.session.commit()
      return jsonify({'message': 'bundle updated'}), 200

  except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to register'}), 403
      pass
 return jsonify({'message': 'User already exist!'}), 409


# ..........................add()


def createBundle(data, db):
 bundleid = uuid.uuid4()  # to bdo ........... to be return to the setter and getter
 bundlename = data['bundlename']  # example Dar-Mwanza-1-11-2020
 oderstobebundled = data['ordertobebundled']
 bundleto = data['to']

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
 return jsonify({'message': 'Bundle not exist!'}), 407

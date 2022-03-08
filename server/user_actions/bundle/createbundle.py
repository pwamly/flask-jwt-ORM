from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Bundle, Order, Branch
from flask_session import Session
from flask import jsonify, g
import uuid


def createBundle(data, db):
 bundleid = uuid.uuid4()  # to bdo ........... to be return to the setter and getter
 bundlename = data['bundlename']  # example Dar-Mwanza-1-11-2020
 oderstobebundled = data['ordertobebundled']
 bundleto = data['to']

 # check if user exists
 bundle = Bundle.query.filter_by(bundlename=bundlename).first()
 branch = Branch.query.filter_by(branchId=g.userBranchId).first()
 if not bundle:
  try:
      bundle = Bundle(bundleid=bundleid, bundlename=bundlename,
                      bundleto=bundleto, bundlefrom=branch.region, status='Unloaded')
      db.session.add(bundle)
      db.session.commit()

      for order in oderstobebundled:
          updatedorder = Order.query.filter_by(
              orderid=order['orderid']).first()
          updatedorder.bundleId = bundleid
          updatedorder.isbundled = True
          db.session.add(updatedorder)
          db.session.commit()
      return 'registered'

  except Exception as e:
      print('')
      return jsonify({'message': 'Failed to create a bundle'}), 403
      pass
 return jsonify({'message': 'Bundle already exist!'}), 407

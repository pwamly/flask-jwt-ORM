from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Item, Order
from flask import jsonify
from datetime import datetime, timedelta


def deliverBundle(bundleid, data, db):

    orders = Order.query.filter_by(bundleId=bundleid)
    if orders:
        for order in orders:
            try:
                order.orderStatus = 'Dispatched'
                order.orderdeliverytime = datetime.now()
                db.session.add(order)
                db.session.commit()
            except Exception as e:
                print(e)
                return jsonify({'message': 'Failed to dispatch item'}), 403
                pass
        return jsonify({'message': ' Dispatched'}), 200
    return jsonify({'message': 'item does not exist!'}), 409

from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Item, Order, Bundle
from flask import jsonify
from datetime import datetime, timedelta


def deliverBundle(bundleid, data, db):

    orders = Order.query.filter_by(bundleId=bundleid).all()

    bundlec = Bundle.query.filter_by(bundleid=bundleid).first()

    if bundlec:
        bundlec.status = 'Dispatched'
        bundlec.dispatchDelivered = True
        bundlec.updated = datetime.utcnow()
        db.session.add(bundlec)
        db.session.commit()

    if orders:
        for order in orders:
            try:
                itemList = Item.query.filter_by(orderid=order.orderid)

                for item in itemList:
                    item.dispatchDeliveredTime = datetime.now()
                    order.dispatchDelivered = True
                    order.orderStatus = 'Dispatched'
                    item.status = 'Dispatched'
                    db.session.add(item)
                    order.orderdeliverytime = datetime.now()
                    db.session.add(order)
                    db.session.commit()
            except Exception as e:
                print(e)
                return jsonify({'message': 'Failed to dispatch item'}), 403
                pass
        return jsonify({'message': ' Dispatched'}), 200
    return jsonify({'message': 'item does not exist!'}), 409

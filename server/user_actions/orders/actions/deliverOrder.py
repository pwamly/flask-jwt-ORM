from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Item, Order
from flask import jsonify
from datetime import datetime, timedelta


def deliverOrder(itemid, data, db):

    deliveredunits = data['deliveredunits']
    itemdeliverynote = data['itemdeliverynote']
    orderid = data['orderid']

#  todo check if order has all items picked.

    item = Item.query.filter_by(itemid=itemid).first()
    orders = Order.query.filter_by(orderid=orderid).first()
    if Item:
        if orders:

            try:
                if deliveredunits:
                    item.deliveredunits = deliveredunits

                if itemdeliverynote:
                    item.itemdeliverynote = itemdeliverynote

                item.itemdelivered = True
                item.deliverytime = datetime.now()
                orders.orderDelivered = True
                item.status = 'Delivered'
                orders.orderStatus = 'Delivered'
                orders.orderdeliverytime = datetime.now()
                db.session.add(item)
                db.session.add(orders)
                db.session.commit()
                return jsonify({'message': 'item delivered'}), 200

            except Exception as e:
                print(e)
                return jsonify({'message': 'Failed to unload item'}), 403
                pass

    return jsonify({'message': 'item does not exist!'}), 409

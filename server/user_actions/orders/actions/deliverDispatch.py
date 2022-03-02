from xmlrpc.client import Boolean
from flask_sqlalchemy import model
from jwt import exceptions
from sqlalchemy import true
from server.models import Item, Order
from flask import jsonify
from datetime import datetime, timedelta


def deliverDispatch(itemid, data, db):
    dispatchDeliveryunits = data['dispatchDeliveryunits']
    dispatchDeliverynote = data['dispatchDeliverynote']
    orderid = data['orderid']

    item = Item.query.filter_by(itemid=itemid).first()
    orders = Order.query.filter_by(orderid=orderid).first()
    if item:
        if orders:
            try:
                if dispatchDeliveryunits:
                    item.dispatchDeliveryunits = dispatchDeliveryunits

                if dispatchDeliverynote:
                    item.dispatchDeliverynote = dispatchDeliverynote


                item.dispatchDeliveredTime = datetime.now()
                orders.dispatchDelivered = True
                orders.orderStatus = 'Dispatched'
                orders.dispatchDeliveredTime = datetime.now()

                db.session.add(item)
                db.session.add(orders)
                db.session.commit()

                return jsonify({'message': 'dispatch delivered'}), 200

            except Exception as e:
                print(e)
                return jsonify({'message': 'Failed to deliver dispatch'}), 403
                pass

    return jsonify({'message': 'Order does not exist!'}), 409

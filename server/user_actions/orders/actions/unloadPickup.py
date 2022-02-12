from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Item, Order
from flask import jsonify


def unloadloadPickup(itemid, data, db):
    unloadunits = data['unloadunits']
    unloadnote = data['unloadnote']
    orderid = data['orderid']

#  todo check if order has all items picked.

    order = Order.query.filter_by(orderid=orderid).first()
    item = Item.query.filter_by(itemid=itemid).first()
    if order:
        if Item:
            try:
                if unloadunits:
                    item.unloadunits = unloadunits

                if unloadnote:
                    item.unloadnote = unloadnote

                order.pickupUnloaded = True
                order.orderStatus = 'Unloaded'
                db.session.add(order)
                item.pickupUnloaded = True
                item.status = 'Unloaded'
                db.session.add(item)
                db.session.commit()
                return jsonify({'message': 'item picked and unloaded'}), 200

            except Exception as e:
                print(e)
                return jsonify({'message': 'Failed to unload item'}), 403
                pass

    return jsonify({'message': 'item does not exist!'}), 409

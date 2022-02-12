from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Item, Order
from flask import jsonify
from datetime import datetime, timedelta


def unloadDispatch(itemid, data, db):
    unloadeddispatchunits = data['unloadeddispatchunits']
    unloadeddispatchnotes = data['unloadeddispatchnotes']
    orderid = data['orderid']

#  todo check if order has all items picked.
    order = Order.query.filter_by(orderid=orderid).first()
    item = Item.query.filter_by(itemid=itemid).first()

    if order:
        if Item:
            try:
                if unloadeddispatchunits:
                    item.unloadeddispatchunits = unloadeddispatchunits

                if unloadeddispatchnotes:
                    item.unloadeddispatchnotes = unloadeddispatchnotes

                order.dispatchunloaded = True
                item.dispatchunloaded = True
                item.unloadeddispatchtime = datetime.now()
                item.status = 'Dispatch unloaded'
                db.session.add(item)
                db.session.commit()
                return jsonify({'message': 'dispatch unloaded'}), 200

            except Exception as e:
                print(e)
                return jsonify({'message': 'Failed to unload item'}), 403
                pass

    return jsonify({'message': 'item does not exist!'}), 409

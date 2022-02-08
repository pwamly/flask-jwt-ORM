from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Item, Order
from flask import jsonify


def unloadloadPickup(itemid, data, db):
    units = data['units']
    unloadnote = data['unloadnote']

#  todo check if order has all items picked.

    item = Item.query.filter_by(itemid=itemid).first()
    if Item:
        try:
            if units:
                item.units = units

            if unloadnote:
                item.unloadnote = unloadnote

            item.pickupUnloaded = True
            item.status = 'picked and unloaded'
            db.session.add(item)
            db.session.commit()
            return jsonify({'message': 'item picked and unloaded'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to unload item'}), 403
            pass

    return jsonify({'message': 'item does not exist!'}), 409

from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Item, Order
from flask import jsonify


def loadPickup(itemid, data, db):
    loadunits = data['loadunits']
    loadnote = data['loadnote']

#  todo check if order has all items picked.

    item = Item.query.filter_by(itemid=itemid).first()
    if Item:
        try:
            if loadunits:
                item.units = loadunits

            if loadnote:
                item.loadnote = loadnote

            item.pickupLoaded = True
            item.status = 'Picked'
            db.session.add(item)
            db.session.commit()
            return jsonify({'message': 'item loaded'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to load item'}), 403
            pass

    return jsonify({'message': 'item does not exist!'}), 409

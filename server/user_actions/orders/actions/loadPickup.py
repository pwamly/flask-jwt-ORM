from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Item, Order
from flask import jsonify


def loadPickup(orderid, data, db):
    loadnote = data['laodnote']
    items =data['items']

#  todo check if order has all items picked.
    order = Order.query.filter_by(orderid=orderid).first()
    if order:
        for item in items:
            itemrow = Item.query.filter_by(itemid=item['itemid']).first()
            if itemrow:
                    try:
                        if loadnote:
                            itemrow.loadnote = loadnote

                        order.pickupLoaded = True
                        order.orderStatus = 'Picked'
                        db.session.add(order)
                        itemrow.pickupLoaded = True
                        itemrow.status = 'Picked'
                        db.session.add(itemrow)
                        db.session.commit()
                        print('ooooooooooooooooooooo')
                        

                    except Exception as e:
                        print(e)
                        return jsonify({'message': 'Failed to load item'}), 403
                        pass
        return jsonify({'message': 'item loaded'}), 200
    return jsonify({'message': 'order does not exist!'}), 409

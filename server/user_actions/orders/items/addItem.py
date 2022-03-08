from flask_sqlalchemy import model
from jwt import exceptions
from sqlalchemy import true
from server.models import Item, Order
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash
# from datetime import timezone


def addItem(data, db):
    orderid = data['orderid']
    items = data['items']

    # date_time_obj = datetime.datetime.strptime(pickuptime, '%b %d %Y %I:%M%p')

   #  check if order exists

    orders = Order.query.filter_by(orderid=orderid).first()
    if orders:

        for item in items:
            id = uuid.uuid4()  # todo ........... to be return to the setter and getter
            itemname = item['itemname']
            itemtype = item['itemtype']
            units = item['units']
            weight = item['weight']
            note = item['note']
            try:
                newitem = Item(
                    itemid=id,
                    itemname=itemname,
                    orderid=orderid,
                    itemtype=itemtype,
                    units=units,
                    weight=weight,
                    note=note,
                )
                orders.orderStatus = 'Not Picked'
                orders.itemsAdded=True
                db.session.add(newitem)
                db.session.add(orders)
                db.session.commit()
            except Exception as e:
                print(e)
                return jsonify({'message': 'Failed to create Item'}), 403
        return jsonify({'message': 'Item created'}), 200

    return jsonify({'message': 'Order not exist'}), 409

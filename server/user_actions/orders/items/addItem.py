from flask_sqlalchemy import model
from jwt import exceptions
from sqlalchemy import func
from server.models import Item, Order
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash
# from datetime import timezone


def addItem(data, db):
    id = uuid.uuid4()  # todo ........... to be return to the setter and getter
    orderid = data['orderid']
    itemname = data['itemname']
    itemtype = data['itemtype']
    units = data['units']
    weight = data['weight']
    note = data['note']

    # date_time_obj = datetime.datetime.strptime(pickuptime, '%b %d %Y %I:%M%p')

   #  check if order exists

    Order = Order.query.filter_by(orderid=orderid).first()
    if Order:
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

            # ...................add()
            db.session.add(newitem)
            db.session.commit()

            itemList = Item.query.filter_by(orderid=orderid).all()
            print("The Item sum returned is from the model list", itemList)

            return jsonify({'message': 'Item created'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to create Item'}), 403
            pass
    return jsonify({'message': 'Order not exist'}), 409

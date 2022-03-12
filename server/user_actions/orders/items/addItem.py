from flask_sqlalchemy import model
from jwt import exceptions
from sqlalchemy import func
from server.models import Destination, Item, Order, Price, Weight
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

            # .........Calculate billing per Item Added.........#
            newitem.cost = calculateBilling(Order.dregion, weight)

            db.session.add(newitem)
            db.session.commit()

            return jsonify({'message': 'Item created'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to create Item'}), 403
            pass
    return jsonify({'message': 'Order not exist'}), 409



def calculateBilling(location, weightItem):
    destination = Destination.query.filter_by(name=location).first()
    itemWeight = weightItem

    weightList = Weight.query().all()
    subtotal = 0.0
    additionalCost = 0.0
    for weight in weightList:
        if(itemWeight > weight.min and itemWeight <= weight.max):
            subtotal = Price.query.filter_by(
                weightid=weight.id, zoneid=destination.zoneid).first().price

    if itemWeight - 10 >= 0.5:
        additionalCost = itemWeight - 10*1500

    return subtotal + additionalCost

from flask_sqlalchemy import model
from jwt import exceptions
from sqlalchemy import func
from server.models import Destination, Item, Order, Price, Weight
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash
import os





def addItem(data, db):
    vat_percentage = os.environ.get('VAT_PERCENTAGE')

    orderid = data['orderid']
    itmeslist = data['items']

    
    def calculateBilling(location, weightItem):
                destination = Destination.query.filter_by(id=location).first()
                itemWeight = weightItem

                print("Location  ", location)
                print("Weight  ", type(itemWeight))

                weightList = Weight.query.all()

                print("WeightList Array ", weightList)

                subtotal = 0.0
                additionalCost = 0.0

                if int(itemWeight) - 10 >= 0.5:
                    additionalCost = (int(itemWeight) - 10)*1500

                    for weight in weightList:
                        if(10 > weight.min and 10 <= weight.max):
                            subtotal = Price.query.filter_by(
                                weight_d=weight.id, zoneid=destination.zoneid).first().price
                else:
                    for weight in weightList:
                        if(int(itemWeight) > weight.min and int(itemWeight) <= weight.max):
                            subtotal = Price.query.filter_by(
                                weight_d=weight.id, zoneid=destination.zoneid).first().price

                print("Subtotal ", subtotal)

                print("Additional ", additionalCost)

                return int(subtotal) + int(additionalCost)

    order = Order.query.filter_by(orderid=orderid).first()
                

    if order:
        for items in itmeslist:
            itemname = items['itemname']
            itemtype = items['itemtype']
            units = items['units']
            weight = items['weight']
            note = items['note']

            #  date_time_obj = datetime.datetime.strptime(pickuptime, '%b %d %Y %I:%M%p')

           #  check if order exists
            print('bbbbbbbbbbb', order)
            try:
                    newitem = Item(
                        itemid=uuid.uuid4(),
                        itemname=itemname,
                        orderid=orderid,
                        itemtype=itemtype,
                        units=units,
                        weight=weight,
                        note=note,
                    )

                    # .........Calculate billing per Item Added.........#
                    newitem.cost = calculateBilling(order.dregion, weight)

                    db.session.add(newitem)
                    db.session.commit()

            except Exception as e:
                print(e)
                return jsonify({'message': 'Failed to create Item'}), 403
                pass
        return jsonify({'message': 'Item created'}), 200

    return jsonify({'message': 'Order not exist'}), 409
            



          
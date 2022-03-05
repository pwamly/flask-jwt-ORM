from datetime import datetime
from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Order, Item
from flask import jsonify


def schedulePickup(orderid, data, db):
    listitems = data['items']
    driverId = data['driverId']
    vehicleId = data['vehicleId']
    pickupnote = data['pickupnote']
    orderid = data['orderid']

    #  fetch all sheduled items............................

    scheduledItems = Item.query.filter_by(
        orderid=orderid, pickupScheduled=True)
    itemslist = Item.query.filter_by(
        orderid=orderid)
    if itemslist.count() > scheduledItems.count():
        if isinstance(listitems, list):
            print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii',listitems)
            for item in listitems:
                item = Item.query.filter_by(itemid=item['itemid']).first()
                order = Order.query.filter_by(orderid=orderid).first()
                try:
                    item.driverId = driverId
                    # item.pickupScheduled = True
                    item.status = 'Pickup Scheduled'
                    order.orderStatus = 'Partial Pickup Scheduled'
                    item.scheduledPickuptime = datetime.now()
                    order.vehicleId = vehicleId
                    db.session.add(order) 
                    db.session.add(item)
                    db.session.commit()
                    # return jsonify({'message': ' Pickup Scheduled'}), 200
                except Exception as e:
                    print(e)
                    return jsonify({'message': 'Failed to schedule pickup'}), 403
    

            return jsonify({'message': 'No item i'}), 403

    order = Order.query.filter_by(orderid=orderid).first()
    print('all list.................',itemslist.count() )
    print('scheduled list gggggggggggg',scheduledItems.count())
    if order:
        print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',itemslist.count() , scheduledItems.count())
        if itemslist.count() == scheduledItems.count():
            order.pickupScheduled = True
            order.orderStatus = 'Pickup Scheduled'
        
            print(' all has been scheduled')

        try:
            if driverId:
                order.driverId = driverId

            if vehicleId:
                order.vehicleId = vehicleId

            if pickupnote:
                order.pickupnote = pickupnote

            order.scheduledPickuptime = datetime.now()

            db.session.add(order)
            db.session.commit()
            # return jsonify({'message': 'pickup scheduled'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to schedule pickup'}), 403
            pass

    return jsonify({'message': 'Order does not exist!'}), 409

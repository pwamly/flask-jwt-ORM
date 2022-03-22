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
    scheduledPickuptime=data['scheduledPickuptime']

    #  fetch all sheduled items............................
    scheduledItems = Item.query.filter_by(orderid=orderid, pickupScheduled=True)

    #  fetch all  items.........................................

    itemslist = Item.query.filter_by(orderid=orderid)

    if itemslist: # check if items are present 
        if isinstance(listitems, list):
            if itemslist.count() > scheduledItems.count(): # check if still there un scheduled items
                for item in listitems:
                    item = Item.query.filter_by(itemid=item['itemid']).first()
                    order = Order.query.filter_by(orderid=orderid).first()
                    try:
                        item.driverId = driverId
                        item.pickupScheduled = True
                        item.status = 'Pickup Scheduled'
                        order.orderStatus = 'Partial Pickup Scheduled'
                        item.scheduledPickuptime = scheduledPickuptime
                        order.vehicleId = vehicleId
                        db.session.add(order) 
                        db.session.add(item)
                        db.session.commit()
                        NewscheduledItems = Item.query.filter_by(orderid=orderid, pickupScheduled=True)
                        if itemslist.count() == NewscheduledItems.count(): # if all all items 
                                order.pickupScheduled = True
                                order.orderStatus = 'Pickup Scheduled'
                    
                                if driverId:
                                    order.driverId = driverId

                                if vehicleId:
                                    order.vehicleId = vehicleId

                                if pickupnote:
                                    order.pickupnote = pickupnote

                                order.scheduledPickuptime = datetime.now()

                                db.session.add(order)
                                db.session.commit()
                                print('...................................... all has been scheduled',itemslist.count(),scheduledItems.count())

                    except Exception as e:
                        print(e)
                        return jsonify({'message': 'Failed to schedule pickup'}), 403
            return jsonify({'message': 'pickup scheduled'}), 200
        return jsonify({'message': 'no items found'}), 403




def reschedulePickup(itemid, data, db):
    driverId = data['driverId']
    vehicleId = data['vehicleId']
    pickupnote = data['pickupnote']
    scheduledPickuptime=data['scheduledPickuptime']


    item = Item.query.filter_by(itemid=itemid).first()
    if item:
        try:
            if driverId:
                item.driverId = driverId

            if vehicleId:
                item.vehicleId = vehicleId

            if pickupnote:
                item.pickupnote = pickupnote
            
            if scheduledPickuptime:
                item.scheduledPickuptime = scheduledPickuptime


            
            db.session.add(item)
            db.session.commit()
            return jsonify({'message': 'pickup re scheduled'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to re schedule pickup'}), 403
            pass

    return jsonify({'message': 'Item does not exist!'}), 409

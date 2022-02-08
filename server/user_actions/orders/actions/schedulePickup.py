from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Order
from flask import jsonify


def schedulePickup(orderid, data, db):
    driverId = data['driverId']
    vehicleId = data['vehicleId']
    scheduledPickuptime = data['scheduledPickuptime']
    pickupnote = data['pickupnote']
    orderid = data['orderid']

    order = Order.query.filter_by(orderid=orderid).first()
    if order:
        try:
            if driverId:
                order.driverId = driverId

            if vehicleId:
                order.vehicleId = vehicleId

            if scheduledPickuptime:
                order.scheduledPickuptime = scheduledPickuptime

            if pickupnote:
                order.pickupnote = pickupnote

            order.pickupScheduled = True
            db.session.add(order)
            db.session.commit()
            return jsonify({'message': 'pickup scheduled'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to schedule pickup'}), 403
            pass

    return jsonify({'message': 'Order does not exist!'}), 409

from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Order
from flask import jsonify


def scheduleDelivery(orderid, data, db):
    deliveryscheduledtime = data['deliveryscheduledtime']
    vehicleIdfordelivered = data['vehicleIdfordelivered']
    deliveryschedulednote = data['deliveryschedulednote']
    deliveryDriverId = data['deliveryDriverId']

    order = Order.query.filter_by(orderid=orderid).first()
    if order:
        try:
            if deliveryscheduledtime:
                order.deliveryscheduledtime = deliveryscheduledtime

            if vehicleIdfordelivered:
                order.vehicleIdfordelivered = vehicleIdfordelivered

            if deliveryschedulednote:
                order.deliveryschedulednote = deliveryschedulednote

            if deliveryDriverId:
                order.deliveryDriverId = deliveryDriverId

            order.deliveryscheduled = True
            db.session.add(order)
            db.session.commit()
            return jsonify({'message': 'delivery scheduled'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to schedule pickup'}), 403
            pass

    return jsonify({'message': 'Order does not exist!'}), 409

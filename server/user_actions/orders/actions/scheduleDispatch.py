from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Order
from flask import jsonify


def scheduleDispatch(orderid, data, db):
    dispatchDriverId = data['dispatchDriverId']
    transporterid = data['transporterid']
    dispatchvehicleId = data['dispatchvehicleId']
    scheduledDispatchtime = data['scheduledDispatchtime']
    dispatchnote = data['dispatchnote']
    orderid = data['orderid']

    order = Order.query.filter_by(orderid=orderid).first()
    if order:
        try:
            if dispatchDriverId:
                order.dispatchDriverId = dispatchDriverId

            if transporterid:
                order.transporterid = transporterid

            if dispatchvehicleId:
                order.dispatchvehicleId = dispatchvehicleId

            if scheduledDispatchtime:
                order.scheduledDispatchtime = scheduledDispatchtime

            if dispatchnote:
                order.dispatchnote = dispatchnote

            order.dispatchScheduled = True
            db.session.add(order)
            db.session.commit()
            return jsonify({'message': 'dispatch scheduled'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to schedule dispatch'}), 403
            pass

    return jsonify({'message': 'Order does not exist!'}), 409


def scheduleDispatchBundle(bundleid, data, db):
    bundleid = data['bundleid']
    dispatchDriverId = data['dispatchDriverId']
    transporterid = data['transporterid']
    dispatchvehicleId = data['dispatchvehicleId']
    scheduledDispatchtime = data['scheduledDispatchtime']
    dispatchnote = data['dispatchnote']

    orders = Order.query.filter_by(bundleId=bundleid)
    if orders.count() > 0:
        for order in orders:
            try:
                order.dispatchDriverId = dispatchDriverId

                if transporterid:
                    order.transporterid = transporterid

                if dispatchvehicleId:
                    order.dispatchvehicleId = dispatchvehicleId

                if scheduledDispatchtime:
                    order.scheduledDispatchtime = scheduledDispatchtime

                if dispatchnote:
                    order.dispatchnote = dispatchnote

                order.dispatchScheduled = True
                db.session.add(order)
                db.session.commit()

            except Exception as e:
                return jsonify({'message': 'Failed to schedule dispatch'}), 403
                pass

        return jsonify({'message': 'dispatch scheduled'}), 200

    return jsonify({'message': 'Orders does not exist!'}), 409

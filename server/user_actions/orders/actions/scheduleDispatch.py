from datetime import datetime
from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Order, Bundle, Item
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


def scheduleDispatchBundle(data, db):

    bundle_id = data['bundleid_']
    dispatchDriverId = data['dispatchDriverId']
    transporterid = data['transporterid']
    dispatchvehicleId = data['dispatchvehicleId']
    scheduledDispatchtime = data['scheduledDispatchtime']
    dispatchnote = data['dispatchnote']
    nextDestination = data['nextDestination']

    bundlec = Bundle.query.filter_by(bundleid=bundle_id).first()

    if bundlec:
        bundlec.nextDestination = nextDestination
        bundlec.status = 'Scheduled'
        bundlec.dispatchScheduled = True
        bundlec.updated = datetime.utcnow()
        db.session.add(bundlec)
        db.session.commit()

    orders = Order.query.filter_by(bundleId=bundle_id)



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
                order.nextDestinationBranchId = nextDestination
                db.session.add(order)
                db.session.commit()
                return jsonify({'message': 'dispatch scheduled'}), 200
            except Exception as e:
                print(e)
                return jsonify({'message': 'Failed to schedule dispatch'}), 403
                pass

    return jsonify({'message': 'Orders does not exist!'}), 409

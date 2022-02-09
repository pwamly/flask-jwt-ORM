from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Item
from flask import jsonify
from datetime import datetime, timedelta


def deliverDispatch(itemid, data, db):
    dispatchDeliveryunits = data['dispatchDeliveryunits']
    dispatchDeliverynote = data['dispatchDeliverynote']

    item = Item.query.filter_by(itemid=itemid).first()
    if item:
        try:
            if dispatchDeliveryunits:
                item.dispatchDeliveryunits = dispatchDeliveryunits
                print('vvvvvvvvvvvv')

            if dispatchDeliverynote:
                item.dispatchDeliverynote = dispatchDeliverynote

            item.dispatchDeliveredTime = datetime.now()
            item.dispatchDelivered = True
            db.session.add(item)
            db.session.commit()
            return jsonify({'message': 'dispatch delivered'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to deliver dispatch'}), 403
            pass

    return jsonify({'message': 'Order does not exist!'}), 409

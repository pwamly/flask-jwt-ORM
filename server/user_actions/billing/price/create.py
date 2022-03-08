from datetime import datetime
from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Branch, Destination, Price, Weight, Zone
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash



def createPrice(data, db):

    priceid = uuid.uuid4()
    price = data['price']
    zoneid = data['zoneid']
    weightid = data['weightid']

    priceCheck = Price.query.filter_by(priceid=priceid).first()

    if not priceCheck:
        try:
            price = Weight(priceid=priceid, price=price, zoneid= zoneid, weightid=weightid)

            price.created = datetime.utcnow

            db.session.add(price)
            db.session.commit()

            return 'Price created'

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to create price'}), 403
            pass

    return jsonify({'message': 'price already exist!'}), 407
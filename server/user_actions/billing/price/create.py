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

    priceCheck = Price.query.filter_by(price=price).first()

    if not priceCheck:
        try:
            zone_id = Zone.query.filter_by(zoneid=zoneid).first().id
           
            weight_id = Weight.query.filter_by(weightid=weightid).first().id

         

            price = Price(priceid=priceid, price=price, zoneid= zone_id, weight_d=weight_id)

            price.created = datetime.utcnow()

            db.session.add(price)
            db.session.commit()

            return jsonify({'message': 'Price created'}), 201

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to create price'}), 403
            pass

    return jsonify({'message': 'price already exist!'}), 407
from flask_sqlalchemy import model
from jwt import exceptions
from datetime import datetime, timedelta
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash
from ....models import Price, Weight, Zone

    
def updatePrice(data, branchId, db):

    priceid = data['priceid']
    price = data['price']
    zoneid = data['zoneid']
    weightid = data['weightid']
    

    price = Price.query.filter_by(priceid=priceid).first()

    if price:
        try:
            if price:
                price.price = price

            if zoneid:
                price.zoneid = zoneid

            if weightid:
                price.weightid = weightid

            price.updated = datetime.now()

            db.session.add(price)
            db.session.commit()

            return jsonify({'message': 'Price updated'}), 200
            
        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to update price'}), 403
            pass

    return jsonify({'message': 'Price not found!'}), 409

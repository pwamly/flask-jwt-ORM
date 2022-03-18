from datetime import datetime
from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Branch, Destination, Weight, Zone
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash


def createWeight(data, db):

    weightid = uuid.uuid4()
    min = data['min']
    max = data["max"]

    weight = Weight.query.filter_by(min=min,max=max).first()

    if not weight:
        try:
            weight = Weight(weightid=weightid, min=min, max=max)

            weight.created = datetime.utcnow()
            db.session.add(weight)
            db.session.commit()

            return 'Weight created'

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to create weight'}), 403
            pass

    return jsonify({'message': 'weight already exist!'}), 407
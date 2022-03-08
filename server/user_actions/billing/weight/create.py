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
    unit = data['unit']

    zone = Zone.query.filter_by(weightid=weightid).first()

    if not zone:
        try:
            weight = Weight(weightid=weightid, unit=unit)

            weight.created = datetime.utcnow
            db.session.add(weight)
            db.session.commit()

            return 'Weight created'

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to create weight'}), 403
            pass

    return jsonify({'message': 'weight already exist!'}), 407
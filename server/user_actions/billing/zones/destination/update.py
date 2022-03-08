from flask_sqlalchemy import model
from jwt import exceptions
from datetime import datetime, timedelta
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash
from server.helper import destination_serializer
from .....models import Destination


def updateDestination(data, branchId, db):

    destinationid = data['destinationid']
    name = data['name']
    zoneid = data['destination']

    destinations = Destination.query.filter_by(destinationid=destinationid).first()

    if destinations:
        try:
            if name:
                destinations.name = name

            if zoneid:
                destinations.zoneid = zoneid

            destinations.updated = datetime.now()

            db.session.add(destinations)
            db.session.commit()

            return jsonify({'message': 'Destination updated'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to update destiation'}), 403
            pass

    return jsonify({'message': 'Destination not found!'}), 409
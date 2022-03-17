from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Branch, Destination, Zone
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash


def createDestinationOnZone(data, db):

    destinationid = uuid.uuid4()
    name=data['name']
    zone = Zone.query.filter_by(zoneid=data['zoneid']).first()
    zoneid = zone.id
    
    destionation = Destination.query.filter_by(name=name).first()
    
    if not destionation:
        try:
            destionation = Destination(destinationid=destinationid, name=name.upper() , zoneid=zoneid)
            
            db.session.add(destionation)
            db.session.commit()
            
            return 'Destination created'

        except Exception as e:
            print(e)        
            return jsonify({'message': 'Failed to create destination'}), 403
            pass

    return jsonify({'message': 'Destination already exist!'}), 407
 
 
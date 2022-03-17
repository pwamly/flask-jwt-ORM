from datetime import datetime
from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Branch, Destination, Zone
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash



def  createZone(data, db):
    zoneid = uuid.uuid4()
    name = data['name'].upper()
    description = data['description']

    zone =  Zone.query.filter_by(name=name).first()
    
    if not zone:
        try:
            zones = Zone(zoneid=zoneid, name=name, description=description)

            zones.created = datetime.utcnow()
            
            db.session.add(zones)
            db.session.commit()
            print('Zone created')
            return  jsonify({'message': 'zone created '}), 200
            

        except Exception as e:
            return jsonify({'message': 'Failed to create zone'}), 403
        
    print('Zone already exist!')
    return jsonify({'message': 'Zone already exist!'}), 407
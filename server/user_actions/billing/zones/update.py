from flask_sqlalchemy import model
from jwt import exceptions
from datetime import datetime, timedelta
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash
from ....models import Zone


    
def updateZone(data, branchId, db):

    zoneid = uuid.uuid4()
    name = data['name']
    description = data['destination']
    


    zones = Zone.query.filter_by(zoneid=zoneid).first()

    if zones:
        try:
            if name:
                zones.name= name

            if description:
                zones.description= description

            zones.updated = datetime.now()
            db.session.add(zones)
            db.session.commit()

            return jsonify({'message': 'Zone updated'}), 200
            
        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to update zone'}), 403
            pass

    return jsonify({'message': 'Zone not found!'}), 409

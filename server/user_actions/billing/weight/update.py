from flask_sqlalchemy import model
from jwt import exceptions
from datetime import datetime, timedelta
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash
from ....models import Weight, Zone


    
def updateWeight(data, branchId, db):

    weightid = data['weightid']
    unit = data['unit']
    

    weight = Weight.query.filter_by(weightid=weightid).first()

    if weight:
        try:
            if unit:
                weight.unit = unit

            weight.updated = datetime.now()

            db.session.add(weight)
            db.session.commit()

            return jsonify({'message': 'Weight updated'}), 200
            
        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to update weight'}), 403
            pass

    return jsonify({'message': 'Weight not found!'}), 409
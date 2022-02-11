from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Consignor
from flask_session import Session
from flask import jsonify
import uuid

# from datetime import timezone
import datetime
import time


def registerConsignor(data, db):
    id = uuid.uuid4()  # todo ........... to be return to the setter and getter
    fullname = data['fullname']
    customerid = data['customerid']
    email = data['email']
    phone = data['phone']
    nidano = data['nidano']

   #  check if user exists
    consignor = Consignor.query.filter_by(email=email).first()
    if not consignor:
     try:
        newcosignor = Consignor(consginerid=id,
                                fullname=fullname,
                                customerid=customerid,
                                email=email,
                                phone=phone,
                                nidano=nidano,
                                )
        db.session.add(newcosignor)
        db.session.commit()
        return jsonify({'message': 'consignor registered'}), 200

     except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to register consignor'}), 403
      pass
    return jsonify({'message': 'consignor  already exist'}), 409

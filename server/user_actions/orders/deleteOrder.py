from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Order
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash
from sqlalchemy import select, update, delete, values

userid = uuid.uuid4()  # todo ........... to be return to the setter and getter


def deleteOrder(id, db):  
 print(id)
 
 try:
   
    effected_rows = db.session.query(Order).filter(Order.orderid == id).delete()
    if effected_rows == 0:
        print('order not found')
        return {}
    else:
      db.session.commit()
      return jsonify({'message': 'order deleted'}), 200
 except Exception as e:
      print('iiiiiiiiiii',e)
      return jsonify({'message': 'Failed to delete order'}), 403
      pass
 
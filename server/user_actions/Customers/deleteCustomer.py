from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Customer
from flask_session import Session
from flask import jsonify



def deleteCustomer(id, db):  
 print(id)
 
 try:
   
    effected_rows = db.session.query(Customer).filter(Customer.customerid == id).delete()
    if effected_rows == 0:
        print('customer not found')
        return {}
    else:
      db.session.commit()
      return jsonify({'message': 'customer deleted'}), 200
 except Exception as e:
      print('iiiiiiiiiii',e)
      return jsonify({'message': 'Failed to delete customer'}), 403
      pass
 
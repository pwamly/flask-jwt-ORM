from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Customer
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash
# from datetime import timezone
import datetime

def registerCustomer(data, db): 
   
   id = uuid.uuid4()  # todo ........... to be return to the setter and getter

   #  check if user exists
   
   email = data['email']
   phone = data['phone']
   region = data['region'] 
   street = data['street']
   address = data['address']

   customer = Customer.query.filter_by(email=email).first()
   
   if not customer:
      try:
         if data['customertype'] == "individual":
            fullname = data['fname'] + " " + data['lname']

            newocustomer = Customer(customerid = id, email = email, fullname = fullname,
                                 phone = phone, region = region,
                                 address = address, street = street)
            
         elif data['customertype'] == "company" :
            fullname =  data['companyname']
            tin = data['tin']
            vrn  = data['vrn']
            
            newocustomer = Customer(customerid = id, email = email, fullname = fullname,
                                 phone = phone, region = region, tin = tin, vrn = vrn,
                                 address = address, street = street)
         
         db.session.add(newocustomer)
         db.session.commit()
         
         return jsonify({'message': 'Customer registered'}), 200
      
      except Exception as e:
         print(e)
         return jsonify({'message': 'Failed to register customer'}), 403
      pass
   return jsonify({'message': 'Customer  already exist'}), 409

 
 
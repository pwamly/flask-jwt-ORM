from flask import jsonify
import json
from ...models import Customer
from ...helper import customer_serializer

def getcustomers():
    customers = Customer.query.all()
    if customers:
       data = [*map(customer_serializer,customers)]  
       print(data)
       return {'data':data} 
    return jsonify({'message' : 'customers not found'}),403
from flask import jsonify
import json
from ...models import Order
from ...helper import order_serializer

def orders():
    orders = Order.query.all()
    if orders:
       data = [*map(order_serializer,orders)]  
       print(data)
       return {'data':data} 
    return jsonify({'message' : 'orders not found'}),403
from flask import jsonify
import json
from ...models import Order
from ...helper import order_serializer

def orders():
    order = Order.query.all()
    if order:
       data = [*map(order_serializer, order)]
       print(data)
       return {'data':data} 
    return jsonify({'message' : 'orders not found'}),403

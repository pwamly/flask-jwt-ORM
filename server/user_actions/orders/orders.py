from flask import jsonify
import json
from ...models import Order, Item
from ...helper import order_serializer

def orders():
    order = Order.query.all()
    if order:
       data = [*map(order_serializer, order)]
       print(data)
       return {'data':data} 
    return jsonify({'message' : 'orders not found'}),403


def getDeliveries():
    order = Order.query.filter_by(deliveryscheduled=True)
    if order:
        data = [*map(order_serializer, order)]
        return {'data': data}

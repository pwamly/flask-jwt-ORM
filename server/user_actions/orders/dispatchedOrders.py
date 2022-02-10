from flask import jsonify
import json
from ...models import Order
from ...helper import order_serializer


def getdispatchedOrder():
    order = Order.query.filter_by(dispatchDelivered=True)
    if order:
        data = [*map(order_serializer, order)]
        return {'data': data}

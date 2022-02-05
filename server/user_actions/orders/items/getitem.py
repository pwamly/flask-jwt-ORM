from flask import jsonify
import json
from ....models import Item
from ....helper import item_serializer


def getitems(orderid='null'):
    if orderid == 'null':
        item = Item.query.all()
        if item:
            data = [*map(item_serializer, item)]
            print('order id foundnnnnnnnnnnnnnnnnnnnnnnnnnn', type(item))
            print('order id not found')
            return {'data': data}
        return jsonify({'message': 'item not found for the order'}), 200
    item = Item.query.filter_by(orderid=orderid).first()
    if item:
        print('order id found', item)
        data = [*map(item_serializer, item)]
        return {'data': data}

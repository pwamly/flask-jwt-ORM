from flask import jsonify
import json
from ....models import Item
from ....helper import item_serializer


def getitemByorder(orderid):
    if orderid:
        item = Item.query.filter_by(orderid=orderid)
        if item:
            data = [*map(item_serializer, item)]
            return {'data': data}

from flask import jsonify
import json
from ....models import Item
from ....helper import item_serializer


def getitems(orderid='null'):
    pages_perpage = 100
    page = 1
    if orderid == 'null':
        item = Item.query.filter_by().order_by(Item.created.desc()).paginate(
            page, pages_perpage, error_out=False)
        if item:
            data = [*map(item_serializer, item)]
            print('order id not found')
            return {'data': data, "pagination": {"currentpage": item.page, "totalPages": item.pages, "totalItems": item.total, "prev_page": item.prev_num, "next_page": item.next_num, "has_next": item.has_next, "has_prev": item.has_prev}}
        return jsonify({'message': 'item not found for the order'}), 200
    item = Item.query.filter_by(orderid=orderid).first()
    if item:
        print('order id found', item)
        data = [*map(item_serializer, item)]
        return {'data': data}

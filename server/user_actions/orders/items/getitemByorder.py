from flask import jsonify
import json
from ....models import Item
from ....helper import item_serializer


def getitemByorder(orderid):

    pages_perpage = 100
    page = 1
    if orderid:
        item = Item.query.filter_by(orderid=orderid).order_by(
            Item.created.desc()).paginate(int(page), pages_perpage, error_out=False)
        if item:
            data = [*map(item_serializer, item.items)]
            return {'data': data, "pagination": {"currentpage": item.page, "totalPages": item.pages, "totalItems": item.total, "prev_page": item.prev_num, "next_page": item.next_num, "has_next": item.has_next, "has_prev": item.has_prev}}

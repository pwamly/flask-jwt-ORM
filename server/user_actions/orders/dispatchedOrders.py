from flask import jsonify
import json
from ...models import Order
from ...helper import order_serializer


def getdispatchedOrder(page, sort, q):
    pages_perpage = 5
    search = "%{}%".format(q)
    if q:
        order = Order.query.filter((Order.dispatchDelivered == True) &
                                   (Order.customername.like(search)) | (
                                       Order.consignername.like(search))
                                   ).order_by(Order.created.desc()).paginate(int(page), pages_perpage, error_out=False)
        data = [*map(order_serializer, order.items)]
        return {'data': data, "pagination": {"currentpage": order.page, "totalPages": order.pages, "totalItems": order.total, "prev_page": order.prev_num, "next_page": order.next_num, "has_next": order.has_next, "has_prev": order.has_prev}}

    order = Order.query.filter_by(dispatchDelivered=True).order_by(
        Order.created.desc()).paginate(int(page), pages_perpage, error_out=False)
    if order:
        data = [*map(order_serializer, order.items)]
        return {'data': data, "pagination": {"currentpage": order.page, "totalPages": order.pages, "totalItems": order.total, "prev_page": order.prev_num, "next_page": order.next_num, "has_next": order.has_next, "has_prev": order.has_prev}}

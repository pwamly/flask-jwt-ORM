from flask import jsonify
import json
from ...models import Order, Item
from ...helper import order_serializer


def orders():
    pages_perpage = 10
    page = 1
    order = Order.query.order_by(
        Order.created.desc()).paginate(page, pages_perpage, error_out=False)
    if order:
        data = [*map(order_serializer, order.items)]
        print(data)
        return {'data': data, "pagination": {"currentpage": order.page, "totalPages": order.pages, "totalItems": order.total, "prev_page": order.prev_num, "next_page": order.next_num, "has_next": order.has_next, "has_prev": order.has_prev}}
    return jsonify({'message': 'orders not found'}), 403


def getDeliveries():
    pages_perpage = 10
    page = 1
    order = Order.query.filter_by(
        deliveryscheduled=True).order_by(Order.created.desc()).paginate(page, pages_perpage, error_out=False)
    if order:
        data = [*map(order_serializer, order.items)]
        return {'data': data, "pagination": {"currentpage": order.page, "totalPages": order.pages, "totalItems": order.total, "prev_page": order.prev_num, "next_page": order.next_num, "has_next": order.has_next, "has_prev": order.has_prev}}


def orders():
    pages_perpage = 10
    page = 1
    order = Order.query.order_by(
        Order.created.desc()).paginate(page, pages_perpage, error_out=False)
    if order:
        data = [*map(order_serializer, order.items)]
        print(data)
        return {'data': data, "pagination": {"currentpage": order.page, "totalPages": order.pages, "totalItems": order.total, "prev_page": order.prev_num, "next_page": order.next_num, "has_next": order.has_next, "has_prev": order.has_prev}}
    return jsonify({'message': 'orders not found'}), 403

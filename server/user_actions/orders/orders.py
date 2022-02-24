from flask import jsonify
from jinja2 import Undefined
from sqlalchemy import and_, or_, not_
import json
from ...models import Order, Item
from ...helper import order_serializer


def orders(page, sort, q, date, status):
    search = "%{}%".format(q)
    pages_perpage = 5
    if q:
        order = Order.query.filter(
            (Order.customername.like(search)) | (
                Order.consignername.like(search))
        ).order_by(Order.created.desc()).paginate(page, pages_perpage, error_out=False)
        data = [*map(order_serializer, order.items)]
        return {'data': data, "pagination": {"currentpage": order.page, "totalPages": order.pages, "totalItems": order.total, "prev_page": order.prev_num, "next_page": order.next_num, "has_next": order.has_next, "has_prev": order.has_prev}}


    order = Order.query.order_by(
        Order.created.desc()).paginate(page, pages_perpage, error_out=False)
    if order:
        data = [*map(order_serializer, order.items)]
        print(data)
        return {'data': data, "pagination": {"currentpage": order.page, "totalPages": order.pages, "totalItems": order.total, "prev_page": order.prev_num, "next_page": order.next_num, "has_next": order.has_next, "has_prev": order.has_prev}}
    return jsonify({'message': 'orders not found'}), 403


def getDeliveries(page, sort, q):
    search = "%{}%".format(q)
    pages_perpage = 5
    if q:
        order = Order.query.filter((Order.deliveryscheduled == True) & (Order.customername.like(search)) | (
            Order.consignername.like(search))
        ).order_by(Order.created.desc()).paginate(page, pages_perpage, error_out=False)
        data = [*map(order_serializer, order.items)]
        return {'data': data, "pagination": {"currentpage": order.page, "totalPages": order.pages, "totalItems": order.total, "prev_page": order.prev_num, "next_page": order.next_num, "has_next": order.has_next, "has_prev": order.has_prev}}

    order = Order.query.filter_by(deliveryscheduled=True).order_by(
        Order.created.desc()).paginate(page, pages_perpage, error_out=False)
    if order:
        data = [*map(order_serializer, order.items)]
        return {'data': data, "pagination": {"currentpage": order.page, "totalPages": order.pages, "totalItems": order.total, "prev_page": order.prev_num, "next_page": order.next_num, "has_next": order.has_next, "has_prev": order.has_prev}}


# from datetime import datetime

# from_date = datetime(year=datetime.now().year, month=datetime.now().month, day=1)

# current_month_expenses = Expense.filter_by(user_id=current_user.id).filter(Expense.date >= from_date).filter(Expense.date <= datetime.now()).all()

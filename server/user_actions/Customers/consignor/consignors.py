from flask import jsonify
import json
from ....models import Consignor
from ....helper import consignor_serializer


def getconsignorsByCustomer(customerid):
    pages_perpage = 100
    page = 1
    consignors = Consignor.query.filter_by(customerid=customerid).order_by(
        Consignor.created.desc()).paginate(int(page), pages_perpage, error_out=False)
    if consignors:
       data = [*map(consignor_serializer, consignors.items)]
       print(data)
       return {'data': data, "pagination": {"currentpage": consignors.page, "totalPages": consignors.pages, "totalItems": consignors.total, "prev_page": consignors.prev_num, "next_page": consignors.next_num, "has_next": consignors.has_next, "has_prev": consignors.has_prev}}
    return jsonify({'message': 'consignor  not found'}), 403


def getconsignors():
    pages_perpage = 100
    page = 1
    consignors = Consignor.query.filter_by().order_by(
        Consignor.created.desc()).paginate(int(page), pages_perpage, error_out=False)
    if consignors:
       data = [*map(consignor_serializer, consignors.items)]
       print(data)
       return {'data': data, "pagination": {"currentpage": consignors.page, "totalPages": consignors.pages, "totalItems": consignors.total, "prev_page": consignors.prev_num, "next_page": consignors.next_num, "has_next": consignors.has_next, "has_prev": consignors.has_prev}}
    return jsonify({'message': 'consignor  not found'}), 403

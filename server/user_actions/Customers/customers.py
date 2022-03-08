from flask import jsonify
import json
from ...models import Customer
from ...helper import customer_serializer

def getcustomers():
    pages_perpage = 10
    page = 1
    customers = Customer.query.filter_by().order_by(
        Customer.created.desc()).paginate(page, pages_perpage, error_out=False)
    pages_perpage = 100
    page = 1
    if customers:
       data = [*map(customer_serializer, customers.items)]
       print(data)
       return {'data': data, "pagination": {"currentpage": customers.page, "totalPages": customers.pages, "totalItems": customers.total, "prev_page": customers.prev_num, "next_page": customers.next_num, "has_next": customers.has_next, "has_prev": customers.has_prev}}
    return jsonify({'message' : 'customers not found'}),403

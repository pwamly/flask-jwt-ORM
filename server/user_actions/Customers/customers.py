from flask import jsonify
import json
from ...models import Customer
from ...helper import customer_serializer


def getcustomers(page, sort, q):
    pages_perpage = 5
    search = "%{}%".format(q)
    if q:
        customer = Customer.query.filter(
            (Customer.fname.like(search)) | (
                Customer.email.like(search)) | (
                Customer.phone.like(search))
        ).order_by(Customer.created.desc()).paginate(page, pages_perpage, error_out=False)
        data = [*map(customer_serializer, customer.items)]
        return {'data': data, "pagination": {"currentpage": customer.page, "totalPages": customer.pages, "totalItems": customer.total, "prev_page": customer.prev_num, "next_page": customer.next_num, "has_next": customer.has_next, "has_prev": customer.has_prev}}

    customers = Customer.query.filter_by().order_by(
        Customer.created.desc()).paginate(page, pages_perpage, error_out=False)
    pages_perpage = 5
    if customers:
       data = [*map(customer_serializer, customers.items)]
       print(data)
       return {'data': data, "pagination": {"currentpage": customers.page, "totalPages": customers.pages, "totalItems": customers.total, "prev_page": customers.prev_num, "next_page": customers.next_num, "has_next": customers.has_next, "has_prev": customers.has_prev}}
    return jsonify({'message' : 'customers not found'}),403

def getCustomerById(customerId):
     customer = Customer.query.filter_by(customerid=customerId).order_by(
            Customer.created.desc())
     if customer:
            data = [*map(customer_serializer, customer)]
            return {'data': data}

from flask import jsonify
import json
from ....models import Price, Weight 
from ....helper import price_serializer



def getAllPrice():

    pages_perpage = 50
    page = 1

    price = Price.query.filter_by().order_by(Price.created.desc()).paginate(page, pages_perpage, error_out=False)
    pages_perpage = 100
    page = 1

    if price:
        data = [*map(price_serializer, price.items)]
        print(data)
        
        return {'data': data, "pagination": {"currentpage": price.page, "totalPages": price.pages, "totalItems": price.total, "prev_page": price.prev_num, "next_page": price.next_num, "has_next": price.has_next, "has_prev": price.has_prev}}
        
    return jsonify({'message' : 'price not found'}),403
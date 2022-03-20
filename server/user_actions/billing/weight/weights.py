from flask import jsonify
import json
from ....models import Weight 
from ....helper import weight_serializer



def getAllWeight():

    pages_perpage = 30
    page = 1

    weight = Weight.query.filter_by().order_by(Weight.created.desc()).paginate(int(page), pages_perpage, error_out=False)
    pages_perpage = 100
    page = 1

    if weight:
        data = [*map(weight_serializer, weight.items)]
        print(data)
        
        return {'data': data, "pagination": {"currentpage": weight.page, "totalPages": weight.pages, "totalItems": weight.total, "prev_page": weight.prev_num, "next_page": weight.next_num, "has_next": weight.has_next, "has_prev": weight.has_prev}}
        
    return jsonify({'message' : 'weight not found'}),403
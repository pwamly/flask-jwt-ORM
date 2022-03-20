from flask import jsonify
import json
from .....models import Destination 
from .....helper import destination_serializer

def getAllDestinations():
    
    pages_perpage = 10
    page = 1
    
    destinations = Destination.query.filter_by().order_by(Destination.created.desc()).paginate(int(page), pages_perpage, error_out=False)
    pages_perpage = 100
    page = 1
    
    if destinations:
        data = [*map(destination_serializer, destinations.items)]
        print(data)
        return {'data': data, "pagination": {"currentpage": destinations.page, "totalPages": destinations.pages, "totalItems": destinations.total, "prev_page": destinations.prev_num, "next_page": destinations.next_num, "has_next": destinations.has_next, "has_prev": destinations.has_prev}}
        
    return jsonify({'message' : 'customers not found'}),403
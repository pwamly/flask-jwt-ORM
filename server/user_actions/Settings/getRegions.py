from flask import jsonify
import json
from ...helper import regions_serializer
from ...models import Regions


def getregions():
    pages_perpage = 40
    page = 1
    region = Regions.query.filter_by().order_by(
        Regions.created.desc()).paginate(page, pages_perpage, error_out=False)
    if region:
       data = [*map(regions_serializer, region.items)]
       print(data)
       return {'data': data, "pagination": {"currentpage": region.page, "totalPages": region.pages, "totaltransporters": region.total, "prev_page": region.prev_num, "next_page": region.next_num, "has_next": region.has_next, "has_prev": region.has_prev}}
    return jsonify({'message': 'Transporters not found'}), 403

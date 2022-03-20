
from flask import jsonify
import json
from ...helper import vehicle_serializer
from ...models import Vehicle


def getvehicle(page, sort, q):
    pages_perpage = 5

    vehicle = Vehicle.query.filter_by().order_by(
        Vehicle.created.desc()).paginate(int(page), pages_perpage, error_out=False)
    if vehicle:
       data = [*map(vehicle_serializer, vehicle.items)]
       print(data)
       return {'data': data, "pagination": {"currentpage": vehicle.page, "totalPages": vehicle.pages, "totalvehicles": vehicle.total, "prev_page": vehicle.prev_num, "next_page": vehicle.next_num, "has_next": vehicle.has_next, "has_prev": vehicle.has_prev}}
    return jsonify({'message' : 'Branch not found'}),403


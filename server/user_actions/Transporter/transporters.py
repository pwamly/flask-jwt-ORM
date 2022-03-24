from flask import jsonify
import json
from ...helper import transporter_serializer
from ...models import Transporter


def gettransporters(page, sort, q):
    pages_perpage = 5
    transporter = Transporter.query.filter_by().order_by(
        Transporter.created.desc()).paginate(int(page), pages_perpage, error_out=False)
    if transporter:
        data = [*map(transporter_serializer, transporter.items)]
        print(data)
        return {'data': data, "pagination": {"currentpage": transporter.page, "totalPages": transporter.pages, "totaltransporters": transporter.total, "prev_page": transporter.prev_num, "next_page": transporter.next_num, "has_next": transporter.has_next, "has_prev": transporter.has_prev}}
    return jsonify({'message': 'Transporters not found'}), 403
from flask import jsonify
import json
from ....models import Users, Zone
from ....helper import zones_serializer


def getZones():

    pages_perpage = 10
    page = 1

    zones = Zone.query.filter_by().order_by(
        Zone.created.desc()).paginate(page, pages_perpage, error_out=False)

    pages_perpage = 100
    page = 1
    if zones:
        data = [*map(zones_serializer, zones.items)]
        print(data)
        return {'data': data, "pagination": {"currentpage": zones.page, "totalPages": zones.pages, "totalItems": zones.total, "prev_page": zones.prev_num, "next_page": zones.next_num, "has_next": zones.has_next, "has_prev": zones.has_prev}}

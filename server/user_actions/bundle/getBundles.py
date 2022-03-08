from flask import jsonify
import json
from ...models import Bundle
from ...helper import bundle_serializer


def getbundles():
    pages_perpage = 5
    page = 1
    bundle = Bundle.query.filter_by().order_by(
        Bundle.created.desc()).paginate(page, pages_perpage, error_out=False)
    if bundle:
        data = [*map(bundle_serializer, bundle.items)]
        print(data)
        return {'data': data, "pagination": {"currentpage": bundle.page, "totalPages": bundle.pages, "totalbranchs": bundle.total, "prev_page": bundle.prev_num, "next_page": bundle.next_num, "has_next": bundle.has_next, "has_prev": bundle.has_prev}}
    return jsonify({'message': 'bundles not found'}), 403

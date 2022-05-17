from flask import jsonify
import json
from ...models import Branch
from ...helper import branch_serializer


def branches(page, sort, q):
    pages_perpage = 5
    branch = Branch.query.filter_by().order_by(
        Branch.created.desc()).paginate(int(page), pages_perpage, error_out=False)
    if branch:
        data = [*map(branch_serializer, branch.items)]
        print(data)
        return {'data': data, "pagination": {"currentpage": branch.page, "totalPages": branch.pages, "totalbranchs": branch.total, "prev_page": branch.prev_num, "next_page": branch.next_num, "has_next": branch.has_next, "has_prev": branch.has_prev}}
    return jsonify({'message': 'Branch not found'}), 403

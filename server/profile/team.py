from flask import jsonify
import json
from ..models import Users

from ..helper import users_serializer


def users(page, sort, q):
    pages_perpage = 5
    profile = Users.query.filter_by().order_by(
        Users.created.desc()).paginate(int(page), pages_perpage, error_out=False)
    if profile:
       data = [*map(users_serializer, profile.items)]
       return {'data': data, "pagination": {"currentpage": profile.page, "totalPages": profile.pages, "totalusers": profile.total, "prev_page": profile.prev_num, "next_page": profile.next_num, "has_next": profile.has_next, "has_prev": profile.has_prev}}
    return jsonify({'message' : 'Users not found'}),403

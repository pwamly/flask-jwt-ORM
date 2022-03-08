from flask import jsonify
import json

from ..helper import profile_serializer,users_serializer
def users(Users):
    pages_perpage = 100
    page = 1
    profile = Users.query.filter_by().order_by(
        Users.created.desc()).paginate(page, pages_perpage, error_out=False)
    if profile:
       data = [*map(users_serializer, profile.items)]
       return {'data': data, "pagination": {"currentpage": profile.page, "totalPages": profile.pages, "totalusers": profile.total, "prev_page": profile.prev_num, "next_page": profile.next_num, "has_next": profile.has_next, "has_prev": profile.has_prev}}
    return jsonify({'message' : 'Users not found'}),403

from flask import jsonify
from ..models import Users
from ..helper import users_serializer

# ..... TODO capitalize param...................


def getUserbyrole(role):
    pages_perpage = 100
    page = 1
    if role:
        user = Users.query.filter_by(role=role).order_by(
            Users.created.desc()).paginate(int(page), pages_perpage, error_out=False)
        if user:
            data = [*map(users_serializer, user.items)]
            return {'data': data, "pagination": {"currentpage": user.page, "totalPages": user.pages, "totalusers": user.total, "prev_page": user.prev_num, "next_page": user.next_num, "has_next": user.has_next, "has_prev": user.has_prev}}
    return jsonify({'message': 'no role passed'}), 403

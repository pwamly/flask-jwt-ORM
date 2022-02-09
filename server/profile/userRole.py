from flask import jsonify
from ..models import Users
from ..helper import users_serializer

# ..... TODO capitalize param...................


def getUserbyrole(role):
    if role:
        user = Users.query.filter_by(role=role)
        if user:
            data = [*map(users_serializer, user)]
            return {'data': data}
    return jsonify({'message': 'no role passed'}), 403

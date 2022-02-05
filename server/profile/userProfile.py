from flask import jsonify
from ..helper import profile_serializer


def profile(userId, Users):
    profile = Users.query.filter_by(userid=userId).first()

    if profile:
        data = {'username': profile.fname,
                'phone': profile.phone, 'email': profile.email,'branchId': profile.branchId}
        return jsonify({'data': data}), 200
    return jsonify({'message': 'User not found'}), 403

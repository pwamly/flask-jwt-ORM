from flask import jsonify

def profile(userId,Users):
    profile = Users.query.filter_by(userid=userId).first()
    if profile:
       name = profile['username']
       return jsonify({'data' : 'profile'}),200
    print(profile)
    return jsonify({'message' : 'User not found'}),403
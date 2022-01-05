from flask import jsonify
import json

from ..helper import profile_serializer,users_serializer
def users(Users):
    profile = Users.query.all()
    if profile:
       data = [*map(users_serializer,profile)]  
       return {'data':data} 
    return jsonify({'message' : 'Users not found'}),403
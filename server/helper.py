from functools import wraps
from flask import request,jsonify
import jwt
import os


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message':'Token is missing'}),403
        
        parts = token.split()
        if parts[0].lower() != "bearer":
                return jsonify({"message":"Authorization header must start with Bearer"}, 401)
        elif len(parts) == 1:
           return  jsonify({"message": "Token not found"}, 401)
        elif len(parts) > 2:
            return  jsonify({"message":"Invalid header"}, 401)
        token = parts[1]  
        try:

          data =jwt.decode(token,os.environ.get('SECRET_KEY'))
          
        except jwt.ExpiredSignatureError as e:
                     return jsonify({'message': 'Token has expired'})
        return f(*args, **kwargs)
    return decorated   
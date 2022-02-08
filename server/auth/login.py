import jwt
from datetime import datetime,timedelta
from flask import jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token,create_refresh_token
import os
import json

def login(request,Users):
    # check if user exist
     # getting posted data and check for auth
    data=json.loads(request.data)
    if data:
       username = data['username']
       password = data['password']
       print(username,password) 
       user = Users.query.filter_by(email=username).first()
       if not user or not check_password_hash(user.password,password):
           return jsonify({'message' : 'wrong credentials'}),401
    #    refresh = create_refresh_token(identity=user.userid)
    #    access = create_access_token(identity=user.userid)
       token = jwt.encode({'id': user.userid, 'exp': datetime.utcnow() + timedelta(seconds=int(os.environ.get(
           'DURATION'), base=0)), 'role': user.role, 'branchId': user.branchId}, os.environ.get('SECRET_KEY'))
       return jsonify({'token': token})
   
    return jsonify({'message' : 'authorization is missing'}),403
     

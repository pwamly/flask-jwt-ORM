import jwt
from datetime import datetime,timedelta
from flask import jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token,create_refresh_token
import os

def login(request,Users):
    # check if user exist
     # getting posted data and check for auth
    auth = request.authorization
    if auth and auth.password == '123':
       print(auth)
       user= Users.query.filter_by(name=auth.username).first()
       error_messsage=''
       if not user or not check_password_hash(user.password,auth.password):
           error_messsage='Invalid Credentials'
           return error_messsage
    #    refresh = create_refresh_token(identity=user.userid)
    #    access = create_access_token(identity=user.userid)
       token = jwt.encode({'ID' : user.userid,'exp': datetime.utcnow() + timedelta(seconds=int(os.environ.get('DURATION'),base=0)) },os.environ.get('SECRET_KEY'))
       return jsonify({'token':token})
   
    return jsonify({'message' : 'authorization is missing'})
     

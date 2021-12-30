import jwt
from datetime import datetime,timedelta
from flask import jsonify
from werkzeug.security import check_password_hash
import os

def logout(request,Users):
    
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
      
       token = jwt.encode({'user' : auth.username,'exp': datetime.utcnow() + timedelta(seconds=30) },os.environ.get('SECRET_KEY'))
       
       return jsonify({'token':token.decode('UTF-8')})
   
    return jsonify({'message' : 'authorization is missing'})
     

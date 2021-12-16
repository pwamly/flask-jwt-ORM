from flask_sqlalchemy import model
from server.models import  Users


def register(data,db):   
 username = data['username']
 email = data['email']
 phone = data['phone']
 password = data['password']
 # check if user exists
 user= Users.query.filter_by(name=username).first()
 error_messsage=''
 if not user:
  user = Users(name=username,email=email,phone=phone,password_=password,isadmin=True)
  db.session.add(user)
  db.session.commit()
  print('registered')    
  return 'registered'
 return 'user exisists'

 
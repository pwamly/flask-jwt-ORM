from flask import Blueprint,request,jsonify
from .extensions import db
from .models import  Users
from .auth.login import login
from .auth.register import register
from .profile.team import users
from .helper import token_required
from .profile.userProfile import profile
from flask_cors import CORS,cross_origin

main=Blueprint('main',__name__)
CORS(main, support_credentials=True)
#---------- Authentication routes ----------

@main.route('/register',methods=['POST'])
def Userreg():
    data=request.json
    return register(data,db)

@main.route('/login', methods=['POST','OPTIONS'])
@cross_origin(supports_credentials=True)
def Userlogin():
    if(request.method=='POST'):
         return login(request, Users)
    else:
       pass

@main.route('/resetPassword')
def resetPassword():
    return 'reset codes sent'

#---------- Admin actions ----------

@main.route('/create-user')
def createUser():
    return 'user created'

@main.route('/edit-user')
def editUser():
    return 'user updated'

@main.route('/delete-user')
def deleteUser():
    return 'user deleted'

@main.route('/revoke-token')
def revokeToken():
    return 'user deleted'


@main.route('/api/users', methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def users_():
    if(request.method == 'GET'):
        return users(Users)
    else:
       pass


#---------- User actions ----------

@main.route('/api/profile/<userId>',methods=['GET','OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required
def f_profile(userId):
  if(request.method=='GET'):
    return profile(userId,Users)
  else:
       pass

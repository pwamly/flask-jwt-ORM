from flask import Blueprint,request,jsonify
from .extensions import db
from .models import  Users
from .auth.login import login
from .auth.register import register

main=Blueprint('main',__name__)
 
#---------- Authentication routes ----------

@main.route('/register',methods=['POST'])
def Userreg():
    data=request.json
    return register(data,db)

@main.route('/login', methods=['POST'])
def Userlogin():
    return login()

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

#---------- User actions ----------




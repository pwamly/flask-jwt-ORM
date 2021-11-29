from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

api=Blueprint('api',__name__,url_prefix='/api/auth')

@api.route('/register', methods=['POST'])

def  register():
    return {'succesful':True, 'message':'registered'}


@api.route('/login', methods=['POST'])

def  login():
    return {'succesful':True, 'message':'logged in'}


@api.route('/forgot-password', methods=['POST'])

def  forgot_password():
    return {'succesful':True, 'message':'code sent'}


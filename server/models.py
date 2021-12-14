from .extensions import db
from datetime import datetime,timedelta
from werkzeug.security import generate_password_hash

class Users(db.Model):
    
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(120),nullable=False,unique=True)
    phone = db.Column(db.String(120),nullable=False,unique=True)
    password=db.Column(db.String(200),nullable=False,unique=True)
    isadmin=db.Column(db.Boolean,nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)


@property
def password_(self):
    raise ArithmeticError('can not use unhashed password')

@password_.setter
def password_(self,password):
    print('running setter...........................................................')
    self.password = generate_password_hash(password_)
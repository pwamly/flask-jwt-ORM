from server.extension import db
from datetime import datetime,timedelta


class User(db.Model):
    
    __tablename__ = 'Users__66'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(120),nullable=False,unique=True)
    age = db.Column(db.Integer(),nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

# create string 

    def __repr__(self):
        return f"{self.name}:{self.age}"

from flask import Flask,render_template,request,jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timedelta
import jwt
 
app = Flask(__name__)

# add db
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin2:admin123@localhost:5432/flask_demo"
app.config['SECRET_KEY'] = "demo project"

# initialize db
db = SQLAlchemy(app)

# create model 
class User(db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(120),nullable=False,unique=True)
    age = db.Column(db.Integer(),nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

# create string 

    def __repr__(self):
        return f"{self.name}:{self.age}"


 
@app.route('/login', methods = ['POST'])
def login():  
    # getting posted data and check for auth
    auth = request.authorization
    if auth and auth.password == '123':
       token = jwt.encode({'user' : auth.username,'exp': datetime.utcnow() + timedelta(minutes=30) },app.config['SECRET_KEY'])
       print(token)

       return jsonify({'token': token})
 
    return make_response('could not  verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
      
 
if __name__ == '__main__':
    app.run(debug=True)
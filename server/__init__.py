from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
app = Flask(__name__)

# add db
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin2:admin123@localhost:5432/flask_demo"
app.config['SECRET_KEY'] = "demo project"

# initialize db
db = SQLAlchemy(app)

# create model 
class UserT(db.Model):
    __tablename__ = 'Demo2__'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(120),nullable=False,unique=True)
    age = db.Column(db.Integer(),nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

# create string 

    def __repr__(self):
        return f"{self.name}:{self.age}"

@app.route('/form')
def form():
    return render_template('form.html')
 
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    return "Login via the login Form"
     
 
if __name__ == '__main__':
    app.run(debug=True)
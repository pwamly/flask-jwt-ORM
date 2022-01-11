from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Users
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash
from sqlalchemy import select, update, delete, values

userid = uuid.uuid4()  # todo ........... to be return to the setter and getter


def removeUser(id, db):  
#  userid = data['firstname']
 print(id)
 
 try:
    # user = Users.query.filter(Users.userid == id).delete()
    # db.session.add(user)
    # db.session.commit()
    # return jsonify({'message': 'User deleted'}), 200
    # user = delete(Users).where(Users.userid == '292929')
    # deluser = db.session.execute(user)
    # print('dddddddddddddd', deluser)
    # db.session.commit()
    # return {}
    effected_rows = db.session.query(Users).filter(Users.userid == id).delete()
    if effected_rows == 0:
        print('user not found')
        return {}
    else:
      db.session.commit()
      return jsonify({'message': 'User deleted'}), 200
 except Exception as e:
      print('iiiiiiiiiii',e)
      return jsonify({'message': 'Failed to delete user'}), 403
      pass
 
 
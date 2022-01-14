from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Transporter
from flask_session import Session
from flask import jsonify


def deleteTransporter(id, db):
 try:

    effected_rows = db.session.query(Transporter).filter(
        Transporter.transporterid == id).delete()
    if effected_rows == 0:
        print('Transpoorter not found')
        return {}
    else:
      db.session.commit()
      return jsonify({'message': 'Transporter deleted'}), 200
 except Exception as e:
     print('s', e)
     return jsonify({'message': 'Failed to delete transporter'}), 403
     pass

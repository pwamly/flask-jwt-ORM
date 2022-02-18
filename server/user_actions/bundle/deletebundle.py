from server.models import Bundle
from flask import jsonify


def deleteCustomer(id, db):
 print(id)

 try:

    delete_bundle = db.session.query(Bundle).filter(
        Bundle.bundleid == id).delete()
    if delete_bundle == 0:
        print('bundle not found')
        return {}
    else:
      db.session.commit()
      return jsonify({'message': 'bundle deleted'}), 200
 except Exception as e:
     print('iiiiiiiiiii', e)
     return jsonify({'message': 'Failed to delete bundle'}), 403
     pass

from flask import jsonify
import json
from ...helper import transporter_serializer
from ...models import Transporter


def gettransporters():
    transporter = Transporter.query.all()
    if transporter:
       data = [*map(transporter_serializer,transporter)]  
       print(data)
       return {'data':data} 
    return jsonify({'message' : 'Transporters not found'}),403
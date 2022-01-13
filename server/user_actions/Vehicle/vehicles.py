from flask import jsonify
import json
from ...helper import vehicle_serializer
from ...models import Vehicle


def getvehicle():
    vehicle = Vehicle.query.all()
    if vehicle:
       data = [*map(vehicle_serializer,vehicle)]  
       print(data)
       return {'data':data} 
    return jsonify({'message' : 'Branch not found'}),403
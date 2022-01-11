from flask import jsonify
import json
from ...helper import profile_serializer,users_serializer,branch_serializer

def branches(Branch):
    branch = Branch.query.all()
    if branch:
       data = [*map(branch_serializer,branch)]  
       print(data)
       return {'data':data} 
    return jsonify({'message' : 'Branch not found'}),403
from functools import wraps
from flask import request,jsonify
import jwt
import os

# .............. for any user ..........
def token_required_user(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message':'Token is missing'}),403
        
        parts = token.split()
        if parts[0].lower() != "bearer":
                return jsonify({"message":"Authorization header must start with Bearer"}, 401)
        elif len(parts) == 1:
           return  jsonify({"message": "Token not found"}, 401)
        elif len(parts) > 2:
            return  jsonify({"message":"Invalid header"}, 401)
        token = parts[1]  
        try:

          data =jwt.decode(token, os.environ.get('SECRET_KEY'),algorithms="HS256")
          
        except jwt.ExpiredSignatureError as e:
                     return jsonify({'message': 'Token has expired'})
        return f(*args, **kwargs)
    return decorated   




# ................... for admin actions .....add()

def token_required_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message':'Token is missing'}),403
        
        parts = token.split()
        if parts[0].lower() != "bearer":
                return jsonify({"message":"Authorization header must start with Bearer"}, 401)
        elif len(parts) == 1:
           return  jsonify({"message": "Token not found"}, 401)
        elif len(parts) > 2:
            return  jsonify({"message":"Invalid header"}, 401)
        token = parts[1]  
        try:

          data =jwt.decode(token, os.environ.get('SECRET_KEY'),algorithms="HS256")
          
        except jwt.ExpiredSignatureError as e:
                     return jsonify({'message': 'Token has expired'})
        return f(*args, **kwargs)
    return decorated   



def profile_serializer(data):
    return {
        'username': data.name,
        'email': data.email,
        'phone': data.phone
    }


def users_serializer(data):

    return {
        "userid": data.userid,
        "fname": data.fname,
        "lname": data.lname,
        "branch": data.branch,
        "email": data.email,
        "phone": data.phone,
        "role": data.role,
        "created": data.created.isoformat(),
        "updated": data.updated.isoformat(),
    }
    
    
def branch_serializer(data):
    
    return {
        "branchId": data.branchId,
        "branchname": data.branchname,
        "region": data.region,
        "district": data.district,
        "branchaddress": data.branchaddress,
        "created": data.created,
        "updated": data.updated,
    }



def order_serializer(data):
    
    return {
        "orderid":data.orderid,
         "customerid": data.customerid,
         "customername": data.customername,
         "customernotes": data.customernotes,
         "consignername": data.consignername,
         "consignerid": data.consignerid,
         "cnotes": data.cnotes,
         "pregion": data.pregion,
         "pdistrict": data.pdistrict,
        "pstreet": data.pstreet,
        "pnotes": data.pnotes,
        "dregion": data.dregion,
        "ddistrict": data.ddistrict,
        "dstreet": data.dstreet,
        "dnotes": data.dnotes,
        "consigneename": data.consigneename,
        "cnenotes": data.cnenotes,
        "pickuptime": data.pickuptime,
        "expdlrtime": data.expdlrtime
                 
}
    



def customer_serializer(data):
    
    return {
        "customerid":data.customerid,
         "fname": data.fname,
         "lname": data.lname,
         "username":data.fname+' '+' '+data.lname,
         "email": data.email,
         "phone": data.phone,
         "district": data.district,
         "region":data.region,
         "street": data.street,
         "address": data.address,
         "generaladdress":data.region+', '+data.district+', '+data.street+' ,'+data.address,
         "created": data.created
}



def vehicle_serializer(data):
    
    return {
        "vehicleid":data.vehicleid,
         "name": data.name,
         "plateno": data.plateno,
         "model":data.model,
         "loadcapacity": data.loadcapacity,
         "status": data.status,
         "routestatus": data.routestatus,
         "created": data.created
}
# {
#     customerId: 'bdar-2',
#     customername: 'CRD MBEZI',
#     customeraddress: 'P.O.BOX 16,UBUNGO,MAGUFULI BUS STOP STREET,MOBILE:123444',
#   },
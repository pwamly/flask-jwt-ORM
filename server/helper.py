from functools import wraps
from flask import request, jsonify,g
import jwt
import os

# .............. for any user ..........


def token_required_user(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        parts = token.split()
        if parts[0].lower() != "bearer":
            return jsonify({"message": "Authorization header must start with Bearer"}, 401)
        elif len(parts) == 1:
            return jsonify({"message": "Token not found"}, 401)
        elif len(parts) > 2:
            return jsonify({"message": "Invalid header"}, 401)
        token = parts[1]
        try:

            data = jwt.decode(token, os.environ.get(
                'SECRET_KEY'), algorithms="HS256")

            # add role and branchId of the user to all transactions

            g.userRole=data['role']
            g.userBranchId=data['branchId']

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
            return jsonify({'message': 'Token is missing'}), 403

        parts = token.split()
        if parts[0].lower() != "bearer":
            return jsonify({"message": "Authorization header must start with Bearer"}, 401)
        elif len(parts) == 1:
            return jsonify({"message": "Token not found"}, 401)
        elif len(parts) > 2:
            return jsonify({"message": "Invalid header"}, 401)
        token = parts[1]
        try:

            data = jwt.decode(token, os.environ.get(
                'SECRET_KEY'), algorithms="HS256")
        #   add role,branchId to request
        #   request.data={**request.data,'role':}
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
        "branchId": data.branchId,
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
        "orderid": data.orderid,
        "branchid": data.branchid,
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
        "expdlrtime": data.expdlrtime,
        "pickupScheduled": data.pickupScheduled,
        "driverId": data.driverId,
        "vehicleId": data.vehicleId,
        "scheduledPickuptime": data.scheduledPickuptime,
        "pickupnote": data.pickupnote

    }


def customer_serializer(data):

    return {
        "customerid": data.customerid,
        "fname": data.fname,
        "lname": data.lname,
        "username": data.fname+' '+' '+data.lname,
        "email": data.email,
        "phone": data.phone,
        "district": data.district,
        "region": data.region,
        "street": data.street,
        "address": data.address,
        "generaladdress": data.region+', '+data.district+', '+data.street+' ,'+data.address,
        "created": data.created
    }


def vehicle_serializer(data):

    return {
        "vehicleid": data.vehicleid,
        "name": data.name,
        "plateno": data.plateno,
        "model": data.model,
        "loadcapacity": data.loadcapacity,
        "status": data.status,
        "routestatus": data.routestatus,
        "created": data.created
    }


def transporter_serializer(data):

    return {
        "transporterid": data.transporterid,
        "name": data.name,
        "email": data.email,
        "phone": data.phone,
        "address": data.address,
        "route": data.route,
        "vehicledetails": data.vehicledetails,
        "created": data.created
    }


def item_serializer(data):
    return {
        "itemid": data.itemid,
        "itemname": data.itemname,
        "orderid": data.orderid,
        "itemtype": data.itemtype,
        "units": data.units,
        "weight": data.weight,
        "status": data.status,
        "note": data.note,
        "vehicledetails": data.vehicledetails,
    }

from server.models import Users
from functools import wraps
from flask import request, jsonify, g
import jwt
import os
from .models import Weight, Regions
from .models import Price
from .models import Destination
from .models import Zone
import random

size = os.environ.get('TRACKING_ID_SIZE')


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

            g.userRole = data['role']
            g.userBranchId = data['branchId']

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


def randomGenerator():
    min = pow(10, int(size)-1)
    max = pow(10, int(size)) - 1
    return random.randint(min, max)


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
        "employeenumber": data.employeenumber,
        "branchId": data.branchId,
        "email": data.email,
        "phone": data.phone,
        "role": data.role,
        "created": data.created,
        "updated": data.updated,
    }


def branch_serializer(data):

    return {
        "branchId": data.branchId,
        "branchname": data.branchname,
        "region": Destination.query.filter_by(id=data.region).first().name,
        "branchaddress": data.branchaddress,
        "created": data.created,
        "updated": data.updated,
    }


def order_serializer(data):

    return {
        "orderid": data.orderid,
        "branchid": data.branchid,
        "customerid": data.customerid,
        "customername": data.customername.upper(),
        "customernotes": data.customernotes,
        "consignername": data.consignername,
        "consignerid": data.consignerid,
        "orderDelivered":data.orderDelivered,
        "cnotes": data.cnotes,
        "pregion": Destination.query.filter_by(id=data.pregion).first().name,
        "pdistrict": data.pdistrict,
        "pstreet": data.pstreet,
        "pnotes": data.pnotes,
        "dregion": Destination.query.filter_by(id=data.dregion).first().name,
        "ddistrict": data.ddistrict,
        "dstreet": data.dstreet,
        "trackingNo": data.trackingNo,
        "dnotes": data.dnotes,
        "consigneename": data.consigneename,
        "consigneephone": data.consigneephone,
        "consigneeemail": data.consigneeemail,
        "cnenotes": data.cnenotes,
        "pickuptime": data.pickuptime,
        "expdlrtime": data.expdlrtime,
        "pickupScheduled": data.pickupScheduled,
        "driverId": data.driverId,
        "vehicleId": data.vehicleId,
        "scheduledPickuptime": data.scheduledPickuptime,
        "pickupnote": data.pickupnote,
        "pickupnote": data.pickupnote,
        "pickuptime": data.pickuptime,
        "orderStatus": data.orderStatus,
        "pickupLoaded": data.pickupLoaded,
        "pickupUnloaded": data.pickupUnloaded,
        "scheduledPickuptime": data.scheduledPickuptime,
        "Loadedtime": data.Loadedtime,
        "Unloadedtime": data.Unloadedtime,
        "dispatchScheduled": data.dispatchScheduled,
        "dispatchDriverId": data.dispatchDriverId,
        "dispatchvehicleId": data.dispatchvehicleId,
        "dispatchnote": data.dispatchnote,
        "dispatchnote": data.dispatchnote,
        "transporterid": data.transporterid,
        "scheduledDispatchtime": data.scheduledDispatchtime,
        "dispatchDelivered": data.dispatchDelivered,
        "dispatchnote": data.dispatchnote,
        "deliveryscheduledtime": data.deliveryscheduledtime,
        "deliveryDriverId": data.deliveryDriverId,
        "vehicleIdfordelivered": data.vehicleIdfordelivered,
        "deliveryschedulednote": data.deliveryschedulednote,
        "orderdeliverytime": data.orderdeliverytime,
        "dispatchunloaded": data.dispatchunloaded,
        "deliveryscheduled": data.deliveryscheduled,
        "bundleId": data.bundleId,
        "destinationbranchid": data.destinationbranchid,
        "isbundled": data.isbundled,
        "altnativeconsigneefullname": data.altnativeconsigneefullname,
        "altnativeconsigneephone": data.altnativeconsigneefullname,
        "altnativeconsigneeemail": data.altnativeconsigneefullname,
        "alternativeconsignee": data.altnativeconsigneefullname,
        "orderType":data.orderType,
    }


def customer_serializer(data):
    region = ''
    _region = Regions.query.filter_by(regionId=data.regionId).first()

    if _region:
        region = _region.region

    return {
        "customerid": data.customerid,
        "fullname": data.fullname,
        "customertype": data.customertype,
        "vrn": data.vrn,
        "tin": data.tin,
        "username": data.fullname,
        "email": data.email,
        "phone": data.phone,
        "region": region,
        "street": data.street,
        "address": data.address,
        "generaladdress": data.street+' ,'+data.address,
        "created": data.created
    }


def consignor_serializer(data):

    return {
        "consginerid": data.consginerid,
        "fullname": data.fullname,
        "nidano": data.nidano,
        "email": data.email,
        "customerid": data.customerid,
        "phone": data.phone,
        "created": data.created,
        "updated": data.updated
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
        "transporterid": data.transporterid,
        "vrn": data.vrn,
        "tin": data.tin,
        "email": data.email,
        "phone": data.phone,
        "address": data.address,
        "route": data.route,
        "vehicledetails": data.vehicledetails,
        "created": data.created
    }


def item_serializer(data):

    if data.driverId:
        drivers = Users.query.filter_by(userid=data.driverId).first()
        fullName = drivers.fname.upper() + ' ' + drivers.lname.upper()

    else:
        fullName = ''

    return {
        "itemid": data.itemid,
        "itemname": data.itemname,
        "orderid": data.orderid,
        "itemtype": data.itemtype,
        "units": data.units,
        "pickupnote": data.pickupnote,
        "weight": str(data.weight),
        "status": data.status,
        "cost": str(data.cost),
        "note": data.note,
        "loadnote": data.loadnote,
        "vehicledetails": data.vehicledetails,
        "unloadnote": data.unloadnote,
        "driverId": data.driverId,
        "vehicleId": data.vehicleId,
        "pickupLoaded": data.pickupLoaded,
        "pickupUnloaded": data.pickupUnloaded,
        "pickupScheduled": data.pickupScheduled,
        "scheduledPickuptime": data.scheduledPickuptime,
        "Loadedtime": data.Loadedtime,
        "Unloadedtime": data.Unloadedtime,
        "driver": fullName,
        "dispatchScheduled": data.dispatchScheduled,
        "dispatchDelivered": data.dispatchDelivered,
        "dispatchDeliveredTime": data.dispatchDeliveredTime,
        "dispatchDeliverynote": data.dispatchDeliverynote,
        "dispatchDeliveryunits": data.dispatchDeliveryunits
    }


def bundle_serializer(data):

    return {
        "bundleid": data.bundleid,
        "bundlename": data.bundlename,
        "bundleto": data.bundleto,
        "bundlefrom": data.bundlefrom,
        "status": data.status,
        "created": data.updated,
        "updated": data.created
    }


def regions_serializer(data):
    return {
        "region": data.region,
        "regionId": data.regionId,
        "created": data.updated,
        "updated": data.created
    }


def zones_serializer(data):
    return {
        "name": data.name,
        "zoneid": data.zoneid,
        "description": data.description,
        "created": data.created,
        "updated": data.created
    }


def destination_serializer(data):
    zone = Zone.query.filter_by(id=data.zoneid).first().name
    return {
        "name": data.name,
        "destinationid": data.destinationid,
        "zoneid": data.zoneid,
        "zone": zone,
        "created": data.created,
        "updated": data.created
    }


def weight_serializer(data):
    return {
        "weightid": data.weightid,
        "min": str(data.min),
        "max": str(data.max),
        "created": data.created,
        "updated": data.created
    }


def price_serializer(data):

    if data.zoneid:
        zones = Zone.query.filter_by(id=data.zoneid).first()
        zonename = zones.name
    else:
        zonename = ''

    if data.weight_d:
        weights = Weight.query.filter_by(id=data.weight_d).first()
        unitname = weights.weightid
    else:
        unitname = ''

    if unitname:
        min = Weight.query.filter_by(weightid=unitname).first().min
        max = Weight.query.filter_by(weightid=unitname).first().max

    return {
        "price": str(data.price),
        "zone": zonename,
        "priceid": str(data.priceid),
        "weight": str(min) + " - " + str(max),
        "created": data.created,
        "updated": data.created

    }

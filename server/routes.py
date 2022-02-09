from flask import Blueprint, request, jsonify
from .extensions import db
from .models import Users
from .models import Branch
from .auth.login import login
from .admin_actions.createUser import registerUser
from .admin_actions.updateUser import updateUser
from .admin_actions.deleteUser import removeUser
from .admin_actions.branch.branchCreate import create
from .user_actions.orders.createOder import createOder
from .user_actions.orders.orders import orders
from .user_actions.orders.items.getitem import getitems
from .user_actions.orders.items.getitemByorder import getitemByorder
from .user_actions.orders.actions.schedulePickup import schedulePickup
from .user_actions.orders.actions.loadPickup import loadPickup
from .user_actions.orders.actions.unloadPickup import unloadloadPickup
from .user_actions.Customers.customers import getcustomers
from .user_actions.Customers.deleteCustomer import deleteCustomer
from .user_actions.orders.deleteOrder import deleteOrder
from .user_actions.orders.items.addItem import addItem
from .user_actions.Customers.registerCustomer import registerCustomer
from .user_actions.Vehicle.registerVehicle import regvehicle
from .user_actions.Transporter.registerTransporter import regTransporter
from .user_actions.Vehicle.vehicles import getvehicle
from .user_actions.Transporter.transporters import gettransporters
from .user_actions.Vehicle.deleteVehicle import deleteVehicle
from .user_actions.Transporter.deleteTransporter import deleteTransporter
from .auth.register import register
from .profile.team import users
from .profile.userRole import getUserbyrole
from .helper import token_required_user, token_required_admin
from .profile.userProfile import profile
from flask_cors import CORS, cross_origin

main = Blueprint('main', __name__)
CORS(main, support_credentials=True)


# ---------- Authentication routes ----------

@main.route('/register', methods=['POST'])
def Userreg():
    data = request.json
    return register(data, db)


@main.route('/login', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def Userlogin():
    if(request.method == 'POST'):
        return login(request, Users)
    else:
        pass


@main.route('/resetPassword')
def resetPassword():
    return 'reset codes sent'

# ---------- Admin actions ---------------------------


@main.route('/admin/create-user',  methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def createUser():
    data = request.json
    if(request.method == 'POST'):
        return registerUser(data, db)
    else:
        pass


@main.route('/admin/edit-user/<userId>', methods=['PUT', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def editUser(userId):
    data = request.json
    if(request.method == 'PUT'):
        return updateUser(data, userId, db)
    else:
        pass


@main.route('/admin/delete-user/<userId>', methods=['DELETE', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def delete_User(userId):
    if(request.method == 'DELETE'):
        return removeUser(userId, db)
    else:
        pass


@main.route('/revoke-token')
def revokeToken():
    return 'user deleted'


@main.route('/api/users', methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def users_():
    if(request.method == 'GET'):
        return users(Users)
    else:
        pass


@main.route('/api/usersByrole/<role>', methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def users_Byrole(role):
    if(request.method == 'GET'):
        return getUserbyrole(role)
    else:
        pass


# ---------- User actions --------------------------------------

@main.route('/api/profile/<userId>', methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def f_profile(userId):
    if(request.method == 'GET'):
        return profile(userId, Users)
    else:
        pass

# ......................... order urls...............


@main.route('/api/create-order', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def c_order():
    data = request.json
    if(request.method == 'POST'):
        return createOder(data, db)
    else:
        pass


@main.route('/api/orders',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def getorders():
    if(request.method == 'GET'):
        return orders()
    else:
        pass


@main.route('/api/delete-order/<orderid>', methods=['DELETE', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def delete_Order(orderid):
    if(request.method == 'DELETE'):
        return deleteOrder(orderid, db)
    else:
        pass


@main.route('/api/orders/add-item', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def a_item():
    data = request.json
    if(request.method == 'POST'):
        return addItem(data, db)
    else:
        pass


@main.route('/api/orders/items', methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def g_item():
    if(request.method == 'GET'):
        return getitems()
    else:
        pass


@main.route('/api/orders/items/<orderid>', methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def g_itemByid(orderid):
    if(request.method == 'GET'):
        return getitemByorder(orderid)
    else:
        pass


#................. schedule orders


@main.route('/api/orders/schedule/<orderid>', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def schedlue_order(orderid):
    if(request.method == 'POST'):
        data = request.json
        return schedulePickup(orderid, data, db)
    else:
        pass


@main.route('/api/orders/loadpickup/<itmeid>', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def loadpickup(itmeid):
    if(request.method == 'POST'):
        data = request.json
        return loadPickup(itmeid, data, db)
    else:
        pass


@main.route('/api/orders/unloadpickup/<itmeid>', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def unloadpickup(itmeid):
    if(request.method == 'POST'):
        data = request.json
        return unloadloadPickup(itmeid, data, db)
    else:
        pass

# ........................... customer url ...............

@main.route('/api/register-customer', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def r_customer():
    data = request.json
    if(request.method == 'POST'):
        return registerCustomer(data, db)
    else:
        pass


@main.route('/api/customers',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def r_orders():
    if(request.method == 'GET'):
        return getcustomers()
    else:
        pass


@main.route('/api/delete-customer/<customerid>', methods=['DELETE', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def delete_Customer(customerid):
    if(request.method == 'DELETE'):
        return deleteCustomer(customerid, db)
    else:
        pass


# .......................... vehicle urls ....................................

@main.route('/api/register-vehicle', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def r_vehicle():
    data = request.json
    if(request.method == 'POST'):
        return regvehicle(data, db)
    else:
        pass


@main.route('/api/vehicles',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def g_vehicles():
    if(request.method == 'GET'):
        return getvehicle()
    else:
        pass


@main.route('/api/delete-vehicle/<vehicleid>', methods=['DELETE', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def delete_vehicle(vehicleid):
    if(request.method == 'DELETE'):
        return deleteVehicle(vehicleid, db)
    else:
        pass


# ............................ transporters url ................................

@main.route('/api/register-transporter', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def r_transporter():
    data = request.json
    if(request.method == 'POST'):
        return regTransporter(data, db)
    else:
        pass


@main.route('/api/transporters',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def g_transporters():
    if(request.method == 'GET'):
        return gettransporters()
    else:
        pass


@main.route('/api/delete-transporter/<transporterid>', methods=['DELETE', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def delete_transporter(transporterid):
    if(request.method == 'DELETE'):
        return deleteTransporter(transporterid, db)
    else:
        pass

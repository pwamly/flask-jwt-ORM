from flask import Blueprint, request, jsonify

from server.user_actions.orders.actions.scheduleDelivery import scheduleDelivery
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
from .user_actions.orders.bundledOrders import bundledOrders
from .user_actions.bundle.deliverBundle import deliverBundle
from .user_actions.orders.orders import getDeliveries
from .user_actions.orders.items.getitem import getitems
from .user_actions.orders.items.getitemByorder import getitemByorder
from .user_actions.orders.dispatchedOrders import getdispatchedOrder
from .user_actions.orders.actions.schedulePickup import schedulePickup
from .user_actions.Settings.addregions import registerRegion
from .user_actions.Settings.getRegions import getregions
from .user_actions.Settings.editregions import updateRegion
from .user_actions.Settings.deleteregions import deleteRegion
from .user_actions.bundle.createbundle import createBundle
from .user_actions.bundle.updateBundle import updateBundle
from .user_actions.bundle.deletebundle import deleteBudle
from .user_actions.orders.actions.loadPickup import loadPickup
from .user_actions.orders.actions.unloadPickup import unloadloadPickup
from .user_actions.orders.actions.unloaddispatchdelivery import unloadDispatch
from .user_actions.orders.actions.scheduleDispatch import scheduleDispatch, scheduleDispatchBundle
from .user_actions.orders.actions.deliverDispatch import deliverDispatch
from .user_actions.orders.actions.deliverOrder import deliverOrder
from .user_actions.Customers.customers import getcustomers
from .user_actions.Customers.consignor.consignors import getconsignors, getconsignorsByCustomer
from .user_actions.Customers.deleteCustomer import deleteCustomer
from .user_actions.orders.deleteOrder import deleteOrder
from .user_actions.orders.items.addItem import addItem
from .user_actions.Customers.registerCustomer import registerCustomer
from .user_actions.Customers.consignor.addconsignor import registerConsignor
from .user_actions.Vehicle.registerVehicle import regvehicle
from .user_actions.Transporter.registerTransporter import regTransporter
from .user_actions.Vehicle.vehicles import getvehicle
from .user_actions.Transporter.transporters import gettransporters
from .user_actions.bundle.getBundles import getbundles
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
    page = request.args.get('gage')
    sort = request.args.get('sort')
    q = request.args.get('q')
    if(request.method == 'GET'):
        return users(page, sort, q)
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
    page = request.args.get('gage')
    sort = request.args.get('sort')
    q = request.args.get('q')
    date = request.args.get('date')
    status = request.args.get('status')

    if(request.method == 'GET'):
        return orders(page, sort, q, date, status)
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


# ................. schedule orders.........................


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

        # .... dispatch...........


@main.route('/api/orders/scheduleDispatch/<orderid>', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def scheduleDispatch_s(orderid):
    if(request.method == 'POST'):
        data = request.json
        return scheduleDispatch(orderid, data, db)
    else:
        pass


@main.route('/api/orders/deliverDispatch/<itemid>', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def deliverDispatch_d(itemid):
    if(request.method == 'POST'):
        data = request.json
        return deliverDispatch(itemid, data, db)
    else:
        pass


@main.route('/api/dispatchedOrders', methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def getDispatch_d():
    page = request.args.get('gage')
    sort = request.args.get('sort')
    q = request.args.get('q')
    if(request.method == 'GET'):
        return getdispatchedOrder(page, sort, q)
    else:
        pass


@main.route('/api/unloaddispatch/<itemid>', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def unloadDispatch_d(itemid):
    if(request.method == 'POST'):
        data = request.json
        return unloadDispatch(itemid, data, db)
    else:
        pass


@main.route('/api/scheduleDelivery/<orderid>', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def scheduleDelivery_d(orderid):
    if(request.method == 'POST'):
        data = request.json
        return scheduleDelivery(orderid, data, db)
    else:
        pass


@main.route('/api/delivery-item/<itemid>', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def deliveryItem_d(itemid):
    if(request.method == 'POST'):
        data = request.json
        return deliverOrder(itemid, data, db)
    else:
        pass


@main.route('/api/deliveries',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def getdeliveredorders_d():
    page = request.args.get('gage')
    sort = request.args.get('sort')
    q = request.args.get('q')
    if(request.method == 'GET'):
        return getDeliveries(page, sort, q)
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
def r_customers():
    page = request.args.get('gage')
    sort = request.args.get('sort')
    q = request.args.get('q')
    if(request.method == 'GET'):
        return getcustomers(page, sort, q)
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


@main.route('/api/register-consignor', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def r_consignor():
    data = request.json
    if(request.method == 'POST'):
        return registerConsignor(data, db)
    else:
        pass


@main.route('/api/consignors/<customerid>',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def r_consignors_b(customerid):
    if(request.method == 'GET'):
        return getconsignorsByCustomer(customerid)
    else:
        pass


@main.route('/api/consignors',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def r_consignors():
    if(request.method == 'GET'):
        return getconsignors()
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
    page = request.args.get('gage')
    sort = request.args.get('sort')
    q = request.args.get('q')
    if(request.method == 'GET'):
        return getvehicle(page, sort, q)
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
    page = request.args.get('gage')
    sort = request.args.get('sort')
    q = request.args.get('q')
    if(request.method == 'GET'):
        return gettransporters(page, sort, q)
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


# ................. bundle ...............................

@main.route('/api/create-bandle', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def create_bundle():
    if(request.method == 'POST'):
        data = request.json
        return createBundle(data, db)
    else:
        pass


@main.route('/api/bundles',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def g_bundles():
    page = request.args.get('gage')
    sort = request.args.get('sort')
    q = request.args.get('q')
    if(request.method == 'GET'):
        return getbundles(page, sort, q)
    else:
        pass


@main.route('/api/edit-bundle/<bundleid>', methods=['PUT', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def e_bundle(bundleid):
    data = request.json
    if(request.method == 'PUT'):
        return updateBundle(data, bundleid, db)
    else:
        pass


@main.route('/api/delete-bundle/<bundleid>', methods=['DELETE', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def d_bundle(bundleid):
    if(request.method == 'DELETE'):
        return deleteBudle(bundleid, db)
    else:
        pass


@main.route('/api/bundled-orders/<bundleid>',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def b_getorders(bundleid):
    if(request.method == 'GET'):
        return bundledOrders(bundleid)
    else:
        pass


@main.route('/api/bundle/scheduleDispatch/<bundleid>', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def b_scheduleDispatch_s(bundleid):
    if(request.method == 'POST'):
        data = request.json
        return scheduleDispatchBundle(bundleid, data, db)
    else:
        pass


@main.route('/api/bundle/deliver-bundle/<bundleid>', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def b_Deliverbundle(bundleid):
    if(request.method == 'POST'):
        data = request.json
        return deliverBundle(bundleid, data, db)
    else:
        pass


# ................. Regions ...............................


@main.route('/api/add-regions', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def addRegions_a():
    if(request.method == 'POST'):
        data = request.json
        return registerRegion(data, db)
    else:
        pass


@main.route('/api/regions',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def get_regions():
    if(request.method == 'GET'):
        return getregions()
    else:
        pass


@main.route('/api/update-region/<regionid>', methods=['PUT', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def update_region(regionid):
    data = request.json
    if(request.method == 'PUT'):
        return updateRegion(data, regionid, db)
    else:
        pass


@main.route('/api/delete-region/<regionid>', methods=['DELETE', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def delete_region(regionid):
    if(request.method == 'DELETE'):
        return deleteRegion(regionid, db)
    else:
        pass

from sqlalchemy import null
from .extensions import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
import uuid

userid = uuid.uuid4()


class Users(db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(200), nullable=False, unique=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    branchId = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(120), nullable=False, unique=True)
    role = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    isadmin = db.Column(db.Boolean, nullable=False)
    refrestoken = db.Column(db.String(200), nullable=True, unique=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)


class Branch(db.Model):

    __tablename__ = 'Branch'

    id = db.Column(db.Integer, primary_key=True)
    branchId = db.Column(db.Integer, nullable=False, unique=True)
    branchname = db.Column(db.String(200), nullable=False)
    region = db.Column(db.String(200), nullable=False)
    district = db.Column(db.String(200), nullable=False)
    branchaddress = db.Column(db.String(120), nullable=False, unique=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)


class Order(db.Model):

    __tablename__ = 'Order'

    id = db.Column(db.Integer, primary_key=True)
    orderid = db.Column(db.String(200), nullable=False, unique=True)  #
    branchid = db.Column(db.Integer, nullable=True)
    customerid = db.Column(db.String(200), nullable=False)
    customername = db.Column(db.String(200), nullable=False)
    customernotes = db.Column(db.String(200), nullable=True)
    consignername = db.Column(db.String(200), nullable=False)
    consignerid = db.Column(db.String(200), nullable=False)
    cnotes = db.Column(db.String(200), nullable=True)
    pregion = db.Column(db.String(200), nullable=False)
    pdistrict = db.Column(db.String(200), nullable=False)
    pstreet = db.Column(db.String(200), nullable=False)
    pnotes = db.Column(db.String(200), nullable=True)
    dregion = db.Column(db.String(200), nullable=False)
    ddistrict = db.Column(db.String(200), nullable=False)
    dstreet = db.Column(db.String(200), nullable=False)
    dnotes = db.Column(db.String(200), nullable=True)
    consigneename = db.Column(db.String(200), nullable=False)
    cnenotes = db.Column(db.String(200), nullable=True)
    driverId = db.Column(db.String(200), nullable=True)  # driver id for pickup
    # vehicle id for pickup
    vehicleId = db.Column(db.String(200), nullable=True)
    # if there is any details to eraborate
    pickupnote = db.Column(db.String(200), nullable=True)
    pickuptime = db.Column(db.DateTime, nullable=False)
    expdlrtime = db.Column(db.DateTime, nullable=False)
    pickuptime = db.Column(db.DateTime, nullable=True)
    orderStatus = db.Column(
        db.String(200), default='not picked', nullable=True)  # order status .....
    pickupScheduled = db.Column(db.Boolean, nullable=True)
    pickupLoaded = db.Column(db.Boolean, nullable=True)
    pickupUnloaded = db.Column(db.Boolean, nullable=True)
    scheduledPickuptime = db.Column(db.DateTime, nullable=True)
    Loadedtime = db.Column(db.DateTime, nullable=True)
    Unloadedtime = db.Column(db.DateTime, nullable=True)

    #....................for  schedule dispatch....................

    dispatchScheduled = db.Column(db.Boolean, nullable=True)
    dispatchDriverId = db.Column(db.String(200), nullable=True)
    dispatchvehicleId = db.Column(db.String(200), nullable=True)
    dispatchnote = db.Column(db.String(200), nullable=True)
    transporterid = db.Column(db.String(200), nullable=True)
    scheduledDispatchtime = db.Column(db.DateTime, nullable=True)
    dispatchDelivered = db.Column(db.Boolean, nullable=True)

 #....................for  dispatch delivery ....................

    deliveryscheduled = db.Column(db.Boolean, nullable=True)
    deliveryscheduledtime = db.Column(db.DateTime, nullable=True)
    deliveryDriverId = db.Column(db.String(200), nullable=True)
    vehicleIdfordelivered = db.Column(db.String(200), nullable=True)
    deliveryschedulednote = db.Column(db.String(200), nullable=True)
    orderdeliverytime = db.Column(db.DateTime, nullable=True)



    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)


class Customer(db.Model):

    __tablename__ = 'Customer'

    id = db.Column(db.Integer, primary_key=True)
    branchId = db.Column(db.Integer, nullable=True)
    customerid = db.Column(db.String(200), nullable=False, unique=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    phone = db.Column(db.String(200), nullable=False)
    region = db.Column(db.String(200), nullable=False)
    district = db.Column(db.String(200), nullable=False)
    street = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)


class Vehicle(db.Model):

    __tablename__ = 'Vehicles'

    id = db.Column(db.Integer, primary_key=True)
    vehicleid = db.Column(db.String(200), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False)
    plateno = db.Column(db.String(200), nullable=True)
    model = db.Column(db.String(200), nullable=False)
    loadcapacity = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    routestatus = db.Column(db.String(200), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)


class Transporter(db.Model):

    __tablename__ = 'Transporters'

    id = db.Column(db.Integer, primary_key=True)
    transporterid = db.Column(db.String(200), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=True)
    phone = db.Column(db.String(200), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    route = db.Column(db.String(200), nullable=False)
    vehicledetails = db.Column(db.String(200), nullable=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)


class Item(db.Model):

    __tablename__ = 'Item'

    id = db.Column(db.Integer, primary_key=True)
    itemid = db.Column(db.String(200), nullable=False, unique=True)
    itemname = db.Column(db.String(200), nullable=True)
    orderid = db.Column(db.String(200), nullable=False)
    itemtype = db.Column(db.String(200), nullable=True)
    units = db.Column(db.String(200), nullable=False)
    loadunits = db.Column(db.String(200), nullable=True)
    unloadunits = db.Column(db.String(200), nullable=True)
    dispatchunits = db.Column(db.String(200), nullable=True)
    deliveredunits = db.Column(db.String(200), nullable=True)
    weight = db.Column(db.String(200), nullable=False)
    note = db.Column(db.String(200), nullable=False)
    loadnote = db.Column(db.String(200), nullable=True)
    unloadnote = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(200), default='not picked', nullable=True)
    vehicledetails = db.Column(db.String(200), nullable=True)
    pickupLoaded = db.Column(db.Boolean, nullable=True)
    pickupUnloaded = db.Column(db.Boolean, nullable=True)
    Loadedtime = db.Column(db.DateTime, nullable=True)
    Unloadedtime = db.Column(db.DateTime, nullable=True)

    # for dispatch scheduled..................

    dispatchScheduled = db.Column(db.Boolean, nullable=True)
    scheduledPickuptime = db.Column(db.DateTime, nullable=True)
    # for dispatch delivered..................

    dispatchDelivered = db.Column(db.Boolean, nullable=True)
    dispatchDeliveredTime = db.Column(db.DateTime, nullable=True)
    dispatchDeliverynote = db.Column(db.String(200), nullable=True)
    dispatchDeliveryunits = db.Column(db.String(200), nullable=True)

    # for unload dispatch .....................

    dispatchunloaded = db.Column(db.Boolean, nullable=True)
    unloadeddispatchunits = db.Column(db.String(200), nullable=True)
    unloadeddispatchtime = db.Column(db.String(200), nullable=True)
    unloadeddispatchnotes = db.Column(db.String(200), nullable=True)

    # for schedule delivery dispatch .....................

    # for deliverorder....................................

    deliveredunits = db.Column(db.String(200), nullable=True)
    itemdeliverynote = db.Column(db.String(200), nullable=True)
    itemdelivered = db.Column(db.Boolean, nullable=True)
    deliverytime = db.Column(db.DateTime, nullable=True)


    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)

    # @property
    # def password_(self):
    #    raise ArithmeticError('can not use unhashed password')

    # @password_.setter
    # def password_(self, password):
    #  self.userid = userid
    #  self.password = generate_password_hash(password)

# class Order(db.Model):

#     __tablename__ = 'Order'

#     id = db.Column(db.Integer, primary_key=True)
#     branchId = db.Column(db.String(200), nullable=False, unique=True)
#     branchname = db.Column(db.String(200), nullable=False)
#     region = db.Column(db.String(200), nullable=False)
#     district = db.Column(db.String(200), nullable=False)
#     branchaddress = db.Column(db.String(120), nullable=False, unique=True)
#     created = db.Column(db.DateTime, default=datetime.utcnow)
#     updated = db.Column(db.DateTime, default=datetime.utcnow)

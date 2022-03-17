from enum import unique
from sqlalchemy import null
from .extensions import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
import uuid

userid = uuid.uuid4()


class TimestampMixin(object):
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)


class Users(TimestampMixin, db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(200), nullable=False, unique=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    branchId = db.Column(db.Integer, nullable=True)
    employeenumber = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(120), nullable=False, unique=True)
    role = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    isadmin = db.Column(db.Boolean, nullable=False)
    refrestoken = db.Column(db.String(200), nullable=True, unique=True)

    def __repr__(self):
        return '<User %r>' % self.fname + self.lname


class Branch(TimestampMixin, db.Model):

    __tablename__ = 'Branch'

    id = db.Column(db.Integer, primary_key=True)
    branchId = db.Column(db.Integer, nullable=False, unique=True)
    branchname = db.Column(db.String(200), nullable=False)
    region = db.Column(db.String(200), nullable=False)
    district = db.Column(db.String(200), nullable=True)
    branchaddress = db.Column(db.String(120), nullable=False, unique=True)


class Order(TimestampMixin, db.Model):

    __tablename__ = 'Order'

    id = db.Column(db.Integer, primary_key=True)
    orderid = db.Column(db.String(200), nullable=False, unique=True)
    branchid = db.Column(db.Integer, nullable=True)
    customerid = db.Column(db.String(200), nullable=False)
    customername = db.Column(db.String(200), nullable=False)
    customernotes = db.Column(db.String(200), nullable=True)
    consignername = db.Column(db.String(200), nullable=False)
    trackingNo = db.Column(db.String(200), nullable=True)
    consignerid = db.Column(db.String(200), nullable=False)
    cnotes = db.Column(db.String(200), nullable=True)
    pregion = db.Column(db.String(200), nullable=False)
    pdistrict = db.Column(db.String(200), nullable=True)
    pstreet = db.Column(db.String(200), nullable=False)
    pnotes = db.Column(db.String(200), nullable=True)
    dregion = db.Column(db.Integer, db.ForeignKey('Destination.id'))
    ddistrict = db.Column(db.String(200), nullable=True)
    dstreet = db.Column(db.String(200), nullable=False)
    dnotes = db.Column(db.String(200), nullable=True)
    consigneename = db.Column(db.String(200), nullable=False)
    consigneephone = db.Column(db.String(200), nullable=True)
    cnenotes = db.Column(db.String(200), nullable=True)
    orderStatus = db.Column(db.String(200), default='', nullable=True)
    expdlrtime = db.Column(db.DateTime, nullable=False)
    pickuptime = db.Column(db.DateTime, nullable=True)

    # ............. 1. for Add items..............
    itemsAdded = db.Column(db.Boolean, nullable=True)

    # ............. 2. for schedule pickup..............

    driverId = db.Column(db.String(200), nullable=True)
    vehicleId = db.Column(db.String(200), nullable=True)
    pickupnote = db.Column(db.String(200), nullable=True)
    pickupScheduled = db.Column(db.Boolean, nullable=True)
    scheduledPickuptime = db.Column(db.DateTime, nullable=True)

 # ................ 3. for  loadpickup ....................

    pickupLoaded = db.Column(db.Boolean, nullable=True)
    Loadedtime = db.Column(db.DateTime, nullable=True)

 # ................ 3. for  unloadpickup ....................

    pickupUnloaded = db.Column(db.Boolean, nullable=True)
    Unloadedtime = db.Column(db.DateTime, nullable=True)

    dispatchScheduled = db.Column(db.Boolean, nullable=True)
    dispatchDriverId = db.Column(db.String(200), nullable=True)
    dispatchvehicleId = db.Column(db.String(200), nullable=True)
    dispatchnote = db.Column(db.String(200), nullable=True)
    transporterid = db.Column(db.String(200), nullable=True)
    scheduledDispatchtime = db.Column(db.DateTime, nullable=True)
    dispatchDelivered = db.Column(db.Boolean, nullable=True)
    dispatchunloaded = db.Column(db.Boolean, nullable=True)

 # ....................for  dispatch delivery ....................

    deliveryscheduled = db.Column(db.Boolean, nullable=True)
    deliveryscheduledtime = db.Column(db.DateTime, nullable=True)
    deliveryDriverId = db.Column(db.String(200), nullable=True)
    vehicleIdfordelivered = db.Column(db.String(200), nullable=True)
    deliveryschedulednote = db.Column(db.String(200), nullable=True)
    orderdeliverytime = db.Column(db.DateTime, nullable=True)

 # ............................ for bundle .......................
    bundleId = db.Column(db.String(200), nullable=True)
    destinationbranchid = db.Column(db.String(220), nullable=True)
    isbundled = db.Column(db.Boolean, nullable=True)


# ................................. for unziping .......................
    nextDestination = db.Column(db.String(200), nullable=True)
    nextDestinationBranchId = db.Column(db.String(200), nullable=True)
    newBundleid = db.Column(db.String(200), nullable=True)
    Unbundled = db.Column(db.Boolean, nullable=True)
    UnbundledBy = db.Column(db.String(200), nullable=True)


class Customer(TimestampMixin, db.Model):

    __tablename__ = 'Customer'

    id = db.Column(db.Integer, primary_key=True)
    branchId = db.Column(db.Integer, nullable=True)
    customerid = db.Column(db.String(200), nullable=False, unique=True)
    fullname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    phone = db.Column(db.String(200), nullable=False)
    region = db.Column(db.String(200), nullable=False)
    district = db.Column(db.String(200), nullable=True)
    street = db.Column(db.String(200), nullable=False)
    customertype = db.Column(db.String(10))
    vrn = db.Column(db.Integer, nullable=True, unique=True)
    tin = db.Column(db.Integer, nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=True)


class Vehicle(TimestampMixin, db.Model):

    __tablename__ = 'Vehicles'

    id = db.Column(db.Integer, primary_key=True)
    vehicleid = db.Column(db.String(200), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(200), nullable=True)
    plateno = db.Column(db.String(200), nullable=True)
    model = db.Column(db.String(200), nullable=False)
    loadcapacity = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    customertype = db.Column(db.String(10))
    routestatus = db.Column(db.String(200), nullable=False)


class Transporter(TimestampMixin, db.Model):

    __tablename__ = 'Transporters'

    id = db.Column(db.Integer, primary_key=True)
    transporterid = db.Column(db.String(200), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=True)
    phone = db.Column(db.String(200), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    route = db.Column(db.String(200), nullable=False)
    vrn = db.Column(db.Integer, nullable=True, unique=True)
    tin = db.Column(db.Integer, nullable=False, unique=True)
    vehicledetails = db.Column(db.String(200), nullable=True)


class Item(TimestampMixin, db.Model):

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
    weight = db.Column(db.Integer, nullable=False)
    note = db.Column(db.String(200), nullable=False)
    loadnote = db.Column(db.String(200), nullable=True)
    unloadnote = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(200), default='not picked', nullable=True)
    vehicledetails = db.Column(db.String(200), nullable=True)
    cost = db.Column(db.Numeric, nullable=True)

    # ........... 1. for schedule pickup.............
    driverId = db.Column(db.String(200), nullable=True)
    vehicleId = db.Column(db.String(200), nullable=True)
    pickupnote = db.Column(db.String(200), nullable=True)
    pickupScheduled = db.Column(db.Boolean, nullable=True)
    scheduledPickuptime = db.Column(db.DateTime, nullable=True)

    pickupLoaded = db.Column(db.Boolean, nullable=True)
    pickupUnloaded = db.Column(db.Boolean, nullable=True)
    Loadedtime = db.Column(db.DateTime, nullable=True)
    Unloadedtime = db.Column(db.DateTime, nullable=True)

    # for dispatch scheduled..................

    dispatchScheduled = db.Column(db.Boolean, nullable=True)
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


class Consignor(TimestampMixin, db.Model):

    __tablename__ = 'Consignor'

    id = db.Column(db.Integer, primary_key=True)
    consginerid = db.Column(db.String(200), nullable=False)
    customerid = db.Column(db.String(200), nullable=False)
    fullname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    phone = db.Column(db.String(200), nullable=False, unique=True)
    nidano = db.Column(db.String(200), nullable=True, unique=True)


class Bundle(TimestampMixin, db.Model):

    __tablename__ = 'Bundle'

    id = db.Column(db.Integer, primary_key=True)
    bundleid = db.Column(db.String(200), nullable=False)
    bundlename = db.Column(db.String(200), nullable=True)
    bundleto = db.Column(db.String(200), nullable=True)
    bundlefrom = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(200), nullable=True)

    # ........................ for shedule dispatch and deliver dispatch ...........add()

    dispatchScheduled = db.Column(db.Boolean, nullable=True)
    dispatchDelivered = db.Column(db.Boolean, nullable=True)

    # ................................. for unziping .......................
    nextDestination = db.Column(db.String(200), nullable=True)
    nextDestinationBranchId = db.Column(db.String(200), nullable=True)
    newBundleid = db.Column(db.String(200), nullable=True)
    Unbundled = db.Column(db.Boolean, nullable=True)
    UnbundledBy = db.Column(db.String(200), nullable=True)



class Regions(TimestampMixin, db.Model):

    __tablename__ = 'Region'

    id = db.Column(db.Integer, primary_key=True)
    regionId = db.Column(db.String(200), nullable=False)
    region = db.Column(db.String(200), nullable=False)
    descriptions = db.Column(db.String(200), nullable=True)


class Pickup(TimestampMixin, db.Model):

    __tablename__ = 'Pickup'

    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.String(200), nullable=False)
    itemId = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    pickedBy = db.Column(db.String(200), nullable=False)


class Zone(TimestampMixin, db.Model):

    __tablename__ = 'Zone'

    id = db.Column(db.Integer, primary_key=True)
    zoneid = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=True)
    destinations = db.relationship('Destination', backref='Zone')
    prices = db.relationship('Price', backref='Zone')
    
    def __repr__(self):
        return '<Zone %r>' % self.name
    
    


class Destination(TimestampMixin, db.Model):

    __tablename__ = 'Destination'

    id = db.Column(db.Integer, primary_key=True)
    destinationid = db.Column(db.String(200), nullable=False)
    orders = db.relationship('Order', backref='Destination')
    name = db.Column(db.String(200), nullable=False, unique=True)
    zoneid = db.Column(db.Integer, db.ForeignKey('Zone.id'))
    
    def __repr__(self):
        return '<Destination %r>' % self.name


class Weight(TimestampMixin, db.Model):

    __tabllname__ = 'Weight'

    id = db.Column(db.Integer, primary_key=True)
    weightid = db.Column(db.String(200), nullable=False)
    min = db.Column(db.Numeric, unique=True)
    max = db.Column(db.Numeric, unique=True)
    # prices = db.relationship('Price', backref='CSWeight')
    
    def __repr__(self):
        return '<Weight %r>' % self.id


class Price(TimestampMixin, db.Model):

    __tablename__ = 'Price'

    id = db.Column(db.Integer, primary_key=True)
    priceid = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    itemid = db.Column(db.Integer, db.ForeignKey('Item.id'))
    zoneid = db.Column(db.Integer, db.ForeignKey('Zone.id'))
    weight_d = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Price %r>' % self.price

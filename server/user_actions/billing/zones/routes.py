from flask import Blueprint, request, jsonify
from server.user_actions.billing.zones.adddestination import createDestinationOnZone
from server.user_actions.billing.zones.create import createZone
from server.user_actions.billing.zones.update import updateZone
from ....helper import token_required_user, token_required_admin
from flask_cors import CORS, cross_origin
from ....extensions import db
from ...billing.zones.zones import getZones


zones = Blueprint('zones', __name__)


@zones.route('/api/zones',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def getAllZones():
    if(request.method == 'GET'):
        return getZones()
    else:
        pass


@zones.route('/api/zones/register', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def registerZone():
    data = request.json
    if(request.method == 'POST'):
        return createZone(data, db)  
    else:
        pass


@zones.route('/api/zones/register-destination', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def registerDestination():
    data = request.json
    if(request.method == 'POST'):
        return createDestinationOnZone(data, db)
    else:
        pass


@zones.route('/api/zones/edit-zone/<zoneid>', methods=['PUT', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user

def editZones(zoneid):
    data = request.json
    if(request.method == 'PUT'):
        return updateZone(data, zoneid, db)
    else:
        pass
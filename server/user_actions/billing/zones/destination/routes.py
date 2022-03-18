from flask import Blueprint, request, jsonify
from server.user_actions.billing.zones.destination.update import updateDestination
from server.user_actions.billing.zones.destination.destinations import getAllDestinations
from .....helper import token_required_user, token_required_admin
from flask_cors import CORS, cross_origin
from .....extensions import db
from ....billing.zones.destination.get_zone import getDestinationByZone


destination = Blueprint('destination', __name__)

@destination.route('/api/get_destinations',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def getDestinationsByZoneId():
    if(request.method == 'GET'):
        return getDestinationByZone(request.args.get('zoneid'))
    else:
        pass
    
    
@destination.route('/api/destinations',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def _getAllDestinations():
    if(request.method == 'GET'):
        return getAllDestinations()
    else:
        pass


@destination.route('/api/destination/edit-destination/<destinationid>', methods=['PUT', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def editDestination(destinationid):
    data = request.json
    if(request.method == 'PUT'):
        return updateDestination(data, destinationid, db)
    else:
        pass
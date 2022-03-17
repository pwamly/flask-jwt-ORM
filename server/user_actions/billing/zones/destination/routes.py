from flask import Blueprint, request, jsonify
from server.user_actions.billing.zones.destination.update import updateDestination
from .....helper import token_required_user, token_required_admin
from flask_cors import CORS, cross_origin
from .....extensions import db


destination = Blueprint('destination', __name__)


@destination.route('/api/destinations',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def getAllDestinations():
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
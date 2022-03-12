from flask import Blueprint, request, jsonify
from server.user_actions.billing.weight.create import createWeight
from server.user_actions.billing.weight.update import updateWeight
from server.user_actions.billing.zones.create import createZone
from server.user_actions.billing.zones.update import updateZone
from ....helper import token_required_user, token_required_admin
from flask_cors import CORS, cross_origin
from ....extensions import db


weight = Blueprint('weight', __name__)


@weight.route('/api/wights',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def getAllWeights():
    if(request.method == 'GET'):
        return getAllWeights()
    else:
        pass


@weight.route('/api/wights/register', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def registerWeight():
    data = request.json
    if(request.method == 'POST'):
        return createWeight(data, db)
    else:
        pass


@weight.route('/api/wight/edit-weight/<weightid>', methods=['PUT', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def editWeight(destinationid):
    data = request.json
    if(request.method == 'PUT'):
        return updateWeight(data, destinationid, db)
    else:
        pass
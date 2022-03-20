from flask import Blueprint, request, jsonify
from server.user_actions.billing.price.create import createPrice
from server.user_actions.billing.price.update import updatePrice
from server.user_actions.billing.price.prices import getAllPrice
from server.user_actions.billing.weight.create import createWeight
from server.user_actions.billing.weight.update import updateWeight
from server.user_actions.billing.zones.create import createZone
from server.user_actions.billing.zones.update import updateZone
from ....helper import token_required_user, token_required_admin
from flask_cors import CORS, cross_origin
from ....extensions import db


price = Blueprint('price', __name__)


@price.route('/api/price',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def _getAllPrice():
    if(request.method == 'GET'):
        return getAllPrice()
    else:
        pass


@price.route('/api/price/register', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def register():
    data = request.json
    if(request.method == 'POST'):
        return createPrice(data, db)
    else:
        pass


@price.route('/api/price/edit-price/<priceid>', methods=['PUT', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def updatePrice_(priceid):
    data = request.json
    if(request.method == 'PUT'):
        return updatePrice(data, priceid, db)
    else:
        pass
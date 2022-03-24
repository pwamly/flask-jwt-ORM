from flask import Blueprint, request, jsonify
from ...helper import token_required_user, token_required_admin
from flask_cors import CORS, cross_origin
from ...admin_actions.branch.branchCreate import create
from ...admin_actions.branch.branches import branches
from ...admin_actions.branch.deleteBranch import removeBranch
from ...admin_actions.branch.updateBranch import updateBranch
from ...models import Branch

from ...extensions import db

branch = Blueprint('branch', __name__)


@branch.route('/admin/create-branch',  methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
# @token_required_user
def createbranch():
    data = request.json
    if(request.method == 'POST'):
        return create(data, db)
    else:
       pass


@branch.route('/admin/branches',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def getbranch():
    if(request.method == 'GET'):
      return branches(Branch)
    else:
       pass


@branch.route('/admin/delete-branch/<branchId>',  methods=['DELETE', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def removebranch(branchId):
    if(request.method == 'DELETE'):
      return removeBranch(branchId, db)
    else:
       pass


@branch.route('/admin/edit-branch/<branchId>', methods=['PUT', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def editUser(branchId):
    data = request.json
    if(request.method == 'PUT'):
        return updateBranch(data, branchId, db)
    else:
        pass

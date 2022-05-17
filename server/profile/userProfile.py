from flask import jsonify, g
from ..helper import profile_serializer
from ..models import Branch, Customer, Vehicle, Transporter


def profile(userId, Users):
    profile = Users.query.filter_by(userid=userId).first()
    employes = Users.query.filter_by()
    branch = Branch.query.filter_by()
    customer = Customer.query.filter_by()
    vehicle = Vehicle.query.filter_by()
    transporter = Transporter.query.filter_by()

    if profile:
        data = {'username': profile.fname, 'fname': profile.fname, 'lname': profile.lname, 'userRole': profile.role,
                'phone': profile.phone, 'email': profile.email, 'branchId': profile.branchId, 'dashData': {'branches': branch.count(), 'vehicles': vehicle.count(), 'customers': customer.count(), 'employes': employes.count(), 'transporters': transporter.count()}}
        return jsonify(data), 200
    return jsonify({'message': 'User not found'}), 403


#  pages_perpage = 100
#     page = 1
#     profile = Users.query.filter_by().order_by(
#         Users.created.desc()).paginate(int(page), pages_perpage, error_out=False)
#     if profile:
#        data = [*map(users_serializer, profile.items)]
#        return {'data': data, "pagination": {"currentpage": profile.page, "totalPages": profile.pages, "totalusers": profile.total, "prev_page": profile.prev_num, "next_page": profile.next_num, "has_next": profile.has_next, "has_prev": profile.has_prev}}
#     return jsonify({'message' : 'Users not found'}),403

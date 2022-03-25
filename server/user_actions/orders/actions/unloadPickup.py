# from flask_sqlalchemy import model
# from jwt import exceptions
# from server.models import Item, Order
# from flask import jsonify


# def unloadloadPickup(itemid, data, db):
#     unloadunits = data['unloadunits']
#     unloadnote = data['unloadnote']
#     orderid = data['orderid']

# #  todo check if order has all items picked.

#     order = Order.query.filter_by(orderid=orderid).first()
#     item = Item.query.filter_by(itemid=itemid).first()
#     if order:
#         if Item:
#             try:
#                 if unloadunits:
#                     item.unloadunits = unloadunits

#                 if unloadnote:
#                     item.unloadnote = unloadnote

#                 order.pickupUnloaded = True
#                 order.orderStatus = 'Unloaded'
#                 db.session.add(order)
#                 item.pickupUnloaded = True
#                 item.status = 'Unloaded'
#                 db.session.add(item)
#                 db.session.commit()
#                 return jsonify({'message': 'item picked and unloaded'}), 200

#             except Exception as e:
#                 print(e)
#                 return jsonify({'message': 'Failed to unload item'}), 403
#                 pass

#     return jsonify({'message': 'item does not exist!'}), 409



from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Item, Order
from flask import jsonify


def unloadloadPickup(orderid, data, db):
    items =data['items']
    orderid = data['orderid']

#  todo check if order has all items picked.
    order = Order.query.filter_by(orderid=orderid).first()
    if order:
        for item in items:
            unloadnote = item['unloadnote']
            itemrow = Item.query.filter_by(itemid=item['itemid']).first()
            if itemrow:
                try:
                                           
                        if unloadnote:
                            item.unloadnote = unloadnote

                        order.pickupUnloaded = True
                        order.orderStatus = 'Unloaded'
                        db.session.add(order)
                        itemrow.pickupUnloaded = True
                        itemrow.status = 'Unloaded'
                        db.session.add(itemrow)
                        db.session.commit()
                        print('ooooooooooooooooooooo')

                except Exception as e:
                    print(e)
                    return jsonify({'message': 'Failed to load item'}), 403
                    pass
        return jsonify({'message': 'item picked and unloaded'}), 200
    return jsonify({'message': 'order does not exist!'}), 409

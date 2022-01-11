from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Order
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash
# from datetime import timezone
import datetime
import time


  
# ts stores the time in seconds
ts = time.time()
  
# print the current timestamp


def createOder(data, db):    
    id = uuid.uuid4()  # todo ........... to be return to the setter and getter
    consignerdata=data['consignerdata']
    customerdata = data['customerData']
    customername=customerdata['customername']   
    customerid = customerdata['customerId']
    customernotes = data['custnote']
    consignername = consignerdata['cfname']+consignerdata['clname']
    consignerid = consignerdata['consignerid']
    pregion = data['packageRegionData']
    pdistrict = data['Packagedistdata']
    pstreet = data['packagestreet']
    pnotes = data['packagenotes']
    dregion = data['destinationRegionData']
    ddistrict = data['destinationData']
    dstreet = data['destinationstreet']
    dnotes = data['destinationnotes']
    consigneename = data['consigneename']
    pickuptime = data['pickuptime']
    expdlrtime = data['expdlrtime']
    
 
    # date_time_obj = datetime.datetime.strptime(pickuptime, '%b %d %Y %I:%M%p')

    orderid='sga-'+pregion+'-'+'-'+dregion+str(ts).lower()
   #  check if user exists
    order = Order.query.filter_by(orderid=orderid).first()
    if not order:
     try:
        # print('Date:...........', date_time_obj)
        # print('Time:', date_time_obj.time())
        # print('Date-time:', date_time_obj)
        neworder = Order(orderid =orderid,
         customerid = customerid,
         customername = customername,
         customernotes = customernotes,
         consignername = consignername,
         consignerid = consignerid,
         pregion = pregion,
         pdistrict = pdistrict,
         pstreet = pstreet,
         pnotes = pnotes,
         dregion = dregion,
         ddistrict = ddistrict,
         dstreet = dstreet,
         dnotes = dnotes,
         consigneename = consigneename,
         pickuptime = pickuptime,
         expdlrtime = expdlrtime)
        # ...................add()
        db.session.add(neworder)
        db.session.commit()
        return jsonify({'message': 'Order created'}), 200

     except Exception as e:
      print(e)
      return jsonify({'message': 'Failed to create Order'}), 403
      pass
    return jsonify({'message': 'Order already exist'}), 409
 
 
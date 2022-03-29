import requests
import json
import json
import os
import uuid

from server.models import SMSLog


# TANZANIA.AIRTEL.RELAY
# TANZANIA.VODACOM.RELAY
# TANZANIA.TIGO.RELAY
# TANZANIA.HALOTEL.RELAY

def sendSMSSecond():

    url = "http://213.10.81.136:9898/sms?"

    response = requests.get(url)

    print("JSON Response ", response)


def sendSMS(msisdn, message, type, db):

    try:
        URL = os.environ.get('SMS_POST_URL')
        api_key = os.environ.get('SMS_API_KEY')
        secret_key = os.environ.get('SMS_SECRET_KEY')
        content_type = os.environ.get('SMS_CONTENT_TYPE')
        source_addr = os.environ.get('SMS_SOURCE_ADDR')

        apikey_and_apisecret = api_key + ':' + secret_key

        headers_data = {
            "Content-Type": content_type,
            "Authorization": 'Basic ' + api_key + ':' + secret_key,
        }

        data = {
            "source_addr": source_addr,
            "schedule_time": "",
            "encoding": "0",
            "message": message,
            "recipients": [
                {
                    "recipient_id": 1,
                    "dest_addr": str(msisdn),
                }
            ]
        }

        request = requests.post(url=URL, data=json.dumps(
            data), headers=headers_data, auth=(api_key, secret_key), verify=False)

        response = request.json()

        if ((request.status_code == 200) and ((response['code'] == 100) and (response['successful'] == True))):
            
            smsLog = SMSLog(smsid=uuid.uuid4(),
                               destination=msisdn,
                               message=message,
                               type=type)
            
            # ...................add()
            db.session.add(smsLog)
            db.session.commit()
            
            return (request.json())

    except Exception as e:
        print(e.with_traceback)
        pass

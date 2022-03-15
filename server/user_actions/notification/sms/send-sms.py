import requests
import json
import json


# TANZANIA.AIRTEL.RELAY
# TANZANIA.VODACOM.RELAY
# TANZANIA.TIGO.RELAY
# TANZANIA.HALOTEL.RELAY

def sendSMSSecond():

    url = "http://213.10.81.136:9898/sms?"

    response = requests.get(url)
    
    
    print("JSON Response ", response)

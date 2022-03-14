import requests
import json


# TANZANIA.AIRTEL.RELAY
# TANZANIA.VODACOM.RELAY
# TANZANIA.TIGO.RELAY
# TANZANIA.HALOTEL.RELAY

def sendSMS(msisdn, content):

    headers = {
        'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }

    url = "http://213.136.80.136:9090/"

    query = {
        'message': 'MESSAGECONTENT',
        'msisdn': 'PHONENUMBER',
        'channel': 'ROUTE',
        'shortcode': 'CLIENT-SENDER-ID',
        'reference': 'UNIQUEUMESSAGEID',
        'request_dlr': 'TRUE/FALSE',
        'username': 'CLIENT-USERNAME',
        'password': 'CLIENT-PASSWORD'
    }

    response = requests.post(url, headers=headers, json=query)
    json_response = json.loads(response)

    if json_response['error_code'] and json_response['description']:
        print("SMS Sent Successfull")

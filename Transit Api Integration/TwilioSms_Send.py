# -*- coding: utf-8 -*-
from twilio.rest import Client
import json
import logging 
from flask import Flask

logger = logging.getLogger(__name__)
hdlr = logging.FileHandler('myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)
app = Flask(__name__)
log = logging.getLogger(__name__)

class TwilioSms_Send:
    
    cofig_file = open("config.json").read()
    global config_json
    config_json = json.loads(cofig_file)
    
    def twilio_sendSms(sms_to, sms_from, sms_body):
    
        # Your Account SID from twilio.com/console
        account_sid = config_json['twilio']['accountid']
        # Your Auth Token from twilio.com/console
        auth_token  = config_json['twilio']['auth_token']
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to= sms_to, 
            from_= sms_from,
            body= sms_body)
        
        print(message.sid)
#        print('To:', sms_to, '\n From:',sms_from, '/n Sms Body:', sms_body, '/n account_sid:', account_sid, '/n auth_token:', auth_token)

       
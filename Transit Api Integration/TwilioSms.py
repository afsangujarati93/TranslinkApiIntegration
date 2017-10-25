# -*- coding: utf-8 -*-
from twilio.rest import Client
from TransApi_GetSchedule import TransApi_GetSchedule
import json

class TwilioSms:
    
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

    def getSchedule_StopRouteNum():
        
        stop_number = input("Enter the stop number?\n")
        route_number = input("Enter route number for timings\n")       
        
        schedules = TransApi_GetSchedule.main_getScheduleResponse(stop_number, route_number)
        sms_body = "Following is the schedule for " + stop_number + " and route number " + route_number + "\nFollowing is the latest schedule for your request: \n" + "\n".join(schedules)
    
        return sms_body      
       
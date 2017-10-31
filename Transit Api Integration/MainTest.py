# -*- coding: utf-8 -*-
from TwilioSms import TwilioSms

class Main_test:
    sms_body = TwilioSms.getSchedule_StopRouteNum() 
    TwilioSms.twilio_sendSms('+19027041235','+15878033028',sms_body)

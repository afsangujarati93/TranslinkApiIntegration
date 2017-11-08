# -*- coding: utf-8 -*-
from TwilioSms_Send import TwilioSms_Send

class Main_test:
#    sms_body = TwilioSms_Send.getSchedule_StopRouteNum() 
    print('Hello World')    
    route_part = 'route 1234'
    print(route_part)
    stop_part = 'stop 99'
    print(stop_part)
    route_num = (route_part.replace('route','')).strip()
    print(route_num)
    stop_num = (stop_part.replace('stop','')).strip()
    print(stop_num)
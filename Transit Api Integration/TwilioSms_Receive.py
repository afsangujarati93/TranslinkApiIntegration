# -*- coding: utf-8 -*-
from twilio.twiml.messaging_response import MessagingResponse
from TwilioSms_Send import TwilioSms_Send
import sys
#from Log_Handler import Log_Handler as lh
from TransApi_GetSchedule import TransApi_GetSchedule

#logger = lh.log_initializer()
def ReceivedSms(request_form, received_from_num, received_to_num, mess_body):
    try:
        """Respond to incoming calls with a simple text message."""
        print("Before messaging post 1" + str(request_form))
        print("Body and from number and To num. \nFrom:" + received_from_num + "\nTo:" + received_to_num + "\nBody:" + mess_body)
        #logger.debug("Before messaging post 1" + str(request_form))
        #logger.debug("Body and from number and To num. \nFrom:" + received_from_num + "\nTo:" + received_to_num + "\nBody:" + mess_body)

#        make all string lower case
        has_route = 'route' in mess_body
        has_stop = 'stop' in mess_body
        if not (has_route and has_stop):
            resp = MessagingResponse()
            resp.message("Invalid text input. Please make sure you have send <b>route</b> and <b>stop</b> in your text")
        else:
            index_stop = mess_body.index('stop')
            route_part = mess_body[:index_stop]
            stop_part= mess_body[index_stop:]
            print("Route Part:" + route_part + "|stop_part:" + stop_part)
            #logger.debug("Route Part:" + route_part + "|stop_part:" + stop_part)
            route_num = (route_part.replace('route','')).strip()
            stop_num = (stop_part.replace('stop','')).strip()
             
            print("Route Num:" + route_num + "|Stop Num:" + stop_num)
            #logger.debug("Route Num:" + route_num + "|Stop Num:" + stop_num)
            schedules = TransApi_GetSchedule.getSchedule_StopRouteNum(route_num, stop_num)
            print('schedules:' + schedules)
            #logger.debug('schedules:' + schedules)
            resp = MessagingResponse()
            resp.message(schedules)
      
      	print("Before return response")
        #logger.debug("Before return response")
        return str(resp)
    except:
#        imrpove exception handling
        print("Exception occurred while Receving or Sending SMS request ", sys.exc_info()[0])
        #logger.debug("Exception occurred while Receving or Sending SMS request ", sys.exc_info()[0])

    return str(resp)

# -*- coding: utf-8 -*-
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, Gather
#from Log_Handler import Log_Handler as lh

app = Flask(__name__)
#logger = lh.log_initializer()

def ReceivedCallManage(counter):    
    if counter == 1:
        print("Main 1st method| counter" + str(counter))
        #logger.debug("Main 1st method| counter" + str(counter))
        resp = ReceivedRouteCall(counter)
    elif counter == 2: 
        print("Main 2nd method| counter" + str(counter))
        #logger.debug("Main 2nd method| counter" + str(counter))
        resp = ReceivedStopCall(counter)
    return resp

def ReceivedRouteCall(counter):
    """Respond to incoming requests."""
    resp = VoiceResponse()
    resp.say("Hello Monkey",  voice='alice')
    # Say a command, and listen for the caller to press a key. When they press
    # a key, redirect them to /RecordInputSchedule.
    print('Starting call receiving process|name:' + __name__ )
    #logger.debug('Starting call receiving process|name:' + __name__ )
    route_num = Gather(action="/RecordInputSchedule?counter=" + str(counter), method="GET", input = "DTMF Speech")    
    route_num.say("Please press or say the route number, followed by # key",  voice='alice')
    resp.append(route_num)
    print("Before return in route call")
    #logger.debug("Before return in route call")    
    return str(resp)

def ReceivedStopCall(counter):
    """Respond to incoming requests."""
    resp = VoiceResponse()
    resp.say("Hello Monkey",  voice='alice')
    print("Inside Received Stop Call method")
    #logger.debug("Inside Received Stop Call method")
    stop_num = Gather(action="/RecordInputSchedule?counter=" + str(counter), method="GET", input = "DTMF Speech")   
    stop_num.say("Please press or say the stop number, followed by # key",  voice='alice')
    resp.append(stop_num)
    return str(resp)
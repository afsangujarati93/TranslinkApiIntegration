# -*- coding: utf-8 -*-
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, Gather
from Log_Handler import Log_Handler as lh

app = Flask(__name__)
logger = lh.log_initializer()

def ReceivedRouteCall():
    """Respond to incoming requests."""
    resp = VoiceResponse()
    resp.say("Hello Monkey",  voice='alice')    
    # Say a command, and listen for the caller to press a key. When they press
    # a key, redirect them to /RecordInputSchedule.
    logger.debug('Starting call receiving process|name:' + __name__ )
    route_num = Gather(action="/RecordInputSchedule", method="POST", input = "DTMF Speech")    
    route_num.say("Please press or say the route number, followed by # key",  voice='alice')
    resp.append(route_num)
    logger.debug("Before return in route call")    
    return str(resp)

def ReceivedStopCall():
    """Respond to incoming requests."""
    resp = VoiceResponse()
    resp.say("Hello Monkey",  voice='alice')
    logger.debug("Inside Received Stop Call method")
    stop_num = Gather(action="/RecordInputSchedule", method="POST", input = "DTMF Speech")   
    stop_num.say("Please press or say the stop number, followed by # key",  voice='alice')
    resp.append(stop_num)
    return str(resp)
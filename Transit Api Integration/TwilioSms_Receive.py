# -*- coding: utf-8 -*-
from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
from TwilioSms_Send import TwilioSms_Send
from flask import request
import logging 


logger = logging.getLogger(__name__)
hdlr = logging.FileHandler('myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)
app = Flask(__name__)
log = logging.getLogger(__name__)

@app.route("/", methods=['GET', 'POST'])
def RecivedSMS():
    """Respond to incoming calls with a simple text message."""
    logger.debug("Before post")
    if request.method == 'POST':
        logger.debug("Inside post 1")
#        request_values = request.values
#        request_args = request.args
        request_form = request.form
        received_from_num = request.form["From"]
        received_to_num = request.form["To"]
        mess_body = request.form["Body"]
       
        logger.debug("Before messaging post 1" + str(request_form))
        logger.debug("Body and from number and To num. \nFrom:" + received_from_num + "\nTo:" + received_to_num + "\nBody:" + mess_body)
#        resp = MessagingResponse()        
#        resp.message("Hello, Mobile Monkey POST")    
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
            logger.debug("Route Part:" + route_part + "|stop_part:" + stop_part)
            route_num = ''
            stop_num = ''
            
            schedules = TwilioSms_Send.getSchedule_StopRouteNum(route_num, stop_num)
            resp = MessagingResponse()
            resp.message(schedules)
    else:
        resp = MessagingResponse()
        resp.message("Invalid request received from server")  
    logger.debug("Before return response")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)


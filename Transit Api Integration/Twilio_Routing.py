# -*- coding: utf-8 -*-
from flask import Flask, redirect
from twilio.twiml.voice_response import VoiceResponse
import TwilioSms_Receive as tsr
import TwilioCall_Receive as tcr
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from Log_Handler import Log_Handler as lh
from TransApi_GetSchedule import TransApi_GetSchedule

app = Flask(__name__)
logger = lh.log_initializer()
counter = 1
route_num = 0
stop_num= 0

@app.route("/SmsResponse", methods=['GET', 'POST'])
def RecivedSms():
    if request.method == 'POST':
        request_form = request.form
        received_from_num = request.form["From"]
        received_to_num = request.form["To"]
        mess_body = request.form["Body"]
        resp = tsr.ReceivedSms(request_form, received_from_num, received_to_num, mess_body)
    else:
        resp = MessagingResponse()
        resp.message("Invalid request received from server")
    return str(resp)

@app.route("/CallResponse", methods=['GET', 'POST'])
def ReceivedCall():
    """Respond to incoming requests."""
    logger.debug("Starting ReceivedCall flow| name:" + __name__)
    if counter == 1:
        logger.debug("Main 1st method| counter" + str(counter))
        resp = tcr.ReceivedRouteCall()
    elif counter == 2: 
        logger.debug("Main 2nd method| counter" + str(counter))
        resp = tcr.ReceivedStopCall()   
    return str(resp)

@app.route("/RecordInputSchedule", methods=['GET', 'POST'])
def UserInputSchedule():
    global counter
    global stop_num
    global route_num
    isDigit = True
    """Handle key press from a user."""
    # Get the digit pressed by the user
    logger.debug('before considering user input in route|')
    
    digit_val = request.values.get('Digits', None)
    logger.debug("request Form" + str(request.form))
    if not digit_val:
        isDigit = False
    logger.debug("isDigit:" + str(isDigit))
    resp = VoiceResponse()
    if counter == 1:
        if isDigit:
            route_num = request.values.get('Digits', None)
            logger.debug("User first digit input:" +  str(route_num))
        else:
            route_num = request.values['SpeechResult']
#            route_num = request.values.get('SpeechResult', None)
            logger.debug("User first speech input:" +  str(route_num) + "| has digit: " + str(route_num.isdigit()))
            if not route_num.isdigit():
                resp = VoiceResponse()
                resp.say("Invalid route number. Please press or say a proper route number",  voice='alice')
                return redirect("/CallResponse")       
        counter += 1
        return redirect("/CallResponse")
    elif counter == 2:
        if isDigit:
            stop_num = request.values.get('Digits', None)
        else:
            stop_num = request.values['SpeechResult']
            logger.debug("User second speech input:" +  str(stop_num) + "| has digit: " + str(stop_num.isdigit()))
            if not stop_num.isdigit():
                resp = VoiceResponse()
                resp.say("Invalid stop number. Please press or say a proper route number", voice='alice')
                return redirect("/CallResponse")  
        resp.say("Fetching schedules for route number:" + str(route_num) + "and stop number:" + str(stop_num), voice='alice')
        schedules = TransApi_GetSchedule.getSchedule_StopRouteNum(route_num, stop_num)
        logger.debug('before replace schedules:' + schedules)
#        schedules.replace("\n", "...........")
        schedules = " .................................... ".join(schedules.splitlines())
        logger.debug('after replace schedules:' + schedules)
       
        resp.say(schedules,  voice='alice')
        resp.pause()
        resp.hangup()
        return str(resp)     


if __name__ == "__main__":
#    logger.debug("In routing main")
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)

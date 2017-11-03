# -*- coding: utf-8 -*-
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
import TwilioSms_Receive as tsr
import TwilioCall_Receive as tcr
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from Log_Handler import Log_Handler as lh

app = Flask(__name__)
logger = lh.log_initializer()

@app.route("/SmsResponse", methods=['GET', 'POST'])
def RecivedSMS():
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
def hello_monkey():
    """Respond to incoming requests."""
    resp = tcr.hello_monkey()
    return str(resp)

if __name__ == "__main__":
    logger.debug("In routing main")
    app.run(debug=True, host='0.0.0.0', port=80)

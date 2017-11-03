# -*- coding: utf-8 -*-
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
import logging

logger = logging.getLogger(__name__)
hdlr = logging.FileHandler('myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)
#app = Flask(__name__)
log = logging.getLogger(__name__)

#@app.route("/CallResponse", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = VoiceResponse()
    resp.say("Hello Monkey")

    return str(resp)

#if __name__ == "__main__":
#    logger.debug("In call main")
#    app.run(debug=True, host='0.0.0.0', port=80)

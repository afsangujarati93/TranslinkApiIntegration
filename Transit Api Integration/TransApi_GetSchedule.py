# -*- coding: utf-8 -*-
import requests
from xml.etree import ElementTree
import logging 
from flask import Flask
import json

logger = logging.getLogger(__name__)
hdlr = logging.FileHandler('myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)
app = Flask(__name__)
log = logging.getLogger(__name__)

class TransApi_GetSchedule:
    
    cofig_file = open("config.json").read()
    global config_json
    config_json = json.loads(cofig_file)    
    #a method is contained inside a class
    #a function is what that is independent of a class
    def main_getScheduleResponse(stop_number, route_number): 
        api_key = config_json['TranslinkApi']['apiKey']
        logger.debug('Inside Main Schedule Response')
        str_url = "http://api.translink.ca/rttiapi/v1/stops/{0}/estimates?apikey={1}&count=3&timeframe=120"
        str_url = str_url.replace("{0}",stop_number)        
        str_url = str_url.replace("{1}",api_key)        
        logger.debug('Before getting data:' + str_url)
        resp = requests.get(str_url)
        
        if resp.status_code != 200:
            # This means something went wrong.
            raise Exception('Invalid response from web service')            
            logger.debug('After getting data:' + resp.content + '|code' + resp.status_code)
        logger.debug("Before parsing:")
        schedules = TransApi_GetSchedule.parse_getSchduleResponse(resp.content, route_number)        
        logger.debug('After Parsing')
        return schedules
            
    
    def parse_getSchduleResponse(api_content,route_number):
        getapi_response = ElementTree.fromstring(api_content)
        expected_leave_time = []
        for childtags in getapi_response:
            route_num = childtags.find("RouteNo").text            
            if route_num == route_number:
                schedules_main_list = childtags.find("Schedules")
                schedules_list = schedules_main_list.findall("Schedule")
                for perschedule in schedules_list:
                    expected_leave_time.append("\n" + perschedule.find('ExpectedLeaveTime').text)
        return expected_leave_time
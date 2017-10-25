# -*- coding: utf-8 -*-
import requests
from xml.etree import ElementTree

class TransApi_GetSchedule:
        
    #a method is contained inside a class
    #a function is what that is independent of a class
    def main_getScheduleResponse(stop_number, route_number):        
        str_url = "http://api.translink.ca/rttiapi/v1/stops/{0}/estimates?apikey=gIGALlFYjoUiOcz0A7xD&count=3&timeframe=120"
        str_url = str_url.replace("{0}",stop_number)        
        resp = requests.get(str_url)
        if resp.status_code != 200:
            # This means something went wrong.
            raise Exception('Invalid response from web service')            
        schedules = TransApi_GetSchedule.parse_getSchduleResponse(resp.content, route_number)        
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
                    expected_leave_time.append(perschedule.find('ExpectedLeaveTime').text)
        return expected_leave_time
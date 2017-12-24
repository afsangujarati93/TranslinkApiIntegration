# -*- coding: utf-8 -*-
import requests
from xml.etree import ElementTree
import json
#from Log_Handler import Log_Handler as lh

#logger = lh.log_initializer()

class TransApi_GetSchedule:
    
    cofig_file = open("config.json").read()
    global config_json
    config_json = json.loads(cofig_file)       
    #a method is contained inside a class
    #a function is what that is independent of a class
    #so main_get.... is a method
    def main_getScheduleResponse(stop_number, route_number): 
        return_list = []
        api_key = config_json['TranslinkApi']['apiKey']
        print('Inside Main Schedule Response')
        #logger.debug('Inside Main Schedule Response')
        str_url = "http://api.translink.ca/rttiapi/v1/stops/{0}/estimates?apikey={1}&count=3&timeframe=120"
        str_url = str_url.replace("{0}",stop_number)        
        str_url = str_url.replace("{1}",api_key)        
        print('Before getting data:' + str_url)
        #logger.debug('Before getting data:' + str_url)
        resp = requests.get(str_url)
        
        if resp.status_code != 200:
            # This means something went wrong.
#            raise Exception('Invalid response from web service')            
            schedules = "Unable to fetch schedules for the given route and stop number. Please check the route and stop number and retry."
            print('After getting data:' + str(resp.content) + '|code' + str(resp.status_code))
            #logger.debug('After getting data:' + str(resp.content) + '|code' + str(resp.status_code))
            return_list.append(schedules)
            return_list.append(False)
            return return_list
        print("Before parsing:")
        #logger.debug("Before parsing:")
        schedules = TransApi_GetSchedule.parse_getSchduleResponse(resp.content, route_number)        
        print('After Parsing')
        #logger.debug('After Parsing')
        if not schedules:
            schedules = "Unable to fetch schedules for the given route and stop number. Please check the route and stop number and retry."
            return_list.append(schedules)
            return_list.append(False)
        else:
            return_list.append(schedules)
            return_list.append(True)
        return return_list
            
    
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
    
    
    def getSchedule_StopRouteNum(route_num, stop_num):
        print('Inside Schdule Get Method')
        #logger.debug('Inside Schdule Get Method')
        return_list = TransApi_GetSchedule.main_getScheduleResponse(stop_num, route_num)
        if return_list[1]:
            schedule_detail = "Following is the schedule for " + stop_num + " and route number " + route_num + "\nThe latest schedule for your request: \n" + "\n".join(return_list[0])
            schedule_detail += "\nWith Love From GJ"
        else:
            schedule_detail = return_list[0]  
        print('After schdules:' + schedule_detail)
        #logger.debug('After schdules:' + schedule_detail)
        return schedule_detail   
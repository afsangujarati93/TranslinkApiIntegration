# -*- coding: utf-8 -*-
import requests
from xml.etree import ElementTree

stop_number = input("Enter the stop number?\n")
route_number = input("Enter route number for timings\n")

str_url = "http://api.translink.ca/rttiapi/v1/stops/{0}/estimates?apikey=gIGALlFYjoUiOcz0A7xD&count=3&timeframe=120"
str_url = str_url.replace("{0}",stop_number)

resp = requests.get(str_url)
if resp.status_code != 200:
    # This means something went wrong.
    raise Exception('Invalid response from web service')

getapi_response = ElementTree.fromstring(resp.content)

expected_leave_time = []
for childtags in getapi_response:
    route_num = childtags.find("RouteNo").text
    print ('Tag', route_num)
    if route_num == route_number:
        schedules_main_list = childtags.find("Schedules")
        schedules_list = schedules_main_list.findall("Schedule")
        for perschedule in schedules_list:
            expected_leave_time.append(perschedule.find('ExpectedLeaveTime').text)    
        

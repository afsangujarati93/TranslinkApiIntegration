# TranslinkApiIntegration

# Project Title

Creating a project to integrate the translink Api that would fetch the schedule of bus on basis of the stop and route number passed to the program. The schedules can be fetched either through the sending a text or calling the designated number. 

## Getting Started

*Shift+right click in the folder of ngrok.exe and type the command "ngrok.exe http 80". This will run host your app on port 80.
*Go to the url http://localhost:4040/status and copy the URL which would be required to configure twilio's programmable sms and calling
*Paste the url at https://www.twilio.com/console/phone-numbers/incoming followed by the method name. (/CallResponse for voice and /SmsResponse for messages
*Run the Twilio_Routing.py to start the app and start making calls and sms to your twilio number. 


### Prerequisites

Download and Install the ngrok.exe from https://ngrok.com/download for your respective os. Make sure you have the twilio library installed for python. A detailed guide on how to install and run twilio apps is given on twilios official website.
Refer this for more details: https://www.twilio.com/docs/guides/how-to-set-up-your-python-and-flask-development-environment#choose-a-python-version.
Having postman to make api calls is easier and convenient. 
I would also recommend you to sign up for a textnow number to work with your trail twilio app. 


## Deployment

Follow the steps mentioned in Gettings Started for deploying it on local environment.

## Built With

* [twilio](https://www.twilio.com/docs/) - Apis for intergrating sms and call features
* [python](https://www.python.org/downloads/) - Programming langauge


## Authors

* **Afsan Gujarati** - *Initial work*

## Acknowledgments

* Cheers to the twilios documentation team for the wonderful step by step guide for setting up the development environment
* stackoverflow and google for their all time services


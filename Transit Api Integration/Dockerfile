#FROM gcr.io/google-appengine/python
#LABEL python_version=python3.6
#RUN virtualenv --no-download /env -p python3.6
#
## Set virtualenv environment variables. This is equivalent to running
## source /env/bin/activate
#ENV VIRTUAL_ENV /env
#ENV PATH /env/bin:$PATH
#
## Copy the application's requirements.txt and run pip to install all
## dependencies into the virtualenv.
#ADD requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#
#ADD . /app/
#
#EXPOSE 80
##CMD ["Twilio_Routing.py", "--host=0.0.0.0", "."]
##CMD gunicorn -b :$PORT main:app
#ENTRYPOINT [ "python", "Twilio_Routing.py"]
#CMD ["gunicorn", "-b","80"]

FROM python:3.6-alpine3.6 

# dependencies into the virtualenv.
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD . /app
WORKDIR /app


CMD [ "python","Twilio_Routing.py"]
EXPOSE 8080
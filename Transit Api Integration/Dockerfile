FROM gcr.io/google-appengine/python
LABEL python_version=python3.6
RUN virtualenv --no-download /env -p python3.6

# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Copy the application's requirements.txt and run pip to install all
# dependencies into the virtualenv.
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD . /app/

#CMD gunicorn -b :$PORT main:app
ENTRYPOINT [ "python", "Twilio_Routing.py" ]
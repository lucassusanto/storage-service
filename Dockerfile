# our base image
FROM alpine

# Install python and pip
RUN apk update && apk add musl linux-headers build-base py2-pip gcc python-dev libffi-dev libevent-dev

# upgrade pip
RUN pip install --upgrade pip

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY *.py /usr/src/app/

# tell the port number the container should expose
EXPOSE 5000
WORKDIR /usr/src/app

# run the application
CMD ["python", "/usr/src/app/main.py"]

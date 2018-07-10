# Build out application
FROM ubuntu:16.04
# Install python 3.5
RUN apt-get update
RUN apt-get install -y apt-utils python3-dev python3 python3-pip

# Install python
RUN ln /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip python3-tk
RUN ln /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip

# Install requirements
WORKDIR /app
ADD ./requirements.txt requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy application to image
COPY . /app

# Run flask app
ENTRYPOINT ["python"]
CMD ["app.py"]

# download the latest python alpine image
FROM python:3.8-alpine

# set the working directory in the container
WORKDIR /AUTH-USERPROFILE-SERVICE

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . /AUTH-USERPROFILE-SERVICE

# command to run on container start
CMD flask run --host=0.0.0.0

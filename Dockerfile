FROM python:3.11.3-alpine3.17

# setup environment variable  
ENV DockerHOME=/app

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME 

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
&& apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
pango libffi \
gtk+3.0 glib-dev \
&& apk add py3-pip gcc musl-dev python3-dev pango zlib-dev jpeg-dev openjpeg-dev g++ libffi-dev \
&& apk add --no-cache freetype-dev \
&& pip install --upgrade pip 

# copy whole project to your docker home directory. 
COPY . $DockerHOME  
COPY ./manage.py $DockerHOME

# run this command to install all dependencies  
RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
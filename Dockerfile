FROM python:3.10.6-alpine3.16

ENV DockerHOME=/app

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
&& apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
&& apk add --no-cache freetype-dev \
&& apk add --no-cache mariadb-connector-c-dev \
&& apk add --no-cache build-base \
&& pip install --upgrade pip 

COPY . $DockerHOME
COPY ./manage.py $DockerHOME

RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
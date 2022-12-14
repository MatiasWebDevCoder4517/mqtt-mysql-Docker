# FROM python:3.6.11
FROM python:3.6.11-alpine3.11
ARG MYSQL_SERVER
ARG POSTGRES_SERVER
ENV ENVTYPE=local

ENV PATH /compose/bin:$PATH

ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

RUN apk update && apk add --no-cache bash
ADD /compose/scripts.sh $APP_HOME
ADD /requirements/$ENVTYPE.txt $APP_HOME
RUN chmod +x scripts.sh
COPY /src/ $APP_HOME

RUN ./scripts.sh
RUN pip install --upgrade pip
RUN pip install -r /home/app/web/$ENVTYPE.txt; mkdir /log;


CMD ["uvicorn", "main:app", "--proxy-headers", "--reload", "--host", "0.0.0.0", "--port", "8080"]
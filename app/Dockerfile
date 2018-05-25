FROM alvarolizama/python27

ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk upgrade && \
    apk add --no-cache git bash wget

ENV DOCKERIZE_VERSION v0.5.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN pip install --upgrade pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

ADD . /usr/src/app

RUN pip install -e .



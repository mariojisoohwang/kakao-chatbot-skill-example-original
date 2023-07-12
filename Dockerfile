FROM idock.daumkakao.io/chappie/python:3.8.12

ARG WORKERS=4
ARG THREADS=4

RUN apt-get update

ENV APP_HOME=/app
WORKDIR $APP_HOME
RUN mkdir -p $APP_HOME

COPY . $APP_HOME


RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

ENV WORKERS_NUM ${WORKERS}
ENV THREADS_NUM ${THREADS}

EXPOSE 8080

RUN chmod +x docker-entry.sh
ENTRYPOINT ["./docker-entry.sh"]

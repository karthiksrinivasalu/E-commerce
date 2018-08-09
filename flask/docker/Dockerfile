ROM python:3.6-alpine

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app

ENV FLASK_APP weather.py

EXPOSE 80
ENTRYPOINT ["flask", "run"]

FROM python:3.6-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]
EXPOSE 8080
CMD [ "app.py" ]

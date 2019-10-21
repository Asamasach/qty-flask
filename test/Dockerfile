FROM python:3.7-alpine
RUN pip install --upgrade pip
ADD . /code
ADD ./init.sql /docker-entrypoint-initdb.d/
ADD templates/* /code/templates/
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py

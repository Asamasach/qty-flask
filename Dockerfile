FROM python:3.7.1

LABEL Author="@asamasach"
LABEL E-mail="mahdi.sadat@aminsft.com"
LABEL Version="0.0.1b"

ENV PYTHONDONTWRITECODE 1
ENV FLASK_APP "./app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

#RUN yum install -y python-pip python-dev build-essential

RUN mkdir /app
RUN mkdir /app/templates

#COPY Pip* /app/
COPY . /app
COPY ./templates/ /app/templates/
WORKDIR /app


RUN pip3 install --upgrade pip && \
    pip3 install pipenv && \
    pip3 install -r requirements.txt
#    pipenv install --dev --system --deploy --ignore-pipfile


ENTRYPOINT ["python"]
EXPOSE 5000
CMD flask run --host=0.0.0.0

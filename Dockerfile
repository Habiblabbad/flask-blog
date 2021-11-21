FROM python:3.7

ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app

ADD . /app

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile

EXPOSE 8080

CMD python /app/flask-blog/app.py

FROM python:3.8.12-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
ENV LANG C.UTF-8

RUN pip install pipenv \
    psycopg2 \
    gunicorn

WORKDIR /opt/api-deploy

COPY . .

RUN pipenv install --system --skip-lock

CMD gunicorn --workers 4 --bind 0.0.0.0:$PORT wsgi:app --log-level info

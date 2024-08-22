FROM python:3.11-alpine

RUN apk add bash

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV REPORTER_DEBUG='False'
ENV REPORTER_STATIC_ROOT="/static-root"
ENV REPORTER_MEDIA_ROOT="/media-root"
ENV REPORTER_VIRTUAL_HOST="0.0.0.0"
ENV REPORTER_SQLITE3_PATH="/db.sqlite3"
ENV DJANGO_SETTINGS_MODULE="church_reporter.settings.prod"

EXPOSE 8000/

ENTRYPOINT echo Migrating... \
    && python manage.py migrate --no-input \
    && python manage.py collectstatic --no-input \
    && python -m uvicorn --host 0.0.0.0 --port 8000 church_reporter.asgi:application

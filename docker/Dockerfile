FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

# Install build dependencies
RUN apk update && apk add --no-cache \
    build-base \
    gcc \
    libffi-dev \
    musl-dev \
    postgresql-dev

WORKDIR /code

COPY resources/MyChruutundruebli /code/MyChruutundruebli

WORKDIR /code/MyChruutundruebli

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt && \
  chmod +x ./manage.py

# Install nginx
RUN apk add --no-cache nginx

COPY resources/startup.sh /code/MyChruutundruebli
COPY resources/first_startup.txt /code/MyChruutundruebli
COPY resources/cur /etc/nginx/sites-available/default

ENTRYPOINT [ "./startup.sh" ]

EXPOSE 80

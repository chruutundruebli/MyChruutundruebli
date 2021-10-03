FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY resources/MyChruutundruebli /code/MyChruutundruebli

WORKDIR /code/MyChruutundruebli

RUN pip install --upgrade -r requirements.txt && \
  chmod +x ./manage.py

RUN apt update && apt install nginx -y

COPY resources/startup.sh /code/MyChruutundruebli
COPY resources/first_startup.txt /code/MyChruutundruebli
COPY resources/cur /etc/nginx/sites-available/default

ENTRYPOINT [ "./startup.sh" ]

EXPOSE 80
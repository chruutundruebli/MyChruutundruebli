FROM python:3

ENV PYTHONUNBUFFERED=1
ENV JUNTAGRICO_SECRET_KEY="fake-key"
ENV DJANGO_SUPERUSER_PASSWORD="1234"

WORKDIR /code

COPY resources/MyChruutundruebli /code/MyChruutundruebli

WORKDIR /code/MyChruutundruebli

RUN pip install --upgrade -r requirements.txt && \
  chmod +x ./manage.py && \
  ./manage.py migrate && \
  ./manage.py createsuperuser --noinput --username superadmin --email superadmin@localhost && \
  ./manage.py create_member_for_superusers && \
  ./manage.py generate_testdata && \
  ./manage.py collectstatic

RUN apt update && apt install nginx -y

COPY resources/startup.sh /code/MyChruutundruebli
COPY resources/cur /etc/nginx/sites-available/default

ENTRYPOINT [ "./startup.sh" ]

EXPOSE 80
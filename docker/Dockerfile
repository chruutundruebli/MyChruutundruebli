FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libpq-dev \
    build-essential \
    nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY resources/MyChruutundruebli /code/MyChruutundruebli

WORKDIR /code/MyChruutundruebli

# Copy the requirements file
# COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt && \
  chmod +x ./manage.py

# Copy the rest of the resources
COPY resources/startup.sh /code/MyChruutundruebli
COPY resources/first_startup.txt /code/MyChruutundruebli
COPY resources/cur /etc/nginx/sites-available/default

ENTRYPOINT [ "./startup.sh" ]

EXPOSE 80

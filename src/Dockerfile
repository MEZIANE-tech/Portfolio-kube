FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=Portfolio.settings

# Variables fictives juste pour le build
ENV POSTGRES_DB=dummy
ENV POSTGRES_USER=dummy
ENV POSTGRES_PASSWORD=dummy
ENV POSTGRES_HOST=dummy

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput 

EXPOSE 8000

CMD ["gunicorn", "Portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]


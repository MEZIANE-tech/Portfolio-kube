FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=Portfolio.settings

# Variables fictives juste pour le build
ENV SECRET_KEY=dummy-secret-key-for-build-only
ENV DEBUG=False
ENV LOG_LEVEL=INFO
ENV ALLOWED_HOSTS=dummy.com
ENV POSTGRES_HOST=dummy
ENV POSTGRES_DB=dummy
ENV POSTGRES_USER=dummy
ENV POSTGRES_PASSWORD=dummy
ENV EMAIL_HOST=dummy.com
ENV EMAIL_HOST_USER=dummy@dummy.com
ENV EMAIL_HOST_PASSWORD=dummy
ENV RECAPTCHA_PUBLIC_KEY=dummy
ENV RECAPTCHA_PRIVATE_KEY=dummy

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


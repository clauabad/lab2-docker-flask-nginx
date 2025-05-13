FROM python:3.9-slim

## Installer les dépendances système nécessaires à uWSGI et psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

## Définir le dossier de travail
WORKDIR /app

## Copier les dépendances Python
COPY requirements.txt .

## Installer pip et les dépendances Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

## Copier le code de l'application
COPY . .

##  Lancer l'application avec uWSGI
CMD ["uwsgi", "--ini", "uwsgi.ini"]

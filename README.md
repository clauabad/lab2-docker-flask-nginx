# Projet Flask en Production avec PostgreSQL, Nginx, uWSGI et API JSON

Ce projet est une démonstration d'une application Flask moderne mais le vrai objctif est mettre en évidence 
l'utilisation de Docker Compose pour orchestrer plusieurs services interdépendants : 
une **application web Flask**, 
une **base de données PostgreSQL**, 
un **serveur d’application uWSGI**, 
et un **serveur web Nginx**.

L’objectif est de **montrer explicitement les dépendances** entre conteneurs grâce à la directive `depends_on` dans le fichier `docker-compose.yaml`.

---

# Technologies utilisées

- Python 3.9
- Flask
- SQLAlchemy
- PostgreSQL 13
- uWSGI
- Nginx
- Docker / Docker Compose

---

# Structure du projet
flask-nginx-uwsgi/
├── app/
│ ├── init.py # Initialisation de l'app Flask
│ ├── config.py # Configuration globale
│ ├── models.py # Définition des modèles SQLAlchemy
│ ├── routes.py # Routes HTML et API
│ └── templates/
│ └── index.html # Vue Jinja2
├── nginx/
│ └── nginx.conf # Configuration du reverse proxy
├── Dockerfile # Image de l'application Flask
├── docker-compose.yaml # Déploiement multi-conteneurs
├── requirements.txt # Dépendances Python
├── uwsgi.ini # Configuration uWSGI
└── run.py # Point d'entrée de l'app Flask

Client (navigateur)
│
▼
Nginx
│ depends_on: [flask]
▼
uWSGI (serveur Flask)
│ depends_on: [db]
▼
PostgreSQL


- `nginx` dépend du service `flask` pour que le proxy fonctionne.
- `flask` dépend du service `db` (PostgreSQL) pour accéder aux données.

---

## Fichier `docker-compose.yaml` (extrait pertinent)

```yaml
services:
  flask:
    depends_on:
      - db
    ...

  nginx:
    depends_on:
      - flask
    ...

  db:
    ...









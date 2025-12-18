# CFTC – Gestion des Mandatés

Application interne de gestion des mandatés CFTC  
(organismes paritaires et institutionnels en Bretagne)

[![WakaTime](https://wakatime.com/badge/user/EXEMPLE-PERSONNALISE.svg)](https://wakatime.com/@EXEMPLE-PERSONNALISE)  
[![Build Status](https://github.com/UR-CFTC-Bretagne/cftc-mandats/actions/workflows/ci.yml/badge.svg)](https://github.com/UR-CFTC-Bretagne/cftc-mandats/actions)  
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/EXEMPLE-PROJET)](https://www.codacy.com/gh/UR-CFTC-Bretagne/cftc-mandats/dashboard)

---

## Objectifs

- Centraliser les informations des mandatés  
- Suivre les mandats et leurs échéances  
- Faciliter la gouvernance syndicale  
- Assurer la traçabilité administrative

---

## Stack technique

- Python 3.x  
- Django 5.x  
- PostgreSQL  
- uv pour la gestion des dépendances  

---

## Structure du projet

cftc-mandats/
├── uv.lock                 # lock des dépendances uv
├── pyproject.toml
├── backend/                # projet Django principal
│   ├── manage.py
│   ├── config/             # dossier principal (anciennement cftc_mandats)
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── apps/               # apps métiers
│   │   └── user/
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── models.py
│   │       ├── views.py
│   │       ├── urls.py
│   │       └── tests.py
│   ├── tests/              # tests globaux
│   │   └── test_sample.py
│   ├── static/             # fichiers statiques
│   └── templates/          # templates Django et Allauth
│       └── account/
│           ├── login.html
│           ├── signup.html
│           └── logout.html
├── .pre-commit-config.yaml # configuration des hooks pre-commit
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions
├── README.md
└── LICENSE

---

## Installation et environnement

```bash
# Cloner le dépôt
git clone git@github.com:UR-CFTC-Bretagne/cftc-mandats.git
cd cftc-mandats

# Installer uv si nécessaire
pip install uv

# Installer les dépendances et créer l'environnement
uv install

# Créer un superutilisateur Django
uv run python backend/manage.py createsuperuser

# Lancer le serveur
uv run python backend/manage.py runserver

## Contributions

# Vous pouvez contribuer au projet en suivant ces règles :
- Proposez vos modifications directement sur la branche main via une pull request.
- Les administrateurs du dépôt valideront la PR avant toute fusion.
- La CI (tests, linting, formatage, typage) doit passer avant la validation.
- Ne jamais inclure de données réelles des mandatés dans le code ou les tests.



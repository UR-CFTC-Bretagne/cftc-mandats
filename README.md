# CFTC – Gestion des Mandatés

Application interne de gestion des mandatés CFTC  
(organismes paritaires et institutionnels en Bretagne)

[![Build Status](https://github.com/UR-CFTC-Bretagne/cftc-mandats/actions/workflows/ci.yml/badge.svg)](https://github.com/UR-CFTC-Bretagne/cftc-mandats/actions)  

---

## Objectifs

- Centraliser les informations des mandatés  
- Suivre les mandats et leurs échéances  
- Faciliter la gouvernance syndicale  
- Assurer la traçabilité administrative

---

## Stack technique

- Python 3.12  
- Django 6  
- PostgreSQL 15  
- uv pour la gestion des dépendances  

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



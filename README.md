# django-language-school

[![CircleCI](https://circleci.com/gh/pbedn/django-language-school.svg?style=svg)](https://circleci.com/gh/pbedn/django-language-school)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Application for language school management

---

## Setup

Install poetry globally (recommended)
```
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

Create virtual environment manually (recommended)
```
virtualenv path/to/your/venv -p python3
```

Update environmental variables, install dependencies and activate settings
```
cp .env-sample .env # Update the variables on production
poetry install  # use --dev for local
export DJANGO_SETTINGS_MODULE=school.settings.[prod,local]
```

## Run application

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Backend
Settings are split between local and production, and sensitive secrets
should be read from .env file created manually.

Stack: Django 2.1, Python 3.6. 

### Frontend
Frontend is as simple as it can be, just for demo purposes, and not for production.

Stack: Django Templates, Bootstrap 4.

### Deployment
Connected with CircleCI for continuous integration

Stack: CircleCI

# django-language-school

Application for language school management

## Setup

```
cp .env-sample .env # Update the variables on production
pip install -r requirements/[prod,local].txt
export DJANGO_SETTINGS_MODULE=school.settings.[prod,local]
```

## Run application

* Django server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Code

Application written in Python 3.6 and Django 2.1.
Settings are split between local and production, and sensitive secrets
are read from .env file created manually.

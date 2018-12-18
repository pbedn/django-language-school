# django-language-school

Application for language school management

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

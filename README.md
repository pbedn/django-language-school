# django-language-schoo

Application for language school management

## Setup

```
pip install -r doc/requirements/[prod,local].txt
cp school/settings/local.py school/settings/local_settings.py
export DJANGO_SETTINGS_MODULE=school.settings.local_settings
```

## Run application

* Django server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

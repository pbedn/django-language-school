#!/usr/bin/env bash

exec python manage.py dumpdata --indent 2 --exclude=auth --exclude=contenttypes > fixtures/fixtures.json
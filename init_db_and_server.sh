#!/bin/bash

export PGPASSWORD=postgres
psql -h localhost -p 5432 -U postgres -f init_test_db.sql
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

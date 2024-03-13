#!/bin/ash

echo "COLLECT STATIC FILES"
python manage.py collectstatic --noinput

echo "APPLYING MIGRATIONS"
python manage.py makemigrations
python manage.py migrate

exec "$@"
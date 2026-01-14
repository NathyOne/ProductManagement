#!/bin/sh
set -e

# Wait for DB to be ready if DB_HOST is set
if [ -n "$DB_HOST" ]; then
  echo "Waiting for database at $DB_HOST:$DB_PORT..."
  until nc -z $DB_HOST ${DB_PORT:-3306}; do
    sleep 1
  done
fi

# Run migrations then collectstatic
echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting command: $@"
exec "$@"

# Deployment notes

Overview:
- This Django project expects production configuration via environment variables.

Important environment variables:
- `SECRET_KEY` — required for production (no default secure value).
- `DEBUG` — set to `False` in production.
- `ALLOWED_HOSTS` — comma-separated hostnames (e.g. `example.com,www.example.com`).
- `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` — database connection.
- `CORS_ALLOWED_ORIGINS` — comma-separated origins allowed to access the API.

Quick deployment checklist (Ubuntu example):

1) Install system packages and Python venv
```bash
sudo apt update && sudo apt install -y python3-venv python3-dev build-essential libmysqlclient-dev nginx
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2) Configure environment variables (example systemd unit will set these).

3) Collect static files
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

4) Run with Gunicorn (or use systemd + Nginx):
```bash
gunicorn Core.wsgi:application --bind 127.0.0.1:8000 --workers 3
```

5) Configure Nginx as a reverse proxy (example): create `/etc/nginx/sites-available/yoursite` with proxying to `127.0.0.1:8000`, serve static from `/path/to/project/staticfiles`, and enable HTTPS with Certbot.

Security reminders:

Docker usage (local/testing)
----------------------------

This repo includes a `Dockerfile` and `docker-compose.yml` for local containers.

Build and run (will start a MySQL container and the Django web app):

```bash
# build images and start services in background
docker-compose up --build -d

# view logs
docker-compose logs -f web

# to stop and remove containers
docker-compose down -v
```

Notes:
- `docker-compose.yml` runs a MySQL container for local testing. For production prefer a managed DB service and do not expose DB ports publicly.
- Set environment variables in a `.env` file or in your environment before starting compose. Example `.env` values:

```
SECRET_KEY=your-secret
DEBUG=False
DB_NAME=MaterialAndUser
DB_USER=myuser
DB_PASSWORD=strongpassword
MYSQL_ROOT_PASSWORD=rootpassword
ALLOWED_HOSTS=your.domain.com
CORS_ALLOWED_ORIGINS=http://your.frontend.com
```


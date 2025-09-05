# Base Django Project

A minimal Django project template with modern tooling and best practices.

## Features

- Django 5.0+ with Django REST Framework
- PostgreSQL database configuration
- Docker Compose setup with postgres:alpine
- Environment-based configuration with python-dotenv
- Comprehensive logging system (console + file)
- Code formatting and linting with Ruff
- Pre-commit hooks
- UV package manager

## Quick Start

1. **Copy the env.example file to .env and update values:**
   ```bash
   cp env.example .env
   ```

2. **Install dependencies with UV:**
   ```bash
   uv pip install -e .
   uv pip install -e ".[dev]"
   ```

3. **Run with Docker Compose:**
   ```bash
   docker-compose up -d
   ```

4. **Or run locally (ensure PostgreSQL is running):**
   ```bash
   cd app
   python manage.py migrate
   python manage.py runserver
   ```

5. **Install pre-commit hooks (optional):**
   ```bash
   pre-commit install
   ```

## Project Structure

```
base-django/
├── app/                    # Django application code
│   ├── core/              # Django project settings and configuration
│   ├── templates/         # Django templates
│   ├── static/           # Static files
│   ├── media/            # User uploaded files
│   └── manage.py         # Django management script
├── logs/                  # Application logs
├── docker-compose.yml     # Docker services configuration
├── Dockerfile            # Container definition
├── pyproject.toml        # Dependencies and tool configuration
├── .env                  # Environment variables
└── README.md             # Documentation
```

## Development

- **Format code:** `ruff format .`
- **Lint code:** `ruff check .`
- **Run migrations:** `cd app && python manage.py migrate`
- **Create superuser:** `cd app && python manage.py createsuperuser`

## API

- Admin: http://localhost:8000/admin/
- API Root: http://localhost:8000/api/

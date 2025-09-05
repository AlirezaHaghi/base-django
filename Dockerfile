FROM python:3.13-slim

WORKDIR /project

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Create virtual environment
RUN uv venv /opt/venv

# Make sure we use venv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy dependency files
COPY pyproject.toml ./

# Install Python dependencies
RUN uv pip install -e .

# Copy project
COPY . .

# Set working directory to app for Django commands
WORKDIR /project/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Use an official lightweight Python image.
FROM python:3.11.4

# Install poetry
RUN pip install poetry

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock /code/

# Project initialization:
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# We copy just the essentials for the poetry configuration first
COPY . /code/

#!/bin/bash

set -e

# Activate virtual environment (change 'your_virtualenv_name' to the actual name)
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver


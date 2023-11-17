#!/bin/bash

set -e

# Activate virtual environment (change 'your_virtualenv_name' to the actual name)
source venv/bin/activate

# Install requirements
while read requirement; do
    pip install --no-cache-dir --ignore-installed "$requirement" || echo "Failed to install $requirement"
done < requirements.txt


# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver


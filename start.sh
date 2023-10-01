#!/bin/bash

# Check for any new migrations and apply them
echo "Checking for migrations..."
python manage.py makemigrations --no-input
echo "Applying migrations..."
python manage.py migrate --no-input

# Start the Django server
echo "Starting the server..."
python manage.py runserver 0.0.0.0:8000


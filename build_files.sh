#!/bin/bash

# Install dependencies
python3.12 -m pip install -r requirements.txt

# Collect static files
python3.12 manage.py collectstatic --noinput

# Apply database migrations
python3.12 manage.py migrate

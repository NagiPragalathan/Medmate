#!/bin/bash
chmod +x build_files.sh
echo "starting install..."
python3.12 -m pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput
python3.12 manage.py migrate
echo "end install-----------------------"

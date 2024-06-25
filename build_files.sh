echo "starting install..."
pip install -r requirements.txt
python3.12 -m pip install -r requirements.txt
python3.12 manage.py collectstatic
echo "end install-----------------------"
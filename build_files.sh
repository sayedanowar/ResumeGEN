pip install --upgrade pip
pip install -r requirements.txt
echo yes | python3.9 manage.py collectstatic
python3.9 manage.py makemigrations
python3.9 manage.py migrate
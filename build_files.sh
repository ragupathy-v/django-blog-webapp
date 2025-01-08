

which python3 || { echo "Python3 not found"; exit 1; }
which pip3 || { echo "Pip3 not found"; exit 1; }
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput
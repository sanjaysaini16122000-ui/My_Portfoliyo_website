echo "Building the project..."
python3.9 -m pip install -r requirements.txt
python3.9 portfolio/manage.py migrate --noinput
python3.9 portfolio/manage.py collectstatic --noinput --clear
echo "Build complete."

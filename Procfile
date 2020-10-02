release: python manage.py migrate
web: gunicorn placement_exam.wsgi --log-file -
release: python manage.py collectstatic --noinput
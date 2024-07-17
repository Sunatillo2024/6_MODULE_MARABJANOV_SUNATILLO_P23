mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

user:
	python3 manage.py createsuperuser

run:
	python3 manage.py runserver

ap:
	python3 manage.py startapp apps



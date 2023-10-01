Project instalation

1. at first clone my project: git clone https://github.com/giorgibaramidze/sweeft-digital-task.git

2. create .env variable and copy files from .sample-env and generate secret key from https://djecrety.ir/

3. from project directory run command:  docker-compose up -d --build

4. finaly create superuser: docker-compose exec web python manage.py createsuperuser

Done!
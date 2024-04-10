# Указываем базовый образ. Python образы хорошо подходят для многих проектов Python.
FROM python:3.10

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

RUN apt-get update && apt-get install -y gcc libjpeg-dev libpq-dev

RUN pip install --upgrade pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Копируем остальные файлы проекта в рабочую директорию
COPY . .

# Открываем порт, который слушает Django приложение
EXPOSE 8000

# Запускаем миграции и само приложение
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000


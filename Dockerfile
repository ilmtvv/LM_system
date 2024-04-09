# Указываем базовый образ. Python образы хорошо подходят для многих проектов Python.
FROM python:3.10

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем poetry
RUN pip install poetry

# Копируем только файлы poetry.lock и pyproject.toml в рабочую директорию
# для использования кэша зависимостей
COPY pyproject.toml poetry.lock ./

# Отключаем виртуальную среду poetry, так как Docker изолирует среду сам по себе
RUN poetry config virtualenvs.create false

# Устанавливаем зависимости проекта
RUN poetry install --no-interaction --no-ansi

# Копируем остальные файлы проекта в рабочую директорию
COPY . .

# Открываем порт, который слушает Django приложение
EXPOSE 8000

# Запускаем миграции и само приложение
CMD poetry run python manage.py migrate && poetry run python manage.py runserver 0.0.0.0:8000


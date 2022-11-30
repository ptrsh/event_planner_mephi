# Сервис планирования мероприятий
### Проект в рамках проектной практики в МИФИ


## Установка
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/ptrsh/event_planner_mephi
    cd event_planner_mephi
    ```
2. Создайте и активируйте виртуальное окружение:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Установите зависимости:
    ```bash
    pip3 install -r requirements.txt
    ```
4. Cоздайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```
5. Примените миграции:
    ```bash
    python manage.py migrate
    ```

## Запуск сервера
1. Запустите django-сервер:
    ```bash
    python3 manage.py runserver
    ```

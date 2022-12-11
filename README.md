# Сервис планирования мероприятий
### Проект в рамках проектной практики в МИФИ


## Установка
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/ptrsh/event_planner_mephi.git
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
    
4. Примените миграции:
    ```bash
    python3 manage.py migrate
    ```

5. Cоздайте суперпользователя:
    ```bash
    python3 manage.py createsuperuser
    ```
## Запуск через docker

1. 
    ```bash
    docker-compose build
    docker-compose up -d
    ```

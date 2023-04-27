# Проект «Куда пойти»
С помощью сайта можно добавлять интересные места в городе (и не только) на карту.

## Первичная настройка
Для того, чтобы запустить проект локально нужно выполнить следующие действия.

Создать и активировать виртуальное окружение:
```
python -m venv env
source env/bin/activate
```

Для запуска кода у вас уже должен быть установлен Python3.
Используйте в консоли pip для установки зависимостей или pip3, есть есть конфликт с Python2:
```
pip install -r requirements.txt
```
## Переменные окружения
Некоторые чувствительные данные хранятся в настройках окружения, поэтому нужно создать файл .env в корне проекта и прописать там две переменные: `DEBUG` и `SECRET_KEY`.

Пример:
```
SECRET_KEY = 'django-insecure-=1w(-t#(^t$4%i)7q1bz8!)!uk*&2jk-uqw^u*btwz#oki8a$0'
DEBUG = 'True'
```

## Запуск проекта локально

Подготавливаем миграции, прописав в командной строке:
```
python manage.py makemigrations
```
Выполняем миграции:
```
python manage.py migrate
```

Запускаем проект:
```
python manage.py runserver
```

И для того, чтобы в админке можно было добавлять интересные места, нужно создать администратора.
```
python manage.py createsuperuser
```

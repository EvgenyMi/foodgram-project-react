#![S9h4zjvc3sI](https://github.com/EvgenyMi/foodgram-project-react/assets/114211659/5fe1e5a5-13b7-4193-b605-a7f9bf835608)

![r5CFVDPrKsY](https://github.com/EvgenyMi/foodgram-project-react/assets/114211659/11750c33-d536-4d39-9446-d466eb5ef114)

# Проект Продуктовый помощник - Foodgram
### Описание проекта:

"Продуктовый помощник" - это веб-сайт, который предоставляет возможность пользователям публиковать свои собственные рецепты, добавлять рецепты других пользователей в избранное, подписываться на авторов и создавать список покупок для заданных блюд. Этот сервис поможет пользователям находить новые и интересные рецепты, планировать свои покупки и делиться своими кулинарными экспериментами с другими людьми.

### Основные особенности:

- Создан собственный API-сервис на базе фреймворка Django. API предоставляет доступ к функциям приложения, таким как создание и редактирование рецептов, управление списком покупок, подписка на авторов и другие.

- Созданы образы и запущены контейнеры Docker. Docker обеспечивает изолированную среду для запуска приложения и его зависимостей, что упрощает развертывание и масштабирование приложения.

### Инструменты и стек:

- Python: Язык программирования, использованный для разработки бэкенда приложения и взаимодействия с API-сервисами.
- JSON: Формат данных, используемый для обмена информацией с внешними API-сервисами и клиентской частью приложения.
- YAML: Язык разметки, используемый для настройки и конфигурации контейнеров Docker.
- Django: Фреймворк для разработки веб-приложений на языке Python. Используется для создания API-сервиса и обработки запросов от клиентской части приложения.
- API: Интерфейс программирования приложений, используемый для взаимодействия между различными компонентами приложения.
- Docker: Платформа для разработки, доставки и запуска приложений в контейнерах. Облегчает развертывание и управление приложением.
- Nginx: Веб-сервер и обратный прокси, используемый для обслуживания статических файлов и балансировки нагрузки.
- PostgreSQL: Реляционная база данных, используемая для хранения данных приложения.
- Gunicorn: WSGI-сервер (Web Server Gateway Interface), используемый для запуска Python-приложения.
- и прочее...

### Развернуть проект на удаленном сервере:

- Клонировать репозиторий:
```
https://github.com/EvgenyMi/foodgram-project-react.git
```

- Установить на сервере Docker, Docker Compose:

```
sudo apt install curl                                   # установка утилиты для скачивания файлов
curl -fsSL https://get.docker.com -o get-docker.sh      # скачать скрипт для установки
sh get-docker.sh                                        # запуск скрипта
sudo apt-get install docker-compose-plugin              # последняя версия docker compose
```

- Скопировать на сервер файлы docker-compose.yml, nginx.conf из папки infra (команды выполнять находясь в папке infra):

```
scp docker-compose.yml nginx.conf username@IP:/home/username/   # username - имя пользователя на сервере
                                                                # IP - публичный IP сервера
```

- Для работы с GitHub Actions необходимо в репозитории в разделе Secrets > Actions создать переменные окружения:
```
SECRET_KEY              # секретный ключ Django проекта
DOCKER_PASSWORD         # пароль от Docker Hub
DOCKER_USERNAME         # логин Docker Hub
HOST                    # публичный IP сервера
USER                    # имя пользователя на сервере
PASSPHRASE              # *если ssh-ключ защищен паролем
SSH_KEY                 # приватный ssh-ключ
TELEGRAM_TO             # ID телеграм-аккаунта для посылки сообщения
TELEGRAM_TOKEN          # токен бота, посылающего сообщение

DB_ENGINE               # django.db.backends.postgresql
DB_NAME                 # postgres
POSTGRES_USER           # postgres
POSTGRES_PASSWORD       # postgres
DB_HOST                 # db
DB_PORT                 # 5432 (порт по умолчанию)
```

- Создать и запустить контейнеры Docker, выполнить команду на сервере
*(версии команд "docker compose" или "docker-compose" отличаются в зависимости от установленной версии Docker Compose):*
```
sudo docker compose up -d
```

- После успешной сборки выполнить миграции:
```
sudo docker compose exec backend python manage.py migrate
```

- Создать суперпользователя:
```
sudo docker compose exec backend python manage.py createsuperuser
```

- Собрать статику:
```
sudo docker compose exec backend python manage.py collectstatic --noinput
```

- Наполнить базу данных содержимым из файла ingredients.json:
```
sudo docker compose exec backend python manage.py loaddata ingredients.json
```

- Для остановки контейнеров Docker:
```
sudo docker compose down -v      # с их удалением
sudo docker compose stop         # без удаления
```

### После каждого обновления репозитория (push в ветку master) будет происходить:

1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8)
2. Сборка и доставка докер-образов frontend и backend на Docker Hub
3. Разворачивание проекта на удаленном сервере
4. Отправка сообщения в Telegram в случае успеха

### Запуск проекта на локальной машине:

- Клонировать репозиторий:
```
https://github.com/EvgenyMi/foodgram-project-react.git
```

- В директории infra создать файл .env и заполнить своими данными:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY='секретный ключ Django'
```

- Создать и запустить контейнеры Docker, последовательно выполнить команды по созданию миграций, сбору статики, 
созданию суперпользователя, как указано выше.
```
docker-compose -f docker-compose-local.yml up -d
```


- После запуска проект будут доступен по адресу: [http://localhost/](http://localhost/)


- Документация будет доступна по адресу: [http://localhost/api/docs/](http://localhost/api/docs/)

### Над бэкендом проекта работал
- [Минеев Евгений](https://github.com/EvgenyMi)

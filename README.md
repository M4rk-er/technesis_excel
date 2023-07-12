```
Бот Telegram, который имеет возможность принять файл excel с полями :
     a. title - название
     b. url - ссылка на сайт источник
     c. xpath - путь к элементу с ценой
Далее бот сохраняет файл, выводит содержимое пользователю и сохраняет его
в локальную БД sqlite
```

## Для установки:
### 1. Клонировать репозиторий:
```
git@github.com:M4rk-er/excel_saver.git
```
### 2. Перейдите в директорию с проектом и создайте виртуальное окружение
- Windows:
```
cd excel_saver && python -m venv venv && source venv/Scripts/activate
```
- Linux:
```
cd excel_saver && python3 -m venv venv && . venv bin activate
```
### 3. Установите необходимые пакеты и библиотеки:
```
pip install -r requirements.txt
```
### 4. Создайте ``` .env ``` файл с данными о токене бота:
```
bot_token=TELEGRAM_BOT_TOKEN
```
### 5. Выполните миграции:
```
alembic upgrade head
```
### 6. Запустите функции:
```
python main.py

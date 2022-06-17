# Тестовое задание Python-разработчика

### Цели задания:

Реализовать приложение для отображения таблицы заказов из Google таблиц.

#### Описание

| Function                  | REQUEST | Endpoint                           |
|---------------------------|---------|------------------------------------|
| Список заказов JSON       | GET     | http://0.0.0.0:8000/api/v1/orders/ |
| Веб-страница с диаграммой | GET     | http://localhost:3000/             |

Таблица с данными: https://docs.google.com/spreadsheets/d/1o8Nm2n8yEfwtgitELuBJFUz91SB2tdO4Z0l2MA3B4pQ/edit?usp=sharing

### Установка:

Установить make. Установить Poetry. Установить Docker Engine и Docker Compose.
Для работы с Google API скопируйте свои OAuth client ID credentials в файл "credentials.json" и поместите его в корневую папку проекта. 

```bash
git clone https://github.com/EvilMadSquirrel/orders_list_app.git
cd orders_list_app
```
Создайте .env файл по образцу (.env_example)
Сгенерируйте секретный ключ:
```bash
make secretkey
```
Запишите его в .env файл в поле SECRET_KEY

В поле SPREADSHEET_ID запишите ID таблицы с данными.

Запустите настройку проекта:

```bash
make setup
```

В процессе настройки создайте суперпользователя.

Запуск проекта:

```bash
make start
```



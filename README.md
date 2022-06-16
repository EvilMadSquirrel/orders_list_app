# Тестовое задание Python-разработчика

### Цели задания:

Реализовать приложение для отображения таблицы заказов из Google таблиц.

### Установка:

Установить make. Установить Poetry. Установить Docker Engine и Docker Compose.

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



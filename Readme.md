# Warehouse Management
Данная работа представляет собой backend-часть для сервиса управления складом с функционалом:

- Создание товара (POST /products).
- Получение списка товаров (GET /products).
- Получение информации о товаре по id (GET /products/{id}).
- Обновление информации о товаре (PUT /products/{id}).
- Удаление товара (DELETE /products/{id}).
- Создание заказа (POST /orders).
- Получение списка заказов (GET /orders).
- Получение информации о заказе по id (GET /orders/{id}).
- Обновление статуса заказа (PATCH /orders/{id}/status).

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Установка](#установка)



## Технологии
- [FastApi](https://fastapi.tiangolo.com/)
- [SQLalchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Uvicorn](https://www.uvicorn.org/)


## Начало работы


Создание базу данных postgres:
```
CREATE DATABASE db_name
```
Создать .env фаил:
```
Пример заполнения в файле .env.sample
```

## Установка

### Установка зависимостей
Для установки зависимостей, выполните команду:
```
pip install -r requirements.txt
```

### Запуск сервера
Запуск сервера на локальной машине на порту 8000 :
```
uvicorn main:app --reload
```
Документация (URL) :
```
http://localhost:8000/docs/
```

## Запуск проекта через docker-compose

Для запуска через docker-compose выполнить команду находясь в корне проекта:
```
docker-compose up
```


# Rest-api, позволяющее искать и получать информацио о сигнатурах пациента



## Основные сущности

### Patient

Пациент имеет имя и сигнатуры

### Signature

Сигнатура имеет имя и значение

## Основные API методы

Методы обрабатывают HTTP GET запросы.

Документация находится по адресу http://127.0.0.1:8000/docs

### Получить значения выбранных сигнатур данного пациента

![image](https://user-images.githubusercontent.com/81371413/128731093-ed80e7cf-6eee-4dc2-9321-5a17da94ee5e.png)


### Получить значения всех сигнатур данного пациента

![image](https://user-images.githubusercontent.com/81371413/128731142-f49a210d-70a5-47f8-ad71-0985d6235a12.png)


### Получить среднее значение данный сигнатуры по всем пациентам

![image](https://user-images.githubusercontent.com/81371413/128731178-e15b24d7-6d32-457c-a5b6-2e76c788031e.png)


## Установка через Docker<br>
* Клонируем проект
```bash
sudo docker-compose up -d
```

Доступно по адресу http://127.0.0.1:8000/



## Установка без Docker<br>
* Клонируем проект
* Создаем виртуальное окружение 
```bash
python -m venv venv
```
* Активируем виртуальное окружение
```bash
source venv/bin/activate
```
* Устанавливаем зависимости из requirements.txt
```bash
pip install -r requirements.txt
```
* Запускаем http сервер командой
```bash
uvicorn main:app
```




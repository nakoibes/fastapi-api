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

![image](https://user-images.githubusercontent.com/81371413/128727319-b5260be2-6db9-4fc5-9829-d10afdb387d8.png)


### Получить значения всех сигнатур данного пациента

![image](https://user-images.githubusercontent.com/81371413/128727372-186cbe09-cd7b-4f8c-95e3-3790a0943616.png)


### Получить среднее значение данный сигнатуры по всем пациентам

![image](https://user-images.githubusercontent.com/81371413/128727510-7dc69c28-172f-4e6d-8a7a-f2826028bbab.png)


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




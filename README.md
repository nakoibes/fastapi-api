# Rest-api, позволяющее искать и получать информацио о сигнатурах пациента



## Основные сущности

### Patient

Пациент, имеет имя и поля одноименные с названием сигнатур в таблице

## Основные API методы

Методы обрабатывают HTTP GET запросы.

### Получить значения выбранных сигнатур данного пациента
По адресу:

```bash
http://127.0.0.1:8000/person?name=NSCLC378&metrics=MHCII&metrics=Coactivation_molecules&metrics=T_cells&metrics=B_cells
```


### Получить значения всех сигнатур данного пациента
По адресу:

```bash
http://127.0.0.1:8000/person?name=NSCLC378
```

### Получить среднее значение данный сигнатуры по всем пациентам
По адресу:

```bash
http://127.0.0.1:8000/average?signature_name=T_cell_traffic
```
Установка через Docker<br>
* Клонируем проект
```bash
sudo docker-compose up -d
```

Доступно по адресу http://127.0.0.1:8000/

Документация находится по адресу http://127.0.0.1:8000/docs


Установка без Docker<br>
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



